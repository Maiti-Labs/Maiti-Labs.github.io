#!/usr/bin/env python3
"""Generate sector research posts in Physical Intelligence-inspired format."""
from pathlib import Path

from _viz import VIZ

ROOT = Path(__file__).resolve().parent

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

def article(meta, title, dek, body, refs, viz_html=""):
    ref_items = "\n".join(f"<li>{r}</li>" for r in refs)
    viz_block = f"\n{viz_html}\n" if viz_html else ""
    return f'''  <article class="article">
    <div class="wrap-narrow">
      <a class="back-link" href="index.html">‹ All research notes</a>
      <p class="article-meta">{meta}</p>
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

# 1 Weather
POSTS.append({
    "slug": "weather-foundation-models",
    "num": "01",
    "sector": "Weather Foundation Models",
    "viz_key": "weather",
    "card_title": "AI weather models are becoming the new forecast stack",
    "card_blurb": "GraphCast, Aurora, and ClimaX match classic supercomputer forecasts on many scores, in a fraction of the time.",
    "meta": "Research note · August 1, 2026 · Sector 01",
    "title": "AI weather models are becoming the new forecast stack",
    "dek": "Pretrained atmospheric models are changing who can run good forecasts, and how fast those forecasts arrive.",
    "description": "Emerging weather foundation models from DeepMind, Microsoft, ECMWF, and university labs, with citations.",
    "body": '''
        <div class="callout callout-plain">
          <p><strong>In plain terms.</strong> Weather AI learns patterns from decades of global data, then rolls out a forecast in minutes on a single machine. Classic physics models on supercomputers still set the quality bar, but they take hours and sit behind agency walls.</p>
        </div>
        <p>For decades, skillful medium-range forecasts meant one thing: a physics-based numerical weather prediction (NWP) system on a supercomputer. That stack still matters. Data-driven models trained on reanalysis archives can now produce competitive forecasts in minutes on commodity hardware.</p>
        <p>This is not a cosmetic speedup. It changes access. University labs, national agencies, and climate-risk teams that could never operate a full IFS-class system can now evaluate ensemble-scale experiments, downscaling pipelines, and early-warning prototypes. The research question has shifted from "can AI forecast weather?" to "which foundation-model designs generalize under climate change, extremes, and sparse observations?"</p>

        <h2>What "foundation model" means in weather</h2>
        <p>In language and vision, a foundation model is pretrained once on broad data, then adapted to many tasks. Weather and climate need the same idea, but the data are gridded fields, multiple physical variables, and heterogeneous resolutions.</p>
        <p><a href="https://arxiv.org/abs/2301.10343">ClimaX</a>, developed by researchers at UCLA and Microsoft Research, was an early explicit attempt at this framing. It extends a Vision Transformer with variable tokenization and aggregation so one model can be pretrained on heterogeneous CMIP6-derived climate data, then fine-tuned for forecasting, projection, and downscaling tasks, including variables and scales not seen in pretraining [<a href="#r1">1</a>]. That is the core recipe later systems refine: pretrain broadly, specialize cheaply.</p>

        <h2>The current frontier models</h2>
        <h3>Graph neural networks and transformers at global scale</h3>
        <p>Google DeepMind's <a href="https://www.science.org/doi/10.1126/science.adi2336">GraphCast</a> (Lam et al.) encodes the atmosphere as a multi-scale mesh and rolls out 6-hour steps to produce 10-day forecasts. On WeatherBench-style evaluations it matched or exceeded ECMWF's high-resolution IFS on many variables while running orders of magnitude faster [<a href="#r2">2</a>]. Huawei's <a href="https://www.nature.com/articles/s41586-023-06185-3">Pangu-Weather</a> (Bi et al.) uses a 3D Earth Transformer and hierarchical temporal aggregation, again reporting deterministic skill competitive with operational IFS on reanalysis benchmarks [<a href="#r3">3</a>].</p>
        <p>NVIDIA's FourCastNet line and ECMWF's Artificial Intelligence Integrated Forecasting System (AIFS) push the same idea into operational settings. Feldmann et al. use WeatherBench2 to compare Pangu-Weather, GraphCast, and FourCastNet against IFS-HRES for severe convective environments, showing that AI models can produce useful large-scale convective outlooks far faster than classical pipelines [<a href="#r4">4</a>].</p>

        <h3>Toward multi-domain atmospheric foundation models</h3>
        <p>Microsoft Research's <a href="https://doi.org/10.1038/s41586-025-09005-y">Aurora</a> (Bodnar et al.) widens the pretraining mixture beyond ERA5 weather fields, incorporating air quality, ocean, and climate-model outputs into one flexible backbone [<a href="#r5">5</a>]. That is closer to a true Earth-system foundation model than a single-task emulator.</p>
        <div class="callout">
          <p>The practical implication for accessibility: once a strong pretrained checkpoint exists, fine-tuning for a regional hazard, an agricultural index, or an air-quality product becomes a research project rather than a national computing program.</p>
        </div>

        <h2>What top labs are stressing next</h2>
        <p>Skill on ERA5 is necessary but not sufficient. Rackow et al. examine GraphCast, Pangu-Weather, and AIFS under climate-change-like conditions and ask whether models trained on the recent past remain reliable as the climate shifts [<a href="#r6">6</a>]. Extremes remain a hard edge: AI forecasts can be overly smooth and can understate record-breaking events even when mean scores look excellent.</p>
        <p>University groups are therefore focusing on hybrid designs, probabilistic ensembles, and observation-informed fine-tuning. Stanford's Doerr School and related atmospheric research communities emphasize that operational value depends on calibration for hazards people actually manage: heat, flood precursors, wind extremes, and compound events, not only RMSE on 500 hPa geopotential.</p>

        <h2>Hybrid climate modeling: Google Research and Caltech CliMA</h2>
        <p>Parallel to the data-driven weather wave, Caltech's Climate Modeling Alliance (CliMA), led by Tapio Schneider, pursues hybrid physics–machine learning parameterizations that keep dynamical constraints explicit while learning subgrid closures from data. Lopez-Gomez et al., with Google Research and Caltech authors, report dynamical-generative downscaling of climate model ensembles that preserves large-scale circulation while generating high-resolution fields suitable for impact studies [<a href="#r7">7</a>]. Christopoulos et al. show hybrid ML parameterizations for cloud entrainment that can be updated as observations stream in, a design point that differs from frozen pretrained forecasters [<a href="#r8">8</a>].</p>
        <p>The two agendas are complementary. Weather foundation models excel at fast, global deterministic forecasts from reanalysis. Caltech's physics-constrained climate modeling agenda targets long-horizon ensembles, process fidelity, and downscaling that remains tied to conservation laws. Accessible climate research needs both: open checkpoints for short-range hazard work and open process models for scenario stress-testing.</p>

        <h2>Why this matters for accessible climate research</h2>
        <p>Weather foundation models compress a capability that used to sit behind agency firewalls. Open weights, public reanalysis, and benchmarks such as WeatherBench2 let students at Berkeley, researchers in the Global South, and municipal risk teams reproduce modern forecast skill. The open problem is not whether these models exist. It is how to document uncertainty, couple them to impact models, and keep evaluation honest as the climate moves.</p>

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
    ],
})

# 2 Aerospace
POSTS.append({
    "slug": "aerospace-satellites",
    "num": "02",
    "sector": "Aerospace & Satellites",
    "viz_key": "aerospace",
    "card_title": "Earth observation is moving from sensors to foundation models",
    "card_blurb": "Berkeley Panopticon, Caltech-led Carbon-I, and large-scale pretraining are making satellite analysis work across missions.",
    "meta": "Research note · August 1, 2026 · Sector 02",
    "title": "Earth observation is moving from sensors to foundation models",
    "dek": "Satellites still collect the data. Foundation models are starting to define how quickly that data becomes usable maps and metrics.",
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
    ],
})

# 3 Materials
POSTS.append({
    "slug": "materials",
    "num": "03",
    "sector": "Materials",
    "viz_key": "materials",
    "card_title": "Low-carbon materials research is rewriting cement and concrete",
    "card_blurb": "Stanford, Berkeley, and Caltech work on cement chemistry, solar-driven catalytic materials, and abatement cost curves shows materials science is now a climate lever.",
    "meta": "Research note · August 1, 2026 · Sector 03",
    "title": "Low-carbon materials research is rewriting cement and concrete",
    "dek": "Cement is still one of the hardest industrial emissions problems. University labs are attacking the chemistry, the kiln, and the cost curve at once.",
    "description": "Emerging low-carbon materials research from Stanford, Berkeley, and related labs.",
    "body": '''
        <div class="callout callout-plain">
          <p><strong>In plain terms.</strong> Cement releases CO<sub>2</sub> when limestone is heated, not only from fuel. Researchers are testing new rock recipes, recycled concrete, and solar-driven chemistry to shrink that footprint.</p>
        </div>
        <p>Concrete is the world's most-used building material. Cement production alone accounts for roughly 8% of global CO<sub>2</sub> emissions, much of it from limestone calcination rather than fuel burn. That chemistry constraint is why incremental kiln efficiency is not enough, and why materials research has become central to climate strategy.</p>
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
    ],
})

# 4 Energy
POSTS.append({
    "slug": "energy-systems",
    "num": "04",
    "sector": "Energy Systems",
    "viz_key": "energy",
    "card_title": "Long-duration storage is the quiet center of clean grids",
    "card_blurb": "Stanford and Berkeley grid models, plus Caltech storage chemistry and Pasadena smart-grid pilots, show when multi-day storage and local integration actually earn their keep.",
    "meta": "Research note · August 1, 2026 · Sector 04",
    "title": "Long-duration storage is the quiet center of clean grids",
    "dek": "Solar and wind are cheaper in many regions. Keeping a zero-emissions grid reliable across nights and calm weeks is the harder part.",
    "description": "Emerging energy systems research on long-duration storage and clean grids from Stanford and Berkeley.",
    "body": '''
        <div class="callout callout-plain">
          <p><strong>In plain terms.</strong> Batteries that last a few hours cover evening peaks. Multi-day storage fills the gaps when wind and sun dip for days or weeks. Grid models now spell out when each layer pays for itself.</p>
        </div>
        <p>Variable renewables have won the cheap-electron contest in many regions. The research frontier has moved to balancing: how much lithium-ion is enough, when multi-day storage becomes valuable, and which firm resources reduce total system cost.</p>
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
    ],
})

# 5 Manufacturing
POSTS.append({
    "slug": "manufacturing",
    "num": "05",
    "sector": "Manufacturing",
    "viz_key": "manufacturing",
    "card_title": "Advanced manufacturing is becoming a decarbonization toolkit",
    "card_blurb": "NSF and university work on electrification, process substitution, and factory data is turning manufacturing into a climate research domain.",
    "meta": "Research note · August 1, 2026 · Sector 05",
    "title": "Advanced manufacturing is becoming a decarbonization toolkit",
    "dek": "Factories are no longer only an emissions source to regulate. They are a design space for lower-carbon process technology.",
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
    ],
})

# 6 Built environment
POSTS.append({
    "slug": "built-environment",
    "num": "06",
    "sector": "Built Environment",
    "viz_key": "built",
    "card_title": "Whole-life carbon is replacing energy-only building metrics",
    "card_blurb": "Stanford CIFE and Berkeley-linked building research show embodied carbon now rivals operations as grids clean up.",
    "meta": "Research note · August 1, 2026 · Sector 06",
    "title": "Whole-life carbon is replacing energy-only building metrics",
    "dek": "As grids decarbonize, the carbon locked into steel, concrete, and interiors becomes impossible to ignore.",
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
    ],
})

# 7 Mobility
POSTS.append({
    "slug": "mobility",
    "num": "07",
    "sector": "Mobility",
    "viz_key": "mobility",
    "card_title": "EV scale-up is constrained by finance and charging reliability",
    "card_blurb": "Wharton, Harvard, and Caltech research show that loans, broken chargers, and oversubscribed charging networks shape electric mobility adoption.",
    "meta": "Research note · August 1, 2026 · Sector 07",
    "title": "EV scale-up is constrained by finance and charging reliability",
    "dek": "Battery packs get the headlines. Household credit and uptime statistics may decide the adoption curve.",
    "description": "Emerging mobility research from Wharton and Harvard on EV finance and charging infrastructure.",
    "body": '''
        <div class="callout callout-plain">
          <p><strong>In plain terms.</strong> Electric cars improve every year, but buyers still face stricter loans and chargers that fail too often. Fixing finance and uptime may matter as much as battery chemistry for mass adoption.</p>
        </div>
        <p>Electric mobility research often starts with energy density, charging speed, and vehicle cost. Those remain first-order. Wharton and Harvard work adds two less visible constraints that determine whether climate-aligned transport actually reaches households: financing terms and charger reliability.</p>

        <h2>The EV financing gap</h2>
        <p>Research by Bena et al., <em>Financing the Global Shift to Electric Mobility</em>, finds that early-stage EVs receive tighter loan terms than comparable internal-combustion vehicles: higher interest rates, lower loan-to-value ratios, and shorter durations [<a href="#r1">1</a>][<a href="#r2">2</a>]. The dominant mechanism is technological obsolescence risk. Rapid battery and powertrain innovation lowers expected resale values, which raises collateral risk for lenders. Buyer demographics, lender market power, and macro conditions explain little of the spread once technology risk is accounted for.</p>
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
    ],
})

# 8 Industrial processes
POSTS.append({
    "slug": "industrial-processes",
    "num": "08",
    "sector": "Industrial Processes",
    "viz_key": "industrial",
    "card_title": "Hard-to-abate industry is shifting from pilots to playbooks",
    "card_blurb": "Stanford and Berkeley research on steel, cement, heat, and abatement costs is turning industrial decarbonization into transferable methods.",
    "meta": "Research note · August 1, 2026 · Sector 08",
    "title": "Hard-to-abate industry is shifting from pilots to playbooks",
    "dek": "Cement, steel, and chemicals will not decarbonize through one breakthrough. They need sequenced process options with public cost evidence.",
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
    ],
})


def write_posts():
    cards = []
    for p in POSTS:
        viz_html = VIZ.get(p.get("viz_key", ""), "")
        html = page(
            p["title"],
            p["description"],
            article(p["meta"], p["title"], p["dek"], p["body"], p["refs"], viz_html=viz_html),
        )
        (ROOT / f"{p['slug']}.html").write_text(html, encoding="utf-8")
        cards.append(p)
        print("wrote", p["slug"])

    card_html = "\n".join(
        f'''        <a class="post-card" href="{p['slug']}.html">
          <p class="meta">{p['num']} · {p['sector']}</p>
          <h2>{p['card_title']}</h2>
          <p>{p['card_blurb']}</p>
        </a>'''
        for p in cards
    )

    index = page(
        "Research notes",
        "Maiti Labs research notes on emerging technologies across climate sectors.",
        f'''  <header class="page-hero">
    <div class="wrap">
      <p class="eyebrow">Research notes</p>
      <h1>Emerging tech, by sector.</h1>
      <p class="lede">Easy-to-read notes with visuals on climate tech, with research from Stanford, Berkeley, Caltech, Harvard, Wharton, and leading labs.</p>
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
