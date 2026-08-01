"""Markets section: Jevons intro, rebound cards, and cited SVG charts per sector."""

from __future__ import annotations

import math

from _market_maps import market_map_html
from _timelines import SECTOR_SECTIONS, rebound_cards_html
from _viz import BG, BG_ALT, CREAM, FONT, FOREST, MUTED, SOFT, _esc, _uid

JEVONS_REFS = {
    "space-compute": (7, 8),
    "weather-foundation-models": (13, 14),
    "aerospace-satellites": (9, 10),
    "materials": (8, 9),
    "energy-systems": (7, 8),
    "manufacturing": (7, 8),
    "built-environment": (7, 8),
    "mobility": (9, 10),
    "industrial-processes": (8, 9),
}

# Reference indices for consultant-sourced chart captions (see consultant_refs_* in _generate.py).
CONSULTANT_REF_IDS: dict[str, dict[str, int]] = {
    "space-compute": {"mckinsey_dc": 10, "gs_power": 11},
    "weather-foundation-models": {"mckinsey_space": 15, "gs_power": 16},
    "aerospace-satellites": {"mckinsey_space": 11},
    "materials": {"mckinsey_materials": 10},
    "energy-systems": {"mckinsey_ldes": 9, "gs_battery": 10},
    "manufacturing": {"mckinsey_infra": 9},
    "built-environment": {"mckinsey_built": 9},
    "mobility": {"mckinsey_ev": 11, "gs_battery": 12},
    "industrial-processes": {"mckinsey_materials": 10, "mckinsey_infra": 11},
}

CHART_W = 640
CHART_H = 320
BAR_FILL = SOFT
BAR_FILL_ALT = FOREST
LABEL_COL = 150
PLOT_LEFT = 168
PLOT_RIGHT = 620
ROW_H = 38


def _c(n: int) -> str:
    return f'[<a href="#r{n}">{n}</a>]'


def _ref(slug: str, key: str) -> int:
    return CONSULTANT_REF_IDS[slug][key]


def _chart_svg(title: str, inner: str, *, w: int = CHART_W, h: int = CHART_H) -> str:
    uid = _uid("mc")
    title_el = (
        f'<text x="20" y="28" fill="{FOREST}" font-size="13" font-weight="600" '
        f'font-family="{FONT}">{_esc(title)}</text>'
    )
    return f'''        <svg aria-hidden="true" class="viz-svg chart-svg" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="{uid}-bg" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="{BG}"/>
              <stop offset="100%" stop-color="{BG_ALT}"/>
            </linearGradient>
          </defs>
          <rect width="{w}" height="{h}" fill="url(#{uid}-bg)" rx="12"/>
          {title_el}
{inner}
        </svg>'''


def _h_grid(y0: int, y1: int, n: int = 4) -> str:
    lines = []
    step = (y1 - y0) / n
    for i in range(n + 1):
        y = int(y0 + i * step)
        lines.append(
            f'          <line x1="{PLOT_LEFT}" y1="{y}" x2="{PLOT_RIGHT}" y2="{y}" '
            f'stroke="{FOREST}" stroke-width="1" opacity="0.08"/>'
        )
    return "\n".join(lines)


def _figure(
    chart_title: str,
    svg: str,
    caption: str,
    *,
    source_badge: str | None = None,
    wide: bool = False,
) -> str:
    wrap_class = "viz viz-chart chart-wrap chart-wrap--wide" if wide else "viz viz-chart chart-wrap"
    if source_badge:
        label_inner = (
            f'<span class="chart-source">{_esc(source_badge)}</span>'
            f'<span class="chart-label-text">{_esc(chart_title)}</span>'
        )
    else:
        label_inner = f'<span class="chart-label-text">{_esc(chart_title)}</span>'
    return f'''        <figure class="{wrap_class}">
          <p class="viz-label">{label_inner}</p>
{svg}
          <figcaption class="viz-caption">{caption}</figcaption>
        </figure>'''


def _hbar_chart(
    title: str,
    rows: list[tuple[str, float, str]],
    *,
    unit_note: str | None = None,
    max_value: float | None = None,
) -> str:
    plot_top = 48
    plot_w = PLOT_RIGHT - PLOT_LEFT - 72
    mx = max_value if max_value is not None else max(v for _, v, _ in rows) or 1.0
    if mx <= 0:
        mx = 1.0
    n = len(rows)
    plot_bottom = CHART_H - (36 if unit_note else 24)
    total_h = n * ROW_H
    y_start = plot_top + max(0, (plot_bottom - plot_top - total_h) // 2)

    parts = [_h_grid(y_start, y_start + total_h)]
    for i, (label, value, display) in enumerate(rows):
        y = y_start + i * ROW_H
        bar_w = max(4, int(plot_w * (value / mx)))
        bar_y = y + 10
        parts.append(
            f'          <text x="{LABEL_COL}" y="{y + 24}" text-anchor="end" fill="{FOREST}" '
            f'font-size="11" font-family="{FONT}">{_esc(label)}</text>'
        )
        parts.append(
            f'          <rect x="{PLOT_LEFT}" y="{bar_y}" width="{bar_w}" height="18" rx="5" '
            f'fill="{BAR_FILL}"/>'
        )
        parts.append(
            f'          <text x="{PLOT_LEFT + bar_w + 8}" y="{y + 24}" fill="{MUTED}" '
            f'font-size="11" font-weight="500" font-family="{FONT}">{_esc(display)}</text>'
        )
    if unit_note:
        parts.append(
            f'          <text x="20" y="{CHART_H - 12}" fill="{MUTED}" font-size="10" '
            f'font-family="{FONT}">{_esc(unit_note)}</text>'
        )
    return _chart_svg(title, "\n".join(parts))


def _vbar_chart(
    title: str,
    categories: list[str],
    values: list[float],
    *,
    value_labels: list[str],
    y_label: str | None = None,
    max_value: float | None = None,
) -> str:
    n = len(categories)
    axis_bottom = CHART_H - 44
    axis_top = 52
    plot_h = axis_bottom - axis_top - 8
    mx = max_value if max_value is not None else max(values) or 1.0
    gap = 24
    bar_w = min(56, (PLOT_RIGHT - PLOT_LEFT - gap * (n + 1)) // max(n, 1))
    total_bars_w = n * bar_w + (n - 1) * gap
    x0 = PLOT_LEFT + (PLOT_RIGHT - PLOT_LEFT - total_bars_w) // 2

    parts = [_h_grid(axis_top, axis_bottom)]
    if y_label:
        parts.append(
            f'          <text x="16" y="{(axis_top + axis_bottom) // 2}" fill="{MUTED}" '
            f'font-size="10" font-family="{FONT}" transform="rotate(-90 16 {(axis_top + axis_bottom) // 2})">'
            f'{_esc(y_label)}</text>'
        )
    parts.append(
        f'          <line x1="{PLOT_LEFT}" y1="{axis_bottom}" x2="{PLOT_RIGHT}" y2="{axis_bottom}" '
        f'stroke="{FOREST}" stroke-width="1" opacity="0.2"/>'
    )
    for i, (cat, val, vlab) in enumerate(zip(categories, values, value_labels)):
        x = x0 + i * (bar_w + gap)
        h = max(4, int(plot_h * (val / mx)))
        y = axis_bottom - h
        parts.append(
            f'          <rect x="{x}" y="{y}" width="{bar_w}" height="{h}" rx="6" fill="{BAR_FILL}"/>'
        )
        parts.append(
            f'          <text x="{x + bar_w // 2}" y="{y - 8}" text-anchor="middle" fill="{FOREST}" '
            f'font-size="10" font-weight="600" font-family="{FONT}">{_esc(vlab)}</text>'
        )
        parts.append(
            f'          <text x="{x + bar_w // 2}" y="{axis_bottom + 18}" text-anchor="middle" '
            f'fill="{FOREST}" font-size="10" font-family="{FONT}">{_esc(cat)}</text>'
        )
    return _chart_svg(title, "\n".join(parts))


def _line_chart(
    title: str,
    points: list[tuple[float, float]],
    *,
    x_labels: list[str],
    y_label: str | None = None,
    value_labels: list[str] | None = None,
) -> str:
    axis_bottom = CHART_H - 44
    axis_top = 52
    plot_w = PLOT_RIGHT - PLOT_LEFT
    plot_h = axis_bottom - axis_top
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    if y_max == y_min:
        y_max = y_min + 1

    def sx(x: float) -> float:
        if x_max == x_min:
            return PLOT_LEFT + plot_w / 2
        return PLOT_LEFT + plot_w * (x - x_min) / (x_max - x_min)

    def sy(y: float) -> float:
        return axis_bottom - plot_h * (y - y_min) / (y_max - y_min)

    parts = [_h_grid(axis_top, axis_bottom)]
    if y_label:
        parts.append(
            f'          <text x="16" y="{(axis_top + axis_bottom) // 2}" fill="{MUTED}" '
            f'font-size="10" font-family="{FONT}" transform="rotate(-90 16 {(axis_top + axis_bottom) // 2})">'
            f'{_esc(y_label)}</text>'
        )
    parts.append(
        f'          <line x1="{PLOT_LEFT}" y1="{axis_bottom}" x2="{PLOT_RIGHT}" y2="{axis_bottom}" '
        f'stroke="{FOREST}" stroke-width="1" opacity="0.2"/>'
    )
    poly = " ".join(f"{sx(x):.1f},{sy(y):.1f}" for x, y in points)
    parts.append(
        f'          <polyline points="{poly}" fill="none" stroke="{BAR_FILL}" stroke-width="2.5" '
        f'stroke-linejoin="round"/>'
    )
    for i, ((x, y), xlab) in enumerate(zip(points, x_labels)):
        cx, cy = sx(x), sy(y)
        parts.append(f'          <circle cx="{cx:.1f}" cy="{cy:.1f}" r="5" fill="{FOREST}"/>')
        if value_labels and i < len(value_labels):
            parts.append(
                f'          <text x="{cx:.1f}" y="{cy - 10}" text-anchor="middle" fill="{FOREST}" '
                f'font-size="10" font-weight="600" font-family="{FONT}">{_esc(value_labels[i])}</text>'
            )
        parts.append(
            f'          <text x="{cx:.1f}" y="{axis_bottom + 18}" text-anchor="middle" fill="{MUTED}" '
            f'font-size="10" font-family="{FONT}">{_esc(xlab)}</text>'
        )
    return _chart_svg(title, "\n".join(parts))


def _grouped_bars(
    title: str,
    groups: list[str],
    series: list[tuple[str, list[float], str]],
    *,
    value_labels: list[list[str]] | None = None,
    y_label: str | None = None,
    unit_note: str | None = None,
) -> str:
    """groups = x categories; series = (name, values per group, fill color)."""
    n_g = len(groups)
    n_s = len(series)
    axis_bottom = CHART_H - (52 if unit_note else 44)
    axis_top = 52
    plot_h = axis_bottom - axis_top - 8
    all_vals = [v for _, vals, _ in series for v in vals]
    mx = max(all_vals) if all_vals else 1.0
    group_w = (PLOT_RIGHT - PLOT_LEFT - 20) // max(n_g, 1)
    bar_w = min(28, (group_w - 12) // max(n_s, 1))

    parts = [_h_grid(axis_top, axis_bottom)]
    if y_label:
        parts.append(
            f'          <text x="16" y="{(axis_top + axis_bottom) // 2}" fill="{MUTED}" '
            f'font-size="10" font-family="{FONT}" transform="rotate(-90 16 {(axis_top + axis_bottom) // 2})">'
            f'{_esc(y_label)}</text>'
        )
    parts.append(
        f'          <line x1="{PLOT_LEFT}" y1="{axis_bottom}" x2="{PLOT_RIGHT}" y2="{axis_bottom}" '
        f'stroke="{FOREST}" stroke-width="1" opacity="0.2"/>'
    )
    for gi, gname in enumerate(groups):
        gx = PLOT_LEFT + 10 + gi * group_w + group_w // 2
        for si, (sname, vals, color) in enumerate(series):
            val = vals[gi]
            h = max(4, int(plot_h * (val / mx)))
            x = gx - (n_s * bar_w + (n_s - 1) * 4) // 2 + si * (bar_w + 4)
            y = axis_bottom - h
            fill = color or (BAR_FILL if si == 0 else BAR_FILL_ALT)
            parts.append(
                f'          <rect x="{x}" y="{y}" width="{bar_w}" height="{h}" rx="4" fill="{fill}" '
                f'opacity="{0.85 if si else 1}"/>'
            )
            if value_labels and si < len(value_labels) and gi < len(value_labels[si]):
                parts.append(
                    f'          <text x="{x + bar_w // 2}" y="{y - 6}" text-anchor="middle" '
                    f'fill="{FOREST}" font-size="9" font-weight="600" font-family="{FONT}">'
                    f'{_esc(value_labels[si][gi])}</text>'
                )
        parts.append(
            f'          <text x="{gx}" y="{axis_bottom + 18}" text-anchor="middle" fill="{FOREST}" '
            f'font-size="10" font-family="{FONT}">{_esc(gname)}</text>'
        )
    legend_x = PLOT_RIGHT - 140
    for si, (sname, _, color) in enumerate(series):
        ly = 40 + si * 16
        fill = color or BAR_FILL
        parts.append(f'          <rect x="{legend_x}" y="{ly}" width="10" height="10" rx="2" fill="{fill}"/>')
        parts.append(
            f'          <text x="{legend_x + 14}" y="{ly + 9}" fill="{MUTED}" font-size="9" '
            f'font-family="{FONT}">{_esc(sname)}</text>'
        )
    if unit_note:
        parts.append(
            f'          <text x="20" y="{CHART_H - 12}" fill="{MUTED}" font-size="10" '
            f'font-family="{FONT}">{_esc(unit_note)}</text>'
        )
    return _chart_svg(title, "\n".join(parts), h=340)


def _donut_chart(title: str, segments: list[tuple[str, float, str, str]], *, center: tuple[str, str]) -> str:
    """Simple two-segment donut using paths (segments: label, pct 0-100, display, fill)."""
    cx, cy, r = 200, 155, 72
    parts = []
    start = -90
    for label, pct, display, fill in segments:
        angle = 360 * pct / 100
        end = start + angle
        large = 1 if angle > 180 else 0
        def pt(deg: float) -> tuple[float, float]:
            rad = math.radians(deg)
            return cx + r * math.cos(rad), cy + r * math.sin(rad)

        x1, y1 = pt(start)
        x2, y2 = pt(end)
        parts.append(
            f'          <path d="M {cx} {cy} L {x1:.1f} {y1:.1f} A {r} {r} 0 {large} 1 {x2:.1f} {y2:.1f} Z" '
            f'fill="{fill}"/>'
        )
        start = end
    parts.append(f'          <circle cx="{cx}" cy="{cy}" r="48" fill="{BG_ALT}"/>')
    parts.append(
        f'          <text x="{cx}" y="{cy - 4}" text-anchor="middle" fill="{FOREST}" font-size="12" '
        f'font-weight="600" font-family="{FONT}">{_esc(center[0])}</text>'
    )
    parts.append(
        f'          <text x="{cx}" y="{cy + 14}" text-anchor="middle" fill="{MUTED}" font-size="10" '
        f'font-family="{FONT}">{_esc(center[1])}</text>'
    )
    lx = 320
    for i, (label, _, display, fill) in enumerate(segments):
        ly = 100 + i * 36
        parts.append(f'          <rect x="{lx}" y="{ly}" width="12" height="12" rx="2" fill="{fill}"/>')
        parts.append(
            f'          <text x="{lx + 18}" y="{ly + 10}" fill="{FOREST}" font-size="11" '
            f'font-family="{FONT}">{_esc(label)}</text>'
        )
        parts.append(
            f'          <text x="{lx + 18}" y="{ly + 24}" fill="{MUTED}" font-size="10" '
            f'font-family="{FONT}">{_esc(display)}</text>'
        )
    return _chart_svg(title, "\n".join(parts))


def _space_charts() -> list[str]:
    slug = "space-compute"
    c1 = _figure(
        "Orbital vs terrestrial cost",
        _hbar_chart(
            "Relative capital cost (~1 GW class)",
            [
                ("Terrestrial DC (baseline)", 1.0, "1×"),
                ("Orbital DC (WoodMac scenario)", 3.0, "~3×"),
            ],
            unit_note="Illustrative ratio from published WoodMac scenario estimates.",
            max_value=3.2,
        ),
        f"Illustrative redraw of Wood Mackenzie, 2026 scenario: orbital capacity can cost on the order of "
        f"three times a terrestrial equivalent for a ~1 GW class build {_c(4)}.",
        source_badge="WoodMac",
    )
    c2 = _figure(
        "Data center power capacity demand",
        _grouped_bars(
            "Global DC capacity (McKinsey estimate, GW)",
            ["2025", "2030"],
            [
                ("Non-AI workload", [38.0, 63.0], BAR_FILL_ALT),
                ("AI workload", [44.0, 156.0], BAR_FILL),
            ],
            value_labels=[["38", "63"], ["44", "156"]],
            y_label="GW",
            unit_note="Totals ~82 GW (2025) and ~219 GW (2030) in McKinsey scenario.",
        ),
        f"McKinsey estimate of global data center capacity demand, including AI and non-AI workloads "
        f"(scenario, not a forecast of certainty) {_c(_ref(slug, 'mckinsey_dc'))}.",
        source_badge="McKinsey",
    )
    c3 = _figure(
        "Data center power demand index",
        _line_chart(
            "Power demand vs 2023 (Goldman Sachs Research)",
            [(2023, 100), (2027, 150), (2030, 265)],
            x_labels=["2023", "2027", "2030"],
            y_label="Index (2023 = 100)",
            value_labels=["100", "+50%", "+165%"],
        ),
        f"Goldman Sachs Research forecast: data center power demand about +50% by 2027 and up to about "
        f"+165% by 2030 versus 2023 (indexed schematic) {_c(_ref(slug, 'gs_power'))}.",
        source_badge="Goldman Sachs",
        wide=True,
    )
    return [c1, c2, c3]


def _weather_charts() -> list[str]:
    slug = "weather-foundation-models"
    c1 = _figure(
        "Forecast wall-clock",
        _hbar_chart(
            "Inference time (qualitative)",
            [
                ("Classical NWP (supercomputer)", 10.0, "hours-scale"),
                ("AI emulators (GraphCast, FourCastNet)", 1.8, "minutes-scale"),
            ],
            unit_note="Orders of magnitude faster in reported benchmarks; not to scale.",
            max_value=10.0,
        ),
        f"Source: Lam et al., 2023 {_c(2)}; Pathak et al., 2022 {_c(9)}. Absolute runtimes vary by hardware and resolution.",
    )
    c2 = _figure(
        "Benchmark skill vs IFS",
        _vbar_chart(
            "Deterministic skill (schematic index)",
            ["IFS baseline", "Leading AI"],
            [1.0, 1.05],
            value_labels=["1.0", "match / beat"],
            y_label="Relative skill",
            max_value=1.2,
        ),
        f"Source: Rasp et al., 2024 {_c(10)}; Lam et al., 2023 {_c(2)}; Bi et al., 2023 {_c(3)}.",
    )
    c3 = _figure(
        "Space-enabled economy scale",
        _line_chart(
            "Space economy (McKinsey / WEF scenario)",
            [(2023, 630), (2035, 1800)],
            x_labels=["2023", "2035"],
            y_label="USD billions",
            value_labels=["$630B", "$1.8T"],
        ),
        f"McKinsey estimate with WEF framing: space-enabled services (including Earth observation, weather data, "
        f"and climate insights as part of the broader space economy) from about $630B (2023) toward about "
        f"$1.8T (2035) in a growth scenario {_c(_ref(slug, 'mckinsey_space'))}.",
        source_badge="McKinsey",
    )
    c4 = _figure(
        "Compute power demand (enabling AI weather)",
        _line_chart(
            "Data center power vs 2023 (Goldman Sachs Research)",
            [(2023, 100), (2027, 150), (2030, 265)],
            x_labels=["2023", "2027", "2030"],
            y_label="Index (2023 = 100)",
            value_labels=["100", "+50%", "+165%"],
        ),
        f"Goldman Sachs Research forecast: data center power demand growth that underpins large-scale AI weather "
        f"workloads (indexed schematic; same outlook as hyperscale compute) {_c(_ref(slug, 'gs_power'))}.",
        source_badge="Goldman Sachs",
        wide=True,
    )
    return [c1, c2, c3, c4]


def _aerospace_charts() -> list[str]:
    slug = "aerospace-satellites"
    labels = [
        ("SkySense", 21.5, "21.5M seq."),
        ("SkySense++", 27.0, "~27M images"),
        ("Prithvi-EO", 4.2, "4.2M samples"),
        ("Copernicus-FM", 18.7, "18.7M obs."),
    ]
    c1 = _figure(
        "Pretraining corpus scale",
        _hbar_chart(
            "Public-archive pretraining (reported)",
            labels,
            unit_note="Millions of training units per model family.",
            max_value=27.0,
        ),
        f"Source: Guo et al., 2024 {_c(2)}; Wu et al., 2025 {_c(3)}; Szwarcman et al., 2024 {_c(4)}; "
        f"Wang et al., 2025 {_c(5)}.",
    )
    c2 = _figure(
        "Carbon-I resolution targets",
        _hbar_chart(
            "GHG mapping resolution (mission design)",
            [
                ("Global mapping", 10.0, "~300 m"),
                ("Priority targets", 3.0, "~30 m"),
            ],
            max_value=10.0,
        ),
        f"Source: Carbon-I mission materials {_c(7)}.",
    )
    c3 = _figure(
        "Space economy outlook",
        _line_chart(
            "Space economy (McKinsey scenario)",
            [(2023, 630), (2035, 1800)],
            x_labels=["2023", "2035"],
            y_label="USD billions",
            value_labels=["$630B", "$1.8T"],
        ),
        f"McKinsey estimate: global space economy from about $630B (2023) toward about $1.8T (2035), "
        f"including Earth observation and downstream analytics (scenario) {_c(_ref(slug, 'mckinsey_space'))}.",
        source_badge="McKinsey",
    )
    return [c1, c2, c3]


def _materials_charts() -> list[str]:
    slug = "materials"
    c1 = _figure(
        "Cement emissions share",
        _donut_chart(
            "Global CO₂ (cement vs rest)",
            [
                ("Cement (~8%)", 8, "~8% of global CO₂", SOFT),
                ("Other sources", 92, "remainder", MUTED),
            ],
            center=("~8%", "cement share"),
        ),
        f"Source: IEA / IPCC industry briefs {_c(7)}.",
    )
    c2 = _figure(
        "Low-carbon cement targets",
        _hbar_chart(
            "Stanford Phlego (reported project targets)",
            [
                ("Emissions reduction target", 7.6, "up to ~76%"),
                ("Production cost target", 2.0, "up to ~20%"),
            ],
            unit_note="Illustrative bars from project disclosures.",
            max_value=10.0,
        ),
        f"Source: Vanorio et al. / Stanford Sustainability Accelerator {_c(1)}{_c(2)}.",
    )
    c3 = _figure(
        "Low-CO₂ materials market",
        _vbar_chart(
            "Global market by 2030 (McKinsey estimate)",
            ["Low range", "High range"],
            [80.0, 105.0],
            value_labels=["$80B", "$105B"],
            y_label="USD billions",
            max_value=120.0,
        ),
        f"McKinsey estimate: global market for low-CO₂ steel, chemicals, and cement about "
        f"$80B to $105B by 2030 in a materials-transition scenario {_c(_ref(slug, 'mckinsey_materials'))}.",
        source_badge="McKinsey",
    )
    return [c1, c2, c3]


def _energy_charts() -> list[str]:
    slug = "energy-systems"
    c1 = _figure(
        "Battery pack cost trend",
        _line_chart(
            "Li-ion storage cost trajectory (IRENA)",
            [(2010, 100), (2015, 45), (2020, 22), (2023, 15)],
            x_labels=["2010", "2015", "2020", "2023"],
            y_label="Relative cost index",
            value_labels=["high", "", "", "lower"],
        ),
        f"Source: IRENA, 2023 {_c(6)}. Illustrative trend index, not annual published points.",
    )
    c2 = _figure(
        "LDES duration by resource mix",
        _hbar_chart(
            "Useful storage duration (model ranges)",
            [
                ("Solar-heavy regions", 6.0, "6–10 h"),
                ("Wind-heavy regions", 10.0, "10–20 h"),
            ],
            unit_note="Staadecker et al. model ranges for long-duration storage needs.",
            max_value=10.0,
        ),
        f"Source: Staadecker et al., 2024 {_c(1)}.",
    )
    c3 = _figure(
        "LDES investment and capacity",
        _hbar_chart(
            "McKinsey net-zero power scenario (2040)",
            [
                ("Cumulative LDES investment", 3.0, "$1.5T–$3T"),
                ("LDES power capacity potential", 2.5, "1.5–2.5 TW"),
            ],
            unit_note="Endpoint ranges from McKinsey LDES outlook (illustrative bars).",
            max_value=3.0,
        ),
        f"McKinsey estimate: cumulative long-duration storage investment about $1.5T to $3T by 2040, with "
        f"about 1.5 to 2.5 TW power capacity potential in a renewable-grid scenario "
        f"{_c(_ref(slug, 'mckinsey_ldes'))}.",
        source_badge="McKinsey",
    )
    c4 = _figure(
        "Battery pack cost outlook",
        _line_chart(
            "Pack cost toward end-2026 (Goldman Sachs Research)",
            [(2024, 110), (2026, 80)],
            x_labels=["2024", "End-2026"],
            y_label="USD / kWh",
            value_labels=["", "~$80"],
        ),
        f"Goldman Sachs Research forecast: lithium-ion battery pack costs toward about $80/kWh by end-2026 "
        f"in their decarbonization outlook (two-point schematic) {_c(_ref(slug, 'gs_battery'))}.",
        source_badge="Goldman Sachs",
        wide=True,
    )
    return [c1, c2, c3, c4]


def _manufacturing_charts() -> list[str]:
    slug = "manufacturing"
    c1 = _figure(
        "Carbon price and abatement",
        _vbar_chart(
            "EU cement direct emissions cut (modeled)",
            ["~€85 / tCO₂", "> €100 / tCO₂"],
            [33.0, 55.0],
            value_labels=["~⅓ cut", "Sharper cut"],
            y_label="Optimal abatement (%)",
            max_value=60.0,
        ),
        f"Source: Glenk, Meier, &amp; Reichelstein, 2024 {_c(5)}.",
    )
    c2 = _figure(
        "Renewable industrial heat",
        _vbar_chart(
            "U.S. industrial heat economically addressable",
            ["Near term", "By ~2035"],
            [11.0, 34.0],
            value_labels=["~11%", "~34%"],
            y_label="Share of demand (%)",
            max_value=40.0,
        ),
        f"Source: UC Berkeley GSPP working paper {_c(4)}.",
    )
    c3 = _figure(
        "Net-zero infrastructure unit costs",
        _hbar_chart(
            "McKinsey net-zero economy scenario (2050 uplift)",
            [
                ("Cement unit cost", 4.5, "+~45%"),
                ("Steel unit cost", 3.0, "+~30%"),
            ],
            unit_note="Relative uplift vs today in McKinsey infrastructure scenario.",
            max_value=5.0,
        ),
        f"McKinsey estimate: in a net-zero infrastructure scenario, cement unit costs rise about 45% and steel "
        f"about 30% by 2050 versus today (illustrative comparison) {_c(_ref(slug, 'mckinsey_infra'))}.",
        source_badge="McKinsey",
    )
    return [c1, c2, c3]


def _built_charts() -> list[str]:
    slug = "built-environment"
    bars = [
        ("Embodied (ECI median)", 385, "385 kgCO₂e/m²"),
        ("Operational (OCI median)", 228, "228 kgCO₂e/m²"),
        ("Whole-life (WLCI median)", 734, "734 kgCO₂e/m²"),
    ]
    c1 = _figure(
        "California building medians",
        _hbar_chart(
            "30 buildings — median intensities",
            bars,
            unit_note="Shen et al. median whole-life carbon intensities.",
            max_value=734.0,
        ),
        f"Source: Shen et al., 2025 {_c(1)}.",
    )
    c2 = _figure(
        "Whole-life carbon spread",
        _vbar_chart(
            "WLCI range in sample (kgCO₂e/m²)",
            ["Minimum", "Maximum"],
            [232.0, 2230.0],
            value_labels=["232", "2,230"],
            y_label="kgCO₂e/m²",
            max_value=2300.0,
        ),
        f"Source: Shen et al., 2025 {_c(1)}. Endpoint bars for min and max in the same sample.",
    )
    c3 = _figure(
        "Decarbonization lever potential",
        _hbar_chart(
            "McKinsey built environment levers (upper bounds)",
            [
                ("Operational emissions reduction", 9.0, "up to ~90%"),
                ("Embodied emissions reduction", 6.0, "up to ~60%"),
            ],
            unit_note="Selected levers for most built-environment assets in McKinsey analysis.",
            max_value=10.0,
        ),
        f"McKinsey estimate: selected levers can cut operational emissions up to about 90% and embodied emissions "
        f"up to about 60% for most built-environment assets in studied cases "
        f"{_c(_ref(slug, 'mckinsey_built'))}.",
        source_badge="McKinsey",
    )
    return [c1, c2, c3]


def _mobility_charts() -> list[str]:
    slug = "mobility"
    c1 = _figure(
        "Charging reliability",
        _hbar_chart(
            "Public charging success rate (U.S.)",
            [("Successful sessions (review data)", 78.0, "~78%")],
            unit_note="Harvard BiGS analysis of large consumer review dataset.",
            max_value=100.0,
        ),
        f"Source: Asensio et al., Harvard BiGS {_c(3)}.",
    )
    c2 = _figure(
        "EV financing gap",
        _hbar_chart(
            "Loan terms vs ICE (directional)",
            [
                ("EV interest rate", 7.0, "higher"),
                ("ICE interest rate", 4.0, "lower"),
                ("EV loan-to-value", 5.0, "lower LTV"),
                ("ICE loan-to-value", 8.0, "higher LTV"),
            ],
            unit_note="Obsolescence-risk mechanism; qualitative comparison.",
            max_value=10.0,
        ),
        f"Source: Bena, Bian, &amp; Tang {_c(1)}{_c(2)}.",
    )
    c3 = _figure(
        "EV sales and battery demand",
        _grouped_bars(
            "McKinsey Battery 2030 scenario",
            ["2025 / 2022", "2030"],
            [
                ("Global EV share of sales (%)", [23.0, 45.0], BAR_FILL),
                ("Li-ion demand (index, 2022=100)", [100.0, 671.0], BAR_FILL_ALT),
            ],
            value_labels=[["23%", "45%"], ["700 GWh", "4.7 TWh"]],
            y_label="Scenario endpoints",
            unit_note="Li-ion ~700 GWh (2022) to ~4.7 TWh (2030); value chain >$400B per McKinsey.",
        ),
        f"McKinsey estimate: EVs from about 23% of global vehicle sales (2025) to about 45% (2030); "
        f"lithium-ion demand from about 700 GWh (2022) to about 4.7 TWh (2030) in a resilient-supply scenario "
        f"{_c(_ref(slug, 'mckinsey_ev'))}.",
        source_badge="McKinsey",
        wide=True,
    )
    c4 = _figure(
        "Battery pack cost outlook",
        _line_chart(
            "Pack cost toward end-2026 (Goldman Sachs Research)",
            [(2024, 110), (2026, 80)],
            x_labels=["2024", "End-2026"],
            y_label="USD / kWh",
            value_labels=["", "~$80"],
        ),
        f"Goldman Sachs Research forecast: battery pack costs toward about $80/kWh by end-2026 "
        f"(decarbonization outlook; schematic endpoints) {_c(_ref(slug, 'gs_battery'))}.",
        source_badge="Goldman Sachs",
    )
    return [c1, c2, c3, c4]


def _industrial_charts() -> list[str]:
    slug = "industrial-processes"
    c1 = _figure(
        "Industrial heat storage cost",
        _hbar_chart(
            "Relative cost per thermal kWh (schematic)",
            [
                ("Li-ion batteries", 10.0, "higher $/kWh"),
                ("Firebrick storage", 1.0, "~1/10 cost"),
            ],
            max_value=10.0,
        ),
        f"Source: Jacobson et al., 2024 {_c(3)}.",
    )
    c2 = _figure(
        "Heat electrification potential",
        _vbar_chart(
            "U.S. industrial heat — renewable + storage",
            ["Near term", "By ~2035"],
            [11.0, 34.0],
            value_labels=["rising", "~34%"],
            y_label="Addressable share (%)",
            max_value=40.0,
        ),
        f"Source: UC Berkeley GSPP working paper {_c(4)}; Glenk et al. {_c(6)}.",
    )
    c3 = _figure(
        "Low-CO₂ materials market",
        _vbar_chart(
            "Global market by 2030 (McKinsey estimate)",
            ["Low range", "High range"],
            [80.0, 105.0],
            value_labels=["$80B", "$105B"],
            y_label="USD billions",
            max_value=120.0,
        ),
        f"McKinsey estimate: low-CO₂ steel, chemicals, and cement market about $80B to $105B by 2030 "
        f"{_c(_ref(slug, 'mckinsey_materials'))}.",
        source_badge="McKinsey",
    )
    c4 = _figure(
        "Net-zero unit cost uplift",
        _hbar_chart(
            "McKinsey infrastructure scenario (2050)",
            [
                ("Cement unit cost", 4.5, "+~45%"),
                ("Steel unit cost", 3.0, "+~30%"),
            ],
            max_value=5.0,
        ),
        f"McKinsey estimate: cement and steel unit cost uplifts in a net-zero infrastructure scenario "
        f"{_c(_ref(slug, 'mckinsey_infra'))}.",
        source_badge="McKinsey",
    )
    return [c1, c2, c3, c4]


CHART_BUILDERS = {
    "space-compute": _space_charts,
    "weather-foundation-models": _weather_charts,
    "aerospace-satellites": _aerospace_charts,
    "materials": _materials_charts,
    "energy-systems": _energy_charts,
    "manufacturing": _manufacturing_charts,
    "built-environment": _built_charts,
    "mobility": _mobility_charts,
    "industrial-processes": _industrial_charts,
}


def market_charts_html(slug: str) -> str:
    return "\n".join(CHART_BUILDERS[slug]())


def build_markets_section(slug: str) -> str:
    jevons_n, rebound_n = JEVONS_REFS[slug]
    data = SECTOR_SECTIONS[slug]
    intro = (
        f"When a capability gets cheaper, people often use more of it, not less. William Stanley Jevons observed this for coal efficiency in 1865 {_c(jevons_n)}. "
        f"Energy-policy reviews document similar rebound dynamics today {_c(rebound_n)}. "
        f"In this sector, falling costs can expand adoption faster than efficiency alone saves emissions."
    )
    closing = data["rebound_closing"]
    charts = market_charts_html(slug)
    market_map = market_map_html(slug)
    section_note = (
        '<p class="chart-section-note">Market outlook charts below combine research benchmarks with published '
        "estimates from firms such as McKinsey and Goldman Sachs. Figures are scenario estimates, not forecasts "
        "of certainty.</p>"
    )
    return f'''
        <h2>Markets</h2>
        <h3>When cost falls, demand rises</h3>
        <p>{intro}</p>
{rebound_cards_html(slug)}
{section_note}
        <div class="chart-grid">
{charts}
        </div>
{market_map}
        <p>{closing}</p>
'''
