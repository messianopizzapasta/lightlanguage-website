#!/usr/bin/env python3
"""
One-off / thematic PDF: “Master the Geometry of Your Reality” (text only).
Header: app icon. No footer line, no shape illustrations, headings + spaced blocks.
"""
from __future__ import annotations

import os
from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos

FONT = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
ROOT = Path(__file__).resolve().parent.parent
ICON = ROOT / "assets" / "images" / "app-icon.png"
OUT = ROOT / "assets" / "pdfs" / "geometry-of-your-reality.pdf"


class DocPDF(FPDF):
    def header(self) -> None:
        return

    def footer(self) -> None:
        return


def main() -> None:
    if not os.path.isfile(FONT):
        raise SystemExit(f"Missing font file: {FONT}")
    if not ICON.is_file():
        raise SystemExit(f"Missing app icon: {ICON}")

    OUT.parent.mkdir(parents=True, exist_ok=True)

    pdf = DocPDF(format="A4", unit="mm")
    pdf.set_margins(18, 18, 18)
    pdf.set_auto_page_break(True, margin=16)
    pdf.add_font("uni", "", FONT)
    pdf.add_font("uni", "B", FONT)
    pdf.add_font("uni", "I", FONT)
    pdf.add_page()

    usable = pdf.w - pdf.l_margin - pdf.r_margin
    icon_mm = 22.0
    x_icon = pdf.l_margin + (usable - icon_mm) / 2
    pdf.image(str(ICON), x=x_icon, y=pdf.get_y(), w=icon_mm)
    pdf.ln(icon_mm + 6)

    def gap(mm: float) -> None:
        pdf.ln(mm)

    def h1(text: str) -> None:
        pdf.set_font("uni", "B", 14)
        pdf.set_text_color(15, 35, 60)
        pdf.multi_cell(0, 6.2, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        gap(5)

    def h2(text: str) -> None:
        pdf.set_font("uni", "B", 11)
        pdf.set_text_color(22, 45, 78)
        pdf.multi_cell(0, 5.4, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        gap(3.5)

    def h3(text: str) -> None:
        pdf.set_font("uni", "B", 10)
        pdf.set_text_color(35, 55, 90)
        pdf.multi_cell(0, 4.8, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        gap(2)

    def body(text: str) -> None:
        pdf.set_font("uni", "", 9.2)
        pdf.set_text_color(38, 38, 44)
        pdf.multi_cell(0, 4.35, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        gap(4)

    def small_italic(text: str) -> None:
        pdf.set_font("uni", "I", 8.6)
        pdf.set_text_color(70, 70, 78)
        pdf.multi_cell(0, 4.0, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        gap(3)

    h1("Master the Geometry of Your Reality")

    body(
        "Every thought you hold carries a specific message that shapes your environment. "
        "When your intentions are clear, they emanate from the brain as electromagnetic impulses, "
        "forming the very structure of your life. By understanding the universal laws of resonance, "
        "you can stop simply reacting to your circumstances and start consciously designing them."
    )

    h2("The Core Principles of Transformation")
    body(
        "To harness the full power of your personal energy, you must align with three essential truths:"
    )
    pdf.set_font("uni", "", 9.2)
    pdf.set_text_color(38, 38, 44)
    for line in (
        "Your thoughts create your reality.",
        "You are 100% responsible for your experiences.",
        "As above, so below: Changing the energy in your higher spiritual bodies automatically "
        "transforms your physical and emotional world.",
    ):
        pdf.multi_cell(0, 4.35, f"• {line}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    gap(5)

    h2("Tools for Conscious Creation")
    body(
        'Instead of "digging out" old patterns through limited perception, you can use the '
        "building blocks of the universe—Sacred Geometry and Color—to push light into your field "
        "and clear away what no longer serves you."
    )

    shapes: list[tuple[str, str, str]] = [
        (
            "Cube",
            "Stabilization & Limitation",
            "Focuses attention and holds a specific energy in place.",
        ),
        (
            "Sphere",
            "Choices & Creation",
            "Opens up 360 degrees of possibility and gets things moving.",
        ),
        (
            "Pyramid",
            "Preservation & Integration",
            "Sharpens thoughts and keeps a goal or fact intact.",
        ),
        (
            "Cylinder",
            "Connection & Understanding",
            "Confirms and strengthens the flow between two points.",
        ),
    ]
    for name, role, outcome in shapes:
        h3(f"{name} — {role}")
        body(outcome)
        gap(1.5)

    gap(2)
    h2("Color frequencies")
    small_italic("Yuliya Perederiy — Vibrant Living Through Color")
    body(
        "Colors are not just visual; they are frequencies that activate specific planes of existence."
    )
    pdf.set_font("uni", "", 9.2)
    pdf.set_text_color(38, 38, 44)
    for line in (
        "Red: Vitality and movement on the physical plane.",
        "Yellow: Clarity, focus, and active intelligence.",
        "Green: Balance, healing, and the energy of new growth.",
        "Blue: Relaxation and the clearing of karmic flow.",
        "Purple: Wisdom and the activation of psychic knowing.",
    ):
        pdf.multi_cell(0, 4.35, f"• {line}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    gap(5)

    h2("Elevate Your Frequency")
    body(
        'True mastery is a "caught" experience, absorbed through the presence of those who have '
        "already integrated these frequencies. When you choose to live by the law rather than just "
        "with it, you gain the clarity to create exactly what you want and need. By fine-tuning your "
        'internal "receiver" to higher frequencies of light, you can bypass the limitations of the '
        "physical body and experience a new era of spiritual freedom."
    )

    pdf.set_font("uni", "B", 9.2)
    pdf.set_text_color(28, 50, 82)
    pdf.multi_cell(
        0,
        4.5,
        "How would your daily life change if you could consciously stabilize your environment "
        "using nothing but your focused intent?",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    pdf.output(str(OUT))
    print("Wrote", OUT, "size", OUT.stat().st_size)


if __name__ == "__main__":
    main()
