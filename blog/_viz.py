"""Inline SVG infographics for sector research notes."""

def viz_figure(svg_inner, caption):
    return f'''      <figure class="viz">
{svg_inner}
        <figcaption class="viz-caption">{caption}</figcaption>
      </figure>'''

VIZ = {
    "weather": viz_figure(
        '''        <svg aria-hidden="true" class="viz-svg" viewBox="0 0 640 240" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <marker id="w-arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#204028"/></marker>
          </defs>
          <rect width="640" height="240" fill="#faf7ef" rx="8"/>
          <text x="320" y="28" text-anchor="middle" fill="#204028" font-size="13" font-weight="600" font-family="Outfit,sans-serif">Two ways to forecast weather</text>
          <g class="viz-fade-slide">
            <rect x="24" y="52" width="120" height="44" rx="10" fill="#f0e8cc" stroke="#204028" stroke-width="1.2"/>
            <text x="84" y="78" text-anchor="middle" fill="#204028" font-size="11" font-family="Outfit,sans-serif">Past weather data</text>
            <line class="viz-draw" x1="144" y1="74" x2="188" y2="74" stroke="#204028" stroke-width="2" marker-end="url(#w-arrow)"/>
            <rect x="188" y="52" width="100" height="44" rx="10" fill="#204028"/>
            <text x="238" y="78" text-anchor="middle" fill="#f0e8cc" font-size="11" font-family="Outfit,sans-serif">AI model</text>
            <line class="viz-draw" x1="288" y1="74" x2="332" y2="74" stroke="#204028" stroke-width="2" marker-end="url(#w-arrow)"/>
            <rect class="viz-pulse" x="332" y="48" width="130" height="52" rx="10" fill="#2d5640"/>
            <text x="397" y="72" text-anchor="middle" fill="#f0e8cc" font-size="11" font-weight="600" font-family="Outfit,sans-serif">Fast forecast</text>
            <text x="397" y="88" text-anchor="middle" fill="#f0e8cc" font-size="10" font-family="Outfit,sans-serif">minutes</text>
          </g>
          <g class="viz-fade-slide" style="animation-delay:.35s">
            <rect x="24" y="138" width="120" height="44" rx="10" fill="#f0e8cc" stroke="#5a6a5c" stroke-width="1.2"/>
            <text x="84" y="164" text-anchor="middle" fill="#5a6a5c" font-size="11" font-family="Outfit,sans-serif">Supercomputer</text>
            <line x1="144" y1="160" x2="332" y2="160" stroke="#5a6a5c" stroke-width="1.5" stroke-dasharray="6 4" marker-end="url(#w-arrow)"/>
            <rect x="332" y="134" width="130" height="52" rx="10" fill="#f4f0e4" stroke="#5a6a5c" stroke-width="1.2"/>
            <text x="397" y="158" text-anchor="middle" fill="#5a6a5c" font-size="11" font-family="Outfit,sans-serif">Classical forecast</text>
            <text x="397" y="174" text-anchor="middle" fill="#5a6a5c" font-size="10" font-family="Outfit,sans-serif">hours</text>
          </g>
          <text x="520" y="100" fill="#5a6a5c" font-size="10" font-family="Outfit,sans-serif">New path</text>
          <text x="520" y="186" fill="#5a6a5c" font-size="10" font-family="Outfit,sans-serif">Old path</text>
        </svg>''',
        "New AI models learn from past weather and produce forecasts in minutes. Traditional physics models on supercomputers still matter, but they take much longer.",
    ),
    "aerospace": viz_figure(
        '''        <svg aria-hidden="true" class="viz-svg" viewBox="0 0 640 220" xmlns="http://www.w3.org/2000/svg">
          <rect width="640" height="220" fill="#faf7ef" rx="8"/>
          <text x="320" y="28" text-anchor="middle" fill="#204028" font-size="13" font-weight="600" font-family="Outfit,sans-serif">From satellite pixels to useful maps</text>
          <g class="viz-float">
            <rect x="40" y="55" width="90" height="50" rx="8" fill="#f0e8cc" stroke="#204028"/>
            <text x="85" y="78" text-anchor="middle" fill="#204028" font-size="10" font-family="Outfit,sans-serif">Optical</text>
            <text x="85" y="92" text-anchor="middle" fill="#204028" font-size="10" font-family="Outfit,sans-serif">satellite</text>
          </g>
          <g class="viz-float" style="animation-delay:.4s">
            <rect x="40" y="120" width="90" height="50" rx="8" fill="#f0e8cc" stroke="#204028"/>
            <text x="85" y="143" text-anchor="middle" fill="#204028" font-size="10" font-family="Outfit,sans-serif">Radar</text>
            <text x="85" y="157" text-anchor="middle" fill="#204028" font-size="10" font-family="Outfit,sans-serif">(SAR)</text>
          </g>
          <line class="viz-draw" x1="130" y1="80" x2="200" y2="110" stroke="#204028" stroke-width="2"/>
          <line class="viz-draw" x1="130" y1="145" x2="200" y2="115" stroke="#204028" stroke-width="2"/>
          <rect class="viz-pulse" x="200" y="88" width="120" height="54" rx="12" fill="#204028"/>
          <text x="260" y="112" text-anchor="middle" fill="#f0e8cc" font-size="11" font-weight="600" font-family="Outfit,sans-serif">One flexible</text>
          <text x="260" y="128" text-anchor="middle" fill="#f0e8cc" font-size="11" font-family="Outfit,sans-serif">AI model</text>
          <line class="viz-draw" x1="320" y1="115" x2="380" y2="115" stroke="#204028" stroke-width="2"/>
          <g class="viz-fade-slide">
            <rect x="380" y="52" width="100" height="36" rx="8" fill="#2d5640"/>
            <text x="430" y="74" text-anchor="middle" fill="#f0e8cc" font-size="10" font-family="Outfit,sans-serif">Floods</text>
            <rect x="380" y="96" width="100" height="36" rx="8" fill="#2d5640"/>
            <text x="430" y="118" text-anchor="middle" fill="#f0e8cc" font-size="10" font-family="Outfit,sans-serif">Crops</text>
            <rect x="380" y="140" width="100" height="36" rx="8" fill="#2d5640"/>
            <text x="430" y="162" text-anchor="middle" fill="#f0e8cc" font-size="10" font-family="Outfit,sans-serif">Emissions</text>
          </g>
        </svg>''',
        "Foundation models train on many satellite types, then adapt quickly to tasks like flood mapping, crop monitoring, or emissions tracking.",
    ),
    "materials": viz_figure(
        '''        <svg aria-hidden="true" class="viz-svg" viewBox="0 0 640 220" xmlns="http://www.w3.org/2000/svg">
          <rect width="640" height="220" fill="#faf7ef" rx="8"/>
          <text x="320" y="28" text-anchor="middle" fill="#204028" font-size="13" font-weight="600" font-family="Outfit,sans-serif">Cement emissions: two routes</text>
          <rect x="48" y="50" width="240" height="140" rx="12" fill="#f4f0e4" stroke="#5a6a5c" stroke-width="1.2"/>
          <text x="168" y="78" text-anchor="middle" fill="#5a6a5c" font-size="12" font-weight="600" font-family="Outfit,sans-serif">Limestone cement</text>
          <ellipse class="viz-pulse" cx="168" cy="120" rx="55" ry="28" fill="none" stroke="#8a7060" stroke-width="1.5" opacity=".6"/>
          <ellipse cx="168" cy="120" rx="35" ry="18" fill="#8a7060" opacity=".35"/>
          <text x="168" y="125" text-anchor="middle" fill="#5a6a5c" font-size="10" font-family="Outfit,sans-serif">CO₂ from chemistry</text>
          <rect x="352" y="50" width="240" height="140" rx="12" fill="#f0e8cc" stroke="#204028" stroke-width="1.2"/>
          <text x="472" y="78" text-anchor="middle" fill="#204028" font-size="12" font-weight="600" font-family="Outfit,sans-serif">New rock &amp; recycle</text>
          <circle cx="420" cy="125" r="22" fill="#204028" opacity=".25"/>
          <circle cx="472" cy="115" r="18" fill="#2d5640" opacity=".35"/>
          <circle cx="520" cy="130" r="20" fill="#204028" opacity=".2"/>
          <text x="472" y="168" text-anchor="middle" fill="#204028" font-size="10" font-family="Outfit,sans-serif">Smaller CO₂ footprint</text>
        </svg>''',
        "Most cement CO₂ comes from heating limestone. Labs are testing rock blends without carbonate and ways to recycle old concrete to cut those chemistry emissions.",
    ),
    "energy": viz_figure(
        '''        <svg aria-hidden="true" class="viz-svg" viewBox="0 0 640 220" xmlns="http://www.w3.org/2000/svg">
          <rect width="640" height="220" fill="#faf7ef" rx="8"/>
          <text x="320" y="28" text-anchor="middle" fill="#204028" font-size="13" font-weight="600" font-family="Outfit,sans-serif">Balancing sun and wind on the grid</text>
          <g class="viz-float">
            <circle cx="80" cy="100" r="28" fill="#f0e8cc" stroke="#204028"/>
            <text x="80" y="105" text-anchor="middle" fill="#204028" font-size="18">☀</text>
          </g>
          <g class="viz-float" style="animation-delay:.3s">
            <path d="M140 115 Q155 85 175 100 Q195 70 210 115" fill="none" stroke="#204028" stroke-width="2"/>
            <text x="175" y="135" text-anchor="middle" fill="#5a6a5c" font-size="10" font-family="Outfit,sans-serif">wind</text>
          </g>
          <line class="viz-draw" x1="220" y1="100" x2="270" y2="100" stroke="#204028" stroke-width="2"/>
          <rect x="270" y="72" width="100" height="56" rx="10" fill="#204028"/>
          <text x="320" y="96" text-anchor="middle" fill="#f0e8cc" font-size="10" font-family="Outfit,sans-serif">Short battery</text>
          <text x="320" y="112" text-anchor="middle" fill="#f0e8cc" font-size="9" font-family="Outfit,sans-serif">hours</text>
          <line class="viz-draw" x1="370" y1="100" x2="420" y2="100" stroke="#204028" stroke-width="2"/>
          <rect class="viz-pulse" x="420" y="68" width="110" height="64" rx="10" fill="#2d5640"/>
          <text x="475" y="94" text-anchor="middle" fill="#f0e8cc" font-size="10" font-weight="600" font-family="Outfit,sans-serif">Long storage</text>
          <text x="475" y="110" text-anchor="middle" fill="#f0e8cc" font-size="9" font-family="Outfit,sans-serif">days to weeks</text>
          <line class="viz-draw" x1="530" y1="100" x2="580" y2="100" stroke="#204028" stroke-width="2"/>
          <rect x="560" y="85" width="60" height="30" rx="6" fill="#f0e8cc" stroke="#204028"/>
          <text x="590" y="104" text-anchor="middle" fill="#204028" font-size="10" font-family="Outfit,sans-serif">Grid</text>
          <text x="320" y="175" text-anchor="middle" fill="#5a6a5c" font-size="11" font-family="Outfit,sans-serif">Steady power through nights and calm weeks</text>
        </svg>''',
        "Solar and wind vary by hour and season. Short batteries cover evenings; long-duration storage helps keep clean grids reliable over multi-day gaps.",
    ),
    "manufacturing": viz_figure(
        '''        <svg aria-hidden="true" class="viz-svg" viewBox="0 0 640 200" xmlns="http://www.w3.org/2000/svg">
          <rect width="640" height="200" fill="#faf7ef" rx="8"/>
          <text x="320" y="28" text-anchor="middle" fill="#204028" font-size="13" font-weight="600" font-family="Outfit,sans-serif">Factory heat: old vs new</text>
          <rect x="40" y="55" width="250" height="115" rx="12" fill="#f4f0e4" stroke="#5a6a5c"/>
          <text x="165" y="82" text-anchor="middle" fill="#5a6a5c" font-size="11" font-weight="600" font-family="Outfit,sans-serif">Fossil flame</text>
          <path d="M145 105 Q165 85 185 105 Q205 80 225 105" fill="#c06040" opacity=".7"/>
          <text x="185" y="130" text-anchor="middle" fill="#5a6a5c" font-size="10" font-family="Outfit,sans-serif">gas or coal burn</text>
          <rect x="95" y="140" width="140" height="22" rx="4" fill="#5a6a5c" opacity=".3"/>
          <text x="165" y="155" text-anchor="middle" fill="#5a6a5c" font-size="9" font-family="Outfit,sans-serif">factory</text>
          <rect x="350" y="55" width="250" height="115" rx="12" fill="#f0e8cc" stroke="#204028"/>
          <text x="475" y="82" text-anchor="middle" fill="#204028" font-size="11" font-weight="600" font-family="Outfit,sans-serif">Electric &amp; solar heat</text>
          <circle class="viz-pulse" cx="430" cy="108" r="16" fill="#204028" opacity=".2"/>
          <text x="430" y="113" text-anchor="middle" fill="#204028" font-size="14">⚡</text>
          <circle class="viz-float" cx="520" cy="100" r="14" fill="#f0e8cc" stroke="#204028"/>
          <text x="520" y="105" text-anchor="middle" fill="#204028" font-size="12">☀</text>
          <rect x="405" y="140" width="140" height="22" rx="4" fill="#204028" opacity=".25"/>
          <text x="475" y="155" text-anchor="middle" fill="#204028" font-size="9" font-family="Outfit,sans-serif">same factory, cleaner heat</text>
        </svg>''',
        "Much factory carbon comes from burning fuel for heat. Electrification and solar-driven reactors aim to deliver the same temperatures without combustion.",
    ),
    "built": viz_figure(
        '''        <svg aria-hidden="true" class="viz-svg" viewBox="0 0 640 240" xmlns="http://www.w3.org/2000/svg">
          <rect width="640" height="240" fill="#faf7ef" rx="8"/>
          <text x="320" y="28" text-anchor="middle" fill="#204028" font-size="13" font-weight="600" font-family="Outfit,sans-serif">Carbon in a building's life</text>
          <rect x="220" y="48" width="200" height="130" rx="6" fill="#f0e8cc" stroke="#204028" stroke-width="1.5"/>
          <polygon points="220,48 320,18 420,48" fill="#204028" opacity=".15" stroke="#204028"/>
          <line x1="270" y1="48" x2="270" y2="178" stroke="#204028" stroke-width="1" opacity=".4"/>
          <line x1="370" y1="48" x2="370" y2="178" stroke="#204028" stroke-width="1" opacity=".4"/>
          <rect x="48" y="70" width="140" height="90" rx="10" fill="#2d5640" class="viz-pulse"/>
          <text x="118" y="100" text-anchor="middle" fill="#f0e8cc" font-size="11" font-weight="600" font-family="Outfit,sans-serif">Embodied</text>
          <text x="118" y="118" text-anchor="middle" fill="#f0e8cc" font-size="9" font-family="Outfit,sans-serif">steel, concrete,</text>
          <text x="118" y="132" text-anchor="middle" fill="#f0e8cc" font-size="9" font-family="Outfit,sans-serif">materials</text>
          <line class="viz-draw" x1="188" y1="115" x2="218" y2="115" stroke="#204028" stroke-width="2"/>
          <rect x="452" y="70" width="140" height="90" rx="10" fill="#204028" class="viz-float"/>
          <text x="522" y="100" text-anchor="middle" fill="#f0e8cc" font-size="11" font-weight="600" font-family="Outfit,sans-serif">Operating</text>
          <text x="522" y="118" text-anchor="middle" fill="#f0e8cc" font-size="9" font-family="Outfit,sans-serif">heat, power,</text>
          <text x="522" y="132" text-anchor="middle" fill="#f0e8cc" font-size="9" font-family="Outfit,sans-serif">daily use</text>
          <line class="viz-draw" x1="422" y1="115" x2="452" y2="115" stroke="#204028" stroke-width="2"/>
          <line x1="120" y1="200" x2="520" y2="200" stroke="#5a6a5c" stroke-width="2"/>
          <circle class="viz-float" cx="320" cy="200" r="10" fill="#204028"/>
          <text x="320" y="225" text-anchor="middle" fill="#5a6a5c" font-size="10" font-family="Outfit,sans-serif">Balance shifts as grids get cleaner</text>
        </svg>''',
        "Embodied carbon is locked in at construction. Operating carbon comes from years of energy use. On cleaner grids, materials often matter more.",
    ),
    "mobility": viz_figure(
        '''        <svg aria-hidden="true" class="viz-svg" viewBox="0 0 640 220" xmlns="http://www.w3.org/2000/svg">
          <rect width="640" height="220" fill="#faf7ef" rx="8"/>
          <text x="320" y="28" text-anchor="middle" fill="#204028" font-size="13" font-weight="600" font-family="Outfit,sans-serif">Two gates to EV adoption</text>
          <rect x="240" y="55" width="160" height="50" rx="10" fill="#204028"/>
          <text x="320" y="85" text-anchor="middle" fill="#f0e8cc" font-size="12" font-family="Outfit,sans-serif">Electric car</text>
          <line class="viz-draw" x1="280" y1="105" x2="200" y2="140" stroke="#204028" stroke-width="2"/>
          <line class="viz-draw" x1="360" y1="105" x2="440" y2="140" stroke="#204028" stroke-width="2"/>
          <rect class="viz-pulse" x="100" y="140" width="200" height="56" rx="12" fill="#f0e8cc" stroke="#204028" stroke-width="1.2"/>
          <text x="200" y="165" text-anchor="middle" fill="#204028" font-size="11" font-weight="600" font-family="Outfit,sans-serif">Charger reliability</text>
          <text x="200" y="182" text-anchor="middle" fill="#5a6a5c" font-size="9" font-family="Outfit,sans-serif">works when you need it</text>
          <rect class="viz-pulse" x="340" y="140" width="200" height="56" rx="12" fill="#f0e8cc" stroke="#204028" stroke-width="1.2" style="animation-delay:.25s"/>
          <text x="440" y="165" text-anchor="middle" fill="#204028" font-size="11" font-weight="600" font-family="Outfit,sans-serif">Loan terms</text>
          <text x="440" y="182" text-anchor="middle" fill="#5a6a5c" font-size="9" font-family="Outfit,sans-serif">affordable financing</text>
        </svg>''',
        "Better batteries help, but drivers also need chargers that work and loans that match gasoline-car terms.",
    ),
    "industrial": viz_figure(
        '''        <svg aria-hidden="true" class="viz-svg" viewBox="0 0 640 240" xmlns="http://www.w3.org/2000/svg">
          <rect width="640" height="240" fill="#faf7ef" rx="8"/>
          <text x="320" y="28" text-anchor="middle" fill="#204028" font-size="13" font-weight="600" font-family="Outfit,sans-serif">Hard industries need a playbook</text>
          <g class="viz-steps">
            <rect x="32" y="55" width="88" height="48" rx="8" fill="#f0e8cc" stroke="#204028"/>
            <text x="76" y="82" text-anchor="middle" fill="#204028" font-size="10" font-family="Outfit,sans-serif">Cement</text>
            <rect x="32" y="115" width="88" height="48" rx="8" fill="#f0e8cc" stroke="#204028"/>
            <text x="76" y="142" text-anchor="middle" fill="#204028" font-size="10" font-family="Outfit,sans-serif">Steel</text>
            <rect x="32" y="175" width="88" height="48" rx="8" fill="#f0e8cc" stroke="#204028"/>
            <text x="76" y="202" text-anchor="middle" fill="#204028" font-size="10" font-family="Outfit,sans-serif">Chemicals</text>
          </g>
          <line class="viz-draw" x1="120" y1="110" x2="180" y2="110" stroke="#204028" stroke-width="2"/>
          <rect class="viz-pulse" x="180" y="78" width="140" height="64" rx="12" fill="#204028"/>
          <text x="250" y="105" text-anchor="middle" fill="#f0e8cc" font-size="11" font-weight="600" font-family="Outfit,sans-serif">Decarbonization</text>
          <text x="250" y="122" text-anchor="middle" fill="#f0e8cc" font-size="11" font-family="Outfit,sans-serif">playbook</text>
          <line class="viz-draw" x1="320" y1="110" x2="360" y2="110" stroke="#204028" stroke-width="2"/>
          <g class="viz-fade-slide">
            <rect x="360" y="52" width="115" height="40" rx="8" fill="#2d5640"/>
            <text x="417" y="76" text-anchor="middle" fill="#f0e8cc" font-size="10" font-family="Outfit,sans-serif">Clean heat</text>
            <rect x="360" y="100" width="115" height="40" rx="8" fill="#2d5640"/>
            <text x="417" y="124" text-anchor="middle" fill="#f0e8cc" font-size="10" font-family="Outfit,sans-serif">New materials</text>
            <rect x="360" y="148" width="115" height="40" rx="8" fill="#2d5640"/>
            <text x="417" y="172" text-anchor="middle" fill="#f0e8cc" font-size="10" font-family="Outfit,sans-serif">Cost tools</text>
          </g>
          <rect x="500" y="70" width="120" height="80" rx="10" fill="#f4f0e4" stroke="#5a6a5c"/>
          <text x="560" y="100" text-anchor="middle" fill="#5a6a5c" font-size="10" font-family="Outfit,sans-serif">Public evidence</text>
          <text x="560" y="118" text-anchor="middle" fill="#5a6a5c" font-size="10" font-family="Outfit,sans-serif">for plant</text>
          <text x="560" y="136" text-anchor="middle" fill="#5a6a5c" font-size="10" font-family="Outfit,sans-serif">decisions</text>
        </svg>''',
        "Cement, steel, and chemicals won't decarbonize from one invention. Research is bundling heat options, material swaps, and cost curves into playbooks operators can use.",
    ),
}
