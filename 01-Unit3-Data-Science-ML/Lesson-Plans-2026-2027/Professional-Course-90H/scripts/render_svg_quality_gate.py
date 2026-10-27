#!/usr/bin/env python3
"""Render all Unit3 Meetings 17-23 SVGs, save PNGs/contact sheet and machine-readable report.

Checks syntax/render ability and basic markup only; human visual QA remains required.
"""
import json
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET

import cairosvg
from bidi.algorithm import get_display
from PIL import Image, ImageOps, ImageDraw

BASE = Path(__file__).resolve().parents[1]
ASSETS = {
    17: ["accuracy-four-observations.svg","error-inspection-table.svg","knn-train-test-evaluation.svg"],
    18: ["confusion-matrix-binary-eight.svg"],
    19: ["precision-recall-denominators.svg"],
    20: ["baseline-accuracy-vs-recall.svg","imbalance-95-5.svg"],
    21: ["train-validation-candidates.svg","train-validation-test-flow.svg"],
    22: ["cv-three-folds.svg","pipeline-no-leakage.svg"],
    23: ["grid-search-3x5.svg","gridsearch-pipeline-flow.svg"]
}
DEST = BASE / "svg-render-output"
DEST.mkdir(parents=True,exist_ok=True)
report={"date_utc":datetime.now(timezone.utc).isoformat(),"items":[]}
fail=0
tiles=[]
for num,names in ASSETS.items():
    for name in names:
        src=BASE / f"Meeting-{num}" / "Teaching-Edition-v3" / name
        out=DEST / f"Meeting-{num}_{name.removesuffix('.svg')}.png"
        item={"meeting":num,"svg":name,"status":"FAIL"}
        try:
            tree=ET.parse(src)
            root=tree.getroot()
            if not root.tag.endswith("svg"):
                raise ValueError("Root element is not SVG")
            if not ("viewBox" in root.attrib or ("width" in root.attrib and "height" in root.attrib)):
                raise ValueError("Missing intrinsic SVG size")
            # CairoSVG lacks Unicode bidi; this transforms only the PNG preview copy.
            # Original accessible SVG text remains in logical Hebrew Unicode order.
            for text_node in root.iter():
                if text_node.tag.endswith("text") and text_node.text and any(
                    "\u0590" <= char <= "\u05FF" for char in text_node.text
                ):
                    text_node.text = get_display(text_node.text)
            cairosvg.svg2png(bytestring=ET.tostring(root, encoding="utf-8"),
                             write_to=str(out),output_width=960)
            with Image.open(out) as png:
                if png.width<400 or png.height<150:
                    raise ValueError(f"Rendered image too small {png.size}")
                rgba=png.convert("RGBA")
                item["pixel_size"]=[png.width,png.height]
                tile=ImageOps.contain(rgba.convert("RGB"),(580,310))
                preview=Image.new("RGB",(600,355),"white")
                preview.paste(tile,((600-tile.width)//2,32+(310-tile.height)//2))
                ImageDraw.Draw(preview).text((12,8),f"Meeting {num}: {name}",fill="black")
                tiles.append(preview)
            item["status"]="PASS"
        except Exception as e:
            fail+=1
            item["error"]=str(e)
        report["items"].append(item)
        print(f"Meeting {num}: {name} -> {item['status']}",flush=True)
if tiles:
    cols=2
    rows=(len(tiles)+cols-1)//cols
    sheet=Image.new("RGB",(cols*600,rows*355),"#eeeeee")
    for i,tile in enumerate(tiles):
        sheet.paste(tile,((i%cols)*600,(i//cols)*355))
    sheet.save(DEST/"all-meetings-contact-sheet.png")
(DEST/"render-report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(f"SUMMARY: {len(report['items'])-fail}/{len(report['items'])} PASS; {fail} FAIL",flush=True)
raise SystemExit(1 if fail else 0)
