#!/usr/bin/env python3
"""Complete and execute audited student notebooks of Meetings 01–16 in memory only."""
import json,re,sys
from pathlib import Path
from datetime import datetime,timezone
import nbformat
from nbclient import NotebookClient
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[2]
DATA=REPO/"Datasets"
URL="https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
KEYS={}
for file in ("early_completion_keys_01_08.json","early_completion_keys_09_12.json","early_completion_keys_13_16.json"):
    KEYS.update(json.loads((Path(__file__).parent/file).read_text(encoding="utf-8")))
def main():
    report={"timestamp_utc":datetime.now(timezone.utc).isoformat(),"notebooks":[]}
    for n in range(1,17):
        entry={"meeting":n,"status":"FAIL"}
        try:
            path=ROOT/f"Meeting-{n:02d}"/"Teaching-Edition-v3"/"Student-Fill-Blanks-Audited.ipynb"
            nb=nbformat.read(path,as_version=4)
            code=[c for c in nb.cells if c.cell_type=="code"]
            key=KEYS[str(n)]
            if len(code)!=len(key):raise ValueError(f"cell count {len(code)} vs keys {len(key)}")
            blanks=0
            for i,c in enumerate(code):
                matches=re.findall(r"\?{1,3}",c.source)
                if len(matches)!=len(key[i]):
                    raise ValueError(f"cell {i} has {len(matches)} blanks vs {len(key[i])} keys")
                it=iter(key[i])
                c.source=re.sub(r"\?{1,3}",lambda _:next(it),c.source)
                c.source=c.source.replace(URL,str(DATA/"penguins.csv"))
                if "?" in c.source:raise ValueError(f"unfilled placeholder in cell {i}")
                compile(c.source,f"Meeting-{n:02d}/cell-{i}","exec")
                blanks+=len(matches)
            NotebookClient(nb,timeout=240,kernel_name="python3",allow_errors=False,
                           resources={"metadata":{"path":str(REPO)}}).execute()
            entry.update(status="PASS",completed_blanks=blanks,code_cells=len(code))
        except Exception as exc:
            entry["error"]=str(exc)[-2500:]
        report["notebooks"].append(entry)
        print(f"Early student Meeting {n:02d}: {entry['status']}",flush=True)
        if "error" in entry:print(entry["error"][-950:],flush=True)
    Path("unit3-early-student-run-report.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    passed=sum(e["status"]=="PASS" for e in report["notebooks"])
    print(f"EARLY STUDENT REPORT: {passed}/16 PASS, {16-passed} FAIL",flush=True)
    return int(passed!=16)
if __name__=="__main__":sys.exit(main())
