"""Author the seven editorial SVG scenes used by The Agent Race.

The shapes are intentionally diagrammatic: they describe relationships, not
measured quantities or a reconstruction of a particular cyber incident.
"""

from pathlib import Path


OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

INK = "#173342"
MUTED = "#829198"
COPPER = "#b7623f"
COPPER_LIGHT = "#e2a071"
TEAL = "#267c80"
TEAL_LIGHT = "#9cccca"
PAPER = "#f3f0e7"
WHITE = "#fffdf7"


def svg(parts, *, bg=PAPER, accent=COPPER):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" role="img">
<defs>
  <pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M60 0H0V60" fill="none" stroke="{INK}" stroke-width="1" opacity=".065"/></pattern>
  <pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.3" fill="{INK}" opacity=".12"/></pattern>
  <pattern id="hatch" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="14" stroke="{accent}" stroke-width="2" opacity=".35"/></pattern>
  <filter id="shadow" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="12" stdDeviation="12" flood-color="{INK}" flood-opacity=".14"/></filter>
  <linearGradient id="paper" x2="0" y2="1"><stop stop-color="{bg}"/><stop offset="1" stop-color="#e4e4dc"/></linearGradient>
</defs>
<rect width="1600" height="900" fill="url(#paper)"/>
<rect width="1600" height="900" fill="url(#grid)"/>
<rect x="37" y="37" width="1526" height="826" rx="5" fill="none" stroke="{INK}" stroke-width="2" opacity=".35"/>
<path d="M37 108H1563 M37 792H1563" stroke="{INK}" stroke-width="2" opacity=".16"/>
<circle cx="91" cy="74" r="9" fill="{accent}"/><circle cx="124" cy="74" r="9" fill="{INK}" opacity=".22"/><circle cx="157" cy="74" r="9" fill="{INK}" opacity=".22"/>
{''.join(parts)}
</svg>'''


def rect(x, y, w, h, fill=WHITE, stroke=INK, sw=4, rx=8, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


def line(x1, y1, x2, y2, color=INK, sw=5, extra=""):
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" {extra}/>'


def path(d, color=INK, sw=5, fill="none", extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'


def circ(cx, cy, r, fill=WHITE, stroke=INK, sw=4, extra=""):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


def window(x, y, w=72, h=112):
    return rect(x, y, w, h, "#bcd1d0", INK, 3, 2) + line(x+w/2, y, x+w/2, y+h, INK, 2) + line(x, y+h/2, x+w, y+h/2, INK, 2)


def card(x, y, w, h, color=INK):
    return (rect(x, y, w, h, WHITE, color, 4, 6, 'filter="url(#shadow)"') +
            line(x+22, y+33, x+w-22, y+33, color, 3) +
            line(x+22, y+56, x+w-52, y+56, MUTED, 3) +
            line(x+22, y+78, x+w-80, y+78, MUTED, 3))


def node(x, y, r, color):
    return circ(x, y, r+7, PAPER, color, 3) + circ(x, y, r, color, color, 2) + circ(x, y, max(r/4, 4), WHITE, WHITE, 0)


def cover():
    p = []
    # Two visibly different task streams converge on the company boundary.
    p += [path("M40 425H182L280 348H465", COPPER, 23), path("M42 558H210L298 618H465", COPPER, 12),
          path("M1560 425H1418L1320 348H1135", TEAL, 23), path("M1558 558H1390L1302 618H1135", TEAL, 12)]
    for x, y, c in [(170,425,COPPER),(290,348,COPPER),(204,558,COPPER),(1420,425,TEAL),(1310,348,TEAL),(1390,558,TEAL)]:
        p.append(node(x,y,18,c))
    p += [rect(467, 253, 666, 427, WHITE, INK, 6, 2, 'filter="url(#shadow)"'),
          rect(467, 253, 666, 59, INK, INK, 0, 0),
          rect(514, 352, 572, 279, "#edf4f1", INK, 4, 2)]
    for x in [538, 642, 746, 850, 954]:
        p.append(window(x, 385, 78, 150))
    p += [rect(720, 549, 160, 82, "#d7e4e0", INK, 4, 3),
          path("M750 589H850 M800 560V619", TEAL, 4),
          rect(581, 661, 438, 154, INK, INK, 5, 12, 'filter="url(#shadow)"'),
          rect(608, 686, 384, 102, "#294957", "#738f95", 3, 5),
          circ(670, 738, 27, COPPER, COPPER_LIGHT, 4), circ(800, 738, 47, WHITE, COPPER, 9),
          circ(800, 738, 18, COPPER, COPPER, 2), circ(930, 738, 27, TEAL, TEAL_LIGHT, 4),
          path("M480 342H432 M1120 342H1168", INK, 3)]
    return svg(p, bg="#f2eee4")


def manual():
    p = []
    p += [rect(139, 314, 1322, 418, "#f8f5ed", INK, 4, 8, 'filter="url(#shadow)"'),
          rect(139, 314, 1322, 44, INK, INK, 0, 0)]
    for x in [690, 1030]:
        p += [path(f"M{x} 360V731", MUTED, 2, extra='stroke-dasharray="7 12"')]
    p += [rect(277, 412, 290, 237, "#e4c49f", INK, 6, 4, 'filter="url(#shadow)"'),
          rect(277, 392, 144, 44, "#e4c49f", INK, 6, 4),
          path("M319 474H518 M319 497H494", COPPER, 6),
          rect(342, 489, 186, 116, WHITE, INK, 3, 2),
          line(364, 520, 506, 520, MUTED, 3), line(364, 543, 485, 543, MUTED, 3),
          circ(451, 546, 72, "#f6d7b3", COPPER, 4),
          path("M418 547L442 570L486 519", COPPER, 11)]
    # Sequence of human review surfaces, leaving generous negative space.
    p += [path("M577 545H724", INK, 5, extra='stroke-dasharray="8 12"'),
          card(755, 420, 216, 206),
          circ(862, 552, 38, WHITE, INK, 5),
          path("M849 552L860 563L881 538", TEAL, 7),
          path("M977 545H1084", INK, 5, extra='stroke-dasharray="8 12"'),
          rect(1120, 430, 231, 187, "#e4ede8", INK, 4, 5, 'filter="url(#shadow)"'),
          circ(1236, 514, 62, WHITE, INK, 5),
          path("M1236 472V515L1267 542", COPPER, 8),
          line(1138, 652, 1337, 652, MUTED, 3)]
    return svg(p, bg="#ede9df")


def attack():
    p = []
    p += [rect(96, 300, 1408, 467, "#fff9ef", INK, 4, 7, 'filter="url(#shadow)"'),
          rect(96, 300, 1408, 49, INK, INK, 0, 0),
          rect(165, 412, 214, 221, "#e9b88f", INK, 5, 8),
          rect(197, 442, 149, 122, "#f7e6ce", INK, 3, 4),
          path("M219 473H324 M219 499H303 M219 525H277", INK, 5),
          path("M382 520H536L610 414H1008", COPPER, 13),
          path("M605 414V667H1008", COPPER, 9),
          path("M720 414V505H1008", COPPER, 7),
          node(605,414,16,COPPER), node(605,667,16,COPPER), node(720,505,14,COPPER),
          circ(1008, 414, 75, "#f1c19a", COPPER, 7, 'filter="url(#shadow)"'),
          circ(1008, 414, 48, WHITE, COPPER, 4),
          path("M984 414H1033 M1008 390V439", COPPER, 7)]
    # Branch lines end in distinct abstract work tiles, never tactical instructions.
    for d in ["M1085 414H1200V411", "M1085 414H1157V567H1210", "M1085 414H1140V673H1210"]:
        p.append(path(d, COPPER, 8))
    for x, y, w, h in [(1210,363,200,96),(1210,519,200,96),(1210,625,200,96)]:
        p += [rect(x,y,w,h,WHITE,INK,4,4), rect(x+21,y+22,54,52,"url(#hatch)",COPPER,3,2),
              line(x+95,y+29,x+w-23,y+29,INK,4),line(x+95,y+53,x+w-49,y+53,MUTED,3)]
    p += [rect(419, 669, 106, 52, "url(#hatch)", COPPER, 3, 2),
          path("M133 695H379", COPPER, 5, extra='stroke-dasharray="12 12"')]
    return svg(p, bg="#eee7d9")


def defend():
    p = []
    p += [rect(111, 289, 1380, 493, "#f2f8f3", INK, 4, 6, 'filter="url(#shadow)"'),
          rect(111, 289, 1380, 49, INK, INK, 0, 0)]
    # A source map, triage lens and expert review destination.
    for x,y in [(216,450),(362,402),(362,584),(541,478),(646,603),(730,405),(865,509)]:
        p.append(node(x,y,16,TEAL))
    for x1,y1,x2,y2 in [(216,450,362,402),(216,450,362,584),(362,402,541,478),(362,584,541,478),(541,478,646,603),(541,478,730,405),(730,405,865,509),(646,603,865,509)]:
        p.append(line(x1,y1,x2,y2,TEAL,8))
    p += [circ(734, 509, 122, "#dceee8", TEAL, 8),
          circ(734, 509, 88, "none", TEAL_LIGHT, 5),
          path("M668 518L711 555L799 455", TEAL, 15),
          path("M905 509H1134V660H1180", TEAL, 10),
          rect(1172, 514, 265, 249, WHITE, INK, 5, 8, 'filter="url(#shadow)"'),
          rect(1200, 547, 210, 29, "#c4ddd7", "none", 0, 3),
          line(1204,605,1399,605,MUTED,4),line(1204,637,1372,637,MUTED,4),
          circ(1296, 667, 47, "#b9dbd1", TEAL, 6),
          path("M1272 666L1289 683L1322 649", TEAL, 11),
          path("M181 697H982", TEAL, 4, extra='stroke-dasharray="9 13"')]
    return svg(p, bg="#e5eeea", accent=TEAL)


def risk():
    p = []
    p += [rect(91, 302, 1418, 473, "#f6f2e9", INK, 4, 6, 'filter="url(#shadow)"'),
          rect(91, 302, 1418, 47, INK, INK, 0, 0),
          path("M1045 350V774", COPPER, 5, extra='stroke-dasharray="12 11"'),
          rect(120, 418, 325, 255, "#dbe2df", INK, 4, 6),
          rect(159, 455, 244, 172, WHITE, INK, 4, 3),
          path("M177 482H383 M177 515H339 M177 549H360", MUTED, 5),
          path("M448 544H642", COPPER, 9, extra='stroke-dasharray="12 11"'),
          rect(688, 423, 280, 294, WHITE, COPPER, 6, 4, 'filter="url(#shadow)"'),
          path("M714 465H939 M714 505H903 M714 542H921", INK, 5),
          rect(714, 583, 226, 100, "url(#hatch)", COPPER, 3, 2),
          circ(829, 575, 52, WHITE, COPPER, 7),
          path("M829 550V584 M829 601V605", COPPER, 11),
          path("M979 544H1084", COPPER, 9, extra='stroke-dasharray="11 13"'),
          rect(1122, 434, 266, 244, "#d6ebe4", INK, 5, 9),
          circ(1255, 506, 57, WHITE, TEAL, 5),
          path("M1230 507H1280 M1255 482V531", TEAL, 7),
          rect(1171, 593, 168, 45, INK, INK, 2, 6),
          path("M1073 405H1445", TEAL, 3)]
    return svg(p, bg="#eae5e1")


def human():
    p = []
    p += [rect(193, 289, 1214, 488, "#fffaf0", INK, 5, 9, 'filter="url(#shadow)"'),
          rect(193, 289, 1214, 47, INK, INK, 0, 0),
          # Three concrete control objects around a central evidence surface.
          rect(260, 406, 265, 202, "#e8d0b2", INK, 5, 7),
          circ(390, 484, 41, WHITE, COPPER, 5),
          path("M387 458V508 M368 483H408", COPPER, 7),
          line(300,552,482,552,INK,5),
          circ(1190, 486, 77, "#d9ede4", TEAL, 6),
          circ(1181, 477, 37, WHITE, TEAL, 6),
          path("M1211 507L1250 548", TEAL, 10),
          rect(1112, 607, 218, 83, INK, INK, 3, 8),
          rect(1154, 627, 133, 42, COPPER, COPPER, 2, 21),
          rect(617, 390, 378, 314, WHITE, INK, 5, 5, 'filter="url(#shadow)"'),
          rect(657, 428, 298, 45, "#d8e8e1", TEAL, 3, 3),
          line(657, 506, 935, 506, MUTED, 4),line(657, 538, 897, 538, MUTED, 4),
          line(657, 571, 928, 571, MUTED, 4),
          circ(807, 614, 64, "#f1e2c9", INK, 5),
          path("M776 615L799 638L840 586", TEAL, 12),
          path("M525 506H616 M996 506H1112 M807 705V746H1209", INK, 4, extra='stroke-dasharray="9 10"')]
    return svg(p, bg="#f1eee2")


def final():
    p = []
    # A map rather than a synthetic city: two networks, one controlled boundary.
    p += [rect(103, 311, 1394, 449, "#faf8ef", INK, 4, 7, 'filter="url(#shadow)"'),
          rect(103, 311, 1394, 47, INK, INK, 0, 0),
          path("M132 496H296L405 411H598L726 536", COPPER, 13),
          path("M143 624H329L451 644H613L726 536", COPPER, 8),
          path("M1468 496H1304L1195 411H1002L874 536", TEAL, 13),
          path("M1457 624H1271L1149 644H987L874 536", TEAL, 8)]
    for x,y,c in [(296,496,COPPER),(405,411,COPPER),(451,644,COPPER),(1304,496,TEAL),(1195,411,TEAL),(1149,644,TEAL)]:
        p.append(node(x,y,16,c))
    p += [rect(725, 397, 150, 278, WHITE, INK, 6, 12, 'filter="url(#shadow)"'),
          rect(752, 427, 96, 50, "#dce7df", INK, 3, 3),
          circ(800, 545, 54, "#ead2af", INK, 5),
          path("M773 545L793 565L830 522", INK, 10),
          rect(757, 621, 86, 21, INK, INK, 1, 4),
          path("M795 676V731", INK, 5),
          path("M485 690H649 M951 690H1115", INK, 3, extra='stroke-dasharray="8 10"')]
    return svg(p, bg="#e8eae3", accent=TEAL)


for name, scene in {
    "cover": cover,
    "manual": manual,
    "attack": attack,
    "defend": defend,
    "risk": risk,
    "human": human,
    "final": final,
}.items():
    (OUT / f"{name}.svg").write_text(scene(), encoding="utf-8")
    print(f"wrote {name}.svg")
