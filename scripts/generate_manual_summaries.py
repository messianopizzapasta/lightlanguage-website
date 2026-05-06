#!/usr/bin/env python3
"""
Generate one-page PDF summaries (original wording) inspired by themes in
Beginning Light Language Student Manual (2014), © Starr Fuentes.
Not a reproduction of the manual — for educational context on apps.justbe.works.

Source material for the author’s study (not embedded in output):
~/Documents/Spiritualität/Light Language /BeginningLL_StudentManual_2014.pdf
"""
from __future__ import annotations

import math
import os
from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos

# macOS universal font for DE/ES/FR/IT/PT
FONT = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"

OUT_DIR = Path(__file__).resolve().parent.parent / "assets" / "pdfs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

META = (
    "Independent overview — not a substitute for the full manual (2014) or in-person teaching. "
    "Light Language Grid Creator (JustBe) is a separate visual studio app."
)

# Localised label under the schematic shape
SHAPE_LEGEND: dict[str, str] = {
    "en": "Example: one isometric wireframe shape (grid vocabulary — schematic, not app artwork)",
    "de": "Beispiel: eine isometrische Drahtgitter-Form (Raster-Vokabular — schematisch)",
    "es": "Ejemplo: una forma isométrica en alambre (vocabulario de cuadrícula — esquemático)",
    "fr": "Exemple : une forme filaire isométrique (vocabulaire de grille — schématique)",
    "it": "Esempio: una forma isometrica a fil di ferro (vocabolario griglia — schematico)",
    "pt": "Exemplo: uma forma isométrica em arame (vocabulário da grelha — esquemático)",
}

# (document title, subtitle, list of (section title, section body))
TEXTS: dict[str, tuple[str, str, list[tuple[str, str]]]] = {
    "en": (
        "Beginning Light Language (2014)",
        "One-page study summary",
        [
            (
                "About this sheet",
                "This sheet condenses recurring themes from introductory Light Language coursework—especially how manuals such as the 2014 student guide frame the practice—using new wording so it is not a copy of any book.",
            ),
            (
                "Lineage and setting",
                "Public materials describe Light Language as a structured form of work with color and sacred geometry, historically taught through lineages in Mexico and later shared internationally in workshops. Respect for indigenous teachers and consenting communities belongs at the centre of how we speak about these roots.",
            ),
            (
                "What practitioners often emphasise",
                "Clear intention is treated like information that organises subtle fields around a person. Many teachings picture multiple “bodies” or layers (physical, emotional, mental, spiritual) nested inside an auric field; changing finer layers first is presented as gentler than forcing change only from dense patterns.",
            ),
            (
                "Three attitudes",
                "(1) Thoughts participate in shaping experience. (2) Self-responsibility for one’s choices. (3) “As above, so below”—inner patterns and outer life mirror each other. These are philosophical lenses, not medical claims.",
            ),
            (
                "Transmission",
                "Manuals stress that Light Language is partly a “caught” teaching: sitting with an experienced facilitator helps the nervous system recognise tone, spacing, and presence that print alone rarely conveys.",
            ),
            (
                "Practical note",
                "Use official manuals and ethical teachers for depth. Between classes, Light Language Grid Creator (JustBe) is a full visual studio—88 shapes, 144 colours, words/sets/stages, grids, autosave, reminders, PNG export—for daily practice; it is not affiliated with the manual’s publisher.",
            ),
        ],
    ),
    "de": (
        "Beginning Light Language (2014)",
        "Einseitige Lernübersicht",
        [
            (
                "Über dieses Blatt",
                "Dieses Blatt fasst wiederkehrende Themen einführender Light-Language-Kurse zusammen—so, wie sie etwa im Studentenhandbuch von 2014 gerahmt werden—in neuer Formulierung, ohne den Text des Buches abzuschreiben.",
            ),
            (
                "Herkunft und Kontext",
                "Öffentliche Materialien beschreiben Light Language als strukturierte Arbeit mit Farbe und heiliger Geometrie, historisch in mexikanischen Lehrlinien vermittelt und später international in Seminaren geteilt. Respekt vor indigenen Lehrpersonen und Gemeinschaften sollte im Zentrum stehen.",
            ),
            (
                "Was Praktizierende betonen",
                "Klare Absicht wird wie Information behandelt, die feinere Felder um eine Person ordnet. Viele Lehren stellen mehrere „Körper“ oder Schichten (physisch, emotional, mental, spirituell) in einem aurischen Feld dar; zuerst feinere Schichten zu verändern, gilt oft als sanfter.",
            ),
            (
                "Drei Haltungen",
                "(1) Gedanken wirken auf die Erfahrung mit. (2) Eigenverantwortung. (3) „Wie oben, so unten“—innere Muster und äußeres Leben spiegeln sich. Das sind philosophische Linsen, keine Heilversprechen.",
            ),
            (
                "Übertragung",
                "Handbücher betonen „erlebtes“ Lernen in der Nähe erfahrener Facilitatorinnen—Präsenz, die Druck allein selten ersetzt.",
            ),
            (
                "Hinweis",
                "Vertiefte Arbeit gehört in offizielle Handbücher und ethische Lehre. Light Language Grid Creator (JustBe) ist ein digitales Trainingsstudio (88 Formen, 144 Farben, Raster, PNG-Export) und nicht mit dem Verlag des Manuals verbunden.",
            ),
        ],
    ),
    "es": (
        "Beginning Light Language (2014)",
        "Resumen de estudio de una página",
        [
            (
                "Sobre esta hoja",
                "Esta hoja resume temas recurrentes de cursos introductorios de Light Language—tal como los enmarca, por ejemplo, el manual del estudiante de 2014—con redacción nueva, sin copiar el libro.",
            ),
            (
                "Linaje y contexto",
                "Los materiales públicos describen la Light Language como trabajo estructurado con color y geometría sagrada, enseñado históricamente en linajes de México y luego compartido internacionalmente. El respeto a maestras indígenas y comunidades debe ser central.",
            ),
            (
                "Lo que suelen enfatizar",
                "La intención clara se trata como información que organiza campos sutiles. Muchas enseñanzas imaginaron varios “cuerpos” o capas dentro del campo áurico; cambiar capas más sutiles primero se presenta como más amable que forzar solo lo denso.",
            ),
            (
                "Tres actitudes",
                "(1) Los pensamientos participan en la experiencia. (2) Autoresponsabilidad. (3) “Como es arriba, es abajo”—eco entre interior y exterior. Son lentes filosóficos, no promesas médicas.",
            ),
            (
                "Transmisión",
                "Los manuales insisten en aprendizaje “contagiado” junto a facilitadores experimentados—presencia que el papel raramente sustituye.",
            ),
            (
                "Nota",
                "Para profundidad, usa manuales oficiales y docentes éticos. Grid Creator es una app creativa aparte (diseño, exportación PNG) y no está afiliada a la editorial del manual.",
            ),
        ],
    ),
    "fr": (
        "Beginning Light Language (2014)",
        "Résumé d’étude d’une page",
        [
            (
                "À propos de cette feuille",
                "Cette feuille résume des thèmes récurrents des cours d’introduction au Light Language—sur le même type de contenu que le manuel de l’étudiant de 2014—avec une formulation nouvelle, sans copier le livre.",
            ),
            (
                "Lignée et contexte",
                "Les supports publics décrivent le Light Language comme un travail structuré avec la couleur et la géométrie sacrée, enseigné historiquement au Mexique puis partagé internationalement. Le respect des enseignants autochtones et des communautés doit rester central.",
            ),
            (
                "Points souvent soulignés",
                "L’intention claire est traitée comme une information qui organise des champs subtils. Plusieurs enseignements imaginent des « corps » ou couches à l’intérieur de l’aura; ajuster d’abord les couches fines est souvent présenté comme plus doux.",
            ),
            (
                "Trois attitudes",
                "(1) Les pensées participent à l’expérience. (2) Responsabilité personnelle. (3) « Comme en haut, ainsi en bas »—résonance intérieur/extérieur. Ce sont des cadres philosophiques, pas des promesses médicales.",
            ),
            (
                "Transmission",
                "Les manuels insistent sur un apprentissage « attrapé » auprès de facilitateurs expérimentés—présence difficile à remplacer par l’imprimé.",
            ),
            (
                "Note",
                "Pour la profondeur, utilisez les manuels officiels et des enseignants éthiques. L’app Grid Creator est un outil créatif séparé (mise en page, export PNG) sans affiliation à l’éditeur du manuel.",
            ),
        ],
    ),
    "it": (
        "Beginning Light Language (2014)",
        "Riassunto di studio su una pagina",
        [
            (
                "Su questo foglio",
                "Questo foglio riassume temi ricorrenti dei corsi introduttivi di Light Language—come li incornicia ad esempio il manuale dello studente del 2014—con formulazione nuova, senza copiare il libro.",
            ),
            (
                "Lignaggio e contesto",
                "I materiali pubblici descrivono la Light Language come lavoro strutturato con colore e geometria sacra, insegnato storicamente in lignaggi in Messico e poi condiviso internazionalmente. Rispetto per insegnanti indigeni e comunità al centro.",
            ),
            (
                "Cosa si sottolinea",
                "L’intenzione chiara è trattata come informazione che ordina campi sottili. Molti insegnamenti immaginano più “corpi” o strati nell’aura; cambiare prima strati sottili è spesso presentato come più gentile.",
            ),
            (
                "Tre atteggiamenti",
                "(1) I pensieri partecipano all’esperienza. (2) Autoresponsabilità. (3) “Come sopra, così sotto”—eco interno/esterno. Lenti filosofiche, non promesse mediche.",
            ),
            (
                "Trasmissione",
                "I manuali insistono su un apprendimento “preso” accanto a facilitatori esperti—presenza che la carta raramente sostituisce.",
            ),
            (
                "Nota",
                "Per approfondire, manuali ufficiali e insegnanti etici. Grid Creator è un’app creativa separata (layout, export PNG) non affiliata all’editore del manuale.",
            ),
        ],
    ),
    "pt": (
        "Beginning Light Language (2014)",
        "Resumo de estudo de uma página",
        [
            (
                "Sobre esta folha",
                "Esta folha resume temas recorrentes de cursos introdutórios de Light Language—como os enquadra, por exemplo, o manual do estudante de 2014—com redação nova, sem copiar o livro.",
            ),
            (
                "Linhagem e contexto",
                "Materiais públicos descrevem Light Language como trabalho estruturado com cor e geometria sagrada, ensinado historicamente em linhagens no México e depois compartilhado internacionalmente. Respeito a mestres indígenas e comunidades deve ser central.",
            ),
            (
                "Ênfases comuns",
                "Intenção clara é tratada como informação que organiza campos sutis. Muitos ensinos imaginam vários “corpos” ou camadas na aura; mudar camadas finas primeiro costuma ser apresentado como mais suave.",
            ),
            (
                "Três atitudes",
                "(1) Pensamentos participam da experiência. (2) Autorresponsabilidade. (3) “Como acima, assim abaixo”—eco interno/externo. São lentes filosóficas, não promessas médicas.",
            ),
            (
                "Transmissão",
                "Manuais enfatizam aprendizado “pegado” junto a facilitadores experientes—presença que o papel raramente substitui.",
            ),
            (
                "Nota",
                "Para profundidade, use manuais oficiais e professores éticos. Grid Creator é um app criativo separado (layout, exportação PNG) sem afiliação à editora do manual.",
            ),
        ],
    ),
}


class SummaryPDF(FPDF):
    def __init__(self, title: str, subtitle: str) -> None:
        super().__init__(format="A4", unit="mm")
        self._doc_title = title
        self._subtitle = subtitle

    def header(self) -> None:  # noqa: D102
        self.set_x(self.l_margin)
        usable = self.w - self.r_margin - self.l_margin
        self.set_font("uni", "B", 11.5)
        self.set_text_color(15, 35, 60)
        self.cell(usable, 6.5, self._doc_title, new_x="LMARGIN", new_y="NEXT", align="C")
        self.set_font("uni", "", 9.5)
        self.set_text_color(120, 95, 30)
        self.cell(usable, 5.5, self._subtitle, new_x="LMARGIN", new_y="NEXT", align="C")
        self.ln(1)
        self.set_draw_color(200, 190, 160)
        y = self.get_y()
        self.line(self.l_margin, y, self.w - self.r_margin, y)
        self.ln(3)

    def footer(self) -> None:  # noqa: D102
        self.set_y(-12)
        self.set_font("uni", "", 6.5)
        self.set_text_color(100, 100, 100)
        self.multi_cell(0, 2.8, META, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def _cube_vertices_screen(self, cx: float, cy: float, edge_mm: float) -> list[tuple[float, float]]:
        verts = [
            (0, 0, 0),
            (1, 0, 0),
            (1, 1, 0),
            (0, 1, 0),
            (0, 0, 1),
            (1, 0, 1),
            (1, 1, 1),
            (0, 1, 1),
        ]
        c30 = math.cos(math.radians(30))
        s30 = math.sin(math.radians(30))
        s = edge_mm

        def p_local(x: float, y: float, z: float) -> tuple[float, float]:
            px = (x - y) * c30 * s
            py = -(x + y) * s30 * s - z * s * 1.22
            return px, py

        ox, oy = p_local(0.5, 0.5, 0.5)
        out: list[tuple[float, float]] = []
        for x, y, z in verts:
            lx, ly = p_local(x, y, z)
            out.append((cx + lx - ox, cy + ly - oy))
        return out

    def draw_shape_panel(self, legend: str) -> None:
        """Light panel with one isometric wireframe cube (3D shape vocabulary)."""
        x0 = self.l_margin
        w = self.w - self.l_margin - self.r_margin
        y0 = self.get_y()
        panel_h = 22.0

        self.set_draw_color(198, 192, 175)
        self.set_fill_color(252, 250, 246)
        self.rect(x0, y0, w, panel_h, style="DF")

        cx = x0 + w / 2
        cy = y0 + panel_h * 0.38
        verts = self._cube_vertices_screen(cx, cy, edge_mm=6.2)
        edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 4),
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7),
        ]
        top_face_edges = {frozenset({4, 5}), frozenset({5, 6}), frozenset({6, 7}), frozenset({7, 4})}
        for a, b in edges:
            if frozenset((a, b)) in top_face_edges:
                self.set_draw_color(28, 72, 118)
                self.set_line_width(0.42)
            else:
                self.set_draw_color(140, 148, 165)
                self.set_line_width(0.28)
            x1, y1 = verts[a]
            x2, y2 = verts[b]
            self.line(x1, y1, x2, y2)

        cap_y = y0 + panel_h - 8.2
        self.set_xy(x0 + 2.5, cap_y)
        self.set_font("uni", "", 7.1)
        self.set_text_color(48, 52, 62)
        self.multi_cell(
            w - 5, 3.2, legend, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT
        )

        self.set_xy(self.l_margin, y0 + panel_h + 2.2)


def build(code: str) -> Path:
    title, subtitle, sections = TEXTS[code]
    pdf = SummaryPDF(title, subtitle)
    pdf.set_margins(16, 16, 16)
    pdf.set_auto_page_break(True, margin=14)
    pdf.add_font("uni", "", FONT)
    pdf.add_font("uni", "B", FONT)
    pdf.add_page()

    pdf.draw_shape_panel(SHAPE_LEGEND[code])

    title_h = 3.9
    body_h = 3.75
    for sec_title, body in sections:
        pdf.set_font("uni", "B", 9.2)
        pdf.set_text_color(18, 38, 68)
        pdf.multi_cell(
            0, title_h, sec_title, new_x=XPos.LMARGIN, new_y=YPos.NEXT
        )
        pdf.set_font("uni", "", 8.15)
        pdf.set_text_color(38, 38, 44)
        pdf.multi_cell(0, body_h, body, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(0.9)

    out = OUT_DIR / f"beginning-light-language-summary-{code}.pdf"
    pdf.output(str(out))
    return out


def main() -> None:
    if not os.path.isfile(FONT):
        raise SystemExit(f"Missing font file: {FONT}")
    for code in TEXTS:
        path = build(code)
        reader = __import__("pypdf", fromlist=["PdfReader"]).PdfReader(str(path))
        n = len(reader.pages)
        print("Wrote", path, "size", path.stat().st_size, "pages", n)
        if n != 1:
            raise SystemExit(f"Expected 1 page for {code}, got {n}")


if __name__ == "__main__":
    main()
