#!/usr/bin/env python3
"""Run completed student Audited notebooks using a separate instructor answer key.

Student notebooks are left intact with their ??? blanks. The resolved copy stays
only in memory; no filled student notebook is written to the public repository.
"""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
import nbformat
from nbclient import NotebookClient

def complete(source, answers):
    occurrences = source.count("???")
    if occurrences != len(answers):
        raise ValueError(f"Expected {occurrences} blanks, got {len(answers)} answers")
    iterator = iter(answers)
    result = re.sub(r"\?\?\?", lambda _: next(iterator), source)
    if "???" in result:
        raise ValueError("Unfilled placeholders")
    compile(result, "<completed student cell>", "exec")
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", type=int, choices=range(17,26))
    parser.add_argument("--out", default="student-quality-run-report.json")
    args = parser.parse_args()
    course = Path(__file__).resolve().parents[1]
    repo = course.parents[2]
    dataset = repo / "Datasets" / "penguins.csv"
    keys = json.loads((Path(__file__).parent / "student_completion_keys.json").read_text(encoding="utf8"))
    original_url = "https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
    report = {"timestamp_utc":datetime.now(timezone.utc).isoformat(),"results":[]}
    failures = 0
    for n in ([args.only] if args.only else range(17,26)):
        file = course / f"Meeting-{n}" / "Teaching-Edition-v3" / "Student-Fill-Blanks-Audited.ipynb"
        outcome = {"meeting":n,"notebook":file.name,"status":"FAIL"}
        try:
            nb = nbformat.read(file, as_version=4)
            code_cells = [c for c in nb.cells if c.cell_type=="code"]
            answers = keys[str(n)]
            if len(code_cells)!=len(answers):
                raise ValueError(f"Code cells {len(code_cells)} != keyed {len(answers)}")
            for i,cell in enumerate(code_cells):
                cell.source=complete(cell.source,answers[i]).replace(original_url,str(dataset))
            NotebookClient(nb,timeout=240,kernel_name="python3",allow_errors=False,
                           resources={"metadata":{"path":str(repo)}}).execute()
            outcome.update(status="PASS",code_cells=len(code_cells),
                           executed_cells=sum(c.execution_count is not None for c in code_cells),
                           blanks_filled=sum(map(len,answers)))
        except Exception as ex:
            failures+=1
            outcome["error"]=str(ex)[-4000:]
        print(f"Meeting {n} student filled notebook: {outcome['status']}",flush=True)
        if outcome.get("error"):
            print(outcome["error"][-950:],flush=True)
        report["results"].append(outcome)
    Path(args.out).write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf8")
    print(f"REPORT {args.out}: {len(report['results'])-failures} PASS, {failures} FAIL",flush=True)
    return 1 if failures else 0

if __name__=="__main__":
    raise SystemExit(main())
