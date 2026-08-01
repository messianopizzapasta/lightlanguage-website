#!/usr/bin/env python3
"""Write rewritten Learn vocabulary JSON (EN + DE) for the JustBe.Works website."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_EN = ROOT / "docs" / "grid-vocabulary" / "learn-vocabulary.en.json"
OUT_DE = ROOT / "docs" / "grid-vocabulary" / "learn-vocabulary.de.json"

EN = {
    "title": "Grid vocabulary: shapes, sets & stages",
    "disclaimer": (
        "Original reference notes for personal study with Light Language Grid Creator. "
        "Rewritten in our own words for JustBe.Works — not a substitute for live teacher training "
        "or the Beginning Light Language Student Manual lineage."
    ),
    "intros": {
        "shapes": (
            "Each three-dimensional form acts like a lens: it steadies, opens, filters, or redirects "
            "intention on the grid. Pair a shape with colour; the short keyword on a cell is a reminder, "
            "not the whole story."
        ),
        "sets": (
            "A set is a fixed stack of shape-and-colour pairs. In a 7×7 grid it belongs in column 1 and "
            "column 7. Read its flow from bottom to top. Ask: Where in the body — or where in daily life — "
            "does this imbalance show up? Where do you want to activate and strengthen this living flow?"
        ),
        "stages": (
            "A stage is another fixed stack of shape-and-colour pairs. In a 7×7 grid it belongs in column 2 "
            "and column 6. Read its flow from top to bottom. Ask: How did this pattern or imbalance enter "
            "my life? Which desired pattern do you want to consciously bring into your life and anchor "
            "with this stage?"
        ),
    },
    "sections": [
        {
            "id": "shapes",
            "title": "Shapes",
            "items": [
                {
                    "id": "cube",
                    "title": "Cube",
                    "summary": "Steadies, contains, and can feel limiting.",
                    "body": (
                        "Six equal square faces make the cube one of the most grounding Platonic forms. "
                        "It can hold energy at the centre and define a clear box of reality. "
                        "Use it when structure, containment, or firm boundaries are needed — knowing that "
                        "too much cube can feel tight."
                    ),
                },
                {
                    "id": "sphere",
                    "title": "Sphere",
                    "summary": "Opens movement and many directions at once.",
                    "body": (
                        "With no corners, the sphere keeps energy rolling smoothly around a centre. "
                        "It suggests harmony and a full circle of options — everything visible from the middle. "
                        "Reach for a sphere when you want momentum, wholeness, or a gentle start."
                    ),
                },
                {
                    "id": "pyramid",
                    "title": "Pyramid",
                    "summary": "Integrates, preserves, and sharpens focus.",
                    "body": (
                        "Four triangular sides meeting a square base make the pyramid a classic vessel for "
                        "cultivation. It helps energies mature rather than scatter. "
                        "Choose it when something needs time to ripen, be protected, or be brought into one point."
                    ),
                },
                {
                    "id": "cone",
                    "title": "Cone",
                    "summary": "Gathers and assimilates quickly.",
                    "body": (
                        "The hollow cone channels flow between two poles — narrowing as it moves. "
                        "Energy can spiral inward like a coin circling a funnel before it drops through. "
                        "Use it for gentle uptake, direction, or quick integration."
                    ),
                },
                {
                    "id": "megaphone",
                    "title": "Megaphone cone",
                    "summary": "Amplifies and sends energy outward.",
                    "body": (
                        "A cone turned to broadcast rather than absorb. "
                        "It declares, announces, or pushes intention into the field. "
                        "Helpful when a message needs volume without losing a single direction."
                    ),
                },
                {
                    "id": "focuscone",
                    "title": "Focus cone",
                    "summary": "Collects scattered attention inward.",
                    "body": (
                        "The inward-facing cone gathers choices back to one centre. "
                        "It supports concentration, listening, and precise aim. "
                        "Use it when noise needs to quiet and one path should stand out."
                    ),
                },
                {
                    "id": "cylinder",
                    "title": "Cylinder",
                    "summary": "Connects, confirms, and clarifies understanding.",
                    "body": (
                        "A solid tube links two sides without corners breaking the line. "
                        "What passes through is strengthened as understanding; what does not belong to knowing "
                        "can fall away. Reach for a cylinder when rapport, proof, or clean transmission matters."
                    ),
                },
                {
                    "id": "dodecahedron",
                    "title": "Dodecahedron",
                    "summary": "Offers twelve distinct paths — enough, not infinite.",
                    "body": (
                        "Twelve pentagonal faces give structured choice without overwhelm. "
                        "It lifts perspective slightly above the problem so decisions can be compared. "
                        "Useful when you need options, but not an endless list."
                    ),
                },
                {
                    "id": "octahedron",
                    "title": "Octahedron",
                    "summary": "Balances above and below; filters and refines.",
                    "body": (
                        "Two pyramids joined at the base mirror spirit and matter meeting in the heart. "
                        "It weaves between subtle and physical levels. "
                        "Choose it to clarify, sort, or polish what is true from what is residue."
                    ),
                },
                {
                    "id": "icosahedron",
                    "title": "Icosahedron",
                    "summary": "Expands gently and multiplies possibilities.",
                    "body": (
                        "Twenty triangular faces stretch outward from a sphere-like core. "
                        "Growth happens evenly — one facet moving pulls the whole. "
                        "Use when you want more room, more reasonable choices, or soft amplification."
                    ),
                },
                {
                    "id": "mobius",
                    "title": "Möbius strip",
                    "summary": "Repeats growth while staying linked.",
                    "body": (
                        "One side, one loop — the strip models continuity and recursion. "
                        "It echoes what was first intended while allowing change. "
                        "Use alone or between other shapes when connection must survive transformation."
                    ),
                },
                {
                    "id": "double_spiral",
                    "title": "Double spiral",
                    "summary": "Verifies and links — like a second reading.",
                    "body": (
                        "One spiral descends while the other rises, echoing paired strands in living codes. "
                        "It checks information against the original pattern. "
                        "In column stacks it also bridges neighbouring shapes."
                    ),
                },
                {
                    "id": "torus",
                    "title": "Torus",
                    "summary": "Keeps what nourishes; releases what drains.",
                    "body": (
                        "The ring shape circulates energy around a hollow centre. "
                        "With clear intention, vitality stays on the ring while what no longer serves can exit "
                        "through the middle. Use to invite in or let go — never both at once without focus."
                    ),
                },
                {
                    "id": "tetrahedron",
                    "title": "Tetrahedron",
                    "summary": "Simplest volume — sparks manifestation.",
                    "body": (
                        "Four triangular faces form the leanest Platonic solid. "
                        "It points energy toward action and ignition with little ornament. "
                        "Reach for it when something needs to start, flame, or commit to form."
                    ),
                },
            ],
        },
        {
            "id": "sets",
            "title": "Sets",
            "items": [
                {
                    "id": "circulatory",
                    "title": "Circulatory",
                    "summary": "Heart, blood, vessels — circulation in body and life.",
                    "body": (
                        "Covers the cardiovascular system: heart, arteries, veins, capillaries, and blood. "
                        "On the grid it can support networking, travel, rhythm, budgeting, or getting the word out — "
                        "anywhere life force needs to move and refresh."
                    ),
                },
                {
                    "id": "digestive",
                    "title": "Digestive",
                    "summary": "Intake, processing, and release.",
                    "body": (
                        "From first bite to final elimination — and metaphorically, from new information to "
                        "integrated knowing. Choose it when you swallow things whole, delay finishing, or need "
                        "to clear what no longer belongs."
                    ),
                },
                {
                    "id": "gland",
                    "title": "Gland",
                    "summary": "Hormonal balance and slow, deep adjustment.",
                    "body": (
                        "The endocrine system sends chemical messages more slowly than nerves — steady tuning "
                        "of the whole organism. On the grid it helps long-term balance, such as home and work, "
                        "or measured change that lasts."
                    ),
                },
                {
                    "id": "lymph",
                    "title": "Lymph",
                    "summary": "Cleaning on physical and subtle levels.",
                    "body": (
                        "The lymphatic system clears toxins and infection, and in this lineage also touches "
                        "subtle bodies that surround the physical form. Use when life — or a room — needs a deep "
                        "wash and fresh order."
                    ),
                },
                {
                    "id": "muscular",
                    "title": "Muscular",
                    "summary": "Movement, effort, and flexible strength.",
                    "body": (
                        "Muscles, tendons, and fascia show how we act in the world. "
                        "They stretch when we expand and contract when we push. "
                        "Choose this set when will feels stuck or a project needs real backing."
                    ),
                },
                {
                    "id": "nervous",
                    "title": "Nervous",
                    "summary": "Fast signals — brain, spine, and nerves.",
                    "body": (
                        "The nervous system carries quick messages in and out. "
                        "Use for clear decisions, clean communication, or when mental pathways feel overloaded "
                        "or frayed."
                    ),
                },
                {
                    "id": "reproductive",
                    "title": "Reproductive",
                    "summary": "Creation, intimacy, and repeatable patterns.",
                    "body": (
                        "Covers sexual and reproductive themes — partnership, children, and any pattern meant "
                        "to copy itself. Helpful when asking whether to stay, begin, or reproduce an idea, product, "
                        "or relationship."
                    ),
                },
                {
                    "id": "respiratory",
                    "title": "Respiratory",
                    "summary": "Breath, expression, and participation in life.",
                    "body": (
                        "Lungs and airways mirror how fully we take life in and let it out. "
                        "Breath resets electromagnetic rhythm. On the grid it can support being talked about, "
                        "referred, or visibly present when you have already put work into the world."
                    ),
                },
                {
                    "id": "skeletal",
                    "title": "Skeletal",
                    "summary": "Bones, framework, and foundation.",
                    "body": (
                        "Bones, cartilage, and ligaments hold the upright structure. "
                        "Every project and relationship has a skeleton too. "
                        "Use when starting something new or when the foundation feels threatened or brittle."
                    ),
                },
                {
                    "id": "integumentary",
                    "title": "Integumentary",
                    "summary": "Skin, hair, nails — boundary with the world.",
                    "body": (
                        "The skin envelope breathes, senses, and shields. "
                        "It marks where you end and the environment begins. "
                        "Choose for boundary work, self-image, temperature of emotion, and interface with "
                        "surroundings."
                    ),
                },
                {
                    "id": "urinary",
                    "title": "Urinary",
                    "summary": "Filtering fluids — discernment and inner inquiry.",
                    "body": (
                        "Kidneys and bladder regulate what stays and what leaves as liquid waste. "
                        "Symbolically this set supports sorting truth from noise, intimacy with oneself, and "
                        "honest self-reflection — not punishment, but clarity."
                    ),
                },
                {
                    "id": "immune_system",
                    "title": "Immune system",
                    "summary": "Recognition, defense, and resilient boundaries.",
                    "body": (
                        "The immune system distinguishes self from foreign and responds without needless war. "
                        "On the grid it supports healthy protection — saying no, recovering after strain, and "
                        "staying open only where safe. Pair with teacher guidance for serious medical questions."
                    ),
                },
            ],
        },
        {
            "id": "stages",
            "title": "Stages",
            "items": [
                {
                    "id": "integrity",
                    "title": "Integrity",
                    "summary": "Truth, authenticity, and alignment with self.",
                    "body": (
                        "When inner values and outer life diverge, integrity stage asks you to walk what you "
                        "believe. It supports releasing shame, blame, and manipulation — and growing trust, "
                        "simplicity, and direct knowing."
                    ),
                },
                {
                    "id": "social",
                    "title": "Social",
                    "summary": "Peer pressure and fitting in.",
                    "body": (
                        "Many patterns formed after puberty to please a group — colds, flus, and certain "
                        "habits often carry a social message. Use when you changed yourself to belong or keep "
                        "pace with others."
                    ),
                },
                {
                    "id": "holographic",
                    "title": "Holographic",
                    "summary": "The whole lives in every part.",
                    "body": (
                        "Some imprints are not linear stories but fields — each fragment contains the entire "
                        "pattern, like a hologram. Choose this stage when issues feel multidimensional, ancestral, "
                        "or repeated across unrelated areas of life at once."
                    ),
                },
                {
                    "id": "reactive",
                    "title": "Reactive",
                    "summary": "Automatic responses and allergies.",
                    "body": (
                        "Covers knee-jerk reactions — including living in anticipation of someone else's anger "
                        "or approval. Also relevant for reactive conditions such as allergies where the body "
                        "answers before the mind catches up."
                    ),
                },
                {
                    "id": "building",
                    "title": "Building",
                    "summary": "Commitment to make something work.",
                    "body": (
                        "Literal buildings, businesses, relationships, or any structure you intend to finish. "
                        "Use when stuck mid-construction or ready to invest for the long term. "
                        "Pairs naturally with the skeletal set for physical projects."
                    ),
                },
                {
                    "id": "genetic",
                    "title": "Genetic",
                    "summary": "Patterns passed through family lines.",
                    "body": (
                        "When imbalance travels generations, healing one member can soften the field for others. "
                        "Raise vibration or process the story consciously. "
                        "Includes inherited lifestyle limits as well as named hereditary conditions."
                    ),
                },
                {
                    "id": "alignment",
                    "title": "Alignment",
                    "summary": "Matching present frequency with systems around you.",
                    "body": (
                        "Bridges you with environments, institutions, or tools that no longer fit your current "
                        "level. Use to release outdated beliefs, fear-based habits, or mismatched solutions — "
                        "and to detach without drama."
                    ),
                },
                {
                    "id": "pattern",
                    "title": "Pattern",
                    "summary": "Self-created loops and habits.",
                    "body": (
                        "Distinct from genetics or environment — patterns you wrote yourself: addictions, "
                        "impulse, recurring failure, or work habits that sabotage. "
                        "Choose when the same scene keeps replaying with your signature on it."
                    ),
                },
                {
                    "id": "environmental",
                    "title": "Environmental",
                    "summary": "Shaped by place, culture, or conditions.",
                    "body": (
                        "Poverty, abuse, prejudice, or rebellion against a hyper-neat childhood home all belong "
                        "here. Not everyone is equally sensitive — personality matters. "
                        "Use when the setting itself taught the imbalance."
                    ),
                },
                {
                    "id": "competitive",
                    "title": "Competitive",
                    "summary": "Rivalry, control, and spotlight.",
                    "body": (
                        "When dis-ease grows from needing to win, dominate, or rebel against control. "
                        "Includes lime-lighting and power struggles. "
                        "Ask whether the grid should soften competition or redirect it into fair play."
                    ),
                },
                {
                    "id": "attitudinal",
                    "title": "Attitudinal",
                    "summary": "Ego, judgment, and rank.",
                    "body": (
                        "Attitude — superiority, inferiority, professional identity — can crystallize imbalance. "
                        "Models, politicians, and experts are archetypes, yet anyone can need this stage when "
                        "self-esteem or anger is frozen in a pose."
                    ),
                },
                {
                    "id": "city",
                    "title": "City",
                    "summary": "Community grids and collective nervous systems.",
                    "body": (
                        "For groups sharing something in common — a town, a demographic, even a species in a "
                        "region. Often used in community grids; sometimes with nervous-system themes such as "
                        "depression or cognitive decline at scale."
                    ),
                },
            ],
        },
    ],
}

DE = {
    "title": "Raster-Vokabular: Formen, Sets & Stufen",
    "disclaimer": (
        "Eigene Referenznotizen für die Arbeit mit Light Language Grid Creator. "
        "In unseren Worten neu formuliert für JustBe.Works — kein Ersatz für live Unterweisung "
        "oder die Beginning Light Language Student Manual-Linie."
    ),
    "intros": {
        "shapes": (
            "Jede dreidimensionale Form wirkt wie eine Linse: sie stabilisiert, öffnet, filtert oder lenkt "
            "Intention im Raster. Form plus Farbe zusammen — das kurze Stichwort in der Zelle ist ein Merker, "
            "nicht die ganze Geschichte."
        ),
        "sets": (
            "Ein Set ist ein fester Stapel aus Form- und Farbkombinationen. Im 7×7-Grid gehört es in Spalte 1 "
            "und Spalte 7. Lies den Fluss von unten nach oben. Frage: Wo im Körper — oder wo im Alltag — "
            "zeigt sich dieses Ungleichgewicht? Wo willst du diesen lebendigen Fluss aktivieren und stärken?"
        ),
        "stages": (
            "Ein Stage ist ebenfalls ein fester Stapel aus Form- und Farbkombinationen. Im 7×7-Grid gehört "
            "sie in Spalte 2 und Spalte 6. Lies den Fluss von oben nach unten. Frage: Wie ist dieses Muster "
            "oder Ungleichgewicht in mein Leben gekommen? Welches gewünschte Muster willst du mit diesem "
            "Stage bewusst in dein Leben bringen und verankern?"
        ),
    },
    "sections": [
        {
            "id": "shapes",
            "title": "Formen",
            "items": [
                {
                    "id": "cube",
                    "title": "Würfel",
                    "summary": "Stabilisiert, umschließt — kann begrenzend wirken.",
                    "body": (
                        "Sechs gleiche Quadratflächen machen den Würfel zu einer der erdendsten platonischen Formen. "
                        "Er kann Energie in der Mitte halten und eine klare Box der Realität definieren. "
                        "Nutze ihn, wenn Struktur, Begrenzung oder feste Grenzen nötig sind — wissend, dass zu viel "
                        "Würfel beengend wirken kann."
                    ),
                },
                {
                    "id": "sphere",
                    "title": "Kugel",
                    "summary": "Öffnet Bewegung und viele Richtungen zugleich.",
                    "body": (
                        "Ohne Ecken rollt die Kugel Energie sanft um ein Zentrum. "
                        "Sie steht für Harmonie und einen vollen Kreis von Möglichkeiten — alles von der Mitte aus sichtbar. "
                        "Greif zu ihr, wenn Schwung, Ganzheit oder ein sanfter Anfang gesucht sind."
                    ),
                },
                {
                    "id": "pyramid",
                    "title": "Pyramide",
                    "summary": "Integriert, bewahrt und schärft den Fokus.",
                    "body": (
                        "Vier Dreiecksflächen auf quadratischer Basis machen die Pyramide zum klassischen Gefäß für Reifung. "
                        "Sie hilft, Energie zu sammeln statt zu zerstreuen. "
                        "Wähle sie, wenn etwas Zeit, Schutz oder einen gemeinsamen Punkt braucht."
                    ),
                },
                {
                    "id": "cone",
                    "title": "Kegel",
                    "summary": "Sammelt und assimiliert schnell.",
                    "body": (
                        "Der hohle Kegel leitet Fluss zwischen zwei Polen — er wird enger, je weiter er geht. "
                        "Energie kann sich spiralförmig nach innen bewegen, bevor sie durchtritt. "
                        "Nutze ihn für sanfte Aufnahme, Richtung oder schnelle Integration."
                    ),
                },
                {
                    "id": "megaphone",
                    "title": "Megafon-Kegel",
                    "summary": "Verstärkt und sendet Energie nach außen.",
                    "body": (
                        "Ein Kegel zum Ausstrahlen statt zum Aufsaugen. "
                        "Er ruft aus, kündigt an oder trägt Intention ins Feld. "
                        "Hilfreich, wenn eine Botschaft laut genug sein soll, ohne die Richtung zu verlieren."
                    ),
                },
                {
                    "id": "focuscone",
                    "title": "Fokus-Kegel",
                    "summary": "Sammelt zerstreute Aufmerksamkeit nach innen.",
                    "body": (
                        "Der nach innen gerichtete Kegel führt Wahlmöglichkeiten zurück zu einem Zentrum. "
                        "Er unterstützt Konzentration, Zuhören und präzises Zielen. "
                        "Nutze ihn, wenn es ruhiger werden soll und ein Weg klar hervortreten soll."
                    ),
                },
                {
                    "id": "cylinder",
                    "title": "Zylinder",
                    "summary": "Verbindet, bestätigt, klärt Verständnis.",
                    "body": (
                        "Ein durchgehender Zylinder verbindet zwei Seiten ohne brechende Ecken. "
                        "Was hindurchgeht, wird als Verstehen gestärkt; was nicht zum Wissen gehört, kann fallen. "
                        "Greif zu ihm, wenn Verbindung, Bestätigung oder klare Übertragung zählen."
                    ),
                },
                {
                    "id": "dodecahedron",
                    "title": "Dodekaeder",
                    "summary": "Zwölf Wege — genug Optionen, nicht unendlich.",
                    "body": (
                        "Zwölf pentagonale Flächen geben strukturierte Wahl ohne Überforderung. "
                        "Er hebt den Blick leicht über das Problem, damit Entscheidungen vergleichbar werden. "
                        "Nützlich, wenn Optionen nötig sind, aber keine endlose Liste."
                    ),
                },
                {
                    "id": "octahedron",
                    "title": "Oktaeder",
                    "summary": "Balanciert oben und unten; filtert und verfeinert.",
                    "body": (
                        "Zwei an der Basis verbundene Pyramiden spiegeln Geist und Materie im Herzen. "
                        "Er webt zwischen feinstofflicher und physischer Ebene. "
                        "Wähle ihn zum Klären, Sortieren oder Polieren des Wahren vom Ballast."
                    ),
                },
                {
                    "id": "icosahedron",
                    "title": "Ikosaeder",
                    "summary": "Dehnt sanft aus und vervielfacht Möglichkeiten.",
                    "body": (
                        "Zwanzig Dreiecksflächen strecken sich von einem kugelähnlichen Kern weg. "
                        "Wachstum geschieht gleichmäßig — bewegt sich eine Facette, folgt das Ganze. "
                        "Nutze ihn für mehr Raum, mehr vertretbare Wahlmöglichkeiten oder sanfte Verstärkung."
                    ),
                },
                {
                    "id": "mobius",
                    "title": "Möbius-Band",
                    "summary": "Wiederholt Wachstum und bleibt verbunden.",
                    "body": (
                        "Eine Seite, eine Schleife — das Band modelliert Kontinuität und Wiederkehr. "
                        "Es trägt die erste Intention weiter und erlaubt zugleich Wandel. "
                        "Allein oder zwischen anderen Formen, wenn Verbindung Transformation überstehen soll."
                    ),
                },
                {
                    "id": "double_spiral",
                    "title": "Doppelspirale",
                    "summary": "Prüft nach und verknüpft — wie eine zweite Lesart.",
                    "body": (
                        "Eine Spirale steigt, die andere sinkt — ähnlich gepaarten Strängen im Lebendigen. "
                        "Sie vergleicht Information mit dem Ursprungsmuster. "
                        "In Spalten-Stapeln verbindet sie auch benachbarte Formen."
                    ),
                },
                {
                    "id": "torus",
                    "title": "Torus",
                    "summary": "Behält Nährendes; lässt Entziehendes gehen.",
                    "body": (
                        "Die Ringform zirkuliert Energie um eine hohle Mitte. "
                        "Mit klarer Intention bleibt Lebendiges am Ring; was nicht mehr dient, kann durch die Mitte "
                        "austreten. Zum Anziehen oder Loslassen — nicht beides zugleich ohne Fokus."
                    ),
                },
                {
                    "id": "tetrahedron",
                    "title": "Tetraeder",
                    "summary": "Einfachstes Volumen — entzündet Manifestation.",
                    "body": (
                        "Vier Dreiecksflächen bilden den schlanksten platonischen Körper. "
                        "Er richtet Energie auf Handlung und Entflammung mit wenig Ornament. "
                        "Greif zu ihm, wenn etwas beginnen, aufflammen oder Form annehmen soll."
                    ),
                },
            ],
        },
        {
            "id": "sets",
            "title": "Sets",
            "items": [
                {
                    "id": "circulatory",
                    "title": "Kreislauf",
                    "summary": "Herz, Blut, Gefäße — Zirkulation im Körper und Leben.",
                    "body": (
                        "Umfasst das Herz-Kreislauf-System: Herz, Arterien, Venen, Kapillaren und Blut. "
                        "Im Raster kann es Vernetzung, Reisen, Rhythmus, Budget oder Sichtbarkeit stützen — "
                        "überall, wo Lebensstrom fließen und sich erneuern soll."
                    ),
                },
                {
                    "id": "digestive",
                    "title": "Verdauung",
                    "summary": "Aufnahme, Verarbeitung und Loslassen.",
                    "body": (
                        "Vom ersten Biss bis zur Ausscheidung — und bildlich von neuer Information zu "
                        "integriertem Wissen. Wähle es, wenn du Dinge ungekaut schluckst, Abschlüsse schiebst "
                        "oder loslassen musst, was nicht mehr gehört."
                    ),
                },
                {
                    "id": "gland",
                    "title": "Drüsen",
                    "summary": "Hormonelle Balance und langsame, tiefe Anpassung.",
                    "body": (
                        "Das endokrine System sendet chemische Botschaften langsamer als Nerven — stetiges Feintuning "
                        "des Ganzen. Im Raster hilft es bei langfristiger Balance, etwa Beruf und Zuhause, "
                        "oder bei maßvollen, haltbaren Veränderungen."
                    ),
                },
                {
                    "id": "lymph",
                    "title": "Lymph",
                    "summary": "Reinigung auf physischer und feiner Ebene.",
                    "body": (
                        "Das Lymphsystem beseitigt Toxine und Infektionen; in dieser Linie berührt es auch feinere "
                        "Hüllen um den physischen Körper. Nutze es, wenn Leben — oder ein Raum — eine gründliche "
                        "Wäsche und neue Ordnung braucht."
                    ),
                },
                {
                    "id": "muscular",
                    "title": "Muskulatur",
                    "summary": "Bewegung, Kraft und flexible Stärke.",
                    "body": (
                        "Muskeln, Sehnen und Faszien zeigen, wie wir in der Welt handeln. "
                        "Sie dehnen sich beim Expandieren und ziehen sich beim Drücken zusammen. "
                        "Wähle dieses Set, wenn der Wille feststeckt oder ein Vorhaben echte Rückendeckung braucht."
                    ),
                },
                {
                    "id": "nervous",
                    "title": "Nervensystem",
                    "summary": "Schnelle Signale — Gehirn, Rückenmark, Nerven.",
                    "body": (
                        "Das Nervensystem überträgt rasch Nachrichten hinein und hinaus. "
                        "Nutze es für klare Entscheidungen, saubere Kommunikation oder wenn mentale Bahnen "
                        "überladen oder ausgefranzt wirken."
                    ),
                },
                {
                    "id": "reproductive",
                    "title": "Fortpflanzung",
                    "summary": "Schöpfung, Intimität und wiederholbare Muster.",
                    "body": (
                        "Betrifft sexuelle und reproduktive Themen — Partnerschaft, Kinder und jedes Muster, "
                        "das sich kopieren soll. Hilfreich, wenn du fragst, ob du bleiben, beginnen oder eine Idee, "
                        "ein Produkt oder eine Beziehung reproduzieren willst."
                    ),
                },
                {
                    "id": "respiratory",
                    "title": "Atmung",
                    "summary": "Atem, Ausdruck und Teilnahme am Leben.",
                    "body": (
                        "Lunge und Atemwege spiegeln, wie voll wir am Leben teilnehmen und es wieder ausströmen lassen. "
                        "Atem setzt elektromagnetischen Rhythmus neu. Im Raster kann es unterstützen, wenn du "
                        "empfohlen oder sichtbar werden willst, nachdem du bereits Arbeit in die Welt gelegt hast."
                    ),
                },
                {
                    "id": "skeletal",
                    "title": "Skelett",
                    "summary": "Knochen, Gerüst und Fundament.",
                    "body": (
                        "Knochen, Knorpel und Bänder tragen die aufrechte Struktur. "
                        "Jedes Projekt und jede Beziehung hat auch ein Skelett. "
                        "Nutze es beim Neubeginn oder wenn das Fundament bedroht oder brüchig wirkt."
                    ),
                },
                {
                    "id": "integumentary",
                    "title": "Haut & Begrenzung",
                    "summary": "Haut, Haare, Nägel — Grenze zur Welt.",
                    "body": (
                        "Die Hülle atmet, nimmt wahr und schützt. "
                        "Sie markiert, wo du endest und die Umgebung beginnt. "
                        "Wähle es für Grenzarbeit, Selbstbild, emotionale Temperatur und den Kontakt zur Umgebung."
                    ),
                },
                {
                    "id": "urinary",
                    "title": "Harnsystem",
                    "summary": "Flüssigkeiten filtern — Unterscheidung und Selbstbefragung.",
                    "body": (
                        "Nieren und Blase regulieren, was bleibt und was als Flüssigkeit geht. "
                        "Symbolisch unterstützt dieses Set, Wahres vom Rauschen zu trennen, Intimität mit sich "
                        "selbst und ehrliche Selbstreflexion — nicht Strafe, sondern Klarheit."
                    ),
                },
                {
                    "id": "immune_system",
                    "title": "Immunsystem",
                    "summary": "Erkennung, Abwehr und widerstandsfähige Grenzen.",
                    "body": (
                        "Das Immunsystem unterscheidet Eigenes von Fremdem und reagiert ohne unnötigen Krieg. "
                        "Im Raster stützt es gesunden Schutz — Nein sagen, Erholung nach Belastung und nur dort "
                        "offen bleiben, wo es sicher ist. Bei ernsten medizinischen Fragen Lehrperson hinzuziehen."
                    ),
                },
            ],
        },
        {
            "id": "stages",
            "title": "Stufen",
            "items": [
                {
                    "id": "integrity",
                    "title": "Integrität",
                    "summary": "Wahrheit, Authentizität und Übereinstimmung mit dem Selbst.",
                    "body": (
                        "Wenn innere Werte und äußeres Leben auseinanderlaufen, fragt diese Stufe, ob du lebst, "
                        "was du glaubst. Sie unterstützt das Loslassen von Scham, Schuld und Manipulation — "
                        "und das Wachsen von Vertrauen, Einfachheit und direktem Wissen."
                    ),
                },
                {
                    "id": "social",
                    "title": "Sozial",
                    "summary": "Gruppendruck und Anpassung.",
                    "body": (
                        "Viele Muster entstanden nach der Pubertät, um dazuzugehören — Erkältungen, Grippe "
                        "und manche Gewohnheiten tragen oft eine soziale Botschaft. Nutze sie, wenn du dich "
                        "verändert hast, um zu passen oder mit anderen mitzuhalten."
                    ),
                },
                {
                    "id": "holographic",
                    "title": "Holografisch",
                    "summary": "Das Ganze steckt in jedem Teil.",
                    "body": (
                        "Manche Prägungen sind keine linearen Geschichten, sondern Felder — jedes Fragment "
                        "enthält das ganze Muster wie ein Hologramm. Wähle diese Stufe, wenn Themen "
                        "mehrdimensional, familiär oder gleichzeitig in vielen Lebensbereichen auftauchen."
                    ),
                },
                {
                    "id": "reactive",
                    "title": "Reaktiv",
                    "summary": "Automatische Antworten und Allergien.",
                    "body": (
                        "Betrifft Reflexhandlungen — auch Leben in Erwartung fremder Wut oder Zustimmung. "
                        "Relevant auch bei reaktiven Zuständen wie Allergien, wenn der Körper antwortet, "
                        "bevor der Verstand nachkommt."
                    ),
                },
                {
                    "id": "building",
                    "title": "Bauen",
                    "summary": "Commitment, etwas tragfähig zu machen.",
                    "body": (
                        "Gebäude, Unternehmen, Beziehungen oder jede Struktur, die du fertigstellen willst. "
                        "Nutze sie bei Stocken im Aufbau oder bei Bereitschaft für langfristige Investition. "
                        "Passt natürlich zum Skelett-Set bei physischen Projekten."
                    ),
                },
                {
                    "id": "genetic",
                    "title": "Genetisch",
                    "summary": "Muster über Familienlinien.",
                    "body": (
                        "Wenn Ungleichgewicht Generationen wandert, kann Heilung eines Mitglieds das Feld "
                        "für andere erweichen. Schwingung erhöhen oder die Geschichte bewusst verarbeiten. "
                        "Umfasst geerbte Lebensstil-Grenzen ebenso wie benannte erbliche Themen."
                    ),
                },
                {
                    "id": "alignment",
                    "title": "Ausrichtung",
                    "summary": "Gegenwärtige Frequenz und umgebende Systeme abstimmen.",
                    "body": (
                        "Verbindet dich mit Umgebungen, Institutionen oder Werkzeugen, die nicht mehr zu deinem "
                        "aktuellen Stand passen. Nutze sie, um veraltete Überzeugungen, angstgetriebene Gewohnheiten "
                        "oder falsche Lösungen loszulassen — und dich ohne Drama zu lösen."
                    ),
                },
                {
                    "id": "pattern",
                    "title": "Muster",
                    "summary": "Selbst geschriebene Schleifen und Gewohnheiten.",
                    "body": (
                        "Unterschiedlich zu Genetik oder Umfeld — Muster, die du selbst schreibst: Süchte, Impuls, "
                        "wiederholtes Scheitern oder sabotierende Arbeitsgewohnheiten. "
                        "Wähle sie, wenn dieselbe Szene mit deiner Handschrift erneut läuft."
                    ),
                },
                {
                    "id": "environmental",
                    "title": "Umwelt",
                    "summary": "Geprägt durch Ort, Kultur oder Bedingungen.",
                    "body": (
                        "Armut, Missbrauch, Vorurteile oder Rebellion gegen ein hyperordentliches Elternhaus "
                        "gehören hierher. Nicht jede Person ist gleich empfindlich — der Charakter zählt. "
                        "Nutze sie, wenn die Umgebung selbst das Ungleichgewicht lehrte."
                    ),
                },
                {
                    "id": "competitive",
                    "title": "Wettbewerb",
                    "summary": "Rivalität, Kontrolle und Rampenlicht.",
                    "body": (
                        "Wenn Unwohlsein aus dem Bedürfnis wächst zu gewinnen, zu dominieren oder Kontrolle "
                        "abzustreiten. Umfasst Rampenlicht und Machtkämpfe. "
                        "Frage, ob das Raster Wettbewerb mildern oder in faires Spiel lenken soll."
                    ),
                },
                {
                    "id": "attitudinal",
                    "title": "Haltung",
                    "summary": "Ego, Urteil und Rang.",
                    "body": (
                        "Haltung — Überlegenheit, Minderwertigkeit, Berufsidentität — kann Ungleichgewicht "
                        "verfestigen. Modelle, Politiker:innen und Expert:innen sind Archetypen; doch jede Person "
                        "kann diese Stufe brauchen, wenn Selbstwert oder Wut in einer Pose erstarrt."
                    ),
                },
                {
                    "id": "city",
                    "title": "Stadt",
                    "summary": "Gemeinschafts-Raster und kollektive Nervensysteme.",
                    "body": (
                        "Für Gruppen mit gemeinsamem Merkmal — eine Stadt, eine Demografie, sogar eine Tierart "
                        "in einer Region. Oft in Gemeinschafts-Rastern; manchmal bei nervensystemischen Themen "
                        "wie Depression oder kognitivem Abbau im großen Maßstab."
                    ),
                },
            ],
        },
    ],
}


def write(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    write(OUT_EN, EN)
    write(OUT_DE, DE)
    print(f"Wrote {OUT_EN} ({OUT_EN.stat().st_size} bytes)")
    print(f"Wrote {OUT_DE} ({OUT_DE.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
