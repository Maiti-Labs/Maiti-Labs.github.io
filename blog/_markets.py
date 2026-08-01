"""Markets section: Jevons intro, rebound cards, and cited SVG charts per sector."""

from _market_maps import market_map_html
from _timelines import SECTOR_SECTIONS, rebound_cards_html
from _viz import BG, BG_ALT, CREAM, FONT, FOREST, MUTED, SOFT, _esc, _uid

JEVONS_REFS = {
    "weather-foundation-models": (13, 14),
    "aerospace-satellites": (9, 10),
    "materials": (8, 9),
    "energy-systems": (7, 8),
    "manufacturing": (7, 8),
    "built-environment": (7, 8),
    "mobility": (9, 10),
    "industrial-processes": (8, 9),
}


def _c(n: int) -> str:
    return f'[<a href="#r{n}">{n}</a>]'


def _chart_svg(title: str, inner: str, w: int = 640, h: int = 300) -> str:
    uid = _uid("mc")
    title_el = (
        f'<text x="{w // 2}" y="32" text-anchor="middle" fill="{FOREST}" '
        f'font-size="12" font-weight="600" font-family="{FONT}">{_esc(title)}</text>'
    )
    return f'''        <svg aria-hidden="true" class="viz-svg chart-svg" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="{uid}-bg" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="{BG}"/>
              <stop offset="100%" stop-color="{BG_ALT}"/>
            </linearGradient>
            <linearGradient id="{uid}-bar" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="{SOFT}"/>
              <stop offset="100%" stop-color="{FOREST}"/>
            </linearGradient>
          </defs>
          <rect width="{w}" height="{h}" fill="url(#{uid}-bg)" rx="12"/>
          {title_el}
{inner}
        </svg>'''


def _figure(chart_title: str, svg: str, caption: str) -> str:
    return f'''        <figure class="viz viz-chart chart-wrap">
          <p class="viz-label">{_esc(chart_title)}</p>
{svg}
          <figcaption class="viz-caption">{caption}</figcaption>
        </figure>'''


def _hbar(y: int, x0: int, width: int, height: int, label: str, value_label: str, muted: bool = False) -> str:
    fill = f'fill="{MUTED}" opacity="0.35"' if muted else f'fill="url(#{_uid("x")}-bar)"'
    # use solid fill if gradient id mismatch — use FOREST/SOFT
    bar_fill = f'fill="{MUTED}" opacity="0.3"' if muted else f'fill="{SOFT}"'
    return f'''
          <text x="24" y="{y + 14}" fill="{FOREST}" font-size="11" font-family="{FONT}">{_esc(label)}</text>
          <rect x="{x0}" y="{y + 22}" width="{width}" height="{height}" rx="6" {bar_fill}/>
          <text x="{x0 + width + 8}" y="{y + 14 + height // 2}" fill="{MUTED}" font-size="10" font-family="{FONT}">{_esc(value_label)}</text>'''


def _axis_y(x: int, y0: int, y1: int, label: str) -> str:
    return f'''
          <line x1="{x}" y1="{y0}" x2="{x}" y2="{y1}" stroke="{FOREST}" stroke-width="1" opacity="0.25"/>
          <text x="{x - 6}" y="{y1 + 18}" text-anchor="end" fill="{MUTED}" font-size="9" font-family="{FONT}">{_esc(label)}</text>'''


def _weather_charts() -> list[str]:
    inner = f'''
          {_axis_y(72, 52, 248, "Wall-clock (qualitative)")}
          {_hbar(68, 88, 420, 28, "Classical NWP (supercomputer)", "hours-scale", muted=False)}
          {_hbar(128, 88, 72, 28, "AI emulators (GraphCast, FourCastNet)", "minutes-scale", muted=False)}
          <text x="320" y="278" text-anchor="middle" fill="{MUTED}" font-size="9" font-family="{FONT}">Not to scale — orders of magnitude faster in reported benchmarks</text>'''
    c1 = _figure(
        "Forecast wall-clock",
        _chart_svg("Inference time (qualitative)", inner),
        f"Source: Lam et al., 2023 {_c(2)}; Pathak et al., 2022 {_c(9)}. Absolute runtimes vary by hardware and resolution.",
    )
    inner2 = f'''
          {_axis_y(100, 52, 220, "Relative skill index")}
          <rect x="120" y="88" width="48" height="132" rx="6" fill="{MUTED}" opacity="0.25"/>
          <text x="144" y="238" text-anchor="middle" fill="{FOREST}" font-size="10" font-family="{FONT}">IFS baseline</text>
          <text x="144" y="252" text-anchor="middle" fill="{MUTED}" font-size="9" font-family="{FONT}">index = 1</text>
          <rect x="280" y="72" width="48" height="148" rx="6" fill="{SOFT}"/>
          <text x="304" y="238" text-anchor="middle" fill="{FOREST}" font-size="10" font-family="{FONT}">Leading AI</text>
          <text x="304" y="252" text-anchor="middle" fill="{MUTED}" font-size="9" font-family="{FONT}">match / beat on many vars</text>
          <text x="420" y="120" fill="{MUTED}" font-size="9" font-family="{FONT}">WeatherBench2-style</text>
          <text x="420" y="134" fill="{MUTED}" font-size="9" font-family="{FONT}">comparisons</text>'''
    c2 = _figure(
        "Benchmark skill vs IFS",
        _chart_svg("Deterministic skill (schematic)", inner2),
        f"Source: Rasp et al., 2024 {_c(10)}; Lam et al., 2023 {_c(2)}; Bi et al., 2023 {_c(3)}.",
    )
    return [c1, c2]


def _aerospace_charts() -> list[str]:
    labels = [
        ("SkySense", 21.5, "21.5M sequences"),
        ("SkySense++", 27.0, "~27M images"),
        ("Prithvi-EO", 4.2, "4.2M samples"),
        ("Copernicus-FM", 18.7, "18.7M observations"),
    ]
    max_w = 400
    mx = 27.0
    bars = ""
    y = 58
    for name, num, val in labels:
        w = max(24, int(max_w * (num / mx)))
        bars += _hbar(y, 180, w, 22, name, val)
        y += 52
    c1 = _figure(
        "Pretraining corpus scale",
        _chart_svg("Public-archive pretraining (reported)", bars + _axis_y(160, 48, 248, "Millions of units")),
        f"Source: Guo et al., 2024 {_c(2)}; Wu et al., 2025 {_c(3)}; Szwarcman et al., 2024 {_c(4)}; Wang et al., 2025 {_c(5)}.",
    )
    inner2 = f'''
          {_hbar(78, 120, 360, 32, "Carbon-I global mapping", "~300 m", muted=False)}
          {_hbar(148, 120, 120, 32, "Priority targets (design goal)", "~30 m", muted=False)}
          <text x="320" y="248" text-anchor="middle" fill="{MUTED}" font-size="9" font-family="{FONT}">Spatial resolution (mission design)</text>'''
    c2 = _figure(
        "Carbon-I resolution targets",
        _chart_svg("GHG mapping resolution", inner2),
        f"Source: Carbon-I mission materials {_c(7)}.",
    )
    return [c1, c2]


def _materials_charts() -> list[str]:
    inner = f'''
          <circle cx="220" cy="150" r="88" fill="{BG_ALT}" stroke="{FOREST}" stroke-width="1.2"/>
          <path d="M 220 62 A 88 88 0 0 1 308 150 L 220 150 Z" fill="{SOFT}"/>
          <path d="M 220 150 L 308 150 A 88 88 0 0 1 220 238 Z" fill="{FOREST}" opacity="0.35"/>
          <text x="268" y="118" fill="{CREAM}" font-size="11" font-weight="600" font-family="{FONT}">~8%</text>
          <text x="248" y="132" fill="{CREAM}" font-size="9" font-family="{FONT}">cement CO₂</text>
          <text x="248" y="200" fill="{FOREST}" font-size="9" font-family="{FONT}">Other sources</text>
          <text x="380" y="100" fill="{FOREST}" font-size="10" font-family="{FONT}">Cement ~8% of</text>
          <text x="380" y="116" fill="{FOREST}" font-size="10" font-family="{FONT}">global CO₂</text>
          <text x="380" y="140" fill="{MUTED}" font-size="9" font-family="{FONT}">Schematic share</text>'''
    c1 = _figure(
        "Cement emissions share",
        _chart_svg("Global CO₂ (cement vs rest)", inner),
        f"Source: IEA / IPCC industry briefs {_c(7)}.",
    )
    inner2 = f'''
          <text x="24" y="70" fill="{MUTED}" font-size="9" font-family="{FONT}">Phlego reported targets (project)</text>
          {_hbar(82, 160, 304, 26, "Emissions reduction target", "up to ~76%", muted=False)}
          {_hbar(142, 160, 80, 26, "Production cost target", "up to ~20%", muted=False)}
          <text x="24" y="210" fill="{MUTED}" font-size="9" font-family="{FONT}">Illustrative bars — see project disclosures</text>'''
    c2 = _figure(
        "Low-carbon cement targets",
        _chart_svg("Stanford Phlego (reported)", inner2),
        f"Source: Vanorio et al. / Stanford Sustainability Accelerator {_c(1)}{_c(2)}.",
    )
    return [c1, c2]


def _energy_charts() -> list[str]:
    inner = f'''
          <polyline points="100,210 180,178 260,142 340,108 420,82 500,68" fill="none" stroke="{SOFT}" stroke-width="3"/>
          <circle cx="100" cy="210" r="5" fill="{FOREST}"/>
          <circle cx="500" cy="68" r="5" fill="{FOREST}"/>
          <text x="88" y="228" fill="{MUTED}" font-size="9" font-family="{FONT}">2010</text>
          <text x="488" y="58" fill="{MUTED}" font-size="9" font-family="{FONT}">2020s</text>
          <text x="24" y="120" fill="{MUTED}" font-size="9" font-family="{FONT}">Pack cost</text>
          <text x="24" y="134" fill="{MUTED}" font-size="9" font-family="{FONT}">(↓ steep decline)</text>
          <text x="280" y="268" text-anchor="middle" fill="{MUTED}" font-size="9" font-family="{FONT}">Li-ion battery pack costs — trend, not annual points</text>'''
    c1 = _figure(
        "Battery pack cost trend",
        _chart_svg("Li-ion storage cost trajectory", inner),
        f"Source: IRENA, 2023 {_c(6)}.",
    )
    inner2 = f'''
          {_hbar(88, 160, 200, 30, "Solar-heavy regions", "6–10 h duration", muted=False)}
          {_hbar(158, 160, 320, 30, "Wind-heavy regions", "10–20 h duration", muted=False)}
          <text x="320" y="248" text-anchor="middle" fill="{MUTED}" font-size="9" font-family="{FONT}">Useful storage duration (model ranges)</text>'''
    c2 = _figure(
        "LDES duration by resource mix",
        _chart_svg("Long-duration storage needs", inner2),
        f"Source: Staadecker et al., 2024 {_c(1)}.",
    )
    return [c1, c2]


def _manufacturing_charts() -> list[str]:
    inner = f'''
          <rect x="120" y="100" width="120" height="120" rx="8" fill="{SOFT}" opacity="0.5"/>
          <text x="180" y="168" text-anchor="middle" fill="{FOREST}" font-size="11" font-family="{FONT}">~⅓ cut</text>
          <text x="180" y="238" text-anchor="middle" fill="{FOREST}" font-size="10" font-family="{FONT}">~€85 / tCO₂</text>
          <rect x="320" y="72" width="120" height="148" rx="8" fill="{FOREST}" opacity="0.55"/>
          <text x="380" y="152" text-anchor="middle" fill="{CREAM}" font-size="11" font-family="{FONT}">Sharper</text>
          <text x="380" y="168" text-anchor="middle" fill="{CREAM}" font-size="11" font-family="{FONT}">abatement</text>
          <text x="380" y="238" text-anchor="middle" fill="{FOREST}" font-size="10" font-family="{FONT}">&gt; €100 / tCO₂</text>
          <text x="320" y="268" text-anchor="middle" fill="{MUTED}" font-size="9" font-family="{FONT}">EU cement — optimal direct emissions cut (schematic)</text>'''
    c1 = _figure(
        "Carbon price and abatement",
        _chart_svg("EU ETS cement (modeled)", inner),
        f"Source: Glenk, Meier, &amp; Reichelstein, 2024 {_c(5)}.",
    )
    inner2 = f'''
          <rect x="140" y="110" width="56" height="110" rx="6" fill="{MUTED}" opacity="0.3"/>
          <text x="168" y="238" text-anchor="middle" fill="{FOREST}" font-size="9" font-family="{FONT}">~11%</text>
          <text x="168" y="252" text-anchor="middle" fill="{MUTED}" font-size="8" font-family="{FONT}">near term</text>
          <rect x="280" y="72" width="56" height="148" rx="6" fill="{SOFT}"/>
          <text x="308" y="238" text-anchor="middle" fill="{FOREST}" font-size="9" font-family="{FONT}">~34%</text>
          <text x="308" y="252" text-anchor="middle" fill="{MUTED}" font-size="8" font-family="{FONT}">by ~2035</text>
          <text x="320" y="90" text-anchor="middle" fill="{MUTED}" font-size="9" font-family="{FONT}">U.S. industrial heat economically addressable</text>'''
    c2 = _figure(
        "Renewable industrial heat",
        _chart_svg("Berkeley WP scenarios", inner2),
        f"Source: UC Berkeley GSPP working paper {_c(4)}.",
    )
    return [c1, c2]


def _built_charts() -> list[str]:
    bars = [
        ("Embodied (ECI median)", 385, "kgCO₂e/m²"),
        ("Operational (OCI median)", 228, "kgCO₂e/m²"),
        ("Whole-life (WLCI median)", 734, "kgCO₂e/m²"),
    ]
    mx = 734
    body = ""
    y = 62
    for label, val, unit in bars:
        w = int(360 * val / mx)
        body += _hbar(y, 200, w, 24, label, f"{val} {unit}")
        y += 58
    c1 = _figure(
        "California building medians",
        _chart_svg("30 buildings — median intensities", body),
        f"Source: Shen et al., 2025 {_c(1)}.",
    )
    inner2 = f'''
          <line x1="120" y1="180" x2="520" y2="180" stroke="{FOREST}" stroke-width="2"/>
          <line x1="120" y1="160" x2="120" y2="200" stroke="{FOREST}" stroke-width="2"/>
          <line x1="520" y1="160" x2="520" y2="200" stroke="{FOREST}" stroke-width="2"/>
          <circle cx="180" cy="180" r="6" fill="{SOFT}"/>
          <text x="120" y="148" fill="{MUTED}" font-size="9" font-family="{FONT}">min 232</text>
          <text x="480" y="148" fill="{MUTED}" font-size="9" font-family="{FONT}">max 2,230</text>
          <text x="320" y="220" text-anchor="middle" fill="{FOREST}" font-size="10" font-family="{FONT}">WLCI range (kgCO₂e/m²)</text>
          <text x="320" y="248" text-anchor="middle" fill="{MUTED}" font-size="9" font-family="{FONT}">Whisker schematic — same sample</text>'''
    c2 = _figure(
        "Whole-life carbon spread",
        _chart_svg("WLCI min–max", inner2),
        f"Source: Shen et al., 2025 {_c(1)}.",
    )
    return [c1, c2]


def _mobility_charts() -> list[str]:
    inner = f'''
          <rect x="160" y="80" width="320" height="36" rx="18" fill="{BG_ALT}" stroke="{FOREST}" stroke-width="1"/>
          <rect x="160" y="80" width="250" height="36" rx="18" fill="{SOFT}"/>
          <text x="320" y="104" text-anchor="middle" fill="{CREAM}" font-size="12" font-weight="600" font-family="{FONT}">~78% reliable</text>
          <text x="320" y="148" text-anchor="middle" fill="{FOREST}" font-size="10" font-family="{FONT}">Public charging success rate (U.S.)</text>
          <text x="320" y="268" text-anchor="middle" fill="{MUTED}" font-size="9" font-family="{FONT}">Large review dataset — illustrative gauge</text>'''
    c1 = _figure(
        "Charging reliability",
        _chart_svg("Public charger uptime", inner),
        f"Source: Asensio et al., Harvard BiGS {_c(3)}.",
    )
    inner2 = f'''
          <text x="100" y="78" text-anchor="middle" fill="{FOREST}" font-size="10" font-family="{FONT}">ICE loans</text>
          <text x="320" y="78" text-anchor="middle" fill="{FOREST}" font-size="10" font-family="{FONT}">EV loans</text>
          {_hbar(92, 48, 100, 18, "Interest rate", "lower", muted=True)}
          {_hbar(92, 280, 140, 18, "Interest rate", "higher", muted=False)}
          {_hbar(132, 48, 120, 18, "Loan-to-value", "higher LTV", muted=True)}
          {_hbar(132, 280, 90, 18, "Loan-to-value", "lower LTV", muted=False)}
          {_hbar(172, 48, 130, 18, "Term length", "longer", muted=True)}
          {_hbar(172, 280, 95, 18, "Term length", "shorter", muted=False)}
          <text x="320" y="248" text-anchor="middle" fill="{MUTED}" font-size="9" font-family="{FONT}">Directional comparison — obsolescence risk mechanism</text>'''
    c2 = _figure(
        "EV financing gap",
        _chart_svg("Loan terms (conceptual)", inner2),
        f"Source: Bena, Bian, &amp; Tang {_c(1)}{_c(2)}.",
    )
    return [c1, c2]


def _industrial_charts() -> list[str]:
    inner = f'''
          {_hbar(88, 160, 360, 28, "Li-ion batteries (thermal kWh)", "higher $/kWh", muted=True)}
          {_hbar(148, 160, 36, 28, "Firebrick storage (thermal kWh)", "~1/10 cost", muted=False)}
          <text x="320" y="248" text-anchor="middle" fill="{MUTED}" font-size="9" font-family="{FONT}">Relative cost per thermal kWh (schematic)</text>'''
    c1 = _figure(
        "Industrial heat storage cost",
        _chart_svg("Firebrick vs batteries", inner),
        f"Source: Jacobson et al., 2024 {_c(3)}.",
    )
    inner2 = f'''
          <rect x="140" y="110" width="56" height="110" rx="6" fill="{MUTED}" opacity="0.3"/>
          <text x="168" y="238" text-anchor="middle" fill="{FOREST}" font-size="9" font-family="{FONT}">rising</text>
          <text x="168" y="252" text-anchor="middle" fill="{MUTED}" font-size="8" font-family="{FONT}">addressable</text>
          <rect x="280" y="72" width="56" height="148" rx="6" fill="{SOFT}"/>
          <text x="308" y="238" text-anchor="middle" fill="{FOREST}" font-size="9" font-family="{FONT}">~34%</text>
          <text x="308" y="252" text-anchor="middle" fill="{MUTED}" font-size="8" font-family="{FONT}">by ~2035</text>
          <text x="320" y="90" text-anchor="middle" fill="{MUTED}" font-size="9" font-family="{FONT}">U.S. industrial heat — renewable + storage</text>'''
    c2 = _figure(
        "Heat electrification potential",
        _chart_svg("Berkeley base case", inner2),
        f"Source: UC Berkeley GSPP working paper {_c(4)}; Glenk et al. {_c(6)}.",
    )
    return [c1, c2]


CHART_BUILDERS = {
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
    return f'''
        <h2>Markets</h2>
        <h3>When cost falls, demand rises</h3>
        <p>{intro}</p>
{rebound_cards_html(slug)}
        <div class="chart-grid">
{charts}
        </div>
{market_map}
        <p>{closing}</p>
'''
