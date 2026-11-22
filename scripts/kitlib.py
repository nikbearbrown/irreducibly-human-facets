"""Shared pieces for the round-2 kit scripts: paths, the code sets, reading and checking a hand-in."""
import csv, glob, json, os, re

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINES = os.path.join(KIT, "handout-private", "lines.json")
MODES = ["DO", "KNOW", "BE", "SIT", "OUT"]
FACETS = ["PA", "ES", "SP", "MS", "CC", "CD", "EW", "NH"]
UPPER = ["SP", "MS", "CC", "CD", "EW"]
NAMES = {"PA": "Pattern & Association", "ES": "Embodied & Sensorimotor", "SP": "Social & Personal",
         "MS": "Metacognitive & Supervisory", "CC": "Causal & Counterfactual", "CD": "Collective & Distributed",
         "EW": "Existential & Wisdom", "NH": "No clean home"}
COLUMNS = ["item", "mode", "facet", "facet2", "conf", "cue", "note"]


def load_lines(path=LINES):
    return json.load(open(path))


def all_items(posts):
    return [l["item"] for p in posts for l in p["lines"]]


def clean(s):
    return re.sub(r"\s+", " ", str(s if s is not None else "")).strip()


def normalise(c):
    c = {k: clean(c.get(k)) for k in COLUMNS}
    for k in ("mode", "facet", "facet2", "conf"):
        c[k] = c[k].upper()
    if c["facet2"] in ("-", "NONE", "N/A"):
        c["facet2"] = ""
    return c


def check_code(c):
    """Errors for one normalised code."""
    e, i = [], c["item"]
    if c["mode"] not in MODES:
        e.append(f"{i}: mode {c['mode']!r} is not one of {MODES}")
    if c["facet"] not in FACETS + ["-"]:
        e.append(f"{i}: facet {c['facet']!r} is not a facet code or '-'")
    if c["facet2"] and c["facet2"] not in FACETS:
        e.append(f"{i}: facet2 {c['facet2']!r} is not a facet code")
    if c["conf"] not in ("H", "M", "L"):
        e.append(f"{i}: conf {c['conf']!r} is not H, M or L")
    if c["mode"] == "OUT" and c["facet"] != "-":
        e.append(f"{i}: an OUT line takes facet '-'")
    if c["facet"] == "-" and c["mode"] not in ("OUT", "SIT"):
        e.append(f"{i}: facet '-' is only for OUT or SIT lines")
    if c["facet"] == "-" and c["facet2"]:
        e.append(f"{i}: facet2 must be empty when facet is '-'")
    if c["facet2"] and c["facet2"] == c["facet"]:
        e.append(f"{i}: facet2 repeats facet")
    return e


def check_set(codes, want):
    """Errors for a whole posting or hand-in: every wanted item exactly once, nothing extra."""
    e, got = [], [c["item"] for c in codes]
    dup = sorted({x for x in got if got.count(x) > 1})
    missing = [x for x in want if x not in got]
    extra = sorted(set(got) - set(want))
    if dup:
        e.append(f"items given more than once: {dup}")
    if missing:
        e.append(f"items missing: {missing}")
    if extra:
        e.append(f"items that are not in the posting: {extra}")
    for c in codes:
        e += check_code(c)
    return e


def parse_reply(text):
    """A model reply: a bare JSON object, or one inside a ```json fence."""
    m = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, flags=re.S)
    return json.loads(m.group(1) if m else text)


def read_handin(folder):
    """Return (codes, source, meta). Looks for replies/*.json, replies.jsonl, coding-sheet.xlsx, coding-sheet.csv."""
    meta = []
    files = sorted(glob.glob(os.path.join(folder, "replies", "*.json")))
    if files:
        codes = []
        for f in files:
            d = parse_reply(open(f).read())
            codes += [normalise(c) for c in d.get("codes", [])]
            if d.get("_meta"):
                meta.append({"file": os.path.basename(f), **d["_meta"]})
        return codes, "replies/*.json", meta
    jl = os.path.join(folder, "replies.jsonl")
    if os.path.exists(jl):
        codes = []
        for line in open(jl):
            if line.strip():
                d = json.loads(line)
                codes += [normalise(c) for c in d.get("codes", [])]
                if d.get("_meta"):
                    meta.append(d["_meta"])
        return codes, "replies.jsonl", meta
    xl = os.path.join(folder, "coding-sheet.xlsx")
    if os.path.exists(xl):
        from openpyxl import load_workbook  # only needed for a person's sheet
        ws = load_workbook(xl, read_only=True, data_only=True)["Codes"]
        rows = list(ws.iter_rows(min_row=2, values_only=True))
        codes = [normalise({"item": r[0], "mode": r[3], "facet": r[4], "facet2": r[5], "conf": r[6], "cue": "",
                            "note": r[7]}) for r in rows if r and r[0]]
        return codes, "coding-sheet.xlsx", meta
    cs = os.path.join(folder, "coding-sheet.csv")
    if os.path.exists(cs):
        rows = list(csv.DictReader(open(cs)))
        key = lambda r, *names: next((r[n] for n in names if n in r), "")
        codes = [normalise({"item": key(r, "Item", "item"), "mode": key(r, "Mode", "mode"),
                            "facet": key(r, "Facet", "facet"), "facet2": key(r, "Facet 2", "facet2"),
                            "conf": key(r, "Confidence", "conf"), "cue": "", "note": key(r, "Note", "note")})
                 for r in rows]
        return codes, "coding-sheet.csv", meta
    raise SystemExit(f"{folder}: no replies/, replies.jsonl, coding-sheet.xlsx or coding-sheet.csv found")


def write_codes(path, codes, order):
    by = {c["item"]: c for c in codes}
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(COLUMNS)
        for i in order:
            if i in by:
                w.writerow([by[i][k] for k in COLUMNS])


def load_codes(path):
    return {r["item"]: r for r in csv.DictReader(open(path), delimiter="\t")}
