"""Inline SVG infographics for sector research notes — design-system driven."""

import itertools
import math
from typing import Optional

_uid_gen = itertools.count()

FOREST = "#204028"
SOFT = "#2d5640"
CREAM = "#f0e8cc"
BG = "#faf7ef"
BG_ALT = "#f4f0e4"
MUTED = "#5a6a5c"
FONT = "Outfit,sans-serif"


def _uid(prefix: str = "v") -> str:
    return f"{prefix}{next(_uid_gen)}"


def _esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _figure(kind: str, label: str, svg: str, caption: str) -> str:
    return f'''        <figure class="viz viz-{kind}">
          <p class="viz-label">{label}</p>
{svg}
          <figcaption class="viz-caption">{caption}</figcaption>
        </figure>'''


def _defs(uid: str) -> str:
    return f"""
            <linearGradient id="{uid}-bg" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="{BG}"/>
              <stop offset="100%" stop-color="{BG_ALT}"/>
            </linearGradient>
            <linearGradient id="{uid}-card" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="{SOFT}"/>
              <stop offset="100%" stop-color="{FOREST}"/>
            </linearGradient>
            <pattern id="{uid}-grid" width="28" height="28" patternUnits="userSpaceOnUse">
              <path d="M 28 0 L 0 0 0 28" fill="none" stroke="{FOREST}" stroke-width="0.4" opacity="0.07"/>
            </pattern>
            <filter id="{uid}-shadow" x="-10%" y="-10%" width="120%" height="120%">
              <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="{FOREST}" flood-opacity="0.1"/>
            </filter>
            <marker id="{uid}-arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0,0 L8,4 L0,8 Z" fill="{FOREST}"/>
            </marker>
            <marker id="{uid}-arrm" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0,0 L8,4 L0,8 Z" fill="{MUTED}"/>
            </marker>"""


def _svg(viewbox: str, uid: str, body: str, title: Optional[str] = None, title_x: float = 320) -> str:
    parts = viewbox.split()
    w, h = parts[2], parts[3]
    title_el = ""
    if title:
        title_el = (
            f'<text x="{title_x}" y="34" text-anchor="middle" fill="{FOREST}" '
            f'font-size="12" font-weight="600" letter-spacing="0.06em" font-family="{FONT}">'
            f"{_esc(title)}</text>"
        )
    return f'''        <svg aria-hidden="true" class="viz-svg" viewBox="{viewbox}" xmlns="http://www.w3.org/2000/svg">
          <defs>{_defs(uid)}
          </defs>
          <rect width="{w}" height="{h}" fill="url(#{uid}-bg)" rx="14"/>
          <rect width="{w}" height="{h}" fill="url(#{uid}-grid)" rx="14"/>
          {title_el}
{body}
        </svg>'''


# Module-level uid for nodes in same svg — set before building nodes
_active_uid: str = ""


def _set_uid(u: str) -> str:
    global _active_uid
    _active_uid = u
    return u


def _node_simple(
    uid: str,
    x: float,
    y: float,
    w: float,
    h: float,
    label: str,
    sub: str = "",
    *,
    variant: str = "cream",
    primary: bool = False,
    delay: float = 0,
) -> str:
    cls = "viz-node viz-fade-slide" + (" viz-pulse" if primary else "")
    style = f' style="animation-delay:{delay}s"' if delay else ""
    if variant == "solid":
        rect = f'fill="{FOREST}"'
        stroke = ""
        tf, sf = CREAM, CREAM
    elif variant == "primary":
        rect = f'fill="url(#{uid}-card)"'
        stroke = ""
        tf, sf = CREAM, CREAM
    elif variant == "muted":
        rect = f'fill="{BG_ALT}"'
        stroke = f' stroke="{MUTED}" stroke-width="1.2"'
        tf, sf = MUTED, MUTED
    else:
        rect = f'fill="{CREAM}"'
        stroke = f' stroke="{FOREST}" stroke-width="1.2"'
        tf, sf = FOREST, MUTED
    ty = y + (h / 2 - 2 if sub else h / 2 + 4)
    sub_el = (
        f'<text x="{x + w / 2}" y="{y + h / 2 + 12}" text-anchor="middle" fill="{sf}" '
        f'font-size="10" font-family="{FONT}">{_esc(sub)}</text>'
        if sub
        else ""
    )
    fw = ' font-weight="600"' if variant in ("solid", "primary") else ""
    return f'''          <g class="{cls}"{style}>
            <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" {rect} {stroke}/>
            <text x="{x + w / 2}" y="{ty}" text-anchor="middle" fill="{tf}" font-size="11"{fw} font-family="{FONT}">{_esc(label)}</text>
            {sub_el}
          </g>'''


def _chip(x: float, y: float, text: str, *, accent: bool = True) -> str:
    fill = FOREST if accent else BG_ALT
    fg = CREAM if accent else FOREST
    stroke = "" if accent else f' stroke="{MUTED}" stroke-width="1"'
    return f'''          <g class="viz-fade-slide">
            <rect x="{x}" y="{y}" width="{len(text) * 6.2 + 20}" height="22" rx="11" fill="{fill}"{stroke}/>
            <text x="{x + (len(text) * 6.2 + 20) / 2}" y="{y + 15}" text-anchor="middle" fill="{fg}" font-size="10" font-weight="600" font-family="{FONT}">{_esc(text)}</text>
          </g>'''


def _line(x1, y1, x2, y2, uid: str, *, dashed: bool = False, muted: bool = False, animate: bool = True) -> str:
    cls = "viz-draw" if animate else ""
    dash = ' stroke-dasharray="5 4"' if dashed else ""
    stroke = MUTED if muted else FOREST
    marker = f"url(#{uid}-arrm)" if muted else f"url(#{uid}-arr)"
    return (
        f'          <line class="{cls}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{stroke}" stroke-width="1.5"{dash} marker-end="{marker}"/>'
    )


def _col_label(x: float, y: float, text: str) -> str:
    return (
        f'<text x="{x}" y="{y}" fill="{MUTED}" font-size="10" letter-spacing="0.08em" '
        f'font-weight="600" font-family="{FONT}">{_esc(text.upper())}</text>'
    )


def _loop(uid: str, cx: float, cy: float, r: float, labels: tuple[str, str, str, str]) -> str:
    nodes = []
    lines = []
    n = 4
    for i, lab in enumerate(labels):
        ang = -math.pi / 2 + i * (2 * math.pi / n)
        nx = cx + r * math.cos(ang)
        ny = cy + r * math.sin(ang)
        nodes.append(_node_simple(uid, nx - 52, ny - 18, 104, 36, lab, variant="cream", delay=i * 0.12))
        ang2 = -math.pi / 2 + (i + 0.85) * (2 * math.pi / n)
        mx = cx + (r + 8) * math.cos(ang2)
        my = cy + (r + 8) * math.sin(ang2)
        ang1 = -math.pi / 2 + (i + 0.15) * (2 * math.pi / n)
        mx2 = cx + (r + 8) * math.cos(ang1)
        my2 = cy + (r + 8) * math.sin(ang1)
    arc_paths = []
    for i in range(n):
        a0 = -90 + i * 90
        a1 = a0 + 70
        x0 = cx + (r - 10) * math.cos(math.radians(a0 + 8))
        y0 = cy + (r - 10) * math.sin(math.radians(a0 + 8))
        x1 = cx + (r - 10) * math.cos(math.radians(a1))
        y1 = cy + (r - 10) * math.sin(math.radians(a1))
        arc_paths.append(
            f'          <path class="viz-draw" d="M {x0:.1f} {y0:.1f} A {r-10} {r-10} 0 0 1 {x1:.1f} {y1:.1f}" '
            f'fill="none" stroke="{FOREST}" stroke-width="1.4" marker-end="url(#{uid}-arr)"/>'
        )
    return "\n".join(arc_paths + nodes)


# --- Weather ---

def _weather_hero():
    uid = _set_uid(_uid("wx"))
    body = f"""
          {_col_label(48, 52, "New path")}
          {_node_simple(uid, 24, 58, 118, 40, "Past weather", variant="cream", delay=0)}
          {_line(142, 78, 178, 78, uid)}
          {_node_simple(uid, 178, 58, 96, 40, "AI model", variant="solid", delay=0.08)}
          {_line(274, 78, 310, 78, uid)}
          {_node_simple(uid, 310, 52, 132, 52, "Fast forecast", "minutes", variant="primary", primary=True, delay=0.16)}
          {_chip(448, 66, "minutes")}
          {_col_label(48, 142, "Classic path")}
          {_node_simple(uid, 24, 148, 118, 40, "Supercomputer", variant="muted", delay=0.2)}
          {_line(142, 168, 310, 168, uid, dashed=True, muted=True)}
          {_node_simple(uid, 310, 144, 132, 52, "Physics forecast", "hours", variant="muted", delay=0.28)}
          {_chip(448, 162, "hours", accent=False)}
          <text x="320" y="218" text-anchor="middle" fill="{MUTED}" font-size="10" font-family="{FONT}">Same skill bar on benchmarks; very different run time</text>"""
    return _figure(
        "hero",
        "How it works",
        _svg("0 0 640 240", uid, body, "Two ways to forecast weather"),
        "New AI models learn from reanalysis archives and produce forecasts in minutes. "
        "Classical physics models on supercomputers still set quality bars, but they take hours.",
    )


def _weather_mid():
    uid = _set_uid(_uid("wx"))
    body = f"""
          {_node_simple(uid, 28, 72, 88, 44, "ERA5 data", variant="cream", delay=0)}
          {_line(116, 94, 148, 94, uid)}
          {_node_simple(uid, 148, 72, 96, 44, "Pretrain", variant="cream", delay=0.1)}
          {_line(244, 94, 276, 94, uid)}
          {_node_simple(uid, 276, 72, 96, 44, "Fine-tune", variant="solid", delay=0.2)}
          {_line(372, 94, 404, 94, uid)}
          {_node_simple(uid, 404, 72, 100, 44, "Forecast", variant="primary", primary=True, delay=0.3)}
          <g class="viz-fade-slide" style="animation-delay:.4s">
            <path d="M520 118 Q560 72 600 118" fill="none" stroke="{SOFT}" stroke-width="1.2" opacity="0.5"/>
            <path d="M520 130 Q560 170 600 130" fill="none" stroke="{SOFT}" stroke-width="1.2" opacity="0.35"/>
            <path d="M520 124 Q560 100 600 124" fill="none" stroke="{FOREST}" stroke-width="1.6" opacity="0.7"/>
            <text x="560" y="200" text-anchor="middle" fill="{MUTED}" font-size="10" font-family="{FONT}">Ensemble fan</text>
          </g>
          <rect x="28" y="168" width="584" height="8" rx="4" fill="{BG_ALT}"/>
          <rect x="28" y="168" width="420" height="8" rx="4" fill="{SOFT}" opacity="0.35"/>"""
    return _figure(
        "mid",
        "Progress",
        _svg("0 0 640 220", uid, body, "From archive to operational forecast"),
        "Foundation-model weather stacks pretrain on ERA5-class archives, fine-tune for tasks, "
        "then roll out deterministic or ensemble forecasts from a shared checkpoint.",
    )


def _weather_loop():
    uid = _set_uid(_uid("wx"))
    labels = ("Cost falls", "More runs", "GPU strain", "Better verification")
    return _figure(
        "loop",
        "The rebound loop",
        _svg("0 0 640 280", uid, _loop(uid, 320, 148, 92, labels), "When forecasts get cheaper"),
        "Cheaper inference invites more experiments and ensembles, which strains data and compute "
        "unless verification and open benchmarks keep pace.",
    )


# --- Aerospace ---

def _aerospace_hero():
    uid = _set_uid(_uid("ae"))
    body = f"""
          {_node_simple(uid, 36, 68, 82, 46, "Optical", variant="cream", delay=0)}
          {_node_simple(uid, 36, 128, 82, 46, "SAR", variant="cream", delay=0.08)}
          <line class="viz-draw" x1="118" y1="91" x2="168" y2="110" stroke="{FOREST}" stroke-width="1.5"/>
          <line class="viz-draw" x1="118" y1="151" x2="168" y2="118" stroke="{FOREST}" stroke-width="1.5"/>
          {_node_simple(uid, 168, 88, 124, 52, "Flexible AI", variant="primary", primary=True, delay=0.16)}
          {_line(292, 114, 332, 114, uid)}
          {_node_simple(uid, 332, 68, 96, 36, "Floods", variant="solid", delay=0.22)}
          {_node_simple(uid, 332, 112, 96, 36, "Crops", variant="solid", delay=0.28)}
          {_node_simple(uid, 332, 156, 96, 36, "Emissions", variant="solid", delay=0.34)}"""
    return _figure(
        "hero",
        "How it works",
        _svg("0 0 640 220", uid, body, "From satellite pixels to maps"),
        "Foundation models train on optical and SAR streams, then adapt quickly to flood, crop, and emissions products.",
    )


def _aerospace_mid():
    uid = _set_uid(_uid("ae"))
    bands = ["B1", "B2", "B3", "B4", "B5", "SAR"]
    band_nodes = "\n".join(
        _node_simple(uid, 36 + i * 52, 78, 44, 32, b, variant="cream", delay=i * 0.06)
        for i, b in enumerate(bands)
    )
    body = f"""
          {band_nodes}
          {_line(348, 94, 388, 94, uid)}
          {_node_simple(uid, 388, 72, 120, 48, "One encoder", variant="primary", primary=True, delay=0.4)}
          {_line(508, 96, 548, 96, uid)}
          {_node_simple(uid, 548, 78, 72, 40, "Task head", variant="solid", delay=0.48)}
          <text x="320" y="168" text-anchor="middle" fill="{MUTED}" font-size="10" font-family="{FONT}">Any-sensor: subsample bands at train time; embed metadata at inference</text>"""
    return _figure(
        "mid",
        "Progress",
        _svg("0 0 640 200", uid, body, "Many sensors, one backbone"),
        "Any-sensor encoders accept arbitrary band combinations so one pretrained model serves many missions.",
    )


def _aerospace_loop():
    uid = _set_uid(_uid("ae"))
    labels = ("Cheaper EO AI", "More products", "Label limits", "Downlink strain")
    return _figure(
        "loop",
        "The rebound loop",
        _svg("0 0 640 280", uid, _loop(uid, 320, 148, 92, labels)),
        "Lower inference cost expands downstream products, which can outrun labeling bandwidth and downlink capacity.",
    )


# --- Materials ---

def _materials_hero():
    uid = _set_uid(_uid("mt"))
    body = f"""
          <rect x="40" y="56" width="260" height="148" rx="14" fill="{BG_ALT}" stroke="{MUTED}" stroke-width="1.2"/>
          {_col_label(168, 78, "Before")}
          <text x="170" y="102" text-anchor="middle" fill="{MUTED}" font-size="11" font-weight="600" font-family="{FONT}">Limestone cement</text>
          <ellipse cx="170" cy="138" rx="48" ry="26" fill="none" stroke="{MUTED}" stroke-width="1.2" opacity="0.6"/>
          <text x="170" y="142" text-anchor="middle" fill="{MUTED}" font-size="10" font-family="{FONT}">CO₂ from calcination</text>
          <rect x="340" y="56" width="260" height="148" rx="14" fill="{CREAM}" stroke="{FOREST}" stroke-width="1.2"/>
          {_col_label(470, 78, "After")}
          <text x="470" y="102" text-anchor="middle" fill="{FOREST}" font-size="11" font-weight="600" font-family="{FONT}">New rock and recycle</text>
          <circle cx="420" cy="140" r="18" fill="{SOFT}" opacity="0.35"/>
          <circle cx="470" cy="128" r="22" fill="{FOREST}" opacity="0.25"/>
          <circle cx="520" cy="145" r="16" fill="{SOFT}" opacity="0.3"/>
          <text x="470" y="178" text-anchor="middle" fill="{FOREST}" font-size="10" font-family="{FONT}">Smaller process CO₂</text>"""
    return _figure(
        "hero",
        "How it works",
        _svg("0 0 640 230", uid, body, "Cement emissions: two routes"),
        "Most cement CO₂ comes from limestone chemistry, not fuel alone. Alternatives swap feedstock or recycle clinker.",
    )


def _materials_mid():
    uid = _set_uid(_uid("mt"))
    body = f"""
          {_col_label(100, 58, "Conventional")}
          {_node_simple(uid, 48, 68, 88, 40, "Quarry", variant="cream", delay=0)}
          {_line(136, 88, 168, 88, uid)}
          {_node_simple(uid, 168, 68, 72, 40, "Kiln", variant="cream", delay=0.1)}
          {_line(240, 88, 272, 88, uid)}
          {_node_simple(uid, 272, 68, 88, 40, "Clinker", variant="muted", delay=0.2)}
          <rect x="368" y="74" width="56" height="22" rx="11" fill="{MUTED}" opacity="0.2"/>
          <text x="396" y="89" text-anchor="middle" fill="{MUTED}" font-size="9" font-weight="600" font-family="{FONT}">CO₂</text>
          {_col_label(420, 130, "Alternative path")}
          {_node_simple(uid, 360, 140, 100, 40, "Igneous feed", variant="cream", delay=0.25)}
          {_line(460, 160, 492, 160, uid)}
          {_node_simple(uid, 492, 140, 100, 40, "Electric recycle", variant="primary", primary=True, delay=0.32)}"""
    return _figure(
        "mid",
        "Progress",
        _svg("0 0 640 210", uid, body, "Process steps and swap-in paths"),
        "Researchers map quarry-kiln-clinker emissions while testing carbonate-free feed and electrified recycling.",
    )


def _materials_loop():
    uid = _set_uid(_uid("mt"))
    labels = ("Cheaper binders", "More volume", "Supply gaps", "Standards lag")
    return _figure(
        "loop",
        "The rebound loop",
        _svg("0 0 640 280", uid, _loop(uid, 320, 148, 92, labels)),
        "Lower-cost green binders can raise construction demand before supply chains and codes catch up.",
    )


# --- Energy ---

def _energy_hero():
    uid = _set_uid(_uid("en"))
    body = f"""
          <circle cx="72" cy="108" r="26" fill="{CREAM}" stroke="{FOREST}" stroke-width="1.2"/>
          <circle cx="72" cy="108" r="14" fill="{FOREST}" opacity="0.15"/>
          <text x="72" y="112" text-anchor="middle" fill="{FOREST}" font-size="10" font-weight="600" font-family="{FONT}">Sun</text>
          <path d="M130 118 Q150 88 172 108 Q192 78 212 118" fill="none" stroke="{FOREST}" stroke-width="1.6"/>
          <text x="172" y="138" text-anchor="middle" fill="{MUTED}" font-size="10" font-family="{FONT}">Wind</text>
          {_line(220, 108, 258, 108, uid)}
          {_node_simple(uid, 258, 88, 98, 44, "Short storage", "hours", variant="solid", delay=0.1)}
          {_line(356, 110, 394, 110, uid)}
          {_node_simple(uid, 394, 84, 110, 52, "Long storage", "days–weeks", variant="primary", primary=True, delay=0.2)}
          {_line(504, 110, 542, 110, uid)}
          {_node_simple(uid, 542, 92, 72, 40, "Grid", variant="cream", delay=0.3)}"""
    return _figure(
        "hero",
        "How it works",
        _svg("0 0 640 210", uid, body, "Balancing variable renewables"),
        "Solar and wind need layered storage: short batteries for evenings, long-duration assets for calm weeks.",
    )


def _energy_mid():
    uid = _set_uid(_uid("en"))
    bars = [
        (80, 120, 140, "4 h", "Lithium"),
        (240, 100, 160, "10–20 h", "LDES"),
        (420, 72, 200, "Seasonal", "H₂ / firm"),
    ]
    bar_svg = ""
    for i, (x, y, w, label, sub) in enumerate(bars):
        bar_svg += f'''
          <g class="viz-fade-slide" style="animation-delay:{i * 0.12}s">
            <rect x="{x}" y="{y}" width="{w}" height="{180 - y}" rx="8" fill="url(#{uid}-card)" opacity="{0.35 + i * 0.2}"/>
            <text x="{x + w/2}" y="{y - 8}" text-anchor="middle" fill="{FOREST}" font-size="11" font-weight="600" font-family="{FONT}">{label}</text>
            <text x="{x + w/2}" y="{200}" text-anchor="middle" fill="{MUTED}" font-size="10" font-family="{FONT}">{sub}</text>
          </g>'''
    body = bar_svg + f'<text x="320" y="52" text-anchor="middle" fill="{MUTED}" font-size="10" letter-spacing="0.06em" font-family="{FONT}">DISPATCH DURATION SPECTRUM</text>'
    return _figure(
        "mid",
        "Progress",
        _svg("0 0 640 220", uid, body),
        "Grid models show different optimal storage durations by region: hours for solar peaks, multi-day for wind-heavy systems.",
    )


def _energy_loop():
    uid = _set_uid(_uid("en"))
    labels = ("Cheap clean power", "Electrification", "Interconnect queue", "AI load")
    return _figure(
        "loop",
        "The rebound loop",
        _svg("0 0 640 280", uid, _loop(uid, 320, 148, 92, labels)),
        "Cheaper renewables accelerate electrification and data-center load, stressing interconnection and planning.",
    )


# --- Manufacturing ---

def _manufacturing_hero():
    uid = _set_uid(_uid("mf"))
    body = f"""
          <rect x="36" y="58" width="268" height="130" rx="14" fill="{BG_ALT}" stroke="{MUTED}" stroke-width="1.2"/>
          {_col_label(170, 78, "Old")}
          <path d="M120 118 Q150 92 180 118 Q210 88 240 118" fill="none" stroke="#8a6050" stroke-width="2" opacity="0.55"/>
          <text x="170" y="142" text-anchor="middle" fill="{MUTED}" font-size="10" font-family="{FONT}">Fossil flame heat</text>
          <rect x="120" y="152" width="100" height="24" rx="6" fill="{MUTED}" opacity="0.25"/>
          <rect x="336" y="58" width="268" height="130" rx="14" fill="{CREAM}" stroke="{FOREST}" stroke-width="1.2"/>
          {_col_label(470, 78, "New")}
          <rect x="400" y="108" width="36" height="36" rx="8" fill="{FOREST}" opacity="0.2"/>
          <text x="418" y="131" text-anchor="middle" fill="{FOREST}" font-size="10" font-weight="600" font-family="{FONT}">E</text>
          <circle cx="490" cy="126" r="20" fill="{CREAM}" stroke="{FOREST}"/>
          <circle cx="490" cy="126" r="8" fill="{FOREST}" opacity="0.3"/>
          <text x="470" y="158" text-anchor="middle" fill="{FOREST}" font-size="10" font-family="{FONT}">Electric and solar heat</text>"""
    return _figure(
        "hero",
        "How it works",
        _svg("0 0 640 210", uid, body, "Factory heat: old vs new"),
        "Industrial decarbonization targets high-temperature heat currently supplied by combustion.",
    )


def _manufacturing_mid():
    uid = _set_uid(_uid("mf"))
    layers = [("Efficiency", 0.22), ("Electrify", 0.28), ("Low-carbon fuels", 0.26), ("CCUS", 0.24)]
    y0, h_total = 70, 120
    stack = ""
    y = y0 + h_total
    for i, (name, frac) in enumerate(layers):
        lh = h_total * frac
        y -= lh
        stack += f'''
          <g class="viz-fade-slide" style="animation-delay:{i * 0.1}s">
            <rect x="200" y="{y}" width="240" height="{lh}" fill="{SOFT if i % 2 else FOREST}" opacity="{0.35 + i * 0.15}"/>
            <text x="420" y="{y + lh/2 + 4}" fill="{FOREST}" font-size="10" font-weight="600" font-family="{FONT}">{name}</text>
          </g>'''
    body = stack + f'<text x="320" y="52" text-anchor="middle" fill="{MUTED}" font-size="10" font-family="{FONT}">Abatement stack (illustrative sequencing)</text>'
    return _figure(
        "mid",
        "Progress",
        _svg("0 0 640 220", uid, body),
        "NSF and university work sequences efficiency, electrification, fuels, and capture by cost and temperature needs.",
    )


def _manufacturing_loop():
    uid = _set_uid(_uid("mf"))
    labels = ("Cheaper heat tech", "More output", "Grid gaps", "Data gaps")
    return _figure(
        "loop",
        "The rebound loop",
        _svg("0 0 640 280", uid, _loop(uid, 320, 148, 92, labels)),
        "Affordable process heat can expand production before grid and metering infrastructure keep pace.",
    )


# --- Built ---

def _built_hero():
    uid = _set_uid(_uid("bu"))
    body = f"""
          <line x1="120" y1="168" x2="520" y2="168" stroke="{MUTED}" stroke-width="2"/>
          <polygon points="280,58 320,38 360,58" fill="{FOREST}" opacity="0.12" stroke="{FOREST}"/>
          <rect x="280" y="58" width="80" height="110" fill="{CREAM}" stroke="{FOREST}" stroke-width="1.2"/>
          <circle class="viz-pulse" cx="320" cy="178" r="12" fill="{FOREST}"/>
          <rect x="48" y="88" width="130" height="72" rx="12" fill="url(#{uid}-card)"/>
          <text x="113" y="118" text-anchor="middle" fill="{CREAM}" font-size="11" font-weight="600" font-family="{FONT}">Embodied</text>
          <text x="113" y="134" text-anchor="middle" fill="{CREAM}" font-size="9" font-family="{FONT}">materials</text>
          <rect x="462" y="88" width="130" height="72" rx="12" fill="{FOREST}"/>
          <text x="527" y="118" text-anchor="middle" fill="{CREAM}" font-size="11" font-weight="600" font-family="{FONT}">Operating</text>
          <text x="527" y="134" text-anchor="middle" fill="{CREAM}" font-size="9" font-family="{FONT}">energy use</text>
          <text x="320" y="210" text-anchor="middle" fill="{MUTED}" font-size="10" font-family="{FONT}">Scale tips as grids decarbonize</text>"""
    return _figure(
        "hero",
        "How it works",
        _svg("0 0 640 230", uid, body, "Embodied vs operating carbon"),
        "Whole-life metrics weigh upfront material carbon against decades of operational emissions.",
    )


def _built_mid():
    uid = _set_uid(_uid("bu"))
    stages = [("A1–A3", 48), ("Use phase", 200), ("End of life", 352)]
    stage_svg = ""
    for i, (name, x) in enumerate(stages):
        stage_svg += _node_simple(uid, x, 90, 120, 44, name, variant="cream" if i == 0 else ("solid" if i == 1 else "muted"), delay=i * 0.12)
        if i < 2:
            stage_svg += _line(x + 120, 112, stages[i + 1][1], 112, uid)
    body = stage_svg + f'<rect x="48" y="168" width="544" height="10" rx="5" fill="{BG_ALT}"/><rect x="48" y="168" width="200" height="10" rx="5" fill="{SOFT}" opacity="0.5"/>'
    return _figure(
        "mid",
        "Progress",
        _svg("0 0 640 210", uid, body, "Life-cycle stages"),
        "Modules A1–A3 often dominate embodied totals; use-phase carbon falls as grids clean up.",
    )


def _built_loop():
    uid = _set_uid(_uid("bu"))
    labels = ("Cheap LCA tools", "More claims", "EPD noise", "Trust erodes")
    return _figure(
        "loop",
        "The rebound loop",
        _svg("0 0 640 280", uid, _loop(uid, 320, 148, 92, labels)),
        "Easier LCA software can flood projects with unverified embodied-carbon claims.",
    )


# --- Mobility ---

def _mobility_hero():
    uid = _set_uid(_uid("mb"))
    body = f"""
          {_node_simple(uid, 240, 56, 160, 44, "Electric vehicle", variant="primary", primary=True, delay=0)}
          <line class="viz-draw" x1="280" y1="100" x2="180" y2="138" stroke="{FOREST}" stroke-width="1.5"/>
          <line class="viz-draw" x1="360" y1="100" x2="460" y2="138" stroke="{FOREST}" stroke-width="1.5"/>
          {_node_simple(uid, 80, 142, 200, 52, "Financing", "loan terms", variant="cream", delay=0.15)}
          {_node_simple(uid, 360, 142, 200, 52, "Charger uptime", "reliability", variant="cream", delay=0.25)}"""
    return _figure(
        "hero",
        "How it works",
        _svg("0 0 640 220", uid, body, "Two gates to adoption"),
        "Hardware improves, but credit spreads and charger reliability still gate mass adoption.",
    )


def _mobility_mid():
    uid = _set_uid(_uid("mb"))
    pct = 78
    ang = math.pi * (1 - pct / 100)
    ex = 320 + 100 * math.cos(ang)
    ey = 160 - 100 * math.sin(ang)
    body = f"""
          <text x="320" y="58" text-anchor="middle" fill="{FOREST}" font-size="11" font-weight="600" font-family="{FONT}">Public charging reliability</text>
          <path d="M120 160 A100 100 0 0 1 520 160" fill="none" stroke="{BG_ALT}" stroke-width="18" stroke-linecap="round"/>
          <path class="viz-draw" d="M120 160 A100 100 0 0 1 {ex:.1f} {ey:.1f}" fill="none" stroke="{SOFT}" stroke-width="18" stroke-linecap="round"/>
          <text x="320" y="148" text-anchor="middle" fill="{FOREST}" font-size="28" font-weight="600" font-family="{FONT}">{pct}%</text>
          <text x="320" y="188" text-anchor="middle" fill="{MUTED}" font-size="10" font-family="{FONT}">Successful sessions (estimate)</text>"""
    return _figure(
        "mid",
        "Progress",
        _svg("0 0 640 210", uid, body),
        "Review-based estimates suggest roughly one in five public charging attempts still fails.",
    )


def _mobility_loop():
    uid = _set_uid(_uid("mb"))
    labels = ("Cheaper EVs", "More charging", "Grid strain", "Uptime risk")
    return _figure(
        "loop",
        "The rebound loop",
        _svg("0 0 640 280", uid, _loop(uid, 320, 148, 92, labels)),
        "Lower vehicle prices drive charging demand, which stresses grid hosting and maintenance accountability.",
    )


# --- Industrial ---

def _industrial_hero():
    uid = _set_uid(_uid("in"))
    sec_svg = "\n".join(
        _node_simple(uid, 40, 56 + i * 56, 88, 44, name, variant="cream", delay=i * 0.08)
        for i, name in enumerate(("Cement", "Steel", "Chemicals"))
    )
    body = f"""
          {sec_svg}
          {_line(128, 110, 188, 110, uid)}
          {_node_simple(uid, 188, 88, 132, 48, "Playbook", variant="primary", primary=True, delay=0.3)}
          {_line(320, 112, 360, 112, uid)}
          {_node_simple(uid, 360, 72, 100, 36, "Heat", variant="solid", delay=0.38)}
          {_node_simple(uid, 360, 116, 100, 36, "Materials", variant="solid", delay=0.44)}
          {_node_simple(uid, 360, 160, 100, 36, "Cost tools", variant="solid", delay=0.5)}"""
    return _figure(
        "hero",
        "How it works",
        _svg("0 0 640 220", uid, body, "Hard industries need a playbook"),
        "Cement, steel, and chemicals decarbonize through sequenced heat, material, and cost options—not one silver bullet.",
    )


def _industrial_mid():
    uid = _set_uid(_uid("in"))
    steps = [("Pilot", 48), ("Cost curve", 220), ("Deploy", 392)]
    mid = ""
    for i, (lab, x) in enumerate(steps):
        mid += _node_simple(uid, x, 92, 120, 44, lab, variant="primary" if i == 1 else "cream", primary=(i == 1), delay=i * 0.12)
        if i < 2:
            mid += _line(x + 120, 114, steps[i + 1][1], 114, uid)
    body = mid + f'''
          <rect x="48" y="168" width="544" height="6" rx="3" fill="{BG_ALT}"/>
          <rect x="48" y="168" width="360" height="6" rx="3" fill="{SOFT}" opacity="0.45"/>
          <text x="320" y="198" text-anchor="middle" fill="{MUTED}" font-size="10" font-family="{FONT}">Evidence before scale</text>'''
    return _figure(
        "mid",
        "Progress",
        _svg("0 0 640 220", uid, body, "Pilot to deployment"),
        "University-industry partnerships publish pilots, abatement curves, then deployment thresholds under carbon pricing.",
    )


def _industrial_loop():
    uid = _set_uid(_uid("in"))
    labels = ("Cheaper abatement", "Higher output", "MRV gaps", "Infra lag")
    return _figure(
        "loop",
        "The rebound loop",
        _svg("0 0 640 280", uid, _loop(uid, 320, 148, 92, labels)),
        "Lower abatement cost can raise production before monitoring and infrastructure verify reductions.",
    )


# --- Space compute ---

def _space_hero():
    uid = _set_uid(_uid("sp"))
    body = f"""
          {_col_label(48, 52, "Terrestrial")}
          {_node_simple(uid, 24, 58, 140, 44, "Grid + water", "power wall", variant="cream", delay=0)}
          {_line(164, 80, 200, 80, uid, muted=True)}
          {_node_simple(uid, 200, 58, 120, 44, "AI DC", variant="muted", delay=0.08)}
          {_col_label(380, 52, "Orbital path")}
          {_node_simple(uid, 360, 58, 100, 40, "Solar array", variant="solid", delay=0.16)}
          {_line(460, 78, 496, 78, uid)}
          {_node_simple(uid, 496, 52, 120, 52, "TPU / GPU", "sunlit orbit", variant="primary", primary=True, delay=0.24)}
          <text x="320" y="128" text-anchor="middle" fill="{MUTED}" font-size="10" font-family="{FONT}">Earth faces siting; orbit trades launch for continuous sun + radiative cooling</text>
          {_node_simple(uid, 80, 142, 200, 44, "Permitting queue", variant="muted", delay=0.3)}
          {_node_simple(uid, 360, 142, 200, 44, "Optical downlink", variant="cream", delay=0.38)}"""
    return _figure(
        "hero",
        "How it works",
        _svg("0 0 640 220", uid, body, "Two paths for AI compute"),
        "Terrestrial data centers hit grid and cooling limits; orbital designs chase sun and passive heat rejection.",
    )


def _space_mid():
    uid = _set_uid(_uid("sp"))
    steps = [("Solar", 40), ("TPU/GPU", 180), ("Optical ISL", 320), ("Ground link", 460)]
    mid = ""
    for i, (lab, x) in enumerate(steps):
        mid += _node_simple(uid, x, 92, 120, 44, lab, variant="primary" if i == 1 else "cream", primary=(i == 1), delay=i * 0.1)
        if i < 3:
            mid += _line(x + 120, 114, steps[i + 1][1], 114, uid)
    body = mid + f'''
          <text x="320" y="178" text-anchor="middle" fill="{MUTED}" font-size="10" font-family="{FONT}">Power → compute → mesh → downlink (conceptual pipeline)</text>'''
    return _figure(
        "mid",
        "Progress",
        _svg("0 0 640 220", uid, body, "Orbital AI pipeline"),
        "Google Suncatcher-style designs chain solar power, accelerators, optical inter-satellite links, and ground terminals.",
    )


def _space_loop():
    uid = _set_uid(_uid("sp"))
    labels = ("Cheaper launch", "More orbital compute", "Debris / spectrum", "Thermal limits")
    return _figure(
        "loop",
        "The rebound loop",
        _svg("0 0 640 280", uid, _loop(uid, 320, 148, 92, labels)),
        "Falling launch cost expands orbital AI, which stresses spectrum, debris rules, and thermal design before climate benefit is proven.",
    )


VIZ_SETS = {
    "space": {"hero": _space_hero(), "mid": _space_mid(), "loop": _space_loop()},
    "weather": {"hero": _weather_hero(), "mid": _weather_mid(), "loop": _weather_loop()},
    "aerospace": {"hero": _aerospace_hero(), "mid": _aerospace_mid(), "loop": _aerospace_loop()},
    "materials": {"hero": _materials_hero(), "mid": _materials_mid(), "loop": _materials_loop()},
    "energy": {"hero": _energy_hero(), "mid": _energy_mid(), "loop": _energy_loop()},
    "manufacturing": {"hero": _manufacturing_hero(), "mid": _manufacturing_mid(), "loop": _manufacturing_loop()},
    "built": {"hero": _built_hero(), "mid": _built_mid(), "loop": _built_loop()},
    "mobility": {"hero": _mobility_hero(), "mid": _mobility_mid(), "loop": _mobility_loop()},
    "industrial": {"hero": _industrial_hero(), "mid": _industrial_mid(), "loop": _industrial_loop()},
}

VIZ = {k: v["hero"] for k, v in VIZ_SETS.items()}
