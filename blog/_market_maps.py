"""Illustrative company market maps for sector Markets sections."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from _viz import _esc

ROOT = Path(__file__).resolve().parent
LOGO_DIR = ROOT / "logos"

# Ref indices in each post's References list (appended in _generate.py).
MARKET_MAP_REF_IDS: dict[str, tuple[int, ...]] = {
    "space-compute": (12, 13, 14),
    "weather-foundation-models": (17, 18, 19),
    "aerospace-satellites": (12, 13, 14),
    "materials": (11, 12, 13),
    "energy-systems": (11, 12, 13),
    "manufacturing": (10, 11, 12),
    "built-environment": (10, 11, 12),
    "mobility": (13, 14, 15),
    "industrial-processes": (12, 13, 14),
}


def _c(n: int) -> str:
    return f'[<a href="#r{n}">{n}</a>]'


def _initials(name: str) -> str:
    parts = [p for p in name.replace(".", " ").replace("/", " ").split() if p]
    if not parts:
        return "?"
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[1][0]).upper()


def _logo_src(logo_key: Optional[str]) -> Optional[str]:
    if not logo_key:
        return None
    for ext in (".png", ".jpg", ".jpeg", ".webp", ".svg", ".ico"):
        path = LOGO_DIR / f"{logo_key}{ext}"
        if path.is_file() and path.stat().st_size > 300:
            return f"logos/{logo_key}{ext}"
    return None


def _chip(name: str, role: Optional[str] = None, logo: Optional[str] = None) -> str:
    initials = _esc(_initials(name))
    src = _logo_src(logo)
    if src:
        mark = (
            f'<span class="mm-logo-wrap">'
            f'<img class="mm-logo" src="{_esc(src)}" alt="" width="28" height="28" '
            f'loading="lazy" decoding="async" '
            f'onerror="this.style.display=\'none\';this.nextElementSibling.hidden=false"/>'
            f'<span class="mm-mono" hidden aria-hidden="true">{initials}</span>'
            f"</span>"
        )
    else:
        mark = f'<span class="mm-logo-wrap"><span class="mm-mono" aria-hidden="true">{initials}</span></span>'
    role_html = f'<span class="mm-role">{_esc(role)}</span>' if role else ""
    return (
        f'          <li class="mm-chip">'
        f"{mark}"
        f'<span class="mm-text"><span class="mm-name">{_esc(name)}</span>{role_html}</span>'
        f"</li>"
    )


def _segment(title: str, chips: list[str]) -> str:
    items = "\n".join(chips)
    return f'''        <div class="mm-seg">
          <h4>{_esc(title)}</h4>
          <ul class="mm-chips">
{items}
          </ul>
        </div>'''


def _figure(segments: list[str], caption: str) -> str:
    grid = "\n".join(segments)
    return f'''        <h3>Market map</h3>
        <p class="mm-intro">A snapshot of who is building commercial and operational products in this space. The map is illustrative, not exhaustive.</p>
        <figure class="viz market-map">
          <div class="mm-head">
            <p class="viz-label">Market map</p>
            <p class="mm-title">Who is building here</p>
          </div>
          <div class="mm-grid">
{grid}
          </div>
          <figcaption class="viz-caption">{caption}</figcaption>
        </figure>'''


def _space_map() -> str:
    refs = MARKET_MAP_REF_IDS["space-compute"]
    caption = (
        f"Illustrative map of orbital compute players; not exhaustive. "
        f"Sources: Starcloud {_c(refs[0])}; Google Suncatcher {_c(refs[1])}; "
        f"analyst and platform context {_c(refs[2])}."
    )
    segs = [
        _segment(
            "Hyperscale & platforms",
            [
                _chip("Google", "Project Suncatcher", "google"),
                _chip("SpaceX", "orbital DC filing", "spacex"),
            ],
        ),
        _segment(
            "Orbital DC startups",
            [
                _chip("Starcloud", "GPU demos / constellation", "starcloud"),
                _chip("Axiom Space", "orbital compute nodes", "axiom"),
                _chip("Lonestar", "lunar / edge storage", "lonestar"),
            ],
        ),
        _segment(
            "Mission partners",
            [_chip("Planet", "Suncatcher platforms", "planet")],
        ),
        _segment(
            "Radiation-tolerant compute",
            [
                _chip("Ramon.Space", "space-grade processors", "ramon"),
                _chip("Aethero", "space-rated edge / HPC modules", "aethero"),
            ],
        ),
    ]
    return _figure(segs, caption)


def _weather_map() -> str:
    refs = MARKET_MAP_REF_IDS["weather-foundation-models"]
    caption = (
        f"Illustrative map of notable public companies and startups; not exhaustive. "
        f"Sources: company sites {_c(refs[0])}{_c(refs[1])}; operational AI weather {_c(refs[2])}."
    )
    segs = [
        _segment(
            "Platforms",
            [
                _chip("Google DeepMind", "WeatherNext / GraphCast", "deepmind"),
                _chip("Microsoft Research", "Aurora", "microsoft"),
                _chip("NVIDIA", "Earth-2", "nvidia"),
            ],
        ),
        _segment(
            "Startups",
            [
                _chip("WindBorne Systems", "global sensing network", "windborne"),
                _chip("Atmo", "AI weather forecasts", "atmo"),
                _chip("Jua", "foundation weather models", "jua"),
                _chip("Tomorrow.io", "nowcasting platform", "tomorrow"),
                _chip("Causal Labs", "physics foundation weather models", "causal"),
            ],
        ),
        _segment(
            "Operators & agencies",
            [
                _chip("ECMWF", "AIFS operations", "ecmwf"),
                _chip("NOAA", "AI forecast integration", "noaa"),
            ],
        ),
    ]
    return _figure(segs, caption)


def _aerospace_map() -> str:
    refs = MARKET_MAP_REF_IDS["aerospace-satellites"]
    caption = (
        f"Illustrative map of notable Earth observation companies; not exhaustive. "
        f"Sources: industry surveys {_c(refs[0])}{_c(refs[1])}; company sites {_c(refs[2])}."
    )
    segs = [
        _segment(
            "Optical imaging",
            [
                _chip("Planet", "daily global imaging", "planet"),
                _chip("Maxar", "high-resolution EO", "maxar"),
                _chip("BlackSky", "rapid revisit", "blacksky"),
                _chip("Pixxel", "hyperspectral constellations", "pixxel"),
            ],
        ),
        _segment(
            "SAR",
            [
                _chip("Capella Space", "SAR microsatellites", "capella"),
                _chip("Umbra", "high-res SAR", "umbra"),
            ],
        ),
        _segment(
            "GHG & climate sensing",
            [_chip("GHGSat", "facility-level methane", "ghgsat")],
        ),
        _segment(
            "Weather & RF",
            [
                _chip("Spire Global", "radio occultation", "spire"),
                _chip("HawkEye 360", "RF geolocation", "hawkeye"),
            ],
        ),
    ]
    return _figure(segs, caption)


def _materials_map() -> str:
    refs = MARKET_MAP_REF_IDS["materials"]
    caption = (
        f"Illustrative map of low-carbon materials companies; not exhaustive. "
        f"Sources: sector roundups {_c(refs[0])}{_c(refs[1])}; company disclosures {_c(refs[2])}."
    )
    segs = [
        _segment(
            "Novel cement",
            [
                _chip("Sublime Systems", "electrochemical cement", "sublime"),
                _chip("Brimstone", "calcium silicate cement", "brimstone"),
                _chip("Fortera", "reactive mineral cement", "fortera"),
            ],
        ),
        _segment(
            "CO₂ mineralization & concrete",
            [
                _chip("CarbonCure", "injected CO₂ curing", "carboncure"),
                _chip("Solidia", "lower-carbon binder", "solidia"),
                _chip("CarbonBuilt", "CO₂ mineralized blocks", "carbonbuilt"),
            ],
        ),
        _segment(
            "SCM & circular",
            [_chip("Carbon Upcycling", "CO₂-enhanced SCMs", "carbonupcycling")],
        ),
        _segment(
            "Advanced nanomaterials",
            [_chip("NoPo Nanotechnologies", "HiPCO single-walled CNTs", "nopo")],
        ),
    ]
    return _figure(segs, caption)


def _energy_map() -> str:
    refs = MARKET_MAP_REF_IDS["energy-systems"]
    caption = (
        f"Illustrative map of storage developers; not exhaustive. "
        f"Sources: company sites {_c(refs[0])}{_c(refs[1])}; LDES landscape {_c(refs[2])}."
    )
    segs = [
        _segment(
            "Multi-day batteries",
            [_chip("Form Energy", "iron-air multi-day", "formenergy")],
        ),
        _segment(
            "Flow batteries",
            [
                _chip("ESS Inc.", "iron flow storage", "ess"),
                _chip("Invinity", "vanadium flow", "invinity"),
            ],
        ),
        _segment(
            "Gravity & compressed air",
            [
                _chip("Energy Vault", "gravity storage", "energyvault"),
                _chip("Hydrostor", "compressed air", "hydrostor"),
                _chip("Energy Dome", "CO₂-based storage", "energydome"),
            ],
        ),
        _segment(
            "Geomechanical & other LDES",
            [
                _chip("Quidnet Energy", "geomechanical pumped storage", "quidnet"),
                _chip("Malta Inc.", "thermal electro-mechanical", "malta"),
            ],
        ),
        _segment(
            "Short-duration context",
            [
                _chip("Tesla Energy", "grid-scale Li-ion", "tesla"),
                _chip("Fluence", "storage integrator", "fluence"),
            ],
        ),
    ]
    return _figure(segs, caption)


def _manufacturing_map() -> str:
    refs = MARKET_MAP_REF_IDS["manufacturing"]
    caption = (
        f"Illustrative map of industrial heat and thermal storage firms; not exhaustive. "
        f"Sources: sector coverage {_c(refs[0])}; company sites {_c(refs[1])}{_c(refs[2])}."
    )
    segs = [
        _segment(
            "Thermal batteries & ETES",
            [
                _chip("Rondo Energy", "heat batteries", "rondo"),
                _chip("Antora Energy", "thermal storage", "antora"),
                _chip("Electrified Thermal Solutions", "firebrick storage", "electrifiedthermal"),
            ],
        ),
        _segment(
            "Electrified steam & boilers",
            [_chip("AtmosZero", "industrial heat pumps", "atmoszero")],
        ),
        _segment(
            "Heat-as-a-service",
            [_chip("Zero Industrial", "decarbonized process heat", "zeroindustrial")],
        ),
    ]
    return _figure(segs, caption)


def _built_map() -> str:
    refs = MARKET_MAP_REF_IDS["built-environment"]
    caption = (
        f"Illustrative map of low-carbon building supply chain players; not exhaustive. "
        f"Sources: company sites {_c(refs[0])}{_c(refs[1])}; mass timber {_c(refs[2])}."
    )
    segs = [
        _segment(
            "Low-carbon concrete tech",
            [_chip("CarbonCure", "embedded CO₂ concrete", "carboncure")],
        ),
        _segment(
            "Mass timber producers",
            [
                _chip("Mercer Mass Timber", "cross-laminated timber", "mercer"),
                _chip("SmartLam", "glulam and CLT", "smartlam"),
                _chip("Fabric Workshop", "prefab mass timber", "fabric"),
            ],
        ),
        _segment(
            "Supply-chain platforms",
            [_chip("Cambium", "traceable wood supply", "cambium")],
        ),
        _segment(
            "Software & standards",
            [
                _chip("One Click LCA", "whole-life carbon", "oneclicklca"),
                _chip("Tally", "Revit embodied carbon", "tally"),
            ],
        ),
    ]
    return _figure(segs, caption)


def _mobility_map() -> str:
    refs = MARKET_MAP_REF_IDS["mobility"]
    caption = (
        f"Illustrative map of charging networks and software; not exhaustive. "
        f"Sources: network directories {_c(refs[0])}; managed charging {_c(refs[1])}; "
        f"public CPO coverage {_c(refs[2])}."
    )
    segs = [
        _segment(
            "Public fast charging",
            [
                _chip("Tesla Supercharger", "DC fast network", "tesla"),
                _chip("Electrify America", "highway corridors", "electrifyamerica"),
                _chip("EVgo", "urban fast charging", "evgo"),
                _chip("ChargePoint", "hardware and roaming", "chargepoint"),
                _chip("IONNA", "OEM joint network", "ionna"),
            ],
        ),
        _segment(
            "Smart & managed charging",
            [_chip("PowerFlex", "fleet and workplace ACN", "powerflex")],
        ),
        _segment(
            "Vehicles (context)",
            [
                _chip("Tesla", "EV volume leader", "tesla"),
                _chip("Rivian", "electric trucks and SUVs", "rivian"),
            ],
        ),
    ]
    return _figure(segs, caption)


def _industrial_map() -> str:
    refs = MARKET_MAP_REF_IDS["industrial-processes"]
    caption = (
        f"Illustrative map of hard-to-abate process innovators; not exhaustive. "
        f"Sources: company sites {_c(refs[0])}{_c(refs[1])}; cement and heat {_c(refs[2])}."
    )
    segs = [
        _segment(
            "Industrial heat",
            [
                _chip("Rondo Energy", "thermal batteries", "rondo"),
                _chip("Antora Energy", "thermal storage", "antora"),
                _chip("Electrified Thermal Solutions", "firebrick heat", "electrifiedthermal"),
            ],
        ),
        _segment(
            "Green steel",
            [
                _chip("Stegra", "hydrogen DRI steel", "stegra"),
                _chip("Boston Metal", "molten oxide electrolysis", "bostonmetal"),
            ],
        ),
        _segment(
            "Cement technology",
            [
                _chip("Sublime Systems", "electrochemical cement", "sublime"),
                _chip("Brimstone", "calcium silicate routes", "brimstone"),
                _chip("Fortera", "low-carbon cement", "fortera"),
            ],
        ),
        _segment(
            "Kiln capture add-ons",
            [_chip("Fortera ReCarb", "point-source mineralization", "fortera")],
        ),
    ]
    return _figure(segs, caption)


_MAP_BUILDERS = {
    "space-compute": _space_map,
    "weather-foundation-models": _weather_map,
    "aerospace-satellites": _aerospace_map,
    "materials": _materials_map,
    "energy-systems": _energy_map,
    "manufacturing": _manufacturing_map,
    "built-environment": _built_map,
    "mobility": _mobility_map,
    "industrial-processes": _industrial_map,
}


def market_map_html(slug: str) -> str:
    builder = _MAP_BUILDERS.get(slug)
    if not builder:
        return ""
    return f"\n{builder()}\n"
