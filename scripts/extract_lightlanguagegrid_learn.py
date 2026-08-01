#!/usr/bin/env python3
"""Extract Learn-section copy from lightlanguagegrid.com SPA bundle (Label/Desc/Text)."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

DEFAULT_BUNDLE = "https://www.lightlanguagegrid.com/static/js/main.cc735cec.js"

SHAPE_KEYS = [
    "Cube",
    "Sphere",
    "Pyramid",
    "Cone",
    "Cylinder",
    "Dodecahedron",
    "Octahedron",
    "Icosahedron",
    "Mobius",
    "DoubleSpiral",
    "Torus",
    "Tetrahedron",
    "Megaphone",
    "Focuscone",
]

SET_KEYS = [
    "Circulatory",
    "Digestive",
    "Gland",
    "Lymph",
    "Muscular",
    "Nervous",
    "Reproductive",
    "Respiratory",
    "Skeletal",
    "Integumentary",
    "Urinary",
    "Immune system",
]

STAGE_KEYS = [
    "Integrity",
    "Social",
    "Holographic",
    "Reactive",
    "Building",
    "Genetic",
    "Alignment",
    "Pattern",
    "Environmental",
    "Competitive",
    "Attitudinal",
    "City",
]


def unescape(raw: str) -> str:
    return (
        raw.replace("\\n", "\n")
        .replace('\\"', '"')
        .replace("\\'", "'")
        .replace("\\u201c", '"')
        .replace("\\u201d", '"')
        .replace("\\u2019", "'")
    )


def fetch_bundle(url: str) -> str:
    with urllib.request.urlopen(url, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def label_desc_pairs(text: str) -> dict[str, str]:
    pairs = re.findall(r'"Label":"([^"]+)","Desc":"((?:[^"\\]|\\.)*)"', text)
    out: dict[str, str] = {}
    for label, desc in pairs:
        if label.isascii():
            out[label] = unescape(desc)
    return out


def shape_blocks(text: str) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for name in SHAPE_KEYS:
        m = re.search(
            rf'"{name}":\{{"Label":"{name}","Desc":"((?:[^"\\]|\\.)*)"(?:,"Formula":\{{[^}}]+\}})?,"Text":"((?:[^"\\]|\\.)*)"',
            text,
        )
        if m:
            out[name] = {"summary": unescape(m.group(1)), "body": unescape(m.group(2))}
            continue
        m2 = re.search(rf'"{name}":\{{"Label":"{name}","Desc":"((?:[^"\\]|\\.)*)"', text)
        if m2:
            out[name] = {"summary": unescape(m2.group(1)), "body": ""}
    return out


def section_intro(text: str, needle: str) -> str:
    idx = text.find(needle)
    if idx < 0:
        return ""
    start = text.rfind('"Text":"', max(0, idx - 80), idx)
    if start < 0:
        return ""
    end = text.find('","', start + 8)
    if end < 0 or end > idx + 20:
        end = text.find('"}', start + 8)
    raw = text[start + 8 : end]
    return unescape(raw)


def build_payload(text: str) -> dict:
    pairs = label_desc_pairs(text)
    return {
        "source": DEFAULT_BUNDLE,
        "intros": {
            "sets": section_intro(text, "A set is defined"),
            "stages": section_intro(text, "A stage is defined"),
        },
        "shapes": shape_blocks(text),
        "sets": {key: pairs.get(key, "") for key in SET_KEYS},
        "stages": {key: pairs.get(key, "") for key in STAGE_KEYS},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", default=DEFAULT_BUNDLE, help="JS bundle URL or local path")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "docs" / "grid-vocabulary" / "learn-source.en.json",
        help="Output JSON path",
    )
    args = parser.parse_args()

    bundle = args.bundle
    if bundle.startswith("http://") or bundle.startswith("https://"):
        text = fetch_bundle(bundle)
    else:
        text = Path(bundle).read_text(encoding="utf-8", errors="replace")

    payload = build_payload(text)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
