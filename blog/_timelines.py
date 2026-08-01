"""Timeline milestones and Jevons rebound sections per sector post."""

LEAVES_US_MARKER = '<h2>Where this leaves us</h2>'


def _c(n: int) -> str:
    return f'[<a href="#r{n}">{n}</a>]'


def _timeline_html(intro: str, milestones: list[tuple[str, str]], progress_note: str) -> str:
    items = "\n".join(
        f'''          <div class="timeline-item" role="listitem">
            <p class="timeline-year">{year}</p>
            <p class="timeline-text">{text}</p>
          </div>'''
        for year, text in milestones
    )
    return f'''
        <h2>Timeline</h2>
        <p>{intro}</p>
        <div class="timeline" role="list">
{items}
        </div>
        <p class="progress-note"><strong>Today:</strong> {progress_note}</p>
'''


def rebound_cards_html(slug: str) -> str:
    data = SECTOR_SECTIONS[slug]
    card_blocks = "\n".join(
        f'''          <div class="rebound-card">
            <h3>{title}</h3>
            <p>{text}</p>
          </div>'''
        for title, text in data["rebound_cards"]
    )
    return f'''        <div class="rebound" role="list">
{card_blocks}
        </div>'''


def sections_for_slug(slug: str) -> str:
    data = SECTOR_SECTIONS[slug]
    return _timeline_html(
        data["timeline_intro"],
        data["milestones"],
        data["progress_note"],
    )


def future_section_html(slug: str) -> str:
    data = SECTOR_SECTIONS[slug]
    paras = "\n".join(
        f"        <p><strong>{title}.</strong> {text}</p>"
        for title, text in data["rebound_cards"]
    )
    return f'''
        <p>{data["rebound_intro"]}</p>
{paras}
        <p class="progress-note"><strong>Looking ahead:</strong> {data["progress_note"]}</p>
        <p>{data["rebound_closing"]}</p>
'''


SECTOR_SECTIONS = {
    "space-compute": {
        "timeline_intro": f"Orbital AI moved from radiation-hardened satellite computers to accelerator demos and hyperscale research designs in a few years {_c(1)}{_c(5)}.",
        "milestones": [
            ("Pre-2020s", f"Edge and radiation-tolerant processors serve onboard satellite tasks rather than hyperscale training {_c(1)}."),
            ("2024–2025", f"Lumen Orbit rebrands as Starcloud; orbital data center concepts draw venture funding {_c(5)}."),
            ("Nov 2025", f"Starcloud-1 flies an Nvidia H100 in orbit; Google publishes Project Suncatcher system design {_c(1)}{_c(5)}."),
            ("Jan 2026", f"SpaceX files with the FCC for an orbital data center system, signaling major platform interest {_c(3)}{_c(6)}."),
            ("2026", f"Starcloud Series A and large constellation filing; Wood Mackenzie publishes orbital vs terrestrial cost comparison {_c(4)}{_c(5)}{_c(6)}."),
            ("Early 2027 (planned)", f"Google and Planet target Suncatcher prototype platforms for flight test {_c(1)}{_c(2)}."),
        ],
        "progress_note": f"Demos and public architectures exist; launch cost, link latency, and grid substitution math still gate scale {_c(3)}{_c(4)}{_c(5)}.",
        "rebound_intro": f"If orbital inference gets cheaper, demand for AI compute may rise faster than terrestrial grids decarbonize, a Jevons-style dynamic unless workloads truly substitute for ground build {_c(7)}{_c(8)}.",
        "rebound_cards": [
            ("Cost going down", f"Reusable launch and sunlit orbits target lower $/FLOP for latency-tolerant jobs {_c(3)}{_c(1)}."),
            ("Adoption rising", f"Hyperscalers and startups file constellations and fly GPU demos {_c(5)}{_c(6)}."),
            ("Data problems", f"Link budgets, radiation error rates, and lifecycle LCAs stay thin in public {_c(1)}{_c(4)}."),
            ("Infrastructure problems", f"Spectrum, debris, thermal limits, and ground stations cap usable capacity {_c(3)}{_c(6)}."),
        ],
        "rebound_closing": f"Climate value from space compute holds only if rebound is managed: open cost models, verified substitution for grid build, and spectrum/debris rules that match constellation scale {_c(4)}{_c(7)}{_c(8)}.",
    },
    "weather-foundation-models": {
        "timeline_intro": f"AI weather models moved from research papers to open checkpoints in just a few years {_c(2)}{_c(9)}.",
        "milestones": [
            ("2018–2020", f"Early machine-learning weather emulators show that reanalysis archives such as ERA5 can train competitive short-range models {_c(11)}{_c(10)}."),
            ("2022", f"NVIDIA's FourCastNet line demonstrates fast global forecasts on commodity GPUs {_c(9)}."),
            ("2023", f"Pangu-Weather in <em>Nature</em> {_c(3)}, GraphCast in <em>Science</em> {_c(2)}, and ClimaX at ICML {_c(1)} establish foundation-model-style pretraining for the atmosphere."),
            ("2024", f"Aurora preprint {_c(5)}, WeatherBench2 comparisons {_c(10)}, and ECMWF's AIFS path {_c(12)} push AI toward operational evaluation."),
            ("2025", f"Aurora published in <em>Nature</em> as a broader Earth-system foundation model {_c(5)}."),
            ("2026", f"Minutes-scale global forecasts and open weights are routine for research teams outside major forecasting centers {_c(9)}{_c(4)}."),
        ],
        "progress_note": f"Fast, accessible forecasts are working for many variables; extremes, calibration, and performance under climate shift remain early {_c(6)}{_c(4)}.",
        "rebound_intro": f"When each forecast costs less compute, teams run more ensembles, products, and experiments. That is Jevons paradox in weather: cheaper capability drives more use, which creates new bottlenecks {_c(13)}{_c(14)}.",
        "rebound_cards": [
            ("Cost going down", f"Single-GPU rollouts replace hours on agency supercomputers for many benchmark tasks {_c(9)}{_c(2)}."),
            ("Adoption rising", f"More ensemble runs, downscaling pipelines, and AI weather startups compete on speed {_c(10)}{_c(4)}."),
            ("Data problems", f"ERA5 quality, observation gaps, and verification datasets strain under heavier use {_c(11)}{_c(10)}."),
            ("AI / compute demand", f"GPU clusters for training and inference grow with every new product layer {_c(9)}{_c(5)}."),
        ],
        "rebound_closing": f"Climate gains from faster forecasts only stick if rebound is managed: open verification, honest uncertainty, and shared obs/reanalysis quality {_c(10)}{_c(6)}{_c(11)}.",
    },
    "aerospace-satellites": {
        "timeline_intro": f"Earth observation is shifting from one sensor, one model to pretrained encoders that transfer across missions {_c(6)}{_c(1)}.",
        "milestones": [
            ("1990s–2010s", f"Task-specific remote-sensing classifiers dominate; each satellite product needs its own pipeline {_c(6)}."),
            ("Early 2020s", f"Foundation-model pretraining on public archives becomes a mainstream research direction {_c(6)}{_c(2)}."),
            ("2024", f"SkySense at CVPR {_c(2)} and NASA–IBM Prithvi-EO {_c(4)} scale pretraining on global HLS and multi-modal archives."),
            ("2025", f"Panopticon (any-sensor EO) {_c(1)}, SkySense++ {_c(3)}, and Copernicus-FM {_c(5)} widen sensor-flexible pretraining."),
            ("2025", f"Carbon-I, a Caltech-led NASA Earth System Explorer finalist, targets tropical greenhouse-gas mapping gaps {_c(7)}."),
            ("2026", f"Few-shot adaptation on new constellations is a realistic path for municipal and NGO analysts {_c(1)}{_c(3)}."),
        ],
        "progress_note": f"Sensor-flexible models are working in research and pilots; labeled disaster response data and tropical GHG continuity remain weak {_c(3)}{_c(7)}{_c(8)}.",
        "rebound_intro": f"Cheaper Earth-observation AI lowers the cost of monitoring products, so demand for coverage and refresh rates rises {_c(10)}{_c(9)}. More inference load hits labeling, downlink, and compute before emissions insight scales {_c(6)}.",
        "rebound_cards": [
            ("Cost going down", f"Pretrained encoders cut labeled data and custom training for each new sensor {_c(1)}{_c(2)}."),
            ("Adoption rising", f"Flood, crop, and emissions monitoring products multiply across regions {_c(3)}{_c(7)}."),
            ("Data problems", f"Labeled benchmarks and harmonized archives lag behind model ambition {_c(6)}{_c(5)}."),
            ("Infrastructure problems", f"Downlink, ground processing, and constellation capacity set the real ceiling {_c(8)}{_c(7)}."),
        ],
        "rebound_closing": f"Satellite climate value holds only if rebound is managed: open labels, observation continuity standards, and shared compute for public-good products {_c(8)}{_c(6)}{_c(7)}.",
    },
    "materials": {
        "timeline_intro": f"Low-carbon materials research tracks both century-old cement chemistry and new solar-driven feedstock routes {_c(7)}{_c(1)}.",
        "milestones": [
            ("20th century", f"Portland cement and limestone calcination define the status quo for global construction {_c(7)}."),
            ("2000s–2010s", f"Supplementary cementitious materials and fly ash substitution cut clinker fractions in many markets {_c(5)}."),
            ("2020s", f"Low-carbon clinker races accelerate as process CO<sub>2</sub> enters corporate and policy targets {_c(7)}{_c(5)}."),
            ("2023–2025", f"Stanford Phlego {_c(1)}{_c(2)}, recycled concrete via induction {_c(3)}, and pyrolysis carbon co-products {_c(4)} enter pilot narratives."),
            ("2024–2025", f"Caltech LiSA solar fuels work {_c(6)} and Berkeley MACCs {_c(5)} quantify which substitutions clear cost hurdles."),
            ("2026", f"Lab performance data is rich; kiln integration and codes still gate deployment {_c(1)}{_c(5)}."),
        ],
        "progress_note": f"Promising binders and recycling routes exist in lab and early pilot; standards, feedstock supply, and kiln retrofits are still the choke points {_c(1)}{_c(5)}.",
        "rebound_intro": f"If green binders get cheaper, construction can absorb more volume at similar budgets, which can increase total material throughput unless substitution is enforced {_c(8)}{_c(9)}. Efficiency without supply-chain data can rebound emissions upstream {_c(9)}{_c(5)}.",
        "rebound_cards": [
            ("Cost going down", f"Novel clinker, SCM blends, and co-product carbon routes target lower $/ton abatement {_c(1)}{_c(4)}{_c(5)}."),
            ("Adoption rising", f"More projects specify low-carbon concrete when premiums shrink {_c(5)}."),
            ("Data problems", f"EPD quality, LCA boundaries, and feedstock traceability stay uneven {_c(5)}."),
            ("Infrastructure problems", f"New chemistries need kiln retrofits, logistics, and code acceptance {_c(1)}{_c(2)}."),
        ],
        "rebound_closing": f"Embodied-carbon gains stick when rebound is managed: transparent LCAs, procurement standards, and verified supply for SCMs and novel binders {_c(5)}{_c(9)}.",
    },
    "energy-systems": {
        "timeline_intro": f"Clean grids moved from proving renewables cheap to asking how much storage and firm power the map needs {_c(1)}{_c(2)}.",
        "milestones": [
            ("2010s–2020s", f"Lithium-ion costs fall sharply; short-duration storage pairs with solar and wind at scale {_c(6)}."),
            ("Early 2020s", f"Capacity-expansion models routinely include multi-day storage and hydrogen pathways {_c(1)}{_c(3)}."),
            ("2024", f"Staadecker et al. {_c(1)} and Chu/Baik/Benson LDES valuation papers {_c(2)} clarify when long-duration assets earn their keep."),
            ("2024–2025", f"California BRIDGES-style models show hydrogen power-to-gas alongside batteries in net-zero portfolios {_c(3)}."),
            ("2020s", f"Caltech ACN and Pasadena smart-grid pilots test local integration {_c(5)}; See group work pushes beyond lithium chemistries {_c(5)}."),
            ("2026", f"Models are clear; project finance and interconnection queues decide what actually gets built {_c(3)}{_c(1)}."),
        ],
        "progress_note": f"Short-duration storage is booming; LDES remains expensive, and transmission plus firm clean power largely decide total system value {_c(1)}{_c(2)}{_c(4)}.",
        "rebound_intro": f"Cheaper renewables and batteries invite more electrification load {_c(6)}{_c(8)}. Jevons dynamics show up as interconnection backlogs, storage data gaps, and new data-center demand on the same wires {_c(7)}{_c(3)}.",
        "rebound_cards": [
            ("Cost going down", f"Solar, wind, and four-hour storage undercut fossil energy in many regions {_c(6)}{_c(1)}."),
            ("Adoption rising", f"Building and transport electrification add peak and seasonal load {_c(2)}{_c(3)}."),
            ("Data problems", f"LDES performance, grid constraints, and hourly carbon data stay sparse for planners {_c(1)}{_c(2)}."),
            ("Infrastructure problems", f"Transmission upgrades and substation capacity lag queued projects {_c(3)}{_c(4)}."),
        ],
        "rebound_closing": f"Grid climate gains hold when rebound is managed: open expansion-model inputs, faster interconnection, and LDES standards tied to real scarcity hours {_c(1)}{_c(2)}{_c(3)}.",
    },
    "manufacturing": {
        "timeline_intro": f"Factory decarbonization research now pairs process inventions with techno-economic gates {_c(1)}{_c(5)}.",
        "milestones": [
            ("2010s", f"Efficiency and waste-heat recovery remain the first lever in most plants {_c(1)}."),
            ("2020s", f"Industrial electrification and low-carbon fuels enter mainstream engineering agendas {_c(1)}{_c(4)}."),
            ("2023", f"NSF advanced manufacturing for industrial decarbonization workshop maps four-pillar research priorities {_c(1)}."),
            ("2024", f"Stanford electric thermochemical reactor {_c(2)} and firebrick thermal storage {_c(3)} show electrified heat at industrial temperatures."),
            ("2024–2025", f"Berkeley industrial renewable-heat studies {_c(4)} and Caltech solar-thermal fuel reactors {_c(6)} extend the toolkit."),
            ("2026", f"Pilot units exist; factory retrofit capital and hurdle rates still dominate adoption {_c(5)}{_c(2)}."),
        ],
        "progress_note": f"Electrified heat and storage concepts are in pilots and TEA; upfront retrofit capital is the main choke point for plant operators {_c(2)}{_c(3)}{_c(5)}.",
        "rebound_intro": f"If process heat gets cheaper per ton output, plants may run more capacity when carbon prices are low enough {_c(5)}{_c(7)}. Without sensor data and grid headroom, electrification can shift emissions to the power sector or idle assets {_c(4)}{_c(8)}.",
        "rebound_cards": [
            ("Cost going down", f"Electric reactors, firebricks, and renewable heat configs cut $/MWh thermal targets {_c(2)}{_c(3)}{_c(4)}."),
            ("Adoption rising", f"More lines electrify when TEAs clear corporate carbon prices {_c(5)}{_c(1)}."),
            ("Data problems", f"Plant-level sensor streams and abatement baselines are rarely open {_c(1)}{_c(5)}."),
            ("Infrastructure problems", f"Grid capacity and upgrade timelines constrain electrified factories {_c(4)}{_c(5)}."),
        ],
        "rebound_closing": f"Manufacturing abatement sticks when rebound is managed: shared TEAs, open operational data, and sequenced grid upgrades for electrified heat {_c(1)}{_c(5)}{_c(4)}.",
    },
    "built-environment": {
        "timeline_intro": f"Building metrics are expanding from operational energy to whole-life carbon across the project timeline {_c(1)}{_c(4)}.",
        "milestones": [
            ("1990s–2010s", f"Codes and labels focus on operational energy as the primary climate metric {_c(3)}."),
            ("2010s–2020s", f"Embodied carbon rises in priority as grids decarbonize and material volumes grow {_c(1)}{_c(4)}."),
            ("2023–2025", f"Stanford CIFE industrialized construction tools link design, cost, and decarbonization tradeoffs {_c(2)}."),
            ("2025", f"California whole-life studies on dozens of buildings quantify embodied vs operational splits {_c(1)}."),
            ("2024–2025", f"Caltech Resnick Center mass timber demo {_c(5)} and ASHRAE/ICC 240P whole-life standard work advance practice {_c(6)}."),
            ("2026", f"Methods and tools exist; early-design uptake remains uneven across firms {_c(2)}{_c(1)}."),
        ],
        "progress_note": f"Whole-life assessment and low-carbon assemblies are available; consistent early-design use and trustworthy EPD data are still early {_c(1)}{_c(2)}{_c(6)}.",
        "rebound_intro": f"Cheaper LCA and design tools let more projects claim low carbon {_c(2)}{_c(8)}. Without data quality, lower analysis cost can increase greenwashing volume rather than real reductions {_c(1)}{_c(7)}.",
        "rebound_cards": [
            ("Cost going down", f"Automated whole-life tools shrink consultant time per project {_c(2)}."),
            ("Adoption rising", f"More bids and specs reference embodied carbon targets {_c(4)}{_c(6)}."),
            ("Data problems", f"EPD variance, product swaps, and method choices undermine comparisons {_c(1)}."),
            ("Infrastructure problems", f"Retrofit labor, supply chains for mass timber and low-carbon steel lag demand {_c(5)}{_c(4)}."),
        ],
        "rebound_closing": f"Built-environment gains stick when rebound is managed: verified EPDs, whole-life standards in procurement, and design-stage defaults that count structure and interiors {_c(1)}{_c(6)}{_c(4)}.",
    },
    "mobility": {
        "timeline_intro": f"Electric mobility research now treats finance and charging uptime as first-class constraints alongside batteries {_c(1)}{_c(3)}.",
        "milestones": [
            ("2010s–2020s", f"Battery costs fall and early EV models reach mass-market price bands {_c(8)}."),
            ("2023+", f"Wharton work by Bena, Bian, and Tang documents tighter EV loan terms driven by obsolescence risk {_c(1)}{_c(2)}."),
            ("2024–2025", f"Harvard charging reliability studies find public uptime near 78% in large review datasets {_c(3)}."),
            ("2020s", f"Caltech ACN and PowerFlex research oversubscribed charging with grid-aware scheduling {_c(5)}{_c(6)}."),
            ("2020s", f"NEVI-era U.S. public charging buildout accelerates corridor coverage {_c(7)}."),
            ("2026", f"Vehicle hardware improves; credit spreads and broken chargers still gate household adoption {_c(1)}{_c(3)}."),
        ],
        "progress_note": f"EVs and chargers are scaling; affordable financing and reliable public uptime remain the gating frictions {_c(1)}{_c(3)}{_c(7)}.",
        "rebound_intro": f"Cheaper EVs can increase miles traveled and charging sessions {_c(8)}{_c(10)}. Jevons effects show up as strained public networks, substations, and optimization layers rather than in the battery cell alone {_c(9)}{_c(5)}{_c(3)}.",
        "rebound_cards": [
            ("Cost going down", f"Pack costs and operating cost per mile fall for many segments {_c(8)}{_c(1)}."),
            ("Adoption rising", f"More households and fleets electrify when sticker and fuel math works {_c(1)}{_c(7)}."),
            ("Data problems", f"Reliability metrics, tariff transparency, and residual-value data stay fragmented {_c(3)}{_c(4)}."),
            ("Infrastructure problems", f"Charger maintenance, grid substations, and queueing under peak load {_c(3)}{_c(5)}."),
        ],
        "rebound_closing": f"Transport electrification gains stick when rebound is managed: fair credit products, published uptime standards, and grid-aware charging at scale {_c(1)}{_c(3)}{_c(5)}.",
    },
    "industrial-processes": {
        "timeline_intro": f"Hard-to-abate sectors are moving from isolated pilots to sequenced playbooks with public cost evidence {_c(1)}{_c(6)}.",
        "milestones": [
            ("2010s", f"Hard-to-abate framing consolidates cement, steel, and chemicals as distinct climate challenges {_c(1)}{_c(6)}."),
            ("2020s", f"High-temperature heat is recognized as the binding constraint across process industries {_c(2)}{_c(3)}."),
            ("2023–2025", f"Stanford IDAP and IFAN connect research to plant decision-makers on steel and automotive chains {_c(1)}."),
            ("2024", f"Firebricks and electric reactors enter industrial heat roadmaps alongside hydrogen options {_c(2)}{_c(3)}."),
            ("2024–2025", f"Caltech CO<sub>2</sub>-to-fuels routes {_c(7)} and Stanford/Berkeley abatement curves {_c(6)}{_c(4)} tie chemistry to carbon prices."),
            ("2026", f"Technology pathways are known; sequenced deployment and shared cost data lag policy ambition {_c(1)}{_c(6)}."),
        ],
        "progress_note": f"Playbooks and abatement curves exist for major sectors; coordinated deployment timelines and open plant-level cost data are still catching up {_c(1)}{_c(6)}{_c(4)}.",
        "rebound_intro": f"Cheaper abatement tech can justify higher output under weak carbon constraints, or shift emissions across supply chains {_c(6)}{_c(8)}. Without MRV, 'green' labels can outrun real process change {_c(1)}.",
        "rebound_cards": [
            ("Cost going down", f"Electrified heat, storage, and low-carbon inputs move down abatement curves {_c(2)}{_c(3)}{_c(5)}."),
            ("Adoption rising", f"Firms sequence retrofits when carbon prices cross published thresholds {_c(6)}{_c(4)}."),
            ("Data problems", f"MRV, heat-metering, and shared baseline emissions data remain gaps {_c(1)}{_c(6)}."),
            ("Infrastructure problems", f"Power supply and grid upgrades for electrified process heat at site scale {_c(4)}{_c(3)}."),
        ],
        "rebound_closing": f"Industrial decarbonization sticks when rebound is managed: public abatement curves, MRV standards, and power infrastructure sequenced with heat retrofits {_c(6)}{_c(1)}{_c(4)}.",
    },
}
