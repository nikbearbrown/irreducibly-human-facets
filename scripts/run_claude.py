"""Code all 12 postings with headless Claude Code (`claude -p`) on your own Claude plan (no API key).

Each posting is one call with no tools, no settings, no MCP servers, no memory and no session, run from an empty
folder, so the model sees only the system prompt and the posting's message. The reply must match
schema/reply.schema.json; a reply that fails the checks gets one retry with its errors.

Usage:
  python3 scripts/run_claude.py <hand-in folder> --model claude-sonnet-5-5 [--effort high] [--workers 3]

Writes <hand-in folder>/replies/F01.json ... F12.json (codes plus _meta: requested and served model, effort,
attempts, timing), then runs check_handin.py. Finished postings are skipped, so a rerun resumes.
Check the served model in the output: on some plans a requested model is served by another one.
"""
import argparse, datetime, glob, json, os, re, shutil, subprocess, sys, tempfile, time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kitlib
from render_prompts import load_prompts, render

SCHEMA = json.load(open(os.path.join(kitlib.KIT, "schema", "reply.schema.json")))
LIMIT_WORDS = re.compile(r"usage limit|limit reached|rate.?limit|weekly limit|out of (usage|credits)|429|"
                         r"hit your .{0,20}limit|5-hour limit|exceeded", re.I)
KEEP_ENV = ("HOME", "PATH", "USER", "LOGNAME", "SHELL", "LANG", "LC_ALL", "TMPDIR", "TERM")


class LimitReached(Exception):
    pass


def claude_bin():
    if os.environ.get("CLAUDE_BIN"):
        return os.environ["CLAUDE_BIN"]
    found = glob.glob(os.path.expanduser(
        "~/Library/Application Support/Claude/claude-code/*/*/claude.app/Contents/MacOS/claude"))
    key = lambda p: [int(x) for x in re.findall(r"claude-code/([\d.]+)/", p)[0].split(".")]
    return sorted(found, key=key)[-1] if found else shutil.which("claude")


def ask(model, effort, system, prompt, cwd):
    cmd = [claude_bin(), "-p", "--model", model, "--effort", effort, "--setting-sources", "",
           "--strict-mcp-config", "--disable-slash-commands", "--system-prompt", system, "--tools", "",
           "--no-session-persistence", "--output-format", "json", "--json-schema", json.dumps(SCHEMA)]
    env = {k: v for k, v in os.environ.items() if k in KEEP_ENV}  # no API key, no parent-session variables
    msg = ""
    for tries in range(3):
        t0 = time.time()
        p = subprocess.run(cmd, input=prompt, capture_output=True, text=True, cwd=cwd, env=env, timeout=1800)
        try:
            out = json.loads(p.stdout)
        except json.JSONDecodeError:
            out = {"is_error": True, "result": (p.stdout or p.stderr or "no output")[-2000:]}
        usage = {"seconds": round(time.time() - t0, 1), "served_models": sorted((out.get("modelUsage") or {})),
                 "cost_usd_notional": out.get("total_cost_usd")}
        text = str(out.get("result") or "")
        if not out.get("is_error"):
            data = out.get("structured_output")
            if data is None and LIMIT_WORDS.search(text):
                raise LimitReached(text[:300])
            return data, text, usage
        msg = text
        if LIMIT_WORDS.search(msg):
            raise LimitReached(msg[:300])
        time.sleep(20 * (tries + 1))
    return None, msg, usage


def code_posting(a, system, task, guide, p, cwd):
    path = os.path.join(a.folder, "replies", f"{p['posting']}.json")
    if os.path.exists(path):
        return p["posting"], "skipped (done)", None
    want = [l["item"] for l in p["lines"]]
    base = render(p, guide, task)
    prompt, attempts = base, []
    for n in (1, 2):
        data, text, usage = ask(a.model, a.effort, system, prompt, cwd)
        codes = [kitlib.normalise(c) for c in (data or {}).get("codes", [])]
        errors = kitlib.check_set(codes, want) if data else ["no structured output: " + text[:200]]
        attempts.append({"attempt": n, "errors": errors, **usage})
        if not errors:
            break
        prompt = base + "\n\n# Your previous reply had these problems; fix them\n\n" + "\n".join(errors)
    served = sorted({m for x in attempts for m in x["served_models"]})
    meta = {"model": a.model, "served_models": served, "effort": a.effort, "attempts": attempts,
            "unresolved_errors": errors}
    json.dump({"codes": codes, "_meta": meta}, open(path, "w"), indent=1, ensure_ascii=False)
    status = "ok" if not errors else "FAILED: " + "; ".join(errors)[:160]
    return p["posting"], f"{status} ({len(attempts)} attempt(s), served by {', '.join(served) or '?'})", served


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--model", required=True)
    ap.add_argument("--effort", default="high")
    ap.add_argument("--workers", type=int, default=3)
    a = ap.parse_args()
    os.makedirs(os.path.join(a.folder, "replies"), exist_ok=True)
    system, task, guide = load_prompts()
    posts = kitlib.load_lines()
    started = datetime.datetime.now().isoformat(timespec="minutes")
    version = subprocess.run([claude_bin(), "--version"], capture_output=True, text=True).stdout.strip()
    served_all = set()
    with tempfile.TemporaryDirectory() as cwd, ThreadPoolExecutor(a.workers) as ex:
        futs = [ex.submit(code_posting, a, system, task, guide, p, cwd) for p in posts]
        for f in futs:
            try:
                pid, status, served = f.result()
                served_all.update(served or [])
                print(pid, status, flush=True)
            except LimitReached as e:
                print("STOPPED at the usage limit; rerun later to resume:", e, flush=True)
    run = os.path.join(a.folder, "RUN.md")
    if not os.path.exists(run):
        open(run, "w").write(
            f"# Run notes\n\n- Way in: A, headless Claude Code (`scripts/run_claude.py`)\n"
            f"- Claude Code: {version}\n- Model requested: {a.model}\n"
            f"- Model served (from each reply's modelUsage): {', '.join(sorted(served_all)) or 'unknown'}\n"
            f"- Effort: {a.effort}\n- Started: {started}\n"
            f"- Finished: {datetime.datetime.now().isoformat(timespec='minutes')}\n"
            f"- One call per posting, no tools, empty working folder, settings and MCP off.\n"
            f"- Anything done differently from INSTRUCTIONS.md: none\n")
    check = subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "check_handin.py"), a.folder])
    sys.exit(check.returncode)


if __name__ == "__main__":
    main()
