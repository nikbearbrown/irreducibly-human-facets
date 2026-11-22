"""Render the exact per-posting messages the Claude coders got, for any model.

Usage:  python3 scripts/render_prompts.py prompts.jsonl
Writes one line per posting: {"posting", "items", "system", "user"}. Send each "user" with its "system" in a
fresh conversation (or headless call), and save the reply as replies/<posting>.json in your hand-in folder.
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kitlib


def render(p, guide, task):
    return task.format(codebook=guide, title=p["title"], company=p["company"],
                       heads="; ".join(p["heads"]) or "(none)",
                       lines="\n".join(f"{l['item']}: {l['text']}" for l in p["lines"]))


def load_prompts():
    k = kitlib.KIT
    system = open(os.path.join(k, "prompts", "system.txt")).read().strip()
    task = open(os.path.join(k, "prompts", "task_template.txt")).read()
    guide = open(os.path.join(k, "CODER-GUIDE.md")).read()
    return system, task, guide


def main():
    system, task, guide = load_prompts()
    with open(sys.argv[1], "w") as fh:
        for p in kitlib.load_lines():
            fh.write(json.dumps({"posting": p["posting"], "items": [l["item"] for l in p["lines"]],
                                 "system": system, "user": render(p, guide, task)}, ensure_ascii=False) + "\n")
    print("wrote", sys.argv[1])


if __name__ == "__main__":
    main()
