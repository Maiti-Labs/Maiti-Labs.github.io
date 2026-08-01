"""Timeline milestones and Jevons rebound sections per sector post."""

LEAVES_US_MARKER = '<h2>Where this leaves us</h2>'


def _timeline_html(intro: str, milestones: list[tuple[str, str]], progress_note: str) -> str:
    items = "\n".join(
        f'''          <div class="timeline-item" role="listitem">
            <p class="timeline-year">{year}</p>
            <p class="timeline-text">{text}</p>
          </div>'''
        for year, text in milestones
    )
    return f'''
        <h2>Key milestones</h2>
        <p>{intro}</p>
        <div class="timeline" role="list">
{items}
        </div>
        <p class="progress-note"><strong>Today:</strong> {progress_note}</p>
'''


def _rebound_html(intro: str, cards: list[tuple[str, str]], closing: str) -> str:
    card_blocks = "\n".join(
        f'''          <div class="rebound-card">
            <h3>{title}</h3>
            <p>{text}</p>
          </div>'''
        for title, text in cards
    )
    return f'''
        <h2>When cost falls, demand rises</h2>
        <p>{intro}</p>
        <div class="rebound" role="list">
{card_blocks}
        </div>
        <p>{closing}</p>
'''


def sections_for_slug(slug: str) -> str:
    data = SECTOR_SECTIONS[slug]
    return _timeline_html(
        data["timeline_intro"],
        data["milestones"],
        data["progress_note"],
    ) + _rebound_html(
        data["rebound_intro"],
        data["rebound_cards"],
        data["rebound_closing"],
    )


def inject_before_leaves_us(body: str, slug: str) -> str:
    extra = sections_for_slug(slug)
    if LEAVES_US_MARKER not in body:
        raise ValueError(f"Missing '{LEAVES_US_MARKER.strip()}' in body for {slug}")
    return body.replace(LEAVES_US_MARKER, extra + "\n" + LEAVES_US_MARKER, 1)


SECTOR_SECTIONS = {
    "weather-foundation-models": {
        "timeline_intro": "AI weather models moved from research papers to open checkpoints in just a few years.",
        "milestones": [
            ("2018–2020", "Early machine-learning weather emulators show that reanalysis archives can train competitive short-range models."),
            ("2022", "NVIDIA's FourCastNet line demonstrates fast global forecasts on commodity GPUs."),
            ("2023", "Pangu-Weather in <em>Nature</em>, GraphCast in <em>Science</em>, and ClimaX at ICML establish foundation-model-style pretraining for the atmosphere."),
            ("2024", "Aurora preprint, WeatherBench2 comparisons, and ECMWF's AIFS path push AI toward operational evaluation."),
            ("2025", "Aurora published in <em>Nature</em> as a broader Earth-system foundation model."),
            ("2026", "Minutes-scale global forecasts and open weights are routine for research teams outside major forecasting centers."),
        ],
        "progress_note": "Fast, accessible forecasts are working for many variables; extremes, calibration, and performance under climate shift remain early.",
        "rebound_intro": "When each forecast costs less compute, teams run more ensembles, products, and experiments. That is Jevons paradox in weather: cheaper capability drives more use, which creates new bottlenecks.",
        "rebound_cards": [
            ("Cost going down", "Single-GPU rollouts replace hours on agency supercomputers for many benchmark tasks."),
            ("Adoption rising", "More ensemble runs, downscaling pipelines, and AI weather startups compete on speed."),
            ("Data problems", "ERA5 quality, observation gaps, and verification datasets strain under heavier use."),
            ("AI / compute demand", "GPU clusters for training and inference grow with every new product layer."),
        ],
        "rebound_closing": "Climate gains from faster forecasts only stick if rebound is managed: open verification, honest uncertainty, and shared obs/reanalysis quality.",
    },
    "aerospace-satellites": {
        "timeline_intro": "Earth observation is shifting from one sensor, one model to pretrained encoders that transfer across missions.",
        "milestones": [
            ("1990s–2010s", "Task-specific remote-sensing classifiers dominate; each satellite product needs its own pipeline."),
            ("Early 2020s", "Foundation-model pretraining on public archives becomes a mainstream research direction."),
            ("2024", "SkySense at CVPR and NASA–IBM Prithvi-EO scale pretraining on global HLS and multi-modal archives."),
            ("2025", "Panopticon (any-sensor EO), SkySense++, and Copernicus-FM widen sensor-flexible pretraining."),
            ("2025", "Carbon-I, a Caltech-led NASA Earth System Explorer finalist, targets tropical greenhouse-gas mapping gaps."),
            ("2026", "Few-shot adaptation on new constellations is a realistic path for municipal and NGO analysts."),
        ],
        "progress_note": "Sensor-flexible models are working in research and pilots; labeled disaster response data and tropical GHG continuity remain weak.",
        "rebound_intro": "Cheaper Earth-observation AI lowers the cost of monitoring products, so demand for coverage and refresh rates rises. More inference load hits labeling, downlink, and compute before emissions insight scales.",
        "rebound_cards": [
            ("Cost going down", "Pretrained encoders cut labeled data and custom training for each new sensor."),
            ("Adoption rising", "Flood, crop, and emissions monitoring products multiply across regions."),
            ("Data problems", "Labeled benchmarks and harmonized archives lag behind model ambition."),
            ("Infrastructure problems", "Downlink, ground processing, and constellation capacity set the real ceiling."),
        ],
        "rebound_closing": "Satellite climate value holds only if rebound is managed: open labels, observation continuity standards, and shared compute for public-good products.",
    },
    "materials": {
        "timeline_intro": "Low-carbon materials research tracks both century-old cement chemistry and new solar-driven feedstock routes.",
        "milestones": [
            ("20th century", "Portland cement and limestone calcination define the status quo for global construction."),
            ("2000s–2010s", "Supplementary cementitious materials and fly ash substitution cut clinker fractions in many markets."),
            ("2020s", "Low-carbon clinker races accelerate as process CO<sub>2</sub> enters corporate and policy targets."),
            ("2023–2025", "Stanford Phlego, recycled concrete via induction, and pyrolysis carbon co-products enter pilot narratives."),
            ("2024–2025", "Caltech LiSA solar fuels work and Berkeley MACCs quantify which substitutions clear cost hurdles."),
            ("2026", "Lab performance data is rich; kiln integration and codes still gate deployment."),
        ],
        "progress_note": "Promising binders and recycling routes exist in lab and early pilot; standards, feedstock supply, and kiln retrofits are still the choke points.",
        "rebound_intro": "If green binders get cheaper, construction can absorb more volume at similar budgets, which can increase total material throughput unless substitution is enforced. Efficiency without supply-chain data can rebound emissions upstream.",
        "rebound_cards": [
            ("Cost going down", "Novel clinker, SCM blends, and co-product carbon routes target lower $/ton abatement."),
            ("Adoption rising", "More projects specify low-carbon concrete when premiums shrink."),
            ("Data problems", "EPD quality, LCA boundaries, and feedstock traceability stay uneven."),
            ("Infrastructure problems", "New chemistries need kiln retrofits, logistics, and code acceptance."),
        ],
        "rebound_closing": "Embodied-carbon gains stick when rebound is managed: transparent LCAs, procurement standards, and verified supply for SCMs and novel binders.",
    },
    "energy-systems": {
        "timeline_intro": "Clean grids moved from proving renewables cheap to asking how much storage and firm power the map needs.",
        "milestones": [
            ("2010s–2020s", "Lithium-ion costs fall sharply; short-duration storage pairs with solar and wind at scale."),
            ("Early 2020s", "Capacity-expansion models routinely include multi-day storage and hydrogen pathways."),
            ("2024", "Staadecker et al. and Chu/Baik/Benson LDES valuation papers clarify when long-duration assets earn their keep."),
            ("2024–2025", "California BRIDGES-style models show hydrogen power-to-gas alongside batteries in net-zero portfolios."),
            ("2020s", "Caltech ACN and Pasadena smart-grid pilots test local integration; See group work pushes beyond lithium chemistries."),
            ("2026", "Models are clear; project finance and interconnection queues decide what actually gets built."),
        ],
        "progress_note": "Short-duration storage is booming; LDES remains expensive, and transmission plus firm clean power largely decide total system value.",
        "rebound_intro": "Cheaper renewables and batteries invite more electrification load. Jevons dynamics show up as interconnection backlogs, storage data gaps, and new data-center demand on the same wires.",
        "rebound_cards": [
            ("Cost going down", "Solar, wind, and four-hour storage undercut fossil energy in many regions."),
            ("Adoption rising", "Building and transport electrification add peak and seasonal load."),
            ("Data problems", "LDES performance, grid constraints, and hourly carbon data stay sparse for planners."),
            ("Infrastructure problems", "Transmission upgrades and substation capacity lag queued projects."),
        ],
        "rebound_closing": "Grid climate gains hold when rebound is managed: open expansion-model inputs, faster interconnection, and LDES standards tied to real scarcity hours.",
    },
    "manufacturing": {
        "timeline_intro": "Factory decarbonization research now pairs process inventions with techno-economic gates.",
        "milestones": [
            ("2010s", "Efficiency and waste-heat recovery remain the first lever in most plants."),
            ("2020s", "Industrial electrification and low-carbon fuels enter mainstream engineering agendas."),
            ("2023", "NSF advanced manufacturing for industrial decarbonization workshop maps four-pillar research priorities."),
            ("2024", "Stanford electric thermochemical reactor and firebrick thermal storage show electrified heat at industrial temperatures."),
            ("2024–2025", "Berkeley industrial renewable-heat studies and Caltech solar-thermal fuel reactors extend the toolkit."),
            ("2026", "Pilot units exist; factory retrofit capital and hurdle rates still dominate adoption."),
        ],
        "progress_note": "Electrified heat and storage concepts are in pilots and TEA; upfront retrofit capital is the main choke point for plant operators.",
        "rebound_intro": "If process heat gets cheaper per ton output, plants may run more capacity when carbon prices are low enough. Without sensor data and grid headroom, electrification can shift emissions to the power sector or idle assets.",
        "rebound_cards": [
            ("Cost going down", "Electric reactors, firebricks, and renewable heat configs cut $/MWh thermal targets."),
            ("Adoption rising", "More lines electrify when TEAs clear corporate carbon prices."),
            ("Data problems", "Plant-level sensor streams and abatement baselines are rarely open."),
            ("Infrastructure problems", "Grid capacity and upgrade timelines constrain electrified factories."),
        ],
        "rebound_closing": "Manufacturing abatement sticks when rebound is managed: shared TEAs, open operational data, and sequenced grid upgrades for electrified heat.",
    },
    "built-environment": {
        "timeline_intro": "Building metrics are expanding from operational energy to whole-life carbon across the project timeline.",
        "milestones": [
            ("1990s–2010s", "Codes and labels focus on operational energy as the primary climate metric."),
            ("2010s–2020s", "Embodied carbon rises in priority as grids decarbonize and material volumes grow."),
            ("2023–2025", "Stanford CIFE industrialized construction tools link design, cost, and decarbonization tradeoffs."),
            ("2025", "California whole-life studies on dozens of buildings quantify embodied vs operational splits."),
            ("2024–2025", "Caltech Resnick Center mass timber demo and ASHRAE/ICC 240P whole-life standard work advance practice."),
            ("2026", "Methods and tools exist; early-design uptake remains uneven across firms."),
        ],
        "progress_note": "Whole-life assessment and low-carbon assemblies are available; consistent early-design use and trustworthy EPD data are still early.",
        "rebound_intro": "Cheaper LCA and design tools let more projects claim low carbon. Without data quality, lower analysis cost can increase greenwashing volume rather than real reductions.",
        "rebound_cards": [
            ("Cost going down", "Automated whole-life tools shrink consultant time per project."),
            ("Adoption rising", "More bids and specs reference embodied carbon targets."),
            ("Data problems", "EPD variance, product swaps, and method choices undermine comparisons."),
            ("Infrastructure problems", "Retrofit labor, supply chains for mass timber and low-carbon steel lag demand."),
        ],
        "rebound_closing": "Built-environment gains stick when rebound is managed: verified EPDs, whole-life standards in procurement, and design-stage defaults that count structure and interiors.",
    },
    "mobility": {
        "timeline_intro": "Electric mobility research now treats finance and charging uptime as first-class constraints alongside batteries.",
        "milestones": [
            ("2010s–2020s", "Battery costs fall and early EV models reach mass-market price bands."),
            ("2023+", "Wharton work by Bena, Bian, and Tang documents tighter EV loan terms driven by obsolescence risk."),
            ("2024–2025", "Harvard charging reliability studies find public uptime near 78% in large review datasets."),
            ("2020s", "Caltech ACN and PowerFlex research oversubscribed charging with grid-aware scheduling."),
            ("2020s", "NEVI-era U.S. public charging buildout accelerates corridor coverage."),
            ("2026", "Vehicle hardware improves; credit spreads and broken chargers still gate household adoption."),
        ],
        "progress_note": "EVs and chargers are scaling; affordable financing and reliable public uptime remain the gating frictions.",
        "rebound_intro": "Cheaper EVs can increase miles traveled and charging sessions. Jevons effects show up as strained public networks, substations, and optimization layers rather than in the battery cell alone.",
        "rebound_cards": [
            ("Cost going down", "Pack costs and operating cost per mile fall for many segments."),
            ("Adoption rising", "More households and fleets electrify when sticker and fuel math works."),
            ("Data problems", "Reliability metrics, tariff transparency, and residual-value data stay fragmented."),
            ("Infrastructure problems", "Charger maintenance, grid substations, and queueing under peak load."),
        ],
        "rebound_closing": "Transport electrification gains stick when rebound is managed: fair credit products, published uptime standards, and grid-aware charging at scale.",
    },
    "industrial-processes": {
        "timeline_intro": "Hard-to-abate sectors are moving from isolated pilots to sequenced playbooks with public cost evidence.",
        "milestones": [
            ("2010s", "Hard-to-abate framing consolidates cement, steel, and chemicals as distinct climate challenges."),
            ("2020s", "High-temperature heat is recognized as the binding constraint across process industries."),
            ("2023–2025", "Stanford IDAP and IFAN connect research to plant decision-makers on steel and automotive chains."),
            ("2024", "Firebricks and electric reactors enter industrial heat roadmaps alongside hydrogen options."),
            ("2024–2025", "Caltech CO<sub>2</sub>-to-fuels routes and Stanford/Berkeley abatement curves tie chemistry to carbon prices."),
            ("2026", "Technology pathways are known; sequenced deployment and shared cost data lag policy ambition."),
        ],
        "progress_note": "Playbooks and abatement curves exist for major sectors; coordinated deployment timelines and open plant-level cost data are still catching up.",
        "rebound_intro": "Cheaper abatement tech can justify higher output under weak carbon constraints, or shift emissions across supply chains. Without MRV, 'green' labels can outrun real process change.",
        "rebound_cards": [
            ("Cost going down", "Electrified heat, storage, and low-carbon inputs move down abatement curves."),
            ("Adoption rising", "Firms sequence retrofits when carbon prices cross published thresholds."),
            ("Data problems", "MRV, heat-metering, and shared baseline emissions data remain gaps."),
            ("Infrastructure problems", "Power supply and grid upgrades for electrified process heat at site scale."),
        ],
        "rebound_closing": "Industrial decarbonization sticks when rebound is managed: public abatement curves, MRV standards, and power infrastructure sequenced with heat retrofits.",
    },
}
