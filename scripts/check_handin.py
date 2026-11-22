"""Check a hand-in folder and write its codes.tsv and report.json.

Reads, in this order, whichever exists: replies/*.json (one reply per posting), replies.jsonl,
coding-sheet.xlsx (a person's sheet), coding-sheet.csv.

Usage:  python3 scripts/check_handin.py <hand-in folder>
Exit code 0 when every line is coded and every code is valid.
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kitlib


def main():
    folder = sys.argv[1]
    posts = kitlib.load_lines()
    order = kitlib.all_items(posts)
    codes, source, meta = kitlib.read_handin(folder)
    errors = kitlib.check_set(codes, order)
    warnings = []
    blank_notes = [c["item"] for c in codes if c["conf"] == "L" and not c["note"]]
    if blank_notes:
        warnings.append(f"{len(blank_notes)} low-confidence lines have no note: {blank_notes[:10]}")
    if not os.path.exists(os.path.join(folder, "RUN.md")):
        warnings.append("no RUN.md (INSTRUCTIONS.md, section 6)")
    for m in meta:
        req, served = m.get("model"), m.get("served_models")
        if req and served and any(req not in s for s in served):
            warnings.append(f"{m.get('file', '')}: asked for {req}, served by {served}")
    kitlib.write_codes(os.path.join(folder, "codes.tsv"), codes, order)
    report = {"folder": os.path.basename(os.path.abspath(folder)), "source": source,
              "status": "pass" if not errors else "fail", "lines_expected": len(order),
              "lines_coded": len({c["item"] for c in codes} & set(order)), "errors": errors, "warnings": warnings}
    json.dump(report, open(os.path.join(folder, "report.json"), "w"), indent=1)
    print(f"{report['status']}: {report['lines_coded']}/{len(order)} lines from {source}")
    for e in errors[:30]:
        print("  error:", e)
    for w in warnings:
        print("  warning:", w)
    sys.exit(0 if not errors else 1)


if __name__ == "__main__":
    main()
