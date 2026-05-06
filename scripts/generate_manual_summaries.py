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
        "Study summary",
        [
            (
                "Master the geometry of your reality",
                "Every thought you hold carries a message that shapes how you meet the world. When intention is clear, it organises attention and choice: you move from only reacting to circumstances toward consciously designing them. Many introductions frame this through resonance and layered subtle “bodies”—philosophical imagery, not medical advice.",
            ),
            (
                "Core principles of transformation",
                "• Your thoughts participate in shaping experience.\n• You are responsible for your choices.\n• As above, so below: shifting subtler layers first is often described as gentler than forcing change only at the densest level.",
            ),
            (
                "Sacred geometry — quick reference",
                "Many paths use geometry and colour as levers for clarity—bringing light into the pattern and loosening what no longer fits.\nCube — stabilisation: holds focus; steadies a quality in place.\nSphere — opening: widens options; invites movement.\nPyramid — integration: sharpens a goal; keeps a fact coherent.\nCylinder — connection: bridges two points; strengthens flow between them.",
            ),
            (
                "Colour as frequency",
                "• Red — vitality, physical movement.\n• Yellow — clarity, focus, active intelligence.\n• Green — balance, renewal, growth tone.\n• Blue — rest, spaciousness, easing congested flow imagery.\n• Purple — wisdom tone; reflective intuition.",
            ),
            (
                "Elevate your frequency",
                "Much of this work is “caught” in the field of someone who already lives the tones—not only read in a book. Choosing to live by the pattern, rather than against it, supports creating what you truly need. For depth, study with ethical teachers and printed sources you trust.",
            ),
            (
                "JustBe.Works",
                "Independent summary for orientation; not a copy of the Beginning Light Language Student Manual (2014, © Starr Fuentes). Between classes, Light Language Grid Creator is a visual grid studio (shapes, colours, export)—not affiliated with the manual’s publisher.",
            ),
        ],
    ),
    "de": (
        "Beginning Light Language (2014)",
        "Lernübersicht",
        [
            (
                "Die Geometrie deiner Wirklichkeit meistern",
                "Jeder Gedanke trägt eine Botschaft, die prägt, wie du die Welt triffst. Klare Intention ordnet Aufmerksamkeit und Wahl: du bewegst dich von bloßem Reagieren hin zu bewusstem Gestalten. Viele Einführungen rahmen das über Resonanz und feinere „Körper“-Schichten—philosophisches Bild, kein medizinischer Rat.",
            ),
            (
                "Kernprinzipien der Transformation",
                "• Gedanken wirken an der Erfahrung mit.\n• Du bist für deine Entscheidungen verantwortlich.\n• Wie oben, so unten: zuerst feinere Schichten zu verändern, wird oft als sanfter beschrieben als nur das Dichte zu erzwingen.",
            ),
            (
                "Heilige Geometrie — Kurzüberblick",
                "Viele Wege nutzen Geometrie und Farbe als Hebel für Klarheit—Licht ins Muster, lösen, was nicht mehr passt.\nWürfel — Stabilisierung: Fokus halten; eine Qualität an Ort und Stelle halten.\nKugel — Öffnung: Optionen weiten; Bewegung einladen.\nPyramide — Integration: ein Ziel schärfen; einen Sachverhalt kohärent halten.\nZylinder — Verbindung: zwei Punkte überbrücken; den Fluss zwischen ihnen stärken.",
            ),
            (
                "Farbe als Frequenz",
                "• Rot — Vitalität, körperliche Bewegung.\n• Gelb — Klarheit, Fokus, aktive Intelligenz.\n• Grün — Balance, Erneuerung, Wachstumston.\n• Blau — Ruhe, Weite, Bilder „verstopften“ Flusses lockern.\n• Violett — Weisheitston; reflektive Intuition.",
            ),
            (
                "Frequenz heben",
                "Viel davon wird „mitgefangen“ im Feld von Menschen, die die Töne schon leben—nicht nur im Buch gelesen. Sich dem Muster zuzuwenden statt dagegen zu arbeiten, unterstützt, zu erschaffen, was du wirklich brauchst. Vertiefung: ethische Lehrpersonen und gedruckte Quellen, denen du vertraust.",
            ),
            (
                "JustBe.Works",
                "Unabhängige Kurzfassung zur Orientierung; keine Kopie des Beginning Light Language Student Manual (2014, © Starr Fuentes). Zwischen Workshops: Light Language Grid Creator als visuelles Raster-Studio (Formen, Farben, Export)—nicht verbunden mit dem Verlag des Manuals.",
            ),
        ],
    ),
    "es": (
        "Beginning Light Language (2014)",
        "Resumen de estudio",
        [
            (
                "Domina la geometría de tu realidad",
                "Cada pensamiento lleva un mensaje que moldea cómo te encuentras con el mundo. Cuando la intención es clara, ordena atención y elección: pasas de solo reaccionar a diseñar con más conciencia. Muchas introducciones enmarcan esto con resonancia y cuerpos sutiles en capas—imagen filosófica, no consejo médico.",
            ),
            (
                "Principios centrales de la transformación",
                "• Los pensamientos participan en dar forma a la experiencia.\n• Eres responsable de tus decisiones.\n• Como es arriba, es abajo: cambiar primero capas más sutiles suele describirse como más amable que forzar solo lo denso.",
            ),
            (
                "Geometría sagrada — referencia breve",
                "Muchos caminos usan geometría y color como palancas de claridad—luz al patrón y soltar lo que ya no encaja.\nCubo — estabilización: mantiene el foco; sostiene una cualidad en su sitio.\nEsfera — apertura: amplía opciones; invita al movimiento.\nPirámide — integración: afina una meta; mantiene un hecho coherente.\nCilindro — conexión: une dos puntos; refuerza el flujo entre ellos.",
            ),
            (
                "Color como frecuencia",
                "• Rojo — vitalidad, movimiento físico.\n• Amarillo — claridad, foco, inteligencia activa.\n• Verde — equilibrio, renovación, tono de crecimiento.\n• Azul — descanso, amplitud, imaginería de aliviar flujo congestionado.\n• Púrpura — tono de sabiduría; intuición reflexiva.",
            ),
            (
                "Eleva tu frecuencia",
                "Mucho de esto se “atrapa” en el campo de quien ya vive los tonos—no solo se lee en un libro. Alinearse con el patrón, en lugar de luchar contra él, ayuda a crear lo que realmente necesitas. Para profundizar: maestros éticos y fuentes impresas de confianza.",
            ),
            (
                "JustBe.Works",
                "Resumen independiente para orientación; no es copia del Beginning Light Language Student Manual (2014, © Starr Fuentes). Entre clases, Light Language Grid Creator es un estudio visual en cuadrícula (formas, colores, exportación)—sin afiliación a la editorial del manual.",
            ),
        ],
    ),
    "fr": (
        "Beginning Light Language (2014)",
        "Résumé d’étude",
        [
            (
                "Maîtriser la géométrie de votre réalité",
                "Chaque pensée porte un message qui façonne votre rencontre avec le monde. Quand l’intention est claire, elle organise attention et choix : vous passez de la simple réaction à une mise en forme plus consciente. Beaucoup d’introductions cadreront cela par résonance et « corps » subtils superposés—image philosophique, pas avis médical.",
            ),
            (
                "Principes de transformation",
                "• Les pensées participent à façonner l’expérience.\n• Vous êtes responsable de vos choix.\n• Comme en haut, ainsi en bas : ajuster d’abord les couches fines est souvent présenté comme plus doux que de forcer seulement le dense.",
            ),
            (
                "Géométrie sacrée — aide-mémoire",
                "Plusieurs voies utilisent géométrie et couleur comme leviers de clarté—lumière dans le motif, relâcher ce qui ne convient plus.\nCube — stabilisation : fixe l’attention ; ancre une qualité.\nSphère — ouverture : élargit les options ; invite au mouvement.\nPyramide — intégration : affine un but ; garde un fait cohérent.\nCylindre — connexion : relie deux points ; renforce le flux entre eux.",
            ),
            (
                "Couleur comme fréquence",
                "• Rouge — vitalité, mouvement physique.\n• Jaune — clarté, focus, intelligence active.\n• Vert — équilibre, renouveau, ton de croissance.\n• Bleu — repos, espace, imagerie d’apaisement de flux encombré.\n• Violet — ton de sagesse ; intuition réflexive.",
            ),
            (
                "Élevez votre fréquence",
                "Beaucoup de ce travail se « attrape » dans le champ de personnes qui vivent déjà les tonalités—pas seulement dans un livre. S’aligner sur la loi plutôt que lutter soutient ce dont vous avez vraiment besoin. Pour la profondeur : enseignants éthiques et sources imprimées de confiance.",
            ),
            (
                "JustBe.Works",
                "Synthèse indépendante pour orientation ; pas une copie du Beginning Light Language Student Manual (2014, © Starr Fuentes). Entre les cours, Light Language Grid Creator est un studio grille visuel (formes, couleurs, export)—sans affiliation à l’éditeur du manuel.",
            ),
        ],
    ),
    "it": (
        "Beginning Light Language (2014)",
        "Riassunto di studio",
        [
            (
                "Padroneggia la geometria della tua realtà",
                "Ogni pensiero porta un messaggio che modella come incontri il mondo. Quando l’intenzione è chiara, organizza attenzione e scelta: passi dal solo reagire a progettare con più coscienza. Molte introduzioni incorniciano tutto con risonanza e corpi sottili stratificati—immagine filosofica, non consiglio medico.",
            ),
            (
                "Principi della trasformazione",
                "• I pensieri partecipano a dare forma all’esperienza.\n• Sei responsabile delle tue scelte.\n• Come sopra, così sotto: cambiare prima strati più sottili è spesso descritto come più gentile che forzare solo il denso.",
            ),
            (
                "Geometria sacra — sintesi",
                "Molti percorsi usano geometria e colore come leve di chiarezza—luce nel motivo, sciogliere ciò che non serve più.\nCubo — stabilizzazione: tiene il fuoco; sostiene una qualità al posto.\nSfera — apertura: allarga le opzioni; invita al movimento.\nPiramide — integrazione: affina un obiettivo; mantiene un fatto coerente.\nCilindro — connessione: collega due punti; rafforza il flusso tra loro.",
            ),
            (
                "Colore come frequenza",
                "• Rosso — vitalità, movimento fisico.\n• Giallo — chiarezza, focus, intelligenza attiva.\n• Verde — equilibrio, rinnovo, tono di crescita.\n• Blu — riposo, spazio, immaginario di alleggerire flusso congestionato.\n• Viola — tono di saggezza; intuizione riflessiva.",
            ),
            (
                "Alza la frequenza",
                "Molto di questo lavoro si «prende» nel campo di chi vive già i toni—non solo si legge in un libro. Allinearsi al motivo piuttosto che combatterlo sostiene ciò che davvero ti serve. Per approfondire: insegnanti etici e fonti stampate di fiducia.",
            ),
            (
                "JustBe.Works",
                "Riassunto indipendente per orientamento; non è copia del Beginning Light Language Student Manual (2014, © Starr Fuentes). Tra le lezioni, Light Language Grid Creator è uno studio griglia visivo (forme, colori, export)—non affiliato all’editore del manuale.",
            ),
        ],
    ),
    "pt": (
        "Beginning Light Language (2014)",
        "Resumo de estudo",
        [
            (
                "Domina a geometria da tua realidade",
                "Cada pensamento traz uma mensagem que molda como encontras o mundo. Quando a intenção é clara, organiza atenção e escolha: passas de apenas reagir a desenhar com mais consciência. Muitas introduções enquadram isto com ressonância e corpos subtis em camadas—imagem filosófica, não conselho médico.",
            ),
            (
                "Princípios centrais da transformação",
                "• Os pensamentos participam em dar forma à experiência.\n• És responsável pelas tuas escolhas.\n• Como acima, assim abaixo: mudar primeiro camadas mais sutis costuma ser descrito como mais suave do que forçar só o denso.",
            ),
            (
                "Geometria sagrada — referência rápida",
                "Muitos caminhos usam geometria e cor como alavancas de clareza—luz no padrão, soltar o que já não serve.\nCubo — estabilização: mantém foco; sustém uma qualidade no lugar.\nEsfera — abertura: alarga opções; convida movimento.\nPirâmide — integração: afina um objetivo; mantém um facto coerente.\nCilindro — ligação: une dois pontos; reforça o fluxo entre eles.",
            ),
            (
                "Cor como frequência",
                "• Vermelho — vitalidade, movimento físico.\n• Amarelo — clareza, foco, inteligência ativa.\n• Verde — equilíbrio, renovação, tom de crescimento.\n• Azul — descanso, amplitude, imagética de aliviar fluxo congestionado.\n• Roxo — tom de sabedoria; intuição reflexiva.",
            ),
            (
                "Eleva a tua frequência",
                "Muito disto é «apanhado» no campo de quem já vive os tons—não só lido num livro. Alinhar-te ao padrão, em vez de lutar contra ele, apoia criar o que realmente precisas. Para aprofundar: mestres éticos e fontes impressas de confiança.",
            ),
            (
                "JustBe.Works",
                "Resumo independente para orientação; não é cópia do Beginning Light Language Student Manual (2014, © Starr Fuentes). Entre aulas, Light Language Grid Creator é um estúdio de grelha visual (formas, cores, exportação)—sem filiação à editora do manual.",
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
