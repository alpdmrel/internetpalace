"""Redraw the thesis block diagrams in English as clean, theme-aware SVGs.

The originals are Turkish screenshots exported from the thesis with hard-coded
black backgrounds. These replacements are generated so column alignment and
wire routing are exact, and they carry no colours of their own — every fill and
stroke is a CSS variable supplied by SystemDiagrams.astro, so the diagrams
follow the site's light/dark theme.

Run with:  npm run diagrams
"""

import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(REPO, "src", "diagrams")

# Geometry
NODE_W = 178
NODE_H = 52
ROW_GAP = 20
COL_GAP = 108
PAD = 16
LINE_H = 15


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def node(x, y, w, h, label, cls="", rx=7):
    """A rounded box with centred, optionally multi-line, label."""
    lines = label.split("\n")
    total = (len(lines) - 1) * LINE_H
    y0 = y + h / 2 - total / 2 + 4
    tspans = "".join(
        f'<tspan x="{x + w / 2:.0f}" y="{y0 + i * LINE_H:.0f}">{esc(l)}</tspan>'
        for i, l in enumerate(lines)
    )
    return (
        f'<g class="node {cls}">'
        f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{rx}"/>'
        f'<text text-anchor="middle">{tspans}</text>'
        f"</g>"
    )


def elbow(x1, y1, x2, y2, both=True):
    """Orthogonal connector: horizontal, vertical, horizontal."""
    mx = (x1 + x2) / 2
    d = f"M {x1:.0f} {y1:.0f} H {mx:.0f} V {y2:.0f} H {x2:.0f}"
    start = ' marker-start="url(#dot)"' if both else ""
    return f'<path class="wire" d="{d}" marker-end="url(#arrow)"{start}/>'


DEFS = """<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6"
        markerHeight="6" orient="auto-start-reverse">
  <path d="M 0 1 L 9 5 L 0 9 z" class="arrowhead"/>
</marker>
<marker id="dot" viewBox="0 0 6 6" refX="3" refY="3" markerWidth="4" markerHeight="4">
  <circle cx="3" cy="3" r="2.4" class="arrowhead"/>
</marker>
</defs>"""

STYLE = """<style>
  .node rect { stroke-width: 1.25; }
  .node text {
    font-family: var(--dg-font, ui-sans-serif, system-ui, sans-serif);
    font-size: 13px; fill: var(--dg-text, #e7ebf0);
  }
  .node rect { fill: var(--dg-neutral-fill, #1a1f27); stroke: var(--dg-neutral-stroke, #3a434f); }
  .sensor rect { fill: var(--dg-sensor-fill, rgba(94,209,138,.13)); stroke: var(--dg-sensor-stroke, #5ed18a); }
  .act rect    { fill: var(--dg-act-fill, rgba(255,159,69,.13));    stroke: var(--dg-act-stroke, #ff9f45); }
  .mcu rect    { fill: var(--dg-mcu-fill, rgba(94,200,242,.13));    stroke: var(--dg-mcu-stroke, #5ec8f2); }
  .ctrl rect   { fill: var(--dg-ctrl-fill, rgba(167,139,250,.16));  stroke: var(--dg-ctrl-stroke, #a78bfa); }
  .mcu text, .ctrl text { font-weight: 600; }
  .wire { fill: none; stroke: var(--dg-wire, #55606e); stroke-width: 1.4; }
  .arrowhead { fill: var(--dg-wire, #55606e); stroke: none; }
  .title {
    font-family: var(--dg-mono, ui-monospace, monospace);
    font-size: 11px; letter-spacing: .14em; text-transform: uppercase;
    fill: var(--dg-muted, #8b94a3);
  }
</style>"""


def svg(width, height, body, title=None):
    t = (
        f'<text class="title" x="{PAD}" y="{PAD + 10}">{esc(title)}</text>'
        if title
        else ""
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} {height:.0f}" '
        f'role="img" preserveAspectRatio="xMidYMid meet">'
        f"{DEFS}{STYLE}{t}{body}</svg>"
    )


def hub(title, mcu_label, left, right, controller=None):
    """Hub-and-spoke unit diagram: inputs left, peripherals right, MCU centre."""
    rows = max(len(left), len(right))
    top = 46
    col_h = rows * NODE_H + (rows - 1) * ROW_GAP
    height = top + col_h + PAD + (0 if controller is None else 0)

    lx = PAD
    cx = lx + NODE_W + COL_GAP
    mcu_w = 132
    rx_ = cx + mcu_w + COL_GAP
    width = rx_ + NODE_W + PAD

    def col_y(i, n):
        """Centre a column of n nodes against the full block height."""
        block = n * NODE_H + (n - 1) * ROW_GAP
        off = top + (col_h - block) / 2
        return off + i * (NODE_H + ROW_GAP)

    parts = []

    # Controller sits above the right column and gets its own lane.
    ctrl_y = None
    if controller:
        ctrl_y = PAD + 14
        height += NODE_H + 26
        top += NODE_H + 26

    # Recompute with the controller lane included.
    def col_y2(i, n):
        block = n * NODE_H + (n - 1) * ROW_GAP
        off = top + (col_h - block) / 2
        return off + i * (NODE_H + ROW_GAP)

    mcu_h = min(col_h, 260)
    mcu_y = top + (col_h - mcu_h) / 2

    if controller:
        parts.append(node(rx_, ctrl_y, NODE_W, NODE_H, controller, "ctrl"))
        parts.append(
            f'<path class="wire" d="M {cx + mcu_w / 2:.0f} {mcu_y:.0f} '
            f'V {ctrl_y + NODE_H / 2:.0f} H {rx_:.0f}" '
            f'marker-end="url(#arrow)" marker-start="url(#dot)"/>'
        )

    for i, (lbl, cls) in enumerate(left):
        y = col_y2(i, len(left))
        parts.append(node(lx, y, NODE_W, NODE_H, lbl, cls))
        parts.append(elbow(lx + NODE_W, y + NODE_H / 2, cx, mcu_y + mcu_h / 2))

    for i, (lbl, cls) in enumerate(right):
        y = col_y2(i, len(right))
        parts.append(node(rx_, y, NODE_W, NODE_H, lbl, cls))
        parts.append(
            elbow(cx + mcu_w, mcu_y + mcu_h / 2, rx_, y + NODE_H / 2)
        )

    parts.append(node(cx, mcu_y, mcu_w, mcu_h, mcu_label, "mcu"))

    return svg(width, height, "".join(parts), title)


def system_diagram():
    """Top-level architecture: field nodes -> router -> Raspberry Pi."""
    W, H = 980, 500
    p = []
    nw, nh = 190, 46

    units = [
        ("Unit 1\nSensing  ·  ESP32", 70),
        ("Unit 2\nActuation  ·  ESP32", 170),
        ("Unit 3\nLighting  ·  ESP8266", 270),
        ("Light Measurement\nESP8266", 370),
    ]
    for lbl, y in units:
        p.append(node(PAD, y, nw, nh + 8, lbl, "mcu"))
        p.append(
            f'<path class="wire" d="M {PAD + nw:.0f} {y + (nh + 8) / 2:.0f} '
            f'H {280:.0f} V {225:.0f} H {320:.0f}" marker-end="url(#arrow)"/>'
        )

    # Router
    p.append(node(320, 200, 120, 50, "Router", ""))
    p.append(
        f'<path class="wire" d="M 380 200 V 130 H 470" marker-end="url(#arrow)"/>'
    )
    p.append(node(470, 106, 120, 48, "WAN", ""))
    p.append(
        f'<path class="wire" d="M 440 225 H 620" marker-end="url(#arrow)" '
        f'marker-start="url(#dot)"/>'
    )

    # Raspberry Pi panel
    p.append(
        '<g class="node ctrl"><rect x="620" y="76" width="344" height="404" rx="12"/>'
        '<text text-anchor="middle">'
        '<tspan x="792" y="106">Main Controller</tspan>'
        '<tspan x="792" y="124" style="font-size:12px;font-weight:400">Raspberry Pi 4</tspan>'
        "</text></g>"
    )
    p.append(node(640, 140, 150, 42, "LAN", ""))
    p.append(node(806, 140, 140, 42, "Database", ""))
    p.append(
        '<path class="wire" d="M 790 161 H 806" marker-end="url(#arrow)"/>'
    )

    p.append(
        '<text class="title" x="640" y="212">Automations</text>'
    )
    autos = [
        "pH balancing",
        "A&B nutrient dosing",
        "Water level top-up",
        "Leak detection",
        "Enclosure temperature",
        "Lighting schedule",
    ]
    for i, a in enumerate(autos):
        col, row = i % 2, i // 2
        x = 640 + col * 160
        y = 226 + row * 56
        p.append(node(x, y, 146, 44, a, "act", rx=6))

    p.append(node(640, 412, 306, 46, "User interface", ""))

    return svg(W, H, "".join(p), "Figure 1 — System architecture")


DIAGRAMS = {
    "system": system_diagram(),
    "unit1": hub(
        "Figure 3 — Unit 1, sensing",
        "ESP32",
        left=[
            ("Water level\nmin", "sensor"),
            ("Water level\nmax", "sensor"),
            ("Temperature", "sensor"),
            ("Ultrasonic\nwater level", "sensor"),
            ("Water flow\nrate", "sensor"),
            ("Control panel\nlid switch", "sensor"),
            ("Current clamp", "sensor"),
            ("INA226\ncurrent · voltage", "sensor"),
        ],
        right=[
            ("pH", "sensor"),
            ("TDS", "sensor"),
            ("Water turbidity", "sensor"),
            ("Water leak\n1 & 2", "sensor"),
            ("AM2315\ntemp & humidity", "sensor"),
            ("SHT20\ntemp & humidity", "sensor"),
        ],
        controller="Main controller",
    ),
    "unit2": hub(
        "Figure 6 — Unit 2, actuation",
        "ESP32",
        left=[
            ("Air pump", "act"),
            ("Ventilation fan", "act"),
            ("HV relay", "act"),
            ("HV relay", "act"),
            ("Buzzer", "act"),
            ("BME280\ntemp & pressure", "sensor"),
            ("INA226\ncurrent · voltage", "sensor"),
        ],
        right=[
            ("pH up pump", "act"),
            ("pH down pump", "act"),
            ("Nutrient A pump", "act"),
            ("Nutrient B pump", "act"),
            ("Main water pump", "act"),
            ("Circulation pump", "act"),
            ("Solenoid water\nvalve", "act"),
            ("LV relay", "act"),
        ],
        controller="Main controller",
    ),
    # Note: avoid arrow glyphs in labels — they are missing from some sans
    # fonts and drag the whole run into a serif fallback.
    "unit3": hub(
        "Figure 7 — Unit 3, lighting",
        "ESP8266",
        left=[
            ("Control panel lamp\nvia TIP122", "act"),
            ("Grow lamp\nvia TIP122", "act"),
        ],
        right=[
            ("INA226\ncurrent · voltage", "sensor"),
        ],
        controller="Main controller",
    ),
    "light": hub(
        "Figure 8 — Light measurement",
        "ESP8266",
        left=[
            ("INA226\ncurrent · voltage", "sensor"),
        ],
        right=[
            ("UV radiation\nVEML6070", "sensor"),
            ("TSL2561\nilluminance", "sensor"),
            ("TCS34725\nRGB · colour temp", "sensor"),
        ],
        controller="Main controller",
    ),
}


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for name, content in DIAGRAMS.items():
        path = os.path.join(OUT_DIR, f"{name}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  {name}.svg  ({len(content) // 1024} KB)")
    print(f"\n{len(DIAGRAMS)} diagram(s) -> {OUT_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
