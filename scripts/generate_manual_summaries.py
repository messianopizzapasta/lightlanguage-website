#!/usr/bin/env python3
"""
Generate one-sheet PDF study summaries from site-authored themes aligned with
introductory Light Language coursework (2014 student guide as a common print
reference, © Starr Fuentes). Not a reproduction of the manual.

Derived from the owner’s summary export (Downloads); text is translated per
locale for website downloads.
"""
from __future__ import annotations

import os
from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos

FONT = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"

OUT_DIR = Path(__file__).resolve().parent.parent / "assets" / "pdfs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

TEXTS: dict[str, tuple[str, str, list[tuple[str, str]]]] = {
    "en": (
        "Beginning Light Language (2014)",
        "A short orientation",
        [
            (
                "Geometry of reality",
                "Light Language uses coloured light and sacred geometry to make clear messages. Clear intention organises what you notice and choose. Introductions often talk about resonance and layered subtle bodies — a way of describing the work, not medical advice.",
            ),
            (
                "A few working points",
                "• Thoughts take part in experience.\n• You are responsible for your choices.\n• As above, so below: many teachers start with the subtler layers rather than forcing only the dense ones.",
            ),
            (
                "Sacred geometry",
                "Colour and geometry are used as tools, not decoration.\nCube — holds focus; steadies a quality in place.\nSphere — opens; invites movement.\nPyramid — sharpens a goal; keeps a fact coherent.\nCylinder — connects two points; strengthens the flow between them.",
            ),
            (
                "Colour",
                "• Red — vitality, physical movement.\n• Yellow — clarity, focus.\n• Green — balance, growth.\n• Blue — rest, space.\n• Purple — reflection, intuition.",
            ),
            (
                "How this is learned",
                "A lot of it is handed down by someone who already lives it — not only read. Work with teachers and printed sources you trust.",
            ),
            (
                "JustBe.Works",
                "Independent notes. Not a copy of the Beginning Light Language Student Manual (2014, © Starr Fuentes). Light Language Grid Creator is a Grid app (shapes, colours, export) — not affiliated with the manual’s publisher.",
            ),
        ],
    ),
    "de": (
        "Beginning Light Language (2014)",
        "Eine kurze Orientierung",
        [
            (
                "Geometrie der Wirklichkeit",
                "Lichtsprache arbeitet mit farbigem Licht und heiliger Geometrie — so entstehen klare Botschaften. Klare Absicht ordnet, was du wahrnimmst und wählst. Einführungen sprechen oft von Resonanz und feineren Körperschichten — eine Beschreibung der Arbeit, kein medizinischer Rat.",
            ),
            (
                "Ein paar Arbeitsregeln",
                "• Gedanken wirken an der Erfahrung mit.\n• Du bist für deine Entscheidungen verantwortlich.\n• Wie oben, so unten: viele Lehrer fangen bei den feineren Schichten an, statt nur am Dichten zu ziehen.",
            ),
            (
                "Heilige Geometrie",
                "Farbe und Geometrie sind Werkzeuge, keine Deko.\nWürfel — hält den Fokus; eine Qualität an Ort und Stelle.\nKugel — öffnet; lädt Bewegung ein.\nPyramide — schärft ein Ziel; hält einen Sachverhalt zusammen.\nZylinder — verbindet zwei Punkte; stärkt den Fluss dazwischen.",
            ),
            (
                "Farbe",
                "• Rot — Vitalität, körperliche Bewegung.\n• Gelb — Klarheit, Fokus.\n• Grün — Balance, Wachstum.\n• Blau — Ruhe, Weite.\n• Violett — Reflexion, Intuition.",
            ),
            (
                "Wie man das lernt",
                "Vieles wird überliefert — von jemandem, der es schon lebt, nicht nur aus dem Buch. Arbeite mit Lehrern und gedruckten Quellen, denen du vertraust.",
            ),
            (
                "JustBe.Works",
                "Eigene Notizen. Keine Kopie des Beginning Light Language Student Manual (2014, © Starr Fuentes). Light Language Grid Creator ist eine Grid-App (Formen, Farben, Export) — nicht verbunden mit dem Verlag des Manuals.",
            ),
        ],
    ),
    "es": (
        "Beginning Light Language (2014)",
        "Una orientación breve",
        [
            (
                "Geometría de la realidad",
                "El lenguaje de luz usa luz de color y geometría sagrada para crear mensajes claros. La intención clara ordena lo que notas y lo que eliges. Las introducciones hablan a menudo de resonancia y cuerpos sutiles — una forma de describir el trabajo, no un consejo médico.",
            ),
            (
                "Algunos puntos de trabajo",
                "• Los pensamientos participan en la experiencia.\n• Eres responsable de tus decisiones.\n• Como es arriba, es abajo: muchas maestras empiezan por las capas más sutiles, no solo por lo denso.",
            ),
            (
                "Geometría sagrada",
                "Color y geometría son herramientas, no adorno.\nCubo — sostiene el foco; fija una cualidad.\nEsfera — abre; invita al movimiento.\nPirámide — afina una meta; mantiene un hecho coherente.\nCilindro — une dos puntos; refuerza el flujo entre ellos.",
            ),
            (
                "Color",
                "• Rojo — vitalidad, movimiento físico.\n• Amarillo — claridad, foco.\n• Verde — equilibrio, crecimiento.\n• Azul — descanso, espacio.\n• Púrpura — reflexión, intuición.",
            ),
            (
                "Cómo se aprende",
                "Gran parte se coge de alguien que ya lo vive — no solo se lee. Trabaja con maestras y fuentes impresas en las que confíes.",
            ),
            (
                "JustBe.Works",
                "Notas propias. No es copia del Beginning Light Language Student Manual (2014, © Starr Fuentes). Light Language Grid Creator es una app de Grid (formas, colores, exportación) — sin afiliación a la editorial del manual.",
            ),
        ],
    ),
    "fr": (
        "Beginning Light Language (2014)",
        "Une orientation courte",
        [
            (
                "Géométrie de la réalité",
                "Le langage de lumière utilise lumière colorée et géométrie sacrée pour créer des messages clairs. L’intention claire organise ce que vous remarquez et ce que vous choisissez. Les introductions parlent souvent de résonance et de corps subtils — une façon de décrire le travail, pas un avis médical.",
            ),
            (
                "Quelques points de travail",
                "• Les pensées participent à l’expérience.\n• Vous êtes responsable de vos choix.\n• Comme en haut, ainsi en bas : beaucoup d’enseignants commencent par les couches plus fines, plutôt que de forcer seulement le dense.",
            ),
            (
                "Géométrie sacrée",
                "Couleur et géométrie sont des outils, pas du décor.\nCube — tient l’attention ; ancre une qualité.\nSphère — ouvre ; invite au mouvement.\nPyramide — affine un but ; tient un fait cohérent.\nCylindre — relie deux points ; renforce le flux entre eux.",
            ),
            (
                "Couleur",
                "• Rouge — vitalité, mouvement physique.\n• Jaune — clarté, focus.\n• Vert — équilibre, croissance.\n• Bleu — repos, espace.\n• Violet — réflexion, intuition.",
            ),
            (
                "Comment on l’apprend",
                "Une grande part se prend auprès de quelqu’un qui le vit déjà — pas seulement dans un livre. Travaillez avec des enseignants et des sources imprimées auxquels vous faites confiance.",
            ),
            (
                "JustBe.Works",
                "Notes indépendantes. Pas une copie du Beginning Light Language Student Manual (2014, © Starr Fuentes). Light Language Grid Creator est une app de Grid (formes, couleurs, export) — sans affiliation à l’éditeur du manuel.",
            ),
        ],
    ),
    "it": (
        "Beginning Light Language (2014)",
        "Un orientamento breve",
        [
            (
                "Geometria della realtà",
                "La lingua di luce usa luce colorata e geometria sacra per creare messaggi chiari. L’intenzione chiara organizza ciò che noti e ciò che scegli. Le introduzioni parlano spesso di risonanza e corpi sottili — un modo di descrivere il lavoro, non un consiglio medico.",
            ),
            (
                "Alcuni punti di lavoro",
                "• I pensieri partecipano all’esperienza.\n• Sei responsabile delle tue scelte.\n• Come sopra, così sotto: molti insegnanti partono dagli strati più sottili, non solo dal denso.",
            ),
            (
                "Geometria sacra",
                "Colore e geometria sono strumenti, non decorazione.\nCubo — tiene il fuoco; ferma una qualità.\nSfera — apre; invita al movimento.\nPiramide — affina un obiettivo; tiene insieme un fatto.\nCilindro — collega due punti; rafforza il flusso tra loro.",
            ),
            (
                "Colore",
                "• Rosso — vitalità, movimento fisico.\n• Giallo — chiarezza, focus.\n• Verde — equilibrio, crescita.\n• Blu — riposo, spazio.\n• Viola — riflessione, intuizione.",
            ),
            (
                "Come si impara",
                "Gran parte si prende da chi lo vive già — non solo dal libro. Lavora con insegnanti e fonti stampate di cui ti fidi.",
            ),
            (
                "JustBe.Works",
                "Note indipendenti. Non è copia del Beginning Light Language Student Manual (2014, © Starr Fuentes). Light Language Grid Creator è un’app per Grid (forme, colori, export) — non affiliata all’editore del manuale.",
            ),
        ],
    ),
    "pt": (
        "Beginning Light Language (2014)",
        "Uma orientação curta",
        [
            (
                "Geometria da realidade",
                "Linguagem de luz usa luz colorida e geometria sagrada para criar mensagens claras. A intenção clara organiza o que notas e o que escolhes. As introduções falam muitas vezes de ressonância e corpos subtis — uma forma de descrever o trabalho, não um conselho médico.",
            ),
            (
                "Alguns pontos de trabalho",
                "• Os pensamentos participam na experiência.\n• És responsável pelas tuas escolhas.\n• Como acima, assim abaixo: muitos professores começam pelas camadas mais subtis, em vez de forçar só o denso.",
            ),
            (
                "Geometria sagrada",
                "Cor e geometria são ferramentas, não decoração.\nCubo — segura o foco; firma uma qualidade.\nEsfera — abre; convida movimento.\nPirâmide — afina um objectivo; mantém um facto coerente.\nCilindro — liga dois pontos; reforça o fluxo entre eles.",
            ),
            (
                "Cor",
                "• Vermelho — vitalidade, movimento físico.\n• Amarelo — clareza, foco.\n• Verde — equilíbrio, crescimento.\n• Azul — descanso, espaço.\n• Roxo — reflexão, intuição.",
            ),
            (
                "Como se aprende",
                "Grande parte apanha-se de quem já o vive — não só do livro. Trabalha com professores e fontes impressas em quem confias.",
            ),
            (
                "JustBe.Works",
                "Notas independentes. Não é cópia do Beginning Light Language Student Manual (2014, © Starr Fuentes). Light Language Grid Creator é uma app de Grid (formas, cores, exportação) — sem ligação à editora do manual.",
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
        pass


def build(code: str) -> Path:
    title, subtitle, sections = TEXTS[code]
    pdf = SummaryPDF(title, subtitle)
    pdf.set_margins(16, 16, 16)
    pdf.set_auto_page_break(True, margin=10)
    pdf.add_font("uni", "", FONT)
    pdf.add_font("uni", "B", FONT)
    pdf.add_page()

    title_h = 3.65
    body_h = 3.55
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
            raise SystemExit(f"Each summary PDF must use a single sheet; {code} has {n}.")


if __name__ == "__main__":
    main()
