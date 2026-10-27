#!/usr/bin/env python3
"""Execute all teacher-facing Meeting 17-23 Audited notebooks with local Penguins CSV.

Usage: python scripts/run_audited_notebooks.py [--only 23] [--out quality-run-report.json]
This is a reproducible quality gate; it never executes incomplete student blanks.
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", type=int, choices=range(17, 24))
    parser.add_argument("--out", default="quality-run-report.json")
    args = parser.parse_args()
    course = Path(__file__).resolve().parents[1]
    repo = course.parents[2]
    dataset = repo / "Datasets" / "penguins.csv"
    if not dataset.is_file():
        raise SystemExit(f"Missing local dataset {dataset}")
    import pandas as pd
    import numpy as np
    import sklearn
    original_url = (
        "https://raw.githubusercontent.com/samiabo75/"
        "Data-Science-ML-Course/main/Datasets/penguins.csv"
    )
    checked = pd.read_csv(dataset)
    if len(checked) != 344 or "species" not in checked.columns:
        raise SystemExit("Dataset sanity check failed")
    report = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0],
        "pandas": pd.__version__,
        "numpy": np.__version__,
        "sklearn": sklearn.__version__,
        "dataset": str(dataset.relative_to(repo)),
        "results": [],
    }
    numbers = [args.only] if args.only else list(range(17, 24))
    failed = 0
    for n in numbers:
        for kind in ("Guided-Audited.ipynb", "Teacher-Solution-Audited.ipynb"):
            file = course / f"Meeting-{n}" / "Teaching-Edition-v3" / kind
            entry = {"meeting": n, "notebook": kind, "status": "FAIL"}
            try:
                notebook = nbformat.read(file, as_version=4)
                for cell in notebook.cells:
                    if cell.cell_type == "code":
                        cell.source = cell.source.replace(original_url, str(dataset))
                client = NotebookClient(
                    notebook, timeout=240, kernel_name="python3", allow_errors=False,
                    resources={"metadata": {"path": str(repo)}},
                )
                client.execute()
                executed = [c for c in notebook.cells if c.cell_type == "code"]
                entry.update(status="PASS", code_cells=len(executed),
                             executed_cells=sum(c.execution_count is not None for c in executed))
            except (CellExecutionError, Exception) as exc:
                failed += 1
                entry["error"] = str(exc)[-3500:]
            report["results"].append(entry)
            print(f"Meeting {n} {kind}: {entry['status']}", flush=True)
            if entry.get("error"):
                print(entry["error"][-900:], flush=True)
    Path(args.out).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"REPORT: {args.out}; {len(report['results']) - failed} PASS, {failed} FAIL", flush=True)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
