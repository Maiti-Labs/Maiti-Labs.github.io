#!/usr/bin/env python3
"""Generate sector research posts in Physical Intelligence-inspired format."""
from pathlib import Path

from _markets import build_markets_section
from _timelines import LEAVES_US_MARKER, future_section_html, sections_for_slug
from _viz import VIZ_SETS

ROOT = Path(__file__).resolve().parent


def _ref(n: int, body: str) -> str:
    return f'<span id="r{n}"></span>{body}'


def ref_fourcastnet(n: int) -> str:
    return _ref(
        n,
        'Pathak, J., Subramanian, S., Harrington, P., et al. (2022). FourCastNet: A global data-driven '
        'high-resolution weather model using adaptive Fourier neural operators. '
        '<a href="https://arxiv.org/abs/2202.11214">arXiv:2202.11214</a>',
    )


def ref_weatherbench2(n: int) -> str:
    return _ref(
        n,
        'Rasp, S., Hoyer, S., Merose, A., et al. (2024). WeatherBench 2: A benchmark for the next '
        'generation of data-driven global weather forecasting. <em>Journal of Advances in Modeling '
        'Earth Systems</em>. <a href="https://doi.org/10.1029/2023MS004019">doi:10.1029/2023MS004019</a>',
    )


def ref_era5(n: int) -> str:
    return _ref(
        n,
        'Hersbach, H., Bell, B., Berrisford, P., et al. (2020). The ERA5 global reanalysis. '
        '<em>Quarterly Journal of the Royal Meteorological Society</em>. '
        '<a href="https://doi.org/10.1002/qj.3803">doi:10.1002/qj.3803</a>',
    )


def ref_aifs(n: int) -> str:
    return _ref(
        n,
        'Lang, S., Hoyer, S., Bishnoi, A., et al. (2024). AIFS-CRPS: Ensemble forecasting using a '
        'model trained with a loss function based on the Continuous Ranked Probability Score. '
        '<a href="https://arxiv.org/abs/2406.01443">arXiv:2406.01443</a> (ECMWF).',
    )


def ref_jevons(n: int) -> str:
    return _ref(
        n,
        'Jevons, W. S. (1865). <em>The Coal Question: An Inquiry Concerning the Progress of the Nation, '
        'and the Probable Exhaustion of Our Coal-Mines</em>. Macmillan. '
        '<a href="https://archive.org/details/coalquestionin00jevorich">archive.org</a>',
    )


def ref_rebound_review(n: int) -> str:
    return _ref(
        n,
        'Sorrell, S., Dimitropoulos, J., & Somerville, M. (2009). Empirical estimates of the direct '
        'rebound effect: A review. <em>Energy Policy</em>. '
        '<a href="https://doi.org/10.1016/j.enpol.2008.11.026">doi:10.1016/j.enpol.2008.11.026</a>',
    )


def ref_iea_cement(n: int) -> str:
    return _ref(
        n,
        'International Energy Agency. (2023). Cement. In industry and emissions briefs. '
        '<a href="https://www.iea.org/energy-system/industry/cement">iea.org/energy-system/industry/cement</a>; '
        'IPCC AR6 WGIII, Ch. 11 (industry emissions). '
        '<a href="https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-11/">ipcc.ch</a>',
    )


def ref_irena_battery(n: int) -> str:
    return _ref(
        n,
        'International Renewable Energy Agency (IRENA). (2023). Renewable power generation costs in 2022. '
        '<a href="https://www.irena.org/Publications/2023/Aug/Renewable-power-generation-costs-in-2022">irena.org</a> '
        '(battery storage cost trends).',
    )


def ref_nevi(n: int) -> str:
    return _ref(
        n,
        'U.S. Department of Energy. National Electric Vehicle Infrastructure (NEVI) Formula Program. '
        '<a href="https://afdc.energy.gov/laws/12859">AFDC summary</a>; '
        '<a href="https://www.federalregister.gov/documents/2022/02/22/2022-03423/national-electric-vehicle-infrastructure-formula-program">'
        'Federal Register (2022)</a>',
    )


def ref_ashrae_240p(n: int) -> str:
    return _ref(
        n,
        'ASHRAE &amp; ICC. (2024). Public review: proposed ASHRAE/ICC Standard 240P, '
        'Standard for Building Decarbonization: Whole Life Carbon. '
        '<a href="https://www.ashrae.org/about/news/2024/ashrae-and-icc-announce-public-review-for-proposed-whole-life-carbon-standard">'
        'ashrae.org</a>',
    )


def consultant_refs_space() -> list[str]:
    return [
        _ref(
            10,
            "McKinsey &amp; Company. The cost of compute: A $7 trillion race to scale data centers; "
            "data center capacity demand charts. "
            '<a href="https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-cost-of-compute-a-7-trillion-dollar-race-to-scale-data-centers">'
            "mckinsey.com</a>; "
            '<a href="https://www.mckinsey.com/featured-insights/sustainable-inclusive-growth/charts/data-center-demands">'
            "mckinsey.com (data center demands)</a>",
        ),
        _ref(
            11,
            "Goldman Sachs Research. AI to drive 165% increase in data center power demand by 2030. "
            '<a href="https://www.goldmansachs.com/insights/articles/ai-to-drive-165-increase-in-data-center-power-demand-by-2030">'
            "goldmansachs.com</a>",
        ),
    ]


def consultant_refs_weather() -> list[str]:
    return [
        _ref(
            15,
            "McKinsey &amp; Company. Space: The $1.8 trillion opportunity for global economic growth "
            "(space-enabled economy scenario). "
            '<a href="https://www.mckinsey.com/industries/aerospace-and-defense/our-insights/space-the-1-point-8-trillion-dollar-opportunity-for-global-economic-growth">'
            "mckinsey.com</a>",
        ),
        _ref(
            16,
            "Goldman Sachs Research. AI to drive 165% increase in data center power demand by 2030 "
            "(compute stack context). "
            '<a href="https://www.goldmansachs.com/insights/articles/ai-to-drive-165-increase-in-data-center-power-demand-by-2030">'
            "goldmansachs.com</a>",
        ),
    ]


def consultant_refs_aerospace() -> list[str]:
    return [
        _ref(
            11,
            "McKinsey &amp; Company. Space: The $1.8 trillion opportunity for global economic growth. "
            '<a href="https://www.mckinsey.com/industries/aerospace-and-defense/our-insights/space-the-1-point-8-trillion-dollar-opportunity-for-global-economic-growth">'
            "mckinsey.com</a>",
        ),
    ]


def consultant_refs_materials() -> list[str]:
    return [
        _ref(
            10,
            "McKinsey &amp; Company. How a materials transition can support the net-zero agenda "
            "(low-CO₂ materials market). "
            '<a href="https://www.mckinsey.com/capabilities/sustainability/our-insights/how-a-materials-transition-can-support-the-net-zero-agenda">'
            "mckinsey.com</a>",
        ),
    ]


def consultant_refs_energy() -> list[str]:
    return [
        _ref(
            9,
            "McKinsey &amp; Company. Net-zero power: Long-duration energy storage for a renewable grid. "
            '<a href="https://www.mckinsey.com/capabilities/sustainability/our-insights/net-zero-power-long-duration-energy-storage-for-a-renewable-grid">'
            "mckinsey.com</a>",
        ),
        _ref(
            10,
            "Goldman Sachs Research. The outlook for the cost of decarbonization (battery pack cost outlook). "
            '<a href="https://www.goldmansachs.com/insights/articles/the-outlook-for-the-cost-of-decarbonization">'
            "goldmansachs.com</a>",
        ),
    ]


def consultant_refs_manufacturing() -> list[str]:
    return [
        _ref(
            9,
            "McKinsey &amp; Company. Infrastructure for a net-zero economy: Transformation ahead "
            "(cement and steel unit cost scenario). "
            '<a href="https://www.mckinsey.com/industries/infrastructure/our-insights/infrastructure-for-a-net-zero-economy-transformation-ahead">'
            "mckinsey.com</a>",
        ),
    ]


def consultant_refs_built() -> list[str]:
    return [
        _ref(
            9,
            "McKinsey &amp; Company. Building value by decarbonizing the built environment. "
            '<a href="https://www.mckinsey.com/industries/engineering-construction-and-building-materials/our-insights/building-value-by-decarbonizing-the-built-environment">'
            "mckinsey.com</a>",
        ),
    ]


def consultant_refs_mobility() -> list[str]:
    return [
        _ref(
            11,
            "McKinsey &amp; Company. Battery 2030: Resilient, sustainable, and circular "
            "(EV sales and lithium-ion demand scenario). "
            '<a href="https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/battery-2030-resilient-sustainable-and-circular">'
            "mckinsey.com</a>; EV share context in "
            '<a href="https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/enabling-renewable-energy-with-battery-energy-storage-systems">'
            "BESS outlook</a>",
        ),
        _ref(
            12,
            "Goldman Sachs Research. The outlook for the cost of decarbonization (battery pack toward ~$80/kWh). "
            '<a href="https://www.goldmansachs.com/insights/articles/the-outlook-for-the-cost-of-decarbonization">'
            "goldmansachs.com</a>",
        ),
    ]


def consultant_refs_industrial() -> list[str]:
    return [
        _ref(
            10,
            "McKinsey &amp; Company. How a materials transition can support the net-zero agenda. "
            '<a href="https://www.mckinsey.com/capabilities/sustainability/our-insights/how-a-materials-transition-can-support-the-net-zero-agenda">'
            "mckinsey.com</a>",
        ),
        _ref(
            11,
            "McKinsey &amp; Company. Infrastructure for a net-zero economy: Transformation ahead. "
            '<a href="https://www.mckinsey.com/industries/infrastructure/our-insights/infrastructure-for-a-net-zero-economy-transformation-ahead">'
            "mckinsey.com</a>",
        ),
    ]


CONSULTANT_REFS_BY_SLUG = {
    "space-compute": consultant_refs_space,
    "weather-foundation-models": consultant_refs_weather,
    "aerospace-satellites": consultant_refs_aerospace,
    "materials": consultant_refs_materials,
    "energy-systems": consultant_refs_energy,
    "manufacturing": consultant_refs_manufacturing,
    "built-environment": consultant_refs_built,
    "mobility": consultant_refs_mobility,
    "industrial-processes": consultant_refs_industrial,
}


def market_map_refs_space() -> list[str]:
    return [
        _ref(
            12,
            'New Space Economy. Orbital data center companies building space-based compute infrastructure. '
            '<a href="https://newspaceeconomy.ca/2026/05/31/orbital-data-center-companies-building-space-based-compute-infrastructure/">'
            'newspaceeconomy.ca</a>',
        ),
        _ref(
            13,
            'Starcloud (orbital data centers). <a href="https://starcloud.com/">starcloud.com</a>; '
            'Aetherflux. <a href="https://aetherflux.com/">aetherflux.com</a>; '
            'Blue Origin. <a href="https://www.blueorigin.com/">blueorigin.com</a>; '
            'Kepler Communications. <a href="https://kepler.space/">kepler.space</a>',
        ),
        _ref(
            14,
            'Google Research. Exploring a space-based scalable AI infrastructure system design (Project Suncatcher). '
            '<a href="https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/">'
            'research.google</a>; Agüera y Arcas, Beals, et al. '
            '<a href="https://arxiv.org/abs/2511.19468">arXiv:2511.19468</a>; Planet partnership. '
            '<a href="https://www.planet.com/pulse/planet-to-build-and-operate-advanced-space-platform-for-google-s-project-suncatcher-moonshot/">'
            'planet.com</a>; Ramon.Space. <a href="https://ramon.space/">ramon.space</a>',
        ),
        _ref(
            15,
            'Bain &amp; Company. Orbital data centers: beyond the grid. '
            '<a href="https://www.bain.com/insights/orbital-data-centers-beyond-the-grid/">bain.com</a>; '
            'Wood Mackenzie press release on orbital data centre costs. '
            '<a href="https://www.woodmac.com/press-releases/wood-mackenzie-orbital-data-centres-cost-three-times-more-than-terrestrial-alternatives-as-global-power-demand-heads-for-3700-twh">'
            'woodmac.com</a>; Axiom Space. <a href="https://www.axiomspace.com/">axiomspace.com</a>; '
            'Aethero. <a href="https://aethero.com/">aethero.com</a>; Crusoe. '
            '<a href="https://www.crusoe.ai/">crusoe.ai</a>',
        ),
    ]


def market_map_refs_weather() -> list[str]:
    return [
        _ref(
            17,
            'Google DeepMind. GraphCast and WeatherNext. '
            '<a href="https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/">'
            'deepmind.google</a>; Microsoft Research. Aurora. '
            '<a href="https://www.microsoft.com/en-us/research/project/aurora/">microsoft.com/research</a>; '
            'NVIDIA. Earth-2. <a href="https://www.nvidia.com/en-us/high-performance-computing/earth-2/">nvidia.com</a>',
        ),
        _ref(
            18,
            'WindBorne Systems. <a href="https://windbornesystems.com/">windbornesystems.com</a>; '
            'Atmo. <a href="https://www.atmo.ai/">atmo.ai</a>; Jua. <a href="https://www.jua.ai/">jua.ai</a>; '
            'Tomorrow.io. <a href="https://www.tomorrow.io/">tomorrow.io</a>; '
            'Causal Labs. <a href="https://causallabs.ai/">causallabs.ai</a>; '
            'Climavision. <a href="https://climavision.com/">climavision.com</a>; '
            'Salient Predictions. <a href="https://salientpredictions.com/">salientpredictions.com</a>',
        ),
        _ref(
            19,
            'ACM News. (2024). AI weather forecasting goes operational. '
            '<em>Communications of the ACM</em>. '
            '<a href="https://cacm.acm.org/news/ai-weather-forecasting-goes-operational/">cacm.acm.org</a>; '
            'ECMWF. <a href="https://www.ecmwf.int/">ecmwf.int</a>; NOAA. '
            '<a href="https://www.noaa.gov/">noaa.gov</a>',
        ),
        _ref(
            20,
            'The Weather Company (IBM). Operational forecast products. '
            '<a href="https://www.weather.com/">weather.com</a>; IBM Weather. '
            '<a href="https://www.ibm.com/products/environmental-intelligence-suite">ibm.com</a>',
        ),
    ]


def market_map_refs_aerospace() -> list[str]:
    return [
        _ref(
            12,
            'New Space Economy. Global directory of Earth observation satellite operators and products. '
            '<a href="https://newspaceeconomy.ca/2026/04/16/global-directory-of-earth-observation-satellite-operators-and-their-products-and-services/">'
            'newspaceeconomy.ca</a>',
        ),
        _ref(
            13,
            'Payload. (2024). The state of Earth observation. '
            '<a href="https://payloadspace.com/the-state-of-earth-observation-2024/">payloadspace.com</a>; '
            'TerraWatch. Earth observation market landscape. '
            '<a href="https://terrawatchspace.com/">terrawatchspace.com</a>',
        ),
        _ref(
            14,
            'Company sites: Planet. <a href="https://www.planet.com/">planet.com</a>; ICEYE. '
            '<a href="https://www.iceye.com/">iceye.com</a>; Satellogic. '
            '<a href="https://satellogic.com/">satellogic.com</a>; Albedo. '
            '<a href="https://albedo.space/">albedo.space</a>; Wyvern. '
            '<a href="https://wyvern.space/">wyvern.space</a>',
        ),
        _ref(
            15,
            'Company sites: Capella Space. <a href="https://www.capellaspace.com/">capellaspace.com</a>; '
            'GHGSat. <a href="https://www.ghgsat.com/">ghgsat.com</a>; OroraTech. '
            '<a href="https://ororatech.com/">ororatech.com</a>; Hydrosat. '
            '<a href="https://hydrosat.com/">hydrosat.com</a>; Muon Space. '
            '<a href="https://www.muonspace.com/">muonspace.com</a>; Airbus Defence and Space. '
            '<a href="https://www.airbus.com/en/products-services/space">airbus.com</a>',
        ),
    ]


def market_map_refs_materials() -> list[str]:
    return [
        _ref(
            11,
            'Wilson, A. GreenBuildingAdvisor. Six startups take CO<sub>2</sub> out of cement and concrete. '
            '<a href="https://www.greenbuildingadvisor.com/article/six-startups-take-co2-out-of-cement-and-concrete">'
            'greenbuildingadvisor.com</a>; six startups with novel low-carbon cement approaches. '
            '<a href="https://www.greenbuildingadvisor.com/article/six-startups-with-novel-approaches-to-low-carbon-cement">'
            'greenbuildingadvisor.com</a>',
        ),
        _ref(
            12,
            'Canary Media. Fortera and low-carbon cement coverage. '
            '<a href="https://www.canarymedia.com/articles/clean-industry/fortera-is-making-cement-that-absorbs-co2-instead-of-emitting-it">'
            'canarymedia.com</a>; Biomason. <a href="https://biomason.com/">biomason.com</a>; '
            'Blue Planet Systems. <a href="https://blueplanetsystems.com/">blueplanetsystems.com</a>',
        ),
        _ref(
            13,
            'Company sites: Sublime Systems. <a href="https://www.sublime-systems.com/">sublime-systems.com</a>; '
            'CarbonCure. <a href="https://www.carboncure.com/">carboncure.com</a>; Brimstone. '
            '<a href="https://www.brimstone.com/">brimstone.com</a>; Carbon Upcycling. '
            '<a href="https://carbonupcycling.com/">carbonupcycling.com</a>; '
            'NoPo Nanotechnologies (HiPCO SWCNTs). <a href="https://www.noponano.com/">noponano.com</a>',
        ),
        _ref(
            14,
            'Hoffmann Green Cement. <a href="https://www.hoffmann-green.com/en">hoffmann-green.com</a>; '
            'Queens Carbon. <a href="https://www.queenscarbon.com/">queenscarbon.com</a>; '
            'Minus Materials. <a href="https://minusmaterials.com/">minusmaterials.com</a>; '
            'Terra CO2. <a href="https://www.terraco2.com/">terraco2.com</a>',
        ),
    ]


def market_map_refs_energy() -> list[str]:
    return [
        _ref(
            11,
            'EPRI. Energy storage wiki and long-duration storage resources. '
            '<a href="https://www.epri.com/research/products/000000003002">epri.com</a>; '
            'Highview Power. Liquid air energy storage. '
            '<a href="https://www.highviewpower.com/">highviewpower.com</a>; '
            'Form Energy. <a href="https://formenergy.com/">formenergy.com</a>',
        ),
        _ref(
            12,
            'Energy Vault. <a href="https://energyvault.com/">energyvault.com</a>; Hydrostor. '
            '<a href="https://www.hydrostor.ca/">hydrostor.ca</a>; Gravitricity. '
            '<a href="https://gravitricity.com/">gravitricity.com</a>; EnergyNest. '
            '<a href="https://energynest.com/">energynest.com</a>',
        ),
        _ref(
            13,
            'ESS Inc. <a href="https://essinc.com/">essinc.com</a>; Invinity. '
            '<a href="https://invinity.com/">invinity.com</a>; CMBlu. '
            '<a href="https://www.cmblu.com/">cmblu.com</a>; EnerVenue. '
            '<a href="https://enervenue.com/">enervenue.com</a>; Ambri. '
            '<a href="https://ambri.com/">ambri.com</a>; EOS Energy. '
            '<a href="https://eose.com/">eose.com</a>; e-Zinc. '
            '<a href="https://e-zinc.ca/">e-zinc.ca</a>',
        ),
        _ref(
            14,
            'Quidnet Energy. <a href="https://www.quidnetenergy.com/">quidnetenergy.com</a>; '
            'Malta Inc. <a href="https://www.maltainc.com/">maltainc.com</a>; Energy Dome. '
            '<a href="https://energydome.com/">energydome.com</a>; Fluence. '
            '<a href="https://fluenceenergy.com/">fluenceenergy.com</a>; '
            'MarketsandMarkets LDES landscape summary. '
            '<a href="https://www.marketsandmarkets.com/ResearchInsight/long-duration-energy-storage-market.asp">'
            'marketsandmarkets.com</a>',
        ),
    ]


def market_map_refs_manufacturing() -> list[str]:
    return [
        _ref(
            10,
            'Canary Media. Thermal batteries for industrial heat. '
            '<a href="https://www.canarymedia.com/articles/clean-industry/thermal-batteries-could-help-decarbonize-industry">'
            'canarymedia.com</a>',
        ),
        _ref(
            11,
            'Rondo Energy. <a href="https://www.rondo.com/">rondo.com</a>; Antora Energy. '
            '<a href="https://www.antora.com/">antora.com</a>; Kraftblock. '
            '<a href="https://kraftblock.com/">kraftblock.com</a>; Kyoto Group. '
            '<a href="https://www.kyotogroup.no/">kyotogroup.no</a>',
        ),
        _ref(
            12,
            'Electrified Thermal Solutions. <a href="https://www.electrifiedthermal.com/">electrifiedthermal.com</a>; '
            'Brenmiller Energy. <a href="https://brenmiller.com/">brenmiller.com</a>; '
            'Zero Industrial. <a href="https://www.zeroindustrial.com/">zeroindustrial.com</a>',
        ),
        _ref(
            13,
            'AtmosZero. <a href="https://www.atmoszero.energy/">atmoszero.energy</a>',
        ),
    ]


def market_map_refs_built() -> list[str]:
    return [
        _ref(
            10,
            'CarbonCure. <a href="https://www.carboncure.com/">carboncure.com</a>; Solidia Technologies. '
            '<a href="https://solidiatech.com/">solidiatech.com</a>',
        ),
        _ref(
            11,
            'Cambium. <a href="https://www.cambiumcarbon.com/">cambiumcarbon.com</a>; SmartLam. '
            '<a href="https://smartlam.com/">smartlam.com</a>; Mercer Mass Timber. '
            '<a href="https://www.mercerint.com/mass-timber/">mercerint.com</a>',
        ),
        _ref(
            12,
            'Fabric Workshop. Mass timber prefabrication. '
            '<a href="https://www.fabricworkshop.com/">fabricworkshop.com</a>; Structurlam. '
            '<a href="https://www.structurlam.com/">structurlam.com</a>; BuildingGreen mass timber resources. '
            '<a href="https://www.buildinggreen.com/primer/mass-timber">buildinggreen.com</a>',
        ),
        _ref(
            13,
            'One Click LCA. <a href="https://www.oneclicklca.com/">oneclicklca.com</a>; EC3 embodied carbon. '
            '<a href="https://buildingtransparency.org/ec3">buildingtransparency.org</a>; '
            'Tally / Carbon Leadership Forum tools. '
            '<a href="https://carbonleadershipforum.org/tally/">carbonleadershipforum.org</a>',
        ),
    ]


def market_map_refs_mobility() -> list[str]:
    return [
        _ref(
            13,
            'EV Charging Stations News. DC fast charging network landscape (July 2026). '
            '<a href="https://evchargingstations.com/chargingnews/dc-fast-charging-july-2026/">'
            'evchargingstations.com</a>; ElectronsX CPO directory. '
            '<a href="https://electronsx.com/">electronsx.com</a>',
        ),
        _ref(
            14,
            'PowerFlex (EDF). Adaptive charging and fleet software. '
            '<a href="https://www.powerflex.com/">powerflex.com</a>; AmpUp. '
            '<a href="https://ampup.io/">ampup.io</a>; Caltech ACN lineage. '
            '<a href="https://ev.caltech.edu/">ev.caltech.edu</a>',
        ),
        _ref(
            15,
            'ChargePoint. <a href="https://www.chargepoint.com/">chargepoint.com</a>; EVgo. '
            '<a href="https://www.evgo.com/">evgo.com</a>; Blink Charging. '
            '<a href="https://blinkcharging.com/">blinkcharging.com</a>; EV Connect. '
            '<a href="https://www.evconnect.com/">evconnect.com</a>; IONNA. '
            '<a href="https://ionna.com/">ionna.com</a>',
        ),
        _ref(
            16,
            'Electrify America. <a href="https://www.electrifyamerica.com/">electrifyamerica.com</a>; '
            'Rivian. <a href="https://rivian.com/">rivian.com</a>; Lucid Motors. '
            '<a href="https://lucidmotors.com/">lucidmotors.com</a>; U.S. public charging summaries. '
            '<a href="https://www.evwire.com/">evwire.com</a>',
        ),
    ]


def market_map_refs_industrial() -> list[str]:
    return [
        _ref(
            12,
            'Boston Metal. Molten oxide electrolysis steel. '
            '<a href="https://www.bostonmetal.com/">bostonmetal.com</a>; Electra. '
            '<a href="https://electra.earth/">electra.earth</a>; Blastr Green Steel. '
            '<a href="https://blastr.no/">blastr.no</a>',
        ),
        _ref(
            13,
            'Stegra (formerly H2 Green Steel). Fossil-free steel. '
            '<a href="https://www.stegra.com/">stegra.com</a>; SSAB HYBRIT initiative. '
            '<a href="https://www.ssab.com/en/company/sustainability/hybrit">ssab.com</a>',
        ),
        _ref(
            14,
            'Rondo Energy. <a href="https://www.rondo.com/">rondo.com</a>; Antora Energy. '
            '<a href="https://www.antora.com/">antora.com</a>; Electrified Thermal Solutions. '
            '<a href="https://www.electrifiedthermal.com/">electrifiedthermal.com</a>; '
            'AtmosZero. <a href="https://www.atmoszero.energy/">atmoszero.energy</a>',
        ),
        _ref(
            15,
            'Fortera. Low-carbon cement. <a href="https://www.fortera.com/">fortera.com</a>; '
            'Sublime Systems. <a href="https://www.sublime-systems.com/">sublime-systems.com</a>; '
            'Brimstone. <a href="https://www.brimstone.com/">brimstone.com</a>; Terra CO2. '
            '<a href="https://www.terraco2.com/">terraco2.com</a>',
        ),
    ]


MARKET_MAP_REFS_BY_SLUG = {
    "space-compute": market_map_refs_space,
    "weather-foundation-models": market_map_refs_weather,
    "aerospace-satellites": market_map_refs_aerospace,
    "materials": market_map_refs_materials,
    "energy-systems": market_map_refs_energy,
    "manufacturing": market_map_refs_manufacturing,
    "built-environment": market_map_refs_built,
    "mobility": market_map_refs_mobility,
    "industrial-processes": market_map_refs_industrial,
}


NAV = '''  <nav class="nav" id="nav">
    <div class="wrap nav-inner">
      <a class="brand" href="../index.html" aria-label="Maiti Labs home">
        <img src="../logo.png" alt="" width="22" height="22" />
        <span>Maiti Labs</span>
      </a>
      <div class="nav-links">
        <a href="../index.html#research">Research</a>
        <a href="index.html">Notes</a>
        <a href="../index.html#sectors">Sectors</a>
      </div>
      <a class="nav-cta" href="index.html">All notes</a>
    </div>
  </nav>'''

FOOTER = '''  <footer class="footer">
    <div class="wrap">
      <div class="footer-row">
        <a class="brand" href="../index.html">
          <img src="../logo.png" alt="" width="18" height="18" />
          <span>Maiti Labs</span>
        </a>
        <p class="footer-tag">Climate research, made accessible.</p>
      </div>
      <p class="copyright">Copyright © 2026 Maiti Labs. All rights reserved.</p>
    </div>
  </footer>
  <script>
    const nav = document.getElementById('nav');
    const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 8);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  </script>'''

def page(title, description, body_html):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} · Maiti Labs</title>
<meta name="description" content="{description}" />
<link rel="icon" href="../logo.png" type="image/png" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css" />
</head>
<body>
{NAV}
{body_html}
{FOOTER}
</body>
</html>
'''

AUTHOR = "Shryas Bhurat"

def article(meta, title, dek, body, refs, viz_html=""):
    ref_items = "\n".join(f"<li>{r}</li>" for r in refs)
    viz_block = f"\n{viz_html}\n" if viz_html else ""
    return f'''  <article class="article">
    <div class="wrap-narrow">
      <a class="back-link" href="index.html">‹ All research notes</a>
      <p class="article-meta">{meta}</p>
      <p class="article-author">By {AUTHOR}</p>
      <h1>{title}</h1>
      <p class="dek">{dek}</p>{viz_block}
      <div class="body">
{body}
      </div>
      <section class="refs">
        <h2>References</h2>
        <ol>
{ref_items}
        </ol>
      </section>
    </div>
  </article>'''

POSTS = []

# 1 Space Compute
POSTS.append({
    "slug": "space-compute",
    "num": "01",
    "sector": "Space Compute",
    "viz_key": "space",
    "card_title": "Orbital compute meets the terrestrial power wall",
    "card_blurb": "AI data centers strain grids on Earth. Orbit offers continuous solar and radiative cooling, if launch costs fall.",
    "meta": "Research note · August 1, 2026 · Sector 01 · Shryas Bhurat",
    "title": "Orbital compute meets the terrestrial power wall",
    "dek": "Always-on solar in orbit is real. Cost parity still depends on launch.",
    "description": "Emerging orbital data center and space compute research from Google, industry analysts, and orbital DC startups, with citations.",
    "body": '''
        <div class="callout callout-plain">
          <p><strong>In plain terms.</strong> Training and serving AI needs enormous electricity, cooling water, and new grid connections on Earth [<a href="#r4">4</a>]. Some teams want to run accelerators in orbit where the sun never sets on a well-chosen path and heat radiates to space, then beam results down by laser or radio [<a href="#r1">1</a>]. Today that still costs far more than a terrestrial rack unless launch gets much cheaper [<a href="#r3">3</a>][<a href="#r4">4</a>].</p>
        </div>
        <p>Terrestrial hyperscale data centers are colliding with the same constraints climate policy already tracks: power purchase agreements, substation queues, freshwater for cooling, and siting fights in communities that did not sign up to host gigawatt-class AI load [<a href="#r4">4</a>]. Orbital compute is not a fantasy escape hatch. It is an engineering bet that continuous solar illumination and radiative cooling can offset the penalty of lifting mass and maintaining links through the atmosphere [<a href="#r1">1</a>][<a href="#r3">3</a>].</p>
        <p>For accessible climate research, the question is not whether orbit is "green" by default. It is whether a watt of inference delivered from space avoids a watt of fossil-backed grid build on the ground, after counting launch, replacement, spectrum, and ground-station energy. Public preprints, analyst models, and early demos are finally making that accounting possible [<a href="#r1">1</a>][<a href="#r4">4</a>][<a href="#r5">5</a>].</p>

        <h2>Why the grid feels like a wall</h2>
        <p>Global electricity demand from data centers is rising quickly enough that analysts now treat AI load as a macro grid variable, not a niche IT line item [<a href="#r4">4</a>]. Regions with cheap renewables still face interconnection delays, transformer lead times, and water limits for evaporative cooling. That friction pushes hyperscalers toward long-lead power deals and novel cooling, and it opens room for architectures that move compute where energy is structurally easier to collect [<a href="#r3">3</a>].</p>
        <p>Orbit does not remove energy use. It relocates collection and rejection. A satellite in a suitable low-Earth path can see repeated sunlit intervals without nights as long as a fixed surface site, while dumping waste heat to deep space instead of warming local rivers [<a href="#r1">1</a>]. The trade is capital cost in launch, radiation tolerance, thermal design, and laser or RF backhaul rather than land and permitting [<a href="#r3">3</a>][<a href="#r4">4</a>].</p>

        <h2>Google Project Suncatcher and the research stack</h2>
        <p>Google Research's Project Suncatcher sketches a constellation of solar-powered satellites carrying Trillium TPUs, linked by free-space optical inter-satellite links, operating in dawn-dusk sun-synchronous orbits so arrays stay sunlit while still overflying populated regions for ground contact [<a href="#r1">1</a>]. The team published a system design preprint, "Towards a future space-based, highly scalable AI infrastructure system design," and reported radiation testing on Trillium hardware [<a href="#r1">1</a>]. Planet agreed to build and operate advanced space platforms for two Suncatcher prototypes targeted for roughly early 2027, connecting Google's moonshot to a flight-proven smallsat operator [<a href="#r2">2</a>].</p>
        <p>This is foundation-model-scale thinking applied to infrastructure: treat compute, power, and networking as one co-designed stack rather than a warehouse full of air-conditioned racks. University labs contribute adjacent pieces, from space systems engineering to the grid and lifecycle footprint of AI, but the most detailed public orbital-AI architecture today comes from Google Research and open preprints rather than campus press releases [<a href="#r1">1</a>].</p>

        <h2>Economics: Bain, Wood Mackenzie, and launch math</h2>
        <p>Bain argues orbital data centers could begin scaling in the early 2030s if launch costs fall and operators can close the business case for latency-tolerant workloads, with SpaceX's January 2026 FCC filing for an orbital data center system treated as a signal that majors are exploring the category [<a href="#r3">3</a>]. Wood Mackenzie estimates that roughly one gigawatt of orbital data center capacity could cost on the order of US$170 billion, more than three times a terrestrial equivalent, with launch and satellite manufacturing comprising about sixty percent of that stack [<a href="#r4">4</a>]. Their headline message is blunt: on the order of a seventy percent cost reduction would be needed for rough parity with ground build [<a href="#r4">4</a>].</p>
        <p>Those numbers are scenario-dependent, but they set the debate correctly. Orbital compute wins only where energy and siting savings plus utilization from sunlit orbits outweigh launch and maintenance. Until that crossover moves, most training and serving stays on Earth, and orbit remains a niche for demos, defense, and experiments that tolerate link latency [<a href="#r3">3</a>][<a href="#r4">4</a>].</p>

        <h2>Hardware in flight and filings on the ground</h2>
        <p>Starcloud (formerly Lumen Orbit) reported flying an Nvidia H100 in orbit on Starcloud-1 in November 2025, with SpaceNews coverage of a large Series A raise and an FCC plan for a very large constellation scale [<a href="#r5">5</a>][<a href="#r6">6</a>]. Axiom Space markets orbital compute nodes as part of its commercial space station roadmap [<a href="#r9">9</a>]. Lonestar and similar firms pitch lunar or edge storage as complementary niches rather than wholesale replacement for hyperscale training clusters, useful to mention carefully as edge cases, not the center of mass [<a href="#r9">9</a>].</p>
        <p>SpaceX's orbital data center application, widely reported alongside the FCC docket in early 2026, matters because it couples the world's lowest marginal launch provider with explicit intent to host compute in space [<a href="#r3">3</a>][<a href="#r6">6</a>]. Whether that filing becomes hardware or stays strategic option value, it changes how regulators and grid planners should treat orbit as a competitor to terrestrial build [<a href="#r3">3</a>].</p>

        <h2>Where this leaves us</h2>
        <p>Space compute sits at the intersection of climate stress on terrestrial AI and aerospace industrialization. The credible near-term story is hybrid: Earth keeps most latency-sensitive inference; orbit tests sun-powered accelerators, optical mesh networking, and radiation-hardened silicon for workloads that can tolerate link delay [<a href="#r1">1</a>][<a href="#r5">5</a>]. Climate gains appear only if orbital watts truly substitute for fossil-backed grid expansion, not if they add a parallel compute boom driven by cheaper orbital cycles [<a href="#r7">7</a>][<a href="#r8">8</a>]. Open cost models, cited demos, and honest link budgets are how this sector stays accessible research rather than launch hype.</p>
''',
    "refs": [
        '<span id="r1"></span>Google Research. (2025). Exploring a space-based scalable AI infrastructure system design (Project Suncatcher); Agüera y Arcas, Beals, et al., '
        'Towards a future space-based, highly scalable AI infrastructure system design. '
        '<a href="https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/">research.google</a>; '
        '<a href="https://arxiv.org/abs/2511.19468">arXiv:2511.19468</a>',
        '<span id="r2"></span>Planet. Planet to build and operate advanced space platform for Google\'s Project Suncatcher moonshot. '
        '<a href="https://www.planet.com/pulse/planet-to-build-and-operate-advanced-space-platform-for-google-s-project-suncatcher-moonshot/">planet.com</a>',
        '<span id="r3"></span>Bain &amp; Company. Orbital data centers: beyond the grid. '
        '<a href="https://www.bain.com/insights/orbital-data-centers-beyond-the-grid/">bain.com</a>',
        '<span id="r4"></span>Wood Mackenzie. (2026). Orbital data centres cost three times more than terrestrial alternatives (press release). '
        '<a href="https://www.woodmac.com/press-releases/wood-mackenzie-orbital-data-centres-cost-three-times-more-than-terrestrial-alternatives-as-global-power-demand-heads-for-3700-twh">woodmac.com</a>',
        '<span id="r5"></span>SpaceNews. Starcloud achieves unicorn status with $170 million raise for orbital data centers; Starcloud-1 H100 demo. '
        '<a href="https://spacenews.com/starcloud-achieves-unicorn-status-with-170-million-raise-for-orbital-data-centers/">spacenews.com</a>',
        '<span id="r6"></span>SpaceNews. Starcloud files plans for 88,000-satellite constellation; SpaceX orbital data center FCC filing context. '
        '<a href="https://spacenews.com/starcloud-files-plans-for-88000-satellite-constellation/">spacenews.com</a>',
        ref_jevons(7),
        ref_rebound_review(8),
        '<span id="r9"></span>Axiom Space. Orbital infrastructure and compute nodes. '
        '<a href="https://www.axiomspace.com/">axiomspace.com</a>; Lonestar. Edge and lunar data services. '
        '<a href="https://lonestar.com/">lonestar.com</a>',
    ],
})

# 2 Weather
POSTS.append({
    "slug": "weather-foundation-models",
    "num": "02",
    "sector": "Weather Foundation Models",
    "viz_key": "weather",
    "card_title": "AI weather models are rewriting the forecast stack",
    "card_blurb": "GraphCast, Aurora, and ClimaX match classic forecasts on many scores, far faster.",
    "meta": "Research note · August 1, 2026 · Sector 02 · Shryas Bhurat",
    "title": "AI weather models are rewriting the forecast stack",
    "dek": "Minutes instead of hours. Open checkpoints instead of agency-only supercomputers.",
    "description": "Emerging weather foundation models from DeepMind, Microsoft, ECMWF, and university labs, with citations.",
    "body": '''
        <div class="callout callout-plain">
          <p><strong>In plain terms.</strong> Weather AI learns patterns from decades of global data, then rolls out a forecast in minutes on a single machine [<a href="#r9">9</a>]. Classic physics models on supercomputers still set the quality bar, but they take hours and sit behind agency walls [<a href="#r2">2</a>].</p>
        </div>
        <p>For decades, skillful medium-range forecasts meant one thing: a physics-based numerical weather prediction (NWP) system on a supercomputer. That stack still matters. Data-driven models trained on reanalysis archives can now produce competitive forecasts in minutes on commodity hardware [<a href="#r9">9</a>][<a href="#r11">11</a>].</p>
        <p>This is not a cosmetic speedup. It changes access. University labs, national agencies, and climate-risk teams that could never operate a full IFS-class system can now evaluate ensemble-scale experiments, downscaling pipelines, and early-warning prototypes. The research question has shifted from "can AI forecast weather?" to "which foundation-model designs generalize under climate change, extremes, and sparse observations?"</p>

        <h2>What "foundation model" means in weather</h2>
        <p>In language and vision, a foundation model is pretrained once on broad data, then adapted to many tasks. Weather and climate need the same idea, but the data are gridded fields, multiple physical variables, and heterogeneous resolutions.</p>
        <p><a href="https://arxiv.org/abs/2301.10343">ClimaX</a>, developed by researchers at UCLA and Microsoft Research, was an early explicit attempt at this framing. It extends a Vision Transformer with variable tokenization and aggregation so one model can be pretrained on heterogeneous CMIP6-derived climate data, then fine-tuned for forecasting, projection, and downscaling tasks, including variables and scales not seen in pretraining [<a href="#r1">1</a>]. That is the core recipe later systems refine: pretrain broadly, specialize cheaply.</p>

        <h2>The current frontier models</h2>
        <h3>Graph neural networks and transformers at global scale</h3>
        <p>Google DeepMind's <a href="https://www.science.org/doi/10.1126/science.adi2336">GraphCast</a> (Lam et al.) encodes the atmosphere as a multi-scale mesh and rolls out 6-hour steps to produce 10-day forecasts. On WeatherBench-style evaluations it matched or exceeded ECMWF's high-resolution IFS on many variables while running orders of magnitude faster [<a href="#r2">2</a>]. Huawei's <a href="https://www.nature.com/articles/s41586-023-06185-3">Pangu-Weather</a> (Bi et al.) uses a 3D Earth Transformer and hierarchical temporal aggregation, again reporting deterministic skill competitive with operational IFS on reanalysis benchmarks [<a href="#r3">3</a>].</p>
        <p>NVIDIA's FourCastNet line [<a href="#r9">9</a>] and ECMWF's Artificial Intelligence Integrated Forecasting System (AIFS) [<a href="#r12">12</a>] push the same idea into operational settings. Feldmann et al. use WeatherBench2 [<a href="#r10">10</a>] to compare Pangu-Weather, GraphCast, and FourCastNet against IFS-HRES for severe convective environments, showing that AI models can produce useful large-scale convective outlooks far faster than classical pipelines [<a href="#r4">4</a>].</p>

        <h3>Toward multi-domain atmospheric foundation models</h3>
        <p>Microsoft Research's <a href="https://doi.org/10.1038/s41586-025-09005-y">Aurora</a> (Bodnar, Bruinsma, Lucic, et al.) widens the pretraining mixture beyond ERA5 weather fields, incorporating air quality, ocean, and climate-model outputs into one flexible backbone [<a href="#r5">5</a>]. That is closer to a true Earth-system foundation model than a single-task emulator.</p>
        <div class="callout">
          <p>The practical implication for accessibility: once a strong pretrained checkpoint exists, fine-tuning for a regional hazard, an agricultural index, or an air-quality product becomes a research project rather than a national computing program.</p>
        </div>

        <h2>What top labs are stressing next</h2>
        <p>Skill on ERA5 [<a href="#r11">11</a>] is necessary but not sufficient. Rackow et al. examine GraphCast, Pangu-Weather, and AIFS under climate-change-like conditions and ask whether models trained on the recent past remain reliable as the climate shifts [<a href="#r6">6</a>]. Extremes remain a hard edge: AI forecasts can be overly smooth and can understate record-breaking events even when mean scores look excellent [<a href="#r6">6</a>][<a href="#r10">10</a>].</p>
        <p>University groups are therefore focusing on hybrid designs, probabilistic ensembles, and observation-informed fine-tuning. Stanford's Doerr School and related atmospheric research communities emphasize that operational value depends on calibration for hazards people actually manage: heat, flood precursors, wind extremes, and compound events, not only RMSE on 500 hPa geopotential.</p>

        <h2>Hybrid climate modeling: Google Research and Caltech CliMA</h2>
        <p>Parallel to the data-driven weather wave, Caltech's Climate Modeling Alliance (CliMA), led by Tapio Schneider, pursues hybrid physics–machine learning parameterizations that keep dynamical constraints explicit while learning subgrid closures from data. Lopez-Gomez et al., with Google Research and Caltech authors, report dynamical-generative downscaling of climate model ensembles that preserves large-scale circulation while generating high-resolution fields suitable for impact studies [<a href="#r7">7</a>]. Christopoulos et al. show hybrid ML parameterizations for cloud entrainment that can be updated as observations stream in, a design point that differs from frozen pretrained forecasters [<a href="#r8">8</a>].</p>
        <p>The two agendas are complementary. Weather foundation models excel at fast, global deterministic forecasts from reanalysis. Caltech's physics-constrained climate modeling agenda targets long-horizon ensembles, process fidelity, and downscaling that remains tied to conservation laws. Accessible climate research needs both: open checkpoints for short-range hazard work and open process models for scenario stress-testing.</p>

        <h2>Why this matters for accessible climate research</h2>
        <p>Weather foundation models compress a capability that used to sit behind agency firewalls. Open weights, public reanalysis [<a href="#r11">11</a>], and benchmarks such as WeatherBench2 [<a href="#r10">10</a>] let students at Berkeley, researchers in the Global South, and municipal risk teams reproduce modern forecast skill. The open problem is not whether these models exist. It is how to document uncertainty, couple them to impact models, and keep evaluation honest as the climate moves [<a href="#r6">6</a>][<a href="#r10">10</a>].</p>

        <h2>Where this leaves us</h2>
        <p>The emerging stack looks familiar to anyone who watched language models mature: pretrain on the broadest physics-consistent archive available, specialize with modest data, evaluate on tasks that matter, and publish the checkpoints. Climate research becomes more accessible when that stack is open, cited, and usable outside a handful of forecasting centers.</p>
''',
    "refs": [
        '<span id="r1"></span>Nguyen, T., Brandstetter, J., Kapoor, A., Gupta, J. K., & Grover, A. (2023). ClimaX: A foundation model for weather and climate. <em>ICML</em>. <a href="https://arxiv.org/abs/2301.10343">arXiv:2301.10343</a>',
        '<span id="r2"></span>Lam, R., et al. (2023). Learning skillful medium-range global weather forecasting. <em>Science</em>. <a href="https://www.science.org/doi/10.1126/science.adi2336">doi:10.1126/science.adi2336</a>',
        '<span id="r3"></span>Bi, K., et al. (2023). Accurate medium-range global weather forecasting with 3D neural networks. <em>Nature</em>. <a href="https://www.nature.com/articles/s41586-023-06185-3">doi:10.1038/s41586-023-06185-3</a>',
        '<span id="r4"></span>Feldmann, M., Beucler, T., Gomez, M., et al. (2024). Lightning-fast convective outlooks: Predicting severe convective environments with global AI-based weather models. <em>Geophysical Research Letters</em>. <a href="https://doi.org/10.1029/2024GL110960">doi:10.1029/2024GL110960</a>',
        '<span id="r5"></span>Bodnar, C., Bruinsma, W. P., Lucic, A., et al. (2025). A foundation model for the Earth system. <em>Nature</em>. <a href="https://doi.org/10.1038/s41586-025-09005-y">doi:10.1038/s41586-025-09005-y</a> (Microsoft Research).',
        '<span id="r6"></span>Rackow, T., Koldunov, N., Lessig, C., et al. (2024). Robustness of AI-based weather forecasts in a changing climate. <a href="https://arxiv.org/abs/2409.18529">arXiv:2409.18529</a> (ECMWF / AWI).',
        '<span id="r7"></span>Lopez-Gomez, I., Wan, Z. Y., Zepeda-Núñez, L., et al. (2025). Dynamical-generative downscaling of climate model ensembles. <em>PNAS</em>. <a href="https://doi.org/10.1073/pnas.2420288122">doi:10.1073/pnas.2420288122</a> (Google Research; Tapio Schneider, Caltech).',
        '<span id="r8"></span>Christopoulos, C., Lopez-Gomez, I., Beucler, T., et al. (2024). Online learning of entrainment closures for hybrid ML parameterization. <em>Journal of Advances in Modeling Earth Systems</em>. <a href="https://doi.org/10.1029/2024MS004485">doi:10.1029/2024MS004485</a> (Caltech CliMA).',
        ref_fourcastnet(9),
        ref_weatherbench2(10),
        ref_era5(11),
        ref_aifs(12),
        ref_jevons(13),
        ref_rebound_review(14),
    ],
})

# 3 Aerospace
POSTS.append({
    "slug": "aerospace-satellites",
    "num": "03",
    "sector": "Aerospace & Satellites",
    "viz_key": "aerospace",
    "card_title": "Earth observation is becoming a foundation-model stack",
    "card_blurb": "Berkeley Panopticon, Carbon-I, and large-scale pretraining make satellite analysis transfer across missions.",
    "meta": "Research note · August 1, 2026 · Sector 03 · Shryas Bhurat",
    "title": "Earth observation is becoming a foundation-model stack",
    "dek": "One backbone, many sensors. A faster path from pixels to climate metrics.",
    "description": "Emerging aerospace and satellite Earth observation foundation models, with university citations.",
    "body": '''
        <div class="callout callout-plain">
          <p><strong>In plain terms.</strong> Satellites produce huge image streams. New AI models train once on many sensor types, then adapt to floods, crops, or emissions with far less hand labeling.</p>
        </div>
        <p>Aerospace climate research used to mean flying instruments and writing task-specific classifiers for each sensor. That work remains essential. The new layer is sensor-agnostic representation learning: models pretrained across optical, SAR, and atmospheric products that can be adapted to flood mapping, crop monitoring, or land-cover change with far less labeled data.</p>
        <p>For accessibility, this matters as much as launch cadence. A municipality does not need a custom deep-learning team for every Sentinel product if a strong pretrained encoder already understands multi-spectral structure.</p>

        <h2>From fixed-sensor models to any-sensor models</h2>
        <p>Most early remote-sensing foundation models were locked to one constellation or band set. The field is now pivoting to models that accept arbitrary channel combinations.</p>
        <p><a href="https://arxiv.org/abs/2503.10845">Panopticon</a> (Waldmann et al.), from UC Berkeley and the Technical University of Munich, extends DINOv2 for Earth observation. It treats co-located multi-sensor views as natural augmentations, subsamples spectral channels during training, and uses cross-attention over channels so the model can embed optical and SAR inputs with wavelength and mode metadata [<a href="#r1">1</a>]. On GEO-Bench it reports strong results on Sentinel-1 and Sentinel-2 while remaining usable on unusual sensor configurations. That is the aerospace analogue of a generalist policy: one backbone, many instruments.</p>

        <h2>Scale pretraining on public satellite archives</h2>
        <h3>SkySense and SkySense++</h3>
        <p><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Guo_SkySense_A_Multi-Modal_Remote_Sensing_Foundation_Model_Towards_Universal_Interpretation_CVPR_2024_paper.pdf">SkySense</a> pretrained a billion-scale multi-modal spatiotemporal encoder on 21.5 million temporal sequences of optical and SAR data, using multi-granularity contrastive learning and geo-context prototypes [<a href="#r2">2</a>]. The follow-on <a href="https://www.nature.com/articles/s42256-025-01078-8">SkySense++</a> work in <em>Nature Machine Intelligence</em> adds progressive representation- and semantic-enhanced pretraining on about 27 million multi-modal images, improving few-shot performance across agriculture, forestry, oceanography, atmosphere, biology, land surveying, and disaster management [<a href="#r3">3</a>]. Few-shot skill is the accessibility lever: rapid flood response cannot wait for a million new labels.</p>

        <h3>NASA–IBM Prithvi and Copernicus-scale models</h3>
        <p><a href="https://arxiv.org/abs/2412.02732">Prithvi-EO-2.0</a>, trained on 4.2 million global HLS time-series samples from NASA Landsat–Sentinel archives, adds explicit temporal and location embeddings. The 600M variant improves over prior Prithvi checkpoints across GEO-Bench-style evaluations and is released openly for downstream use [<a href="#r4">4</a>]. In parallel, <a href="https://arxiv.org/abs/2503.11849">Copernicus-FM</a> targets unified modeling across Sentinel missions with 18.7 million aligned observations and dynamic hypernetworks that ingest spectral and non-spectral modalities plus metadata [<a href="#r5">5</a>].</p>

        <h2>Mission science: Carbon-I and observation continuity</h2>
        <p>Foundation models interpret archives. New missions define what enters those archives. <a href="https://carbon-i.github.io/">Carbon-I</a>, a Caltech-led NASA Earth System Explorer finalist with Bethany Ehlmann among the collaborators, would map CO<sub>2</sub>, CH<sub>4</sub>, and CO at roughly 300 m globally with roughly 30 m resolution over priority targets, closing tropical greenhouse-gas observation gaps that limit attribution of emissions to sources [<a href="#r7">7</a>]. That sensor layer complements Berkeley-style any-sensor encoders: one supplies trace-gas structure at scale, the other supplies transferable visual representations.</p>
        <p>Continuity planning matters as much as any single mission. Waliser and the KISS Continuity Study Team outline a U.S. framework for continuity of satellite observations so climate records remain comparable across instrument generations [<a href="#r8">8</a>]. Accessible aerospace research therefore spans pretrained models, flagship trace-gas missions, and governance for long-term records.</p>

        <h2>What universities are contributing</h2>
        <p>Berkeley's work on Panopticon sits inside a broader campus effort on environmental data systems and open geospatial ML. Caltech's Carbon-I team connects instrument design to emissions accounting. Stanford's aerospace and Earth observation communities connect satellite products to climate risk, land use, and sustainability applications through the Doerr School. Across surveys of remote-sensing foundation models, the consensus is clear: the bottleneck is no longer collecting pixels. It is learning representations that transfer across sensors, seasons, and geographies [<a href="#r6">6</a>].</p>
        <div class="callout">
          <p>Lower-cost smallsat constellations expand coverage. Foundation models expand who can interpret that coverage. Both are required for climate research that reaches beyond specialist agencies.</p>
        </div>

        <h2>Where this leaves us</h2>
        <p>The emerging aerospace research stack is a public satellite archive, a sensor-flexible foundation model, and a thin task head. That is how Earth observation becomes accessible climate infrastructure rather than a sequence of one-off image-processing projects.</p>
''',
    "refs": [
        '<span id="r1"></span>Waldmann, L., Shah, A., Wang, Y., et al. (2025). Panopticon: Advancing any-sensor foundation models for Earth observation. <em>CVPR Workshops</em>. <a href="https://arxiv.org/abs/2503.10845">arXiv:2503.10845</a> (UC Berkeley &amp; TUM).',
        '<span id="r2"></span>Guo, X., et al. (2024). SkySense: A multi-modal remote sensing foundation model towards universal interpretation for Earth observation imagery. <em>CVPR</em>.',
        '<span id="r3"></span>Wu, K., Zhang, Y., Ru, L., et al. (2025). A semantic-enhanced multi-modal remote sensing foundation model for Earth observation. <em>Nature Machine Intelligence</em>. <a href="https://doi.org/10.1038/s42256-025-01078-8">doi:10.1038/s42256-025-01078-8</a>',
        '<span id="r4"></span>Szwarcman, D., et al. (2024). Prithvi-EO-2.0: A versatile multi-temporal foundation model for Earth observation applications. <a href="https://arxiv.org/abs/2412.02732">arXiv:2412.02732</a>',
        '<span id="r5"></span>Wang, Y., et al. (2025). Towards a unified Copernicus foundation model for Earth vision. <a href="https://arxiv.org/abs/2503.11849">arXiv:2503.11849</a>',
        '<span id="r6"></span>Lu, S., et al. (2024). Foundation models for remote sensing and Earth observation: A survey. <a href="https://arxiv.org/abs/2410.16602">arXiv:2410.16602</a>',
        '<span id="r7"></span>Carbon-I mission (Caltech-led NASA Earth System Explorer finalist; Bethany Ehlmann among collaborators). <a href="https://carbon-i.github.io/">carbon-i.github.io</a>; <a href="https://www.caltech.edu/about/news/caltech-led-mission-to-map-greenhouse-gas-emissions-named-finalist-by-nasa">Caltech news</a>',
        '<span id="r8"></span>Waliser, D. E., &amp; KISS Continuity Study Team (2024). Toward a US framework for continuity of satellite observations of Earth\'s changing climate. <em>Earth\'s Future</em>. <a href="https://doi.org/10.1029/2023EF003757">doi:10.1029/2023EF003757</a>',
        ref_jevons(9),
        ref_rebound_review(10),
    ],
})

# 4 Materials
POSTS.append({
    "slug": "materials",
    "num": "04",
    "sector": "Materials",
    "viz_key": "materials",
    "card_title": "Cement chemistry is becoming a climate lever",
    "card_blurb": "Stanford, Berkeley, and Caltech work shows materials science is now a direct climate tool.",
    "meta": "Research note · August 1, 2026 · Sector 04 · Shryas Bhurat",
    "title": "Cement chemistry is becoming a climate lever",
    "dek": "Labs are attacking binders, kilns, and abatement costs together.",
    "description": "Emerging low-carbon materials research from Stanford, Berkeley, and related labs.",
    "body": '''
        <div class="callout callout-plain">
          <p><strong>In plain terms.</strong> Cement releases CO<sub>2</sub> when limestone is heated, not only from fuel. Researchers are testing new rock recipes, recycled concrete, and solar-driven chemistry to shrink that footprint.</p>
        </div>
        <p>Concrete is the world's most-used building material. Cement production alone accounts for roughly 8% of global CO<sub>2</sub> emissions, much of it from limestone calcination rather than fuel burn [<a href="#r7">7</a>]. That chemistry constraint is why incremental kiln efficiency is not enough, and why materials research has become central to climate strategy.</p>
        <p>The emerging technologies worth watching are not marketing labels. They are process inventions that remove carbonate feedstock, recycle existing concrete, or quantify which substitutions actually scale.</p>

        <h2>Replacing limestone chemistry</h2>
        <p>At Stanford, Vanorio et al. have pursued clinker routes inspired by volcanic and hydrothermal systems. Their <strong>Phlego</strong> cement concept replaces carbonate-heavy limestone pathways with carbonate-free igneous rock blends, targeting large emissions cuts while remaining compatible with existing cement infrastructure [<a href="#r1">1</a>][<a href="#r2">2</a>]. Reported project targets include emissions reductions on the order of three-quarters and production-cost reductions around one-fifth, alongside in situ fiber entanglement that improves ductility.</p>
        <p>That combination matters. A low-carbon binder that requires an entirely new construction ecosystem rarely leaves the lab. A binder that drops into existing kilns and standards has a path to use.</p>

        <h2>Circular concrete and co-product carbon</h2>
        <p>Yi Cui's group at Stanford has worked on electromagnetic induction processes that convert waste concrete back into high-performance clinker using renewable electricity, aiming to cut both virgin limestone demand and process emissions [<a href="#r3">3</a>]. Separately, Stanford Sustainability Accelerator work on methane pyrolysis links low-emissions hydrogen to cement-grade solid carbon co-products designed for direct incorporation into cement matrices [<a href="#r4">4</a>]. The industrial logic is important: hydrogen scale-up often fails when the solid carbon has no market. Cement is a market large enough to absorb it.</p>

        <h2>Solar-driven catalytic materials at Caltech</h2>
        <p>Not all low-carbon materials research targets structural binders. The Liquid Sunlight Alliance at Caltech, with Harry Atwater and collaborators, develops photothermocatalytic reactors and selective solar absorbers that couple sunlight to fuel chemistry. Su et al. report integrated reactor designs that concentrate solar flux and drive catalytic conversion of CO<sub>2</sub> and water toward industrial feedstocks [<a href="#r6">6</a>]. The materials story is dual: engineered absorbers and catalyst supports that survive high flux, plus the catalytic systems that turn sunlight and CO<sub>2</sub> into storable molecules rather than only electricity.</p>

        <h2>Berkeley's systems view: which alternatives are worth buying</h2>
        <p>UC Berkeley's Center for the Built Environment has focused on cost-effectiveness and mitigation potential for low-carbon building material alternatives in California, including marginal abatement cost curves for material efficiency, reuse, and substitution [<a href="#r5">5</a>]. This is the research layer practitioners actually need: not only "is the material greener," but "at what cost, with which supply-chain constraints, and with what constructability penalty."</p>
        <div class="callout">
          <p>Accessible climate research in materials means open performance data, transparent LCA assumptions, and abatement curves that policymakers and contractors can act on.</p>
        </div>

        <h2>Where this leaves us</h2>
        <p>The frontier is a portfolio: geology-inspired clinker, electrified recycling, carbon co-product utilization, Caltech solar-fuel catalytic materials, and rigorous abatement analytics. Stanford, Berkeley, and Caltech are not chasing novelty for its own sake. They are trying to make the default building material and feedstock supply less carbon-intensive without making construction or chemistry unaffordable or unbuildable.</p>
''',
    "refs": [
        '<span id="r1"></span>Stanford Doerr School of Sustainability. For a low-carbon cement recipe, Stanford scientists look to Earth\'s cauldrons. <a href="https://sustainability.stanford.edu/news/low-carbon-cement-recipe-stanford-scientists-look-earths-cauldrons">sustainability.stanford.edu</a>',
        '<span id="r2"></span>Vanorio, T., Cargnello, M., Salleo, A. Phlego cement: sustainable innovation, seamless integration. Stanford Sustainability Accelerator. <a href="https://sustainability-accelerator.stanford.edu/phlego-cement-sustainable-innovation-seamless-integration">Project page</a>',
        '<span id="r3"></span>Cui, Y., Zheng, Q., Bhatia, M. Reinventing Cement. Stanford Office of Technology Licensing / HIT Fund. <a href="https://otl.stanford.edu/researchers/high-impact-technology-hit-fund/hit-portfolio">OTL portfolio</a>',
        '<span id="r4"></span>Cargnello, M., Moise, H. Low-emissions hydrogen and low-cost performance cement via methane pyrolysis. Stanford Sustainability Accelerator.',
        '<span id="r5"></span>UC Berkeley Center for the Built Environment. Cost-Effectiveness and Mitigation Potential of Low-Carbon Building Material Alternatives. <a href="https://cbe.berkeley.edu/research/low-carbon-building-material-alternatives/">cbe.berkeley.edu</a>',
        '<span id="r6"></span>Su, M. P., Aitbekova, A., Salazar, M., et al. (2024). Photothermocatalytic reactor and selective solar absorbers for sustainable fuels. <em>Device</em>. <a href="https://doi.org/10.1016/j.device.2024.100604">doi:10.1016/j.device.2024.100604</a>; Caltech news. <a href="https://www.caltech.edu/about/news/harnessing-sunlight-to-make-sustainable-fuels">caltech.edu</a>',
        ref_iea_cement(7),
        ref_jevons(8),
        ref_rebound_review(9),
    ],
})

# 5 Energy
POSTS.append({
    "slug": "energy-systems",
    "num": "05",
    "sector": "Energy Systems",
    "viz_key": "energy",
    "card_title": "Long-duration storage decides clean-grid reliability",
    "card_blurb": "Grid models show when multi-day storage earns its keep alongside short-duration batteries.",
    "meta": "Research note · August 1, 2026 · Sector 05 · Shryas Bhurat",
    "title": "Long-duration storage decides clean-grid reliability",
    "dek": "Cheap renewables won the electron race. Multi-day balance is next.",
    "description": "Emerging energy systems research on long-duration storage and clean grids, with university and national-lab citations.",
    "body": '''
        <div class="callout callout-plain">
          <p><strong>In plain terms.</strong> Batteries that last a few hours cover evening peaks. Multi-day storage fills the gaps when wind and sun dip for days or weeks. Grid models now spell out when each layer pays for itself.</p>
        </div>
        <p>Variable renewables have won the cheap-electron contest in many regions [<a href="#r6">6</a>]. Staadecker et al. and other capacity-expansion models now quantify when multi-day storage becomes valuable and which firm resources reduce total system cost [<a href="#r1">1</a>][<a href="#r2">2</a>].</p>
        <p>University capacity-expansion models are doing the unglamorous work of answering those questions with geographic detail rather than slogans.</p>

        <h2>What grid models now show about LDES</h2>
        <p>Staadecker et al. use the SWITCH model on a zero-emissions Western Interconnect and find that long-duration energy storage (LDES) is especially valuable in wind-heavy regions and places losing hydropower. Seasonal storage becomes cost-effective if capital costs fall below about $5/kWh, and large LDES mandates can cut prices in high-demand hours dramatically by reducing scarcity [<a href="#r1">1</a>]. Duration needs are not uniform: solar-dominant Southwest systems often want 6–10 hour assets, while wind-dominant systems lean toward 10–20 hours.</p>
        <p>Stanford work led with Sally Benson and colleagues examines multi-day to seasonal storage in transmission-constrained systems. When clean firm generation is limited, short-duration storage still delivers more energy in many cases, but LDES plays a distinct role as a dispatchable substitute. Their substitution-ratio framing is useful: one megawatt of LDES can carry system value comparable to many megawatts of renewables paired only with short-duration storage [<a href="#r2">2</a>].</p>

        <h2>California as a laboratory</h2>
        <p>Using the BRIDGES gas-electric capacity-expansion model for California's 2045 net-zero target, Stanford-linked research finds that all electric storage durations appear in the optimal portfolio, totaling on the order of 75 GW of power capacity by mid-century in studied scenarios. Lithium-ion supplies most short-run needs, while hydrogen power-to-gas-to-power dominates bulk energy capacity at roughly 4 TWh, still far below existing natural-gas storage volumes [<a href="#r3">3</a>].</p>
        <p>Complementary Stanford geothermal work shows enhanced geothermal systems (EGS) can act as clean firm power, reducing required solar, battery, and power-to-gas buildout when deep resources are available [<a href="#r4">4</a>]. Storage and firm clean generation are complements, not rivals.</p>

        <h2>Caltech: batteries beyond lithium and campus-scale grids</h2>
        <p>At the Resnick Sustainability Institute, Kimberly See and colleagues study sustainable battery chemistries that reduce reliance on scarce lithium-ion materials, a research line highlighted in Resnick Watson lectures and RSI programming. Chemistry that scales without critical-mineral bottlenecks is as much an energy-systems question as megawatt-scale storage duration.</p>
        <p>Caltech also partners with Pasadena Water and Power on smart-grid solutions for California renewables, and runs campus storage and microgrid research that tests control and integration in a real utility footprint [<a href="#r5">5</a>]. That local laboratory complements Western Interconnect expansion models: it shows how distribution-level assets behave when renewable penetration rises.</p>
        <div class="callout">
          <p>Accessible energy research means publishing the model assumptions, open inputs, and substitution metrics so planners outside elite labs can test their own grids.</p>
        </div>

        <h2>Where this leaves us</h2>
        <p>The emerging technology set is broader than batteries: LDES chemistries and mechanical systems, hydrogen storage in existing gas infrastructure, firm resources such as EGS, and next-generation electrochemistry from Caltech. Stanford, Berkeley, and Caltech research is clarifying the conditions under which each earns a place on a real transmission map and in local grids.</p>
''',
    "refs": [
        '<span id="r1"></span>Staadecker, M., Szinai, J., Sánchez-Pérez, P. A., et al. (2024). The value of long-duration energy storage under various grid conditions in a zero-emissions future. <em>Nature Communications</em>. <a href="https://doi.org/10.1038/s41467-024-53274-6">doi:10.1038/s41467-024-53274-6</a> (UCSD, LBNL, NREL, UC Merced).',
        '<span id="r2"></span>Chu, A., Baik, E., Benson, S. M. (2024). Long-duration energy storage in transmission-constrained variable renewable energy systems. <em>Cell Reports Sustainability</em>. <a href="https://doi.org/10.1016/j.crsus.2024.100285">doi:10.1016/j.crsus.2024.100285</a> (Stanford).',
        '<span id="r3"></span>Energy storage in combined gas-electric energy transitions models: The case of California. BRIDGES model results summarized via OSTI. <a href="https://www.osti.gov/biblio/2562162">OSTI 2562162</a>',
        '<span id="r4"></span>Aljubran, M. J., et al. (2025). Enhanced Geothermal Systems for Reliable Decarbonization of the California Energy Grid. Stanford Geothermal Workshop. <a href="https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Aljubran.pdf">PDF</a>',
        '<span id="r5"></span>Smart grid solutions for California renewables (Caltech and Pasadena Water and Power). <a href="https://www.caltech.edu/about/news/smart-grid-solutions-california-renewables">caltech.edu</a>; Resnick Sustainability Institute, Kimberly See, sustainable battery chemistries (Watson lecture / RSI).',
        ref_irena_battery(6),
        ref_jevons(7),
        ref_rebound_review(8),
    ],
})

# 6 Manufacturing
POSTS.append({
    "slug": "manufacturing",
    "num": "06",
    "sector": "Manufacturing",
    "viz_key": "manufacturing",
    "card_title": "Factories are becoming a climate design space",
    "card_blurb": "NSF and university work on electrification and factory data make manufacturing a climate research domain.",
    "meta": "Research note · August 1, 2026 · Sector 06 · Shryas Bhurat",
    "title": "Factories are becoming a climate design space",
    "dek": "Electrified heat, process data, and cost models turn plants into abatement platforms.",
    "description": "Emerging green manufacturing and industrial electrification research from leading universities.",
    "body": '''
        <div class="callout callout-plain">
          <p><strong>In plain terms.</strong> Factories emit heavily because they burn fuel for high-temperature heat. Researchers are swapping flames for electric and solar reactors, and publishing cost curves so plants know what clears a carbon price.</p>
        </div>
        <p>Manufacturing sits at the intersection of materials, energy, and process control. The emerging research agenda treats decarbonization as an advanced-manufacturing problem: replace inefficient unit operations, electrify heat, redesign products so they need less energy in use, and measure abatement costs with the same rigor used for financial capital budgeting.</p>

        <h2>Four pillars, one manufacturing lens</h2>
        <p>An NSF workshop report on advanced manufacturing for industrial decarbonization organizes the field into energy efficiency, industrial electrification, low-carbon fuels and feedstocks, and carbon capture, utilization, and storage [<a href="#r1">1</a>]. The important contribution is not the taxonomy. It is the insistence that manufacturing research and techno-economic analysis must be co-designed. A beautiful reactor that never clears a factory's hurdle rate is not climate infrastructure.</p>

        <h2>Electrified process heat enters the factory</h2>
        <p>Stanford engineers led by Fan et al. have demonstrated a compact thermochemical reactor that uses high-efficiency power electronics and inductively heated ceramic metamaterial lattices to deliver industrial-grade heat without combustion [<a href="#r2">2</a>]. Because catalysts can sit inside the lattice voids, heat transfer improves and reactors can shrink relative to furnace baselines. Jacobson et al. show that firebrick thermal storage can store renewable electricity as high-temperature heat for cement, steel, glass, and paper processes at a small fraction of battery cost per thermal kilowatt-hour [<a href="#r3">3</a>].</p>
        <p>Berkeley research on off-grid renewable heat with thermal storage and heat pumps estimates that local renewable configurations could economically supply on the order of one-third of U.S. industrial heat demand by 2035 under studied scenarios, with especially strong near-term economics for mid- and high-temperature thermal electric storage [<a href="#r4">4</a>].</p>

        <h2>Solar-thermal process chemistry at Caltech</h2>
        <p>Caltech's Liquid Sunlight Alliance, led by Harry Atwater, demonstrates a solar-thermal reactor that drives ethylene oligomerization without fossil process heat, an emerging manufacturing route toward sustainable fuels and chemical feedstocks [<a href="#r6">6</a>]. The process substitutes concentrated sunlight for combustion heat in a unit operation that normally sits deep in petrochemical value chains. That is advanced manufacturing in the decarbonization sense: new heat source, same downstream chemistry, public performance data from a university-led alliance.</p>

        <h2>Making abatement decisions legible</h2>
        <p>Stanford GSB research by Glenk, Meier, and Reichelstein develops abatement-cost curves for industrial firms, calibrated on European cement producers under the EU ETS. At roughly €85/tCO<sub>2</sub>, firms optimally cut about one-third of direct emissions; willingness to abate rises sharply above €100/t [<a href="#r5">5</a>]. This is manufacturing research in the managerial sense: it tells operators which process changes clear the carbon-price hurdle.</p>
        <div class="callout">
          <p>Accessible manufacturing climate research publishes both the process invention and the cost curve. Factories adopt what they can underwrite.</p>
        </div>

        <h2>Where this leaves us</h2>
        <p>The emerging manufacturing stack pairs electrified heat hardware, thermal storage, solar-thermal fuel chemistry from Caltech, process substitution, and decision tools for abatement sequencing. Stanford, Berkeley, Caltech, and NSF-convened manufacturing communities are building that stack in public.</p>
''',
    "refs": [
        '<span id="r1"></span>Wang, Y., et al. (2024). Report-out from an NSF Workshop on Advanced Manufacturing for Industrial Decarbonization. <em>Green Manufacturing Open</em>. <a href="https://www.oaepublish.com/articles/gmo.2024.121801">Article</a>',
        '<span id="r2"></span>Fan, J., Rivas-Davila, J., Kanan, M., et al. (2024). Electric reactor could cut industrial emissions. Stanford Report / <em>Joule</em>. <a href="https://news.stanford.edu/stories/2024/08/electric-reactor-could-cut-industrial-emissions">stanford.edu</a>',
        '<span id="r3"></span>Jacobson, M. Z., Sambor, D. J., et al. (2024). Effects of firebricks for industrial process heat... <em>PNAS Nexus</em>. <a href="https://web.stanford.edu/group/efmh/jacobson/Articles/Others/24-Firebricks.pdf">PDF</a>',
        '<span id="r4"></span>UC Berkeley Goldman School working paper (2025 draft). Integrating renewable energy with industrial heat demand. <a href="https://gspp.berkeley.edu/archived/files/page/Integrating_Renewable_Energy_with_Industrial_Heat_Demand_-_V20251212.pdf">PDF</a>',
        '<span id="r5"></span>Glenk, G., Meier, R., Reichelstein, S. J. (2024). Assessing the Costs of Industrial Decarbonization. Stanford GSB Working Paper 4202. <a href="https://www.gsb.stanford.edu/faculty-research/working-papers/assessing-costs-industrial-decarbonization">gsb.stanford.edu</a>',
        '<span id="r6"></span>Su, M. P., Aitbekova, A., Salazar, M., et al. (2024). Photothermocatalytic reactor and selective solar absorbers for sustainable fuels. <em>Device</em>. <a href="https://doi.org/10.1016/j.device.2024.100604">doi:10.1016/j.device.2024.100604</a>; <a href="https://www.caltech.edu/about/news/harnessing-sunlight-to-make-sustainable-fuels">caltech.edu</a>',
        ref_jevons(7),
        ref_rebound_review(8),
    ],
})

# 7 Built environment
POSTS.append({
    "slug": "built-environment",
    "num": "07",
    "sector": "Built Environment",
    "viz_key": "built",
    "card_title": "Whole-life carbon is the new building metric",
    "card_blurb": "Whole-life assessment shows embodied carbon rivaling operations as grids decarbonize.",
    "meta": "Research note · August 1, 2026 · Sector 07 · Shryas Bhurat",
    "title": "Whole-life carbon is the new building metric",
    "dek": "As grids clean up, embodied carbon in structure and materials takes center stage.",
    "description": "Emerging built environment research on whole-life and embodied carbon from Stanford and related labs.",
    "body": '''
        <div class="callout callout-plain">
          <p><strong>In plain terms.</strong> Buildings used to be judged mainly on energy bills. As grids get cleaner, the carbon in steel, concrete, and interiors often matters just as much over a building's life.</p>
        </div>
        <p>Building climate research spent decades optimizing operational energy. That work succeeded enough to change the problem. In many new projects, embodied carbon from materials and construction is now comparable to, or larger than, lifetime operational carbon, especially on cleaner grids.</p>

        <h2>Measuring the whole life of a building</h2>
        <p>A 2025 whole-life carbon assessment of thirty California buildings finds whole-life intensities spanning roughly 232–2,230 kgCO<sub>2</sub>e/m<sup>2</sup>, with median embodied, operational, and whole-life intensities around 385, 228, and 734 kgCO<sub>2</sub>e/m<sup>2</sup> respectively [<a href="#r1">1</a>]. Modules A1–A3, structural systems, and concrete/metals dominate embodied totals. Interiors are not negligible. Method choices around grid decarbonization pathways and floor-area normalization materially change results, which is why open methods matter.</p>

        <h2>Industrialized construction and design tools</h2>
        <p>Stanford's Center for Integrated Facility Engineering (CIFE) is building data-driven methods to evaluate architectural, financial, and decarbonization tradeoffs in industrialized construction [<a href="#r2">2</a>]. The hypothesis is straightforward: if components are manufactured in repeatable factories, embodied-carbon analysis can be standardized and automated instead of rebuilt as a bespoke LCA on every project. Related CIFE work on existing-building retrofits emphasizes the tradeoff between operational savings and the embodied carbon of retrofit materials under different state grid trajectories [<a href="#r3">3</a>].</p>

        <h2>Campus-scale demonstration: Caltech Resnick Sustainability Center</h2>
        <p>Stanford CIFE and Berkeley-linked building research supply methods and abatement analytics. Caltech adds a campus-scale demonstration: the Resnick Sustainability Center is designed as a living lab with a mass timber frame to lower embodied carbon, a LEED Platinum track, and rooftop photovoltaics [<a href="#r5">5</a>]. The project makes whole-life carbon choices visible on a flagship building rather than only in spreadsheets. That is accessible built-environment research in architectural form: low-embodied-carbon structure, operational renewables, and a public case study on a dense academic site.</p>

        <h2>National pathways, local decisions</h2>
        <p>Broader U.S. pathway studies, including Carbon Leadership Forum collaborations, show that only aggressive combinations of material efficiency, low-carbon materials, and industrial decarbonization approach 1.5°C-aligned embodied-carbon trajectories by mid-century [<a href="#r4">4</a>]. University research connects that national gap to project-level instruments: EPDs, whole-life standards such as ASHRAE/ICC 240P, and procurement rules that reward verified reductions.</p>
        <div class="callout">
          <p>Accessible built-environment research gives designers a whole-life number they can trust early, when geometry and material choices are still cheap to change.</p>
        </div>

        <h2>Where this leaves us</h2>
        <p>The emerging toolkit is whole-life assessment, industrialized low-carbon assemblies, retrofit analysis that counts embodied carbon, and campus demonstrations such as Caltech's Resnick Center. Stanford and Berkeley-linked building research is pushing those tools from specialist LCA consultants into ordinary design workflows, with Caltech showing how they read on a major new structure.</p>
''',
    "refs": [
        '<span id="r1"></span>Shen, Y., et al. (2025). A novel whole-life carbon assessment of thirty buildings in California. <em>Journal of Building Engineering</em>. <a href="https://doi.org/10.1016/j.jobe.2025.113074">doi:10.1016/j.jobe.2025.113074</a>',
        '<span id="r2"></span>Stanford CIFE. A data-driven evaluation method for architectural, financial and building decarbonization tradeoffs in industrialized construction. <a href="https://cife.stanford.edu/data-driven-evaluation-method-architectural-financial-and-building-decarbonization-tradeoffs">cife.stanford.edu</a>',
        '<span id="r3"></span>Stanford CIFE. Reduction of operational carbon in existing buildings through energy efficiency. <a href="https://cife.stanford.edu/reduction-operational-carbon-existing-buildings-through-energy-efficiency">cife.stanford.edu</a>',
        '<span id="r4"></span>Ashtiani, M., et al. (2025). Embodied Carbon Pathways to 2050 for the United States. Carbon Leadership Forum / RMI / UW Life Cycle Lab. <a href="https://carbonleadershipforum.org/embodied-carbon-pathways-to-2050-for-the-united-states/">carbonleadershipforum.org</a>',
        '<span id="r5"></span>Resnick Sustainability Center highlights campus-wide focus on pressing global issues (mass timber, LEED Platinum track, rooftop PV). <a href="https://www.caltech.edu/about/news/resnick-sustainability-center-highlights-campus-wide-focus-on-pressing-global-issues">caltech.edu</a>',
        ref_ashrae_240p(6),
        ref_jevons(7),
        ref_rebound_review(8),
    ],
})

# 8 Mobility
POSTS.append({
    "slug": "mobility",
    "num": "08",
    "sector": "Mobility",
    "viz_key": "mobility",
    "card_title": "EVs scale on finance and charger uptime",
    "card_blurb": "Wharton, Harvard, and Caltech research show loans and uptime constrain electric mobility.",
    "meta": "Research note · August 1, 2026 · Sector 08 · Shryas Bhurat",
    "title": "EVs scale on finance and charger uptime",
    "dek": "Packs get the headlines. Credit terms and broken chargers shape adoption.",
    "description": "Emerging mobility research from Wharton and Harvard on EV finance and charging infrastructure.",
    "body": '''
        <div class="callout callout-plain">
          <p><strong>In plain terms.</strong> Electric cars improve every year, but buyers still face stricter loans and chargers that fail too often. Fixing finance and uptime may matter as much as battery chemistry for mass adoption.</p>
        </div>
        <p>Electric mobility research often starts with energy density, charging speed, and vehicle cost. Those remain first-order. Wharton and Harvard work adds two less visible constraints that determine whether climate-aligned transport actually reaches households: financing terms and charger reliability.</p>

        <h2>The EV financing gap</h2>
        <p>Research by Bena, Bian, and Tang, <em>Financing the Global Shift to Electric Mobility</em>, finds that early-stage EVs receive tighter loan terms than comparable internal-combustion vehicles: higher interest rates, lower loan-to-value ratios, and shorter durations [<a href="#r1">1</a>][<a href="#r2">2</a>]. The dominant mechanism is technological obsolescence risk. Rapid battery and powertrain innovation lowers expected resale values, which raises collateral risk for lenders. Buyer demographics, lender market power, and macro conditions explain little of the spread once technology risk is accounted for.</p>
        <p>That result reframes climate policy. Purchase subsidies address sticker price. They do not automatically repair the credit spread created by uncertain residual values. Accessible mobility research therefore includes open measurement of residual-value risk and financing products designed for transition technologies.</p>

        <h2>Charging as infrastructure, not amenity</h2>
        <p>Harvard Business School-linked research led by Omar Asensio analyzes on the order of one million consumer charging reviews and estimates U.S. public charging reliability around 78% [<a href="#r3">3</a>]. One in five attempts failing is not a niche UX complaint. It is a system reliability problem that shapes vehicle demand and the credibility of emissions targets. Pricing fragmentation compounds the issue: drivers face inconsistent tariffs with limited transparency.</p>
        <p>Policy follow-ups from the same research community emphasize that no single private actor is fully incentivized to build and maintain a national network at climate-relevant speed [<a href="#r4">4</a>]. Reliability data, maintenance accountability, and targeted public finance become research outputs as important as new connector standards.</p>

        <h2>Caltech Adaptive Charging Network</h2>
        <p>Lee et al. and Steven Low at Caltech built the Adaptive Charging Network (ACN) to study oversubscribed charging infrastructure: more vehicles than ports, limited campus power, and the need for fair, grid-aware schedules. The system uses model predictive control for charging allocation and publishes open research through ACN-Data and ACN-Sim, with technology transfer via PowerFlex [<a href="#r5">5</a>][<a href="#r6">6</a>]. This is mobility research at the intersection of algorithms and hardware: not how fast one car charges, but how a fleet shares constrained capacity without blackouts or arbitrary queuing.</p>
        <p>Wharton and Harvard document financing and public reliability frictions. Caltech documents how to operate dense charging when demand exceeds installed capacity. Together they describe why EV scale-up is a systems problem.</p>
        <div class="callout">
          <p>Emerging mobility technology is not only solid-state batteries. It is also credit models, reliability analytics, and grid-aware charging that make electrification usable.</p>
        </div>

        <h2>Where this leaves us</h2>
        <p>University research from Wharton, Harvard, and Caltech shows why EV transitions stall even when vehicle hardware improves: capital markets price obsolescence, public charging still fails too often, and shared infrastructure needs explicit scheduling under power limits. Climate research made accessible means publishing those frictions clearly enough for lenders, cities, and operators to fix them.</p>
''',
    "refs": [
        '<span id="r1"></span>Bena, J., Bian, B., Tang, H. (2023/2024). Financing the Global Shift to Electric Mobility. Wharton / SSRN. <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4526150">SSRN 4526150</a>',
        '<span id="r2"></span>Knowledge at Wharton. Why Are Electric Vehicle Loans More Expensive? <a href="https://knowledge.wharton.upenn.edu/article/why-are-electric-vehicle-loans-more-expensive/">knowledge.wharton.upenn.edu</a>',
        '<span id="r3"></span>Asensio, O. I., et al. Harvard Business School BiGS. The state of EV charging in America. <a href="https://www.hbs.edu/bigs/the-state-of-ev-charging-in-america">hbs.edu/bigs</a>',
        '<span id="r4"></span>Harvard BiGS. Can government fix the EV infrastructure gap? <a href="https://www.hbs.edu/bigs/can-government-fix-the-ev-infrastructure-gap">hbs.edu/bigs</a>',
        '<span id="r5"></span>Lee, Z. J., Low, S. H., et al. Adaptive Charging Network (ACN). <a href="https://arxiv.org/abs/2012.02636">arXiv:2012.02636</a> (Caltech).',
        '<span id="r6"></span>Caltech ACN portal (ACN-Data, ACN-Sim). <a href="https://ev.caltech.edu/">ev.caltech.edu</a>',
        ref_nevi(7),
        ref_irena_battery(8),
        ref_jevons(9),
        ref_rebound_review(10),
    ],
})

# 9 Industrial processes
POSTS.append({
    "slug": "industrial-processes",
    "num": "09",
    "sector": "Industrial Processes",
    "viz_key": "industrial",
    "card_title": "Hard-to-abate industry needs playbooks, not silver bullets",
    "card_blurb": "University playbooks and abatement curves turn industrial decarbonization into transferable methods.",
    "meta": "Research note · August 1, 2026 · Sector 09 · Shryas Bhurat",
    "title": "Hard-to-abate industry needs playbooks, not silver bullets",
    "dek": "Steel, cement, and chemicals need sequenced options with public cost evidence.",
    "description": "Emerging industrial process decarbonization research from Stanford, Berkeley, and related groups.",
    "body": '''
        <div class="callout callout-plain">
          <p><strong>In plain terms.</strong> Cement, steel, and chemicals cannot wait for one miracle technology. Labs are publishing step-by-step playbooks: cleaner heat, new inputs, and cost tools tied to real carbon prices.</p>
        </div>
        <p>Industrial process emissions are concentrated in a few sectors that are both economically essential and thermodynamically stubborn. The emerging research pattern from Stanford, Berkeley, and collaborating universities is to stop waiting for a single silver bullet and instead publish process pathways, heat options, and abatement costs that operators can compare. The Resnick Sustainability Institute at Caltech frames industrial and climate initiatives around the same principle: sequenced, measurable process change rather than undifferentiated ambition.</p>

        <h2>Solar-to-fuel industrial chemistry at Caltech</h2>
        <p>Caltech's Liquid Sunlight Alliance documents a solar-to-fuel pathway that converts CO<sub>2</sub> to ethylene and onward toward jet-fuel-range products using concentrated sunlight and integrated catalysis [<a href="#r7">7</a>]. That is industrial chemistry routed through renewables: feedstock carbon from the atmosphere, process heat from the sun, and products that slot into existing fuel infrastructure. It complements Stanford electrified reactors and Berkeley heat-storage studies by attacking hydrocarbon demand at the molecule level.</p>

        <h2>Translating campus research into industrial action</h2>
        <p>Stanford's Industrial Decarbonization Action Partnership / Industrial Futures Action Network focuses on iron, steel, and automotive supply chains precisely because academic papers often fail to reach plant decision-makers [<a href="#r1">1</a>]. The model is research plus curated insight databases plus direct engagement with firms and policymakers. That is an accessibility project as much as a technology project.</p>

        <h2>Heat is the binding constraint</h2>
        <p>Much of industry's climate problem is high-temperature heat. Stanford's electrified thermochemical reactor work shows a path to replace combustion with induction-heated metamaterial cores for chemical manufacturing [<a href="#r2">2</a>]. Jacobson and colleagues show that firebrick storage can supply a large share of industrial process heat in 100% renewable scenarios while cutting total system capital cost on the order of $1.27 trillion across 149 countries relative to a no-firebrick case [<a href="#r3">3</a>]. Berkeley working papers on local renewable heat with thermal storage estimate that roughly 34% of U.S. industrial heat demand could be economically addressable by 2035 in base-case trajectories [<a href="#r4">4</a>].</p>

        <h2>Cement as the proving ground for cost curves</h2>
        <p>Cement remains the canonical hard-to-abate case. Stanford materials work on Phlego and related low-carbon clinker routes attacks process CO<sub>2</sub> at the chemistry layer [<a href="#r5">5</a>]. Stanford GSB abatement-cost research converts those options into managerial choices under carbon pricing [<a href="#r6">6</a>]. When carbon prices cross clear thresholds, the optimal process mix changes sharply. Publishing those thresholds is how industrial climate research becomes usable outside academia.</p>
        <div class="callout">
          <p>Deep industrial research is not only a new kiln or reactor. It is a public playbook: technology options, heat supply, carbon price sensitivity, and supply-chain constraints in one place.</p>
        </div>

        <h2>Where this leaves us</h2>
        <p>The frontier technologies are electrified reactors, thermal storage, low-carbon binders, Caltech solar-to-fuel and CO<sub>2</sub>-to-ethylene routes, hydrogen-ready processes, and rigorous abatement analytics. Leading universities, including Caltech through Resnick, are beginning to package them as sector playbooks. That packaging is what makes industrial climate research accessible.</p>
''',
    "refs": [
        '<span id="r1"></span>Li, S., Saltzer, S., Azevedo, I., Karplus, V. Industrial decarbonization action partnership (IDAP) / Industrial Futures Action Network. Stanford Sustainability Accelerator. <a href="https://sustainability-accelerator.stanford.edu/project/industrial-decarbonization-action-partnership-idap">Project page</a>',
        '<span id="r2"></span>Fan, J., et al. (2024). Electric reactor could cut industrial emissions. <em>Joule</em> / Stanford Report. <a href="https://news.stanford.edu/stories/2024/08/electric-reactor-could-cut-industrial-emissions">stanford.edu</a>',
        '<span id="r3"></span>Jacobson, M. Z., et al. (2024). Effects of firebricks for industrial process heat... <em>PNAS Nexus</em>. <a href="https://doi.org/10.1093/pnasnexus/pgae223">doi:10.1093/pnasnexus/pgae223</a>',
        '<span id="r4"></span>UC Berkeley GSPP working paper draft (2025). Integrating renewable energy with industrial heat demand. <a href="https://gspp.berkeley.edu/archived/files/page/Integrating_Renewable_Energy_with_Industrial_Heat_Demand_-_V20251212.pdf">PDF</a>',
        '<span id="r5"></span>Stanford Sustainability Accelerator. Phlego cement. <a href="https://sustainability-accelerator.stanford.edu/phlego-cement-sustainable-innovation-seamless-integration">Project page</a>',
        '<span id="r6"></span>Glenk, G., Meier, R., Reichelstein, S. J. (2024). Assessing the Costs of Industrial Decarbonization. Stanford GSB Working Paper 4202.',
        '<span id="r7"></span>Su, M. P., Aitbekova, A., Salazar, M., et al. (2024). Photothermocatalytic reactor and selective solar absorbers for sustainable fuels. <em>Device</em>. <a href="https://doi.org/10.1016/j.device.2024.100604">doi:10.1016/j.device.2024.100604</a>; <a href="https://www.caltech.edu/about/news/harnessing-sunlight-to-make-sustainable-fuels">caltech.edu</a>; Resnick Sustainability Institute industrial and climate initiatives.',
        ref_jevons(8),
        ref_rebound_review(9),
    ],
})


def _extract_plain_callout(body: str) -> tuple[str, str]:
    marker = '<div class="callout callout-plain">'
    start = body.find(marker)
    if start == -1:
        raise ValueError("Missing plain-terms callout")
    end = body.find("</div>", start)
    if end == -1:
        raise ValueError("Unclosed callout div")
    end += len("</div>")
    callout = body[start:end].strip()
    rest = body[end:].strip()
    return callout, rest


def split_body(body: str) -> tuple[str, str, str, str]:
    """Return (callout_html, tech_overview_html, tech_detail_html, conclusion_html)."""
    body = body.strip()
    callout, rest = _extract_plain_callout(body)
    if LEAVES_US_MARKER not in rest:
        raise ValueError(f"Missing {LEAVES_US_MARKER}")
    detail_part, conclusion_part = rest.split(LEAVES_US_MARKER, 1)
    conclusion_part = conclusion_part.strip()
    detail_part = detail_part.strip()
    h2 = detail_part.find("<h2>")
    if h2 == -1:
        raise ValueError("Missing detail sections")
    tech_overview = detail_part[:h2].strip()
    tech_detail = detail_part[h2:].strip()
    # Keep main outline as H2; demote nested detail headings to H3.
    tech_detail = tech_detail.replace("<h2>", "<h3>").replace("</h2>", "</h3>")
    return callout, tech_overview, tech_detail, conclusion_part


def assemble_body(raw_body: str, slug: str, viz_key: str) -> str:
    callout, tech_overview, tech_detail, conclusion = split_body(raw_body)
    sets = VIZ_SETS.get(viz_key, {})
    hero = sets.get("hero", "")
    mid = sets.get("mid", "")
    loop = sets.get("loop", "")
    markets = build_markets_section(slug)
    timeline = sections_for_slug(slug)
    future = future_section_html(slug)
    return f"""
        <h2>Technology</h2>
        {callout}
{hero}
        {tech_overview}

{markets}
        <h2>Technology in detail</h2>
{mid}
        {tech_detail}

{timeline}
        <h2>Future impact</h2>
{loop}
{future}
        <h2>Conclusion</h2>
        {conclusion}
"""


def write_posts():
    cards = []
    for p in POSTS:
        viz_key = p.get("viz_key", "")
        body = assemble_body(p["body"], p["slug"], viz_key)
        slug = p["slug"]
        refs = (
            list(p["refs"])
            + CONSULTANT_REFS_BY_SLUG[slug]()
            + MARKET_MAP_REFS_BY_SLUG[slug]()
        )
        html = page(
            p["title"],
            p["description"],
            article(p["meta"], p["title"], p["dek"], body, refs, viz_html=""),
        )
        (ROOT / f"{p['slug']}.html").write_text(html, encoding="utf-8")
        cards.append(p)
        print("wrote", p["slug"])

    card_html = "\n".join(
        f'''        <a class="post-card" href="{p['slug']}.html">
          <p class="meta">{p['num']} · {p['sector']} · {AUTHOR}</p>
          <h2>{p['card_title']}</h2>
          <p>{p['card_blurb']}</p>
        </a>'''
        for p in cards
    )

    index = page(
        "Research notes",
        "Maiti Labs research notes on emerging technologies across climate sectors, by Shryas Bhurat.",
        f'''  <header class="page-hero">
    <div class="wrap">
      <p class="eyebrow">Research notes</p>
      <h1>Emerging tech, by sector.</h1>
      <p class="lede">Updated August 1, 2026. Easy-to-read notes with visuals on climate tech, by {AUTHOR}. Research drawn from Stanford, Berkeley, Caltech, Harvard, Wharton, and leading labs.</p>
    </div>
  </header>
  <section class="wrap">
    <div class="post-list">
{card_html}
    </div>
  </section>''',
    )
    # index uses ../ paths in NAV - fix for index in blog/ which is correct
    (ROOT / "index.html").write_text(index, encoding="utf-8")
    print("wrote index")


if __name__ == "__main__":
    write_posts()
