#!/usr/bin/env python3
"""Run early Unit 3 teacher notebooks (Meetings 01–16), statically audit unfinished student scaffolds."""
import json, re, sys
from pathlib import Path
from datetime import datetime, timezone
import nbformat
from nbclient import NotebookClient
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[2]
DATA=REPO/"Datasets"
REPLACE={
"https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv":DATA/"penguins.csv",
"https://raw.githubusercontent.com/arielb30/datasets/main/titanic_data.csv":DATA/"titanic_data.csv",
}
def run():
    result={"date":datetime.now(timezone.utc).isoformat(),"teacher_execution":[],"student_scaffold":[]}
    for number in range(1,17):
        folder=ROOT/f"Meeting-{number:02d}"/"Teaching-Edition-v3"
        for kind in ("Guided-Audited.ipynb","Teacher-Solution-Audited.ipynb"):
            entry={"meeting":number,"file":kind,"status":"FAIL"}
            try:
                nb=nbformat.read(folder/kind,as_version=4)
                for c in nb.cells:
                    if c.cell_type=="code":
                        for url,local in REPLACE.items():
                            c.source=c.source.replace(url,str(local))
                NotebookClient(nb,timeout=240,kernel_name="python3",allow_errors=False,
                               resources={"metadata":{"path":str(REPO)}}).execute()
                code=[c for c in nb.cells if c.cell_type=="code"]
                assert all(c.execution_count is not None for c in code)
                entry.update(status="PASS",code_cells=len(code))
            except Exception as e:
                entry["error"]=str(e)[-3000:]
            result["teacher_execution"].append(entry)
            print(f"Early {number:02d} {kind}: {entry['status']}",flush=True)
            if entry.get("error"):print(entry["error"][-850:],flush=True)
        entry={"meeting":number,"file":"Student-Fill-Blanks-Audited.ipynb","status":"FAIL"}
        try:
            nb=nbformat.read(folder/entry["file"],as_version=4)
            code=[c.source for c in nb.cells if c.cell_type=="code"]
            assert code,"Missing student code"
            slots=sum(len(re.findall(r"(?<!\?)\?(?!\?)",s)) for s in code)
            triple=sum(s.count("???") for s in code)
            entry.update(status="STRUCTURE_PASS",code_cells=len(code),
                         single_question_placeholders=slots,triple_question_placeholders=triple,
                         note="NOT executed; separate student answer-key runner required")
        except Exception as e:entry["error"]=str(e)[-1500:]
        result["student_scaffold"].append(entry)
        print(f"Early {number:02d} student scaffold: {entry['status']}",flush=True)
    path=Path("unit3-early-01-16-run-report.json")
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    passed=sum(x["status"]=="PASS" for x in result["teacher_execution"])
    structured=sum(x["status"]=="STRUCTURE_PASS" for x in result["student_scaffold"])
    print(f"EARLY REPORT: teacher {passed}/32 PASS, student structure {structured}/16; student Run All NOT YET VERIFIED",flush=True)
    return int(passed!=32 or structured!=16)
if __name__=="__main__":sys.exit(run())
