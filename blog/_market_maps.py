"""Illustrative company market maps for sector Markets sections."""

from typing import Optional

from _viz import _esc

# Ref indices in each post's References list (appended in _generate.py).
MARKET_MAP_REF_IDS: dict[str, tuple[int, ...]] = {
    "weather-foundation-models": (15, 16, 17),
    "aerospace-satellites": (11, 12, 13),
    "materials": (10, 11, 12),
    "energy-systems": (9, 10, 11),
    "manufacturing": (9, 10, 11),
    "built-environment": (9, 10, 11),
    "mobility": (11, 12, 13),
    "industrial-processes": (10, 11, 12),
}


def _c(n: int) -> str:
    return f'[<a href="#r{n}">{n}</a>]'


def _chip(name: str, role: Optional[str] = None) -> str:
    role_html = ""
    if role:
        role_html = f'<span class="mm-role">{_esc(role)}</span>'
    return f'          <li class="mm-chip"><span class="mm-name">{_esc(name)}</span>{role_html}</li>'


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
          <p class="viz-label">Market map</p>
          <p class="mm-title">Who is building here</p>
          <div class="mm-grid">
{grid}
          </div>
          <figcaption class="viz-caption">{caption}</figcaption>
        </figure>'''


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
                _chip("Google DeepMind", "WeatherNext / GraphCast"),
                _chip("Microsoft Research", "Aurora"),
                _chip("NVIDIA", "Earth-2"),
            ],
        ),
        _segment(
            "Startups",
            [
                _chip("WindBorne Systems", "global sensing network"),
                _chip("Atmo", "AI weather forecasts"),
                _chip("Jua", "foundation weather models"),
                _chip("Tomorrow.io", "nowcasting platform"),
            ],
        ),
        _segment(
            "Operators & agencies",
            [
                _chip("ECMWF", "AIFS operations"),
                _chip("NOAA", "AI forecast integration"),
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
                _chip("Planet", "daily global imaging"),
                _chip("Maxar", "high-resolution EO"),
                _chip("BlackSky", "rapid revisit"),
                _chip("Pixxel", "hyperspectral constellations"),
            ],
        ),
        _segment(
            "SAR",
            [
                _chip("Capella Space", "SAR microsatellites"),
                _chip("Umbra", "high-res SAR"),
            ],
        ),
        _segment(
            "GHG & climate sensing",
            [_chip("GHGSat", "facility-level methane")],
        ),
        _segment(
            "Weather & RF",
            [
                _chip("Spire Global", "radio occultation"),
                _chip("HawkEye 360", "RF geolocation"),
            ],
        ),
    ]
    return _figure(segs, caption)


def _materials_map() -> str:
    refs = MARKET_MAP_REF_IDS["materials"]
    caption = (
        f"Illustrative map of low-carbon cement and concrete companies; not exhaustive. "
        f"Sources: sector roundups {_c(refs[0])}{_c(refs[1])}; company disclosures {_c(refs[2])}."
    )
    segs = [
        _segment(
            "Novel cement",
            [
                _chip("Sublime Systems", "electrochemical cement"),
                _chip("Brimstone", "calcium silicate cement"),
                _chip("Fortera", "reactive mineral cement"),
            ],
        ),
        _segment(
            "CO₂ mineralization & concrete",
            [
                _chip("CarbonCure", "injected CO₂ curing"),
                _chip("Solidia", "lower-carbon binder"),
                _chip("CarbonBuilt", "CO₂ mineralized blocks"),
            ],
        ),
        _segment(
            "SCM & circular",
            [_chip("Carbon Upcycling", "CO₂-enhanced SCMs")],
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
            [_chip("Form Energy", "iron-air multi-day")],
        ),
        _segment(
            "Flow batteries",
            [
                _chip("ESS Inc.", "iron flow storage"),
                _chip("Invinity", "vanadium flow"),
            ],
        ),
        _segment(
            "Gravity & compressed air",
            [
                _chip("Energy Vault", "gravity storage"),
                _chip("Hydrostor", "compressed air"),
                _chip("Energy Dome", "CO₂-based storage"),
            ],
        ),
        _segment(
            "Geomechanical & other LDES",
            [
                _chip("Quidnet Energy", "geomechanical pumped storage"),
                _chip("Malta Inc.", "thermal electro-mechanical"),
            ],
        ),
        _segment(
            "Short-duration context",
            [
                _chip("Tesla Energy", "grid-scale Li-ion"),
                _chip("Fluence", "storage integrator"),
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
                _chip("Rondo Energy", "heat batteries"),
                _chip("Antora Energy", "thermal storage"),
                _chip("Electrified Thermal Solutions", "firebrick storage"),
            ],
        ),
        _segment(
            "Electrified steam & boilers",
            [_chip("AtmosZero", "industrial heat pumps")],
        ),
        _segment(
            "Heat-as-a-service",
            [_chip("Zero Industrial", "decarbonized process heat")],
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
            [_chip("CarbonCure", "embedded CO₂ concrete")],
        ),
        _segment(
            "Mass timber producers",
            [
                _chip("Mercer Mass Timber", "cross-laminated timber"),
                _chip("SmartLam", "glulam and CLT"),
                _chip("Fabric Workshop", "prefab mass timber"),
            ],
        ),
        _segment(
            "Supply-chain platforms",
            [_chip("Cambium", "traceable wood supply")],
        ),
        _segment(
            "Software & standards",
            [
                _chip("One Click LCA", "whole-life carbon"),
                _chip("Tally", "Revit embodied carbon"),
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
                _chip("Tesla Supercharger", "DC fast network"),
                _chip("Electrify America", "highway corridors"),
                _chip("EVgo", "urban fast charging"),
                _chip("ChargePoint", "hardware and roaming"),
                _chip("IONNA", "OEM joint network"),
            ],
        ),
        _segment(
            "Smart & managed charging",
            [_chip("PowerFlex", "fleet and workplace ACN")],
        ),
        _segment(
            "Vehicles (context)",
            [
                _chip("Tesla", "EV volume leader"),
                _chip("Rivian", "electric trucks and SUVs"),
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
                _chip("Rondo Energy", "thermal batteries"),
                _chip("Antora Energy", "thermal storage"),
                _chip("Electrified Thermal Solutions", "firebrick heat"),
            ],
        ),
        _segment(
            "Green steel",
            [
                _chip("Stegra", "hydrogen DRI steel"),
                _chip("Boston Metal", "molten oxide electrolysis"),
            ],
        ),
        _segment(
            "Cement technology",
            [
                _chip("Sublime Systems", "electrochemical cement"),
                _chip("Brimstone", "calcium silicate routes"),
                _chip("Fortera", "low-carbon cement"),
            ],
        ),
        _segment(
            "Kiln capture add-ons",
            [_chip("Fortera ReCarb", "point-source mineralization")],
        ),
    ]
    return _figure(segs, caption)


_MAP_BUILDERS = {
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
