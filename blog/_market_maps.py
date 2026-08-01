"""Illustrative company market maps for sector Markets sections."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from _viz import _esc

ROOT = Path(__file__).resolve().parent
LOGO_DIR = ROOT / "logos"

# Ref indices in each post's References list (appended in _generate.py).
MARKET_MAP_REF_IDS: dict[str, tuple[int, ...]] = {
    "space-compute": (12, 13, 14, 15),
    "weather-foundation-models": (17, 18, 19, 20),
    "aerospace-satellites": (12, 13, 14, 15),
    "materials": (11, 12, 13, 14),
    "energy-systems": (11, 12, 13, 14),
    "manufacturing": (10, 11, 12, 13),
    "built-environment": (10, 11, 12, 13),
    "mobility": (13, 14, 15, 16),
    "industrial-processes": (12, 13, 14, 15),
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
        f"Landscape survey {_c(refs[0])}; company sites {_c(refs[1])}{_c(refs[2])}; "
        f"platform and analyst context {_c(refs[3])}."
    )
    segs = [
        _segment(
            "Hyperscale & platforms",
            [
                _chip("Google", "Project Suncatcher", "google"),
                _chip("SpaceX", "orbital DC filing", "spacex"),
                _chip("Blue Origin", "Project Sunrise", "blueorigin"),
            ],
        ),
        _segment(
            "Orbital DC startups",
            [
                _chip("Starcloud", "GPU demos / constellation", "starcloud"),
                _chip("Axiom Space", "orbital compute nodes", "axiom"),
                _chip("Lonestar", "lunar / edge storage", "lonestar"),
                _chip("Aetherflux", "space power / compute", "aetherflux"),
            ],
        ),
        _segment(
            "Space-rated compute hardware",
            [
                _chip("Ramon.Space", "space-grade processors", "ramon"),
                _chip("Aethero", "space-rated edge / HPC", "aethero"),
                _chip("Kepler Communications", "optical mesh / edge", "kepler"),
            ],
        ),
        _segment(
            "Connectivity & partners",
            [
                _chip("Planet", "Suncatcher platforms", "planet"),
                _chip("NVIDIA", "space GPU stack context", "nvidia"),
                _chip("Crusoe", "energy-aware compute", "crusoe"),
            ],
        ),
    ]
    return _figure(segs, caption)


def _weather_map() -> str:
    refs = MARKET_MAP_REF_IDS["weather-foundation-models"]
    caption = (
        f"Illustrative map of notable platforms, startups, and agencies; not exhaustive. "
        f"Company and platform sites {_c(refs[0])}{_c(refs[1])}; operational AI weather {_c(refs[2])}; "
        f"commercial forecast context {_c(refs[3])}."
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
                _chip("Causal Labs", "physics foundation models", "causal"),
                _chip("Climavision", "observation + AI forecasts", "climavision"),
                _chip("Salient Predictions", "seasonal / subseasonal AI", "salientpredictions"),
            ],
        ),
        _segment(
            "Operators & agencies",
            [
                _chip("ECMWF", "AIFS operations", "ecmwf"),
                _chip("NOAA", "AI forecast integration", "noaa"),
                _chip("The Weather Company", "IBM operational forecasts", "weathercompany"),
            ],
        ),
    ]
    return _figure(segs, caption)


def _aerospace_map() -> str:
    refs = MARKET_MAP_REF_IDS["aerospace-satellites"]
    caption = (
        f"Illustrative map of Earth observation operators; not exhaustive. "
        f"Global EO directory {_c(refs[0])}; industry surveys {_c(refs[1])}; "
        f"company sites {_c(refs[2])}{_c(refs[3])}."
    )
    segs = [
        _segment(
            "Optical imaging",
            [
                _chip("Planet", "daily global imaging", "planet"),
                _chip("Maxar", "high-resolution EO", "maxar"),
                _chip("BlackSky", "rapid revisit", "blacksky"),
                _chip("Satellogic", "multispectral constellations", "satellogic"),
                _chip("Airbus", "Pleiades / SPOT", "airbus"),
                _chip("Albedo", "very high-res optical", "albedo"),
            ],
        ),
        _segment(
            "SAR",
            [
                _chip("Capella Space", "SAR microsatellites", "capella"),
                _chip("Umbra", "high-res SAR", "umbra"),
                _chip("ICEYE", "SAR flood / disaster", "iceye"),
                _chip("Synspective", "SAR analytics", "synspective"),
            ],
        ),
        _segment(
            "Hyperspectral, thermal & GHG",
            [
                _chip("Pixxel", "hyperspectral constellations", "pixxel"),
                _chip("GHGSat", "facility-level methane", "ghgsat"),
                _chip("OroraTech", "wildfire / thermal", "ororatech"),
                _chip("Wyvern", "hyperspectral imaging", "wyvern"),
                _chip("Hydrosat", "thermal water stress", "hydrosat"),
            ],
        ),
        _segment(
            "Weather & RF",
            [
                _chip("Spire Global", "radio occultation", "spire"),
                _chip("HawkEye 360", "RF geolocation", "hawkeye"),
                _chip("Muon Space", "weather / climate payloads", "muonspace"),
            ],
        ),
    ]
    return _figure(segs, caption)


def _materials_map() -> str:
    refs = MARKET_MAP_REF_IDS["materials"]
    caption = (
        f"Illustrative map of low-carbon materials companies; not exhaustive. "
        f"Sector roundups {_c(refs[0])}{_c(refs[1])}; company disclosures {_c(refs[2])}; "
        f"additional cement innovators {_c(refs[3])}."
    )
    segs = [
        _segment(
            "Novel cement",
            [
                _chip("Sublime Systems", "electrochemical cement", "sublime"),
                _chip("Brimstone", "calcium silicate cement", "brimstone"),
                _chip("Fortera", "reactive mineral cement", "fortera"),
                _chip("Hoffmann Green", "low-carbon clinker", "hoffmanngreen"),
                _chip("Queens Carbon", "electrolytic cement", "queenscarbon"),
                _chip("Minus Materials", "solar-driven cement", "minusmaterials"),
            ],
        ),
        _segment(
            "CO₂ mineralization & concrete",
            [
                _chip("CarbonCure", "injected CO₂ curing", "carboncure"),
                _chip("Solidia", "lower-carbon binder", "solidia"),
                _chip("CarbonBuilt", "CO₂ mineralized blocks", "carbonbuilt"),
                _chip("Blue Planet", "CO₂ mineral aggregates", "blueplanet"),
                _chip("Biomason", "bio-cement tiles", "biomason"),
            ],
        ),
        _segment(
            "SCM & circular",
            [
                _chip("Carbon Upcycling", "CO₂-enhanced SCMs", "carbonupcycling"),
                _chip("Terra CO2", "low-carbon SCM", "terraco2"),
            ],
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
        f"LDES landscape {_c(refs[0])}; company sites {_c(refs[1])}{_c(refs[2])}; "
        f"grid-scale integrators {_c(refs[3])}."
    )
    segs = [
        _segment(
            "Multi-day / metal-air",
            [
                _chip("Form Energy", "iron-air multi-day", "formenergy"),
                _chip("EnerVenue", "metal-hydrogen storage", "enervenue"),
                _chip("Ambri", "liquid metal battery", "ambri"),
                _chip("EOS Energy", "zinc hybrid cathode", "eose"),
                _chip("e-Zinc", "zinc-air LDES", "ezinc"),
            ],
        ),
        _segment(
            "Flow batteries",
            [
                _chip("ESS Inc.", "iron flow storage", "ess"),
                _chip("Invinity", "vanadium flow", "invinity"),
                _chip("CMBlu", "organic flow storage", "cmblu"),
            ],
        ),
        _segment(
            "Mechanical / CAES / gravity / LAES",
            [
                _chip("Energy Vault", "gravity storage", "energyvault"),
                _chip("Hydrostor", "compressed air", "hydrostor"),
                _chip("Energy Dome", "CO₂-based storage", "energydome"),
                _chip("Highview Power", "liquid air storage", "highviewpower"),
                _chip("Quidnet Energy", "geomechanical pumped storage", "quidnet"),
                _chip("Gravitricity", "gravity weights", "gravitricity"),
            ],
        ),
        _segment(
            "Thermal LDES",
            [
                _chip("Malta Inc.", "thermal electro-mechanical", "malta"),
                _chip("EnergyNest", "concrete thermal storage", "energynest"),
            ],
        ),
        _segment(
            "Short-duration integrators",
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
        f"Sector coverage {_c(refs[0])}; thermal battery developers {_c(refs[1])}{_c(refs[2])}; "
        f"electrified heat {_c(refs[3])}."
    )
    segs = [
        _segment(
            "Thermal batteries & ETES",
            [
                _chip("Rondo Energy", "heat batteries", "rondo"),
                _chip("Antora Energy", "thermal storage", "antora"),
                _chip("Electrified Thermal Solutions", "firebrick storage", "electrifiedthermal"),
                _chip("Kraftblock", "high-temp storage media", "kraftblock"),
                _chip("Kyoto Group", "molten-salt heat storage", "kyotogroup"),
                _chip("Brenmiller", "rock / steam storage", "brenmiller"),
            ],
        ),
        _segment(
            "Electric boilers & heat pumps",
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
        f"Company sites {_c(refs[0])}{_c(refs[1])}; mass timber {_c(refs[2])}; "
        f"LCA tools {_c(refs[3])}."
    )
    segs = [
        _segment(
            "Low-carbon concrete tech",
            [
                _chip("CarbonCure", "embedded CO₂ concrete", "carboncure"),
                _chip("Solidia", "lower-carbon binder", "solidia"),
            ],
        ),
        _segment(
            "Mass timber producers",
            [
                _chip("Mercer Mass Timber", "cross-laminated timber", "mercer"),
                _chip("SmartLam", "glulam and CLT", "smartlam"),
                _chip("Fabric Workshop", "prefab mass timber", "fabric"),
                _chip("Structurlam", "mass timber products", "structurlam"),
            ],
        ),
        _segment(
            "Supply-chain platforms",
            [_chip("Cambium", "traceable wood supply", "cambium")],
        ),
        _segment(
            "LCA software & standards",
            [
                _chip("One Click LCA", "whole-life carbon", "oneclicklca"),
                _chip("Tally", "Revit embodied carbon", "tally"),
                _chip("EC3", "embodied carbon database", "ec3"),
            ],
        ),
    ]
    return _figure(segs, caption)


def _mobility_map() -> str:
    refs = MARKET_MAP_REF_IDS["mobility"]
    caption = (
        f"Illustrative map of charging networks and software; not exhaustive. "
        f"DC fast charging landscape {_c(refs[0])}; managed charging {_c(refs[1])}; "
        f"network and CPO coverage {_c(refs[2])}{_c(refs[3])}."
    )
    segs = [
        _segment(
            "Public DCFC",
            [
                _chip("Tesla Supercharger", "DC fast network", "tesla"),
                _chip("Electrify America", "highway corridors", "electrifyamerica"),
                _chip("EVgo", "urban fast charging", "evgo"),
                _chip("ChargePoint", "hardware and roaming", "chargepoint"),
                _chip("IONNA", "OEM joint network", "ionna"),
                _chip("Blink Charging", "public Level 2 / DCFC", "blinkcharging"),
                _chip("EV Connect", "network software / CPO", "evconnect"),
                _chip("Rivian Adventure Network", "OEM fast charging", "rivian"),
            ],
        ),
        _segment(
            "Managed charging",
            [
                _chip("PowerFlex", "fleet and workplace ACN", "powerflex"),
                _chip("AmpUp", "EV charging software", "ampup"),
            ],
        ),
        _segment(
            "OEM context",
            [
                _chip("Tesla", "EV volume leader", "tesla"),
                _chip("Rivian", "electric trucks and SUVs", "rivian"),
                _chip("Lucid", "luxury EVs", "lucid"),
            ],
        ),
    ]
    return _figure(segs, caption)


def _industrial_map() -> str:
    refs = MARKET_MAP_REF_IDS["industrial-processes"]
    caption = (
        f"Illustrative map of hard-to-abate process innovators; not exhaustive. "
        f"Company sites {_c(refs[0])}{_c(refs[1])}; steel and heat {_c(refs[2])}; "
        f"cement technology {_c(refs[3])}."
    )
    segs = [
        _segment(
            "Industrial heat",
            [
                _chip("Rondo Energy", "thermal batteries", "rondo"),
                _chip("Antora Energy", "thermal storage", "antora"),
                _chip("Electrified Thermal Solutions", "firebrick heat", "electrifiedthermal"),
                _chip("AtmosZero", "industrial heat pumps", "atmoszero"),
            ],
        ),
        _segment(
            "Green steel",
            [
                _chip("Stegra", "hydrogen DRI steel", "stegra"),
                _chip("Boston Metal", "molten oxide electrolysis", "bostonmetal"),
                _chip("Electra", "green iron refining", "electra"),
                _chip("Blastr Green Steel", "Nordic green steel", "blastr"),
                _chip("SSAB", "HYBRIT fossil-free steel", "ssab"),
            ],
        ),
        _segment(
            "Cement technology",
            [
                _chip("Sublime Systems", "electrochemical cement", "sublime"),
                _chip("Brimstone", "calcium silicate routes", "brimstone"),
                _chip("Fortera", "low-carbon cement", "fortera"),
                _chip("Terra CO2", "low-carbon SCM", "terraco2"),
            ],
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
