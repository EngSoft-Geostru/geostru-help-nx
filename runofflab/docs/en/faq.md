# FAQ — frequently asked questions

## General

### What do I need to get started?

At least an annual-maxima series for one duration (ideally 5 durations and
≥ 15 years of data). If you don't have data, load one of the Calabria
samples from the Info modal → Resources.

### Can I use Runoff Lab without internet?

For **operational use** yes: the app runs in the browser and saves to
localStorage. Only **AI Import** requires connectivity (calls a backend model).

### Does my data stay private?

Yes. The study is saved in your browser (localStorage) and the local
`.hgstudy` file. Nothing is sent to the server **except**:
- AI Import sends the file to the backend (not retained);
- PDF export if it contains server-side generated images.

## Save and crash recovery

### I closed the tab without saving. Can I recover?

Yes. Reopen the app: browser autosave restores the session automatically.
For safety, save a `.hgstudy` with `Ctrl+Shift+S`: it's a portable JSON.

### The "unsaved changes" badge stays on

It means the browser autosave is up-to-date but you haven't downloaded the
final `.hgstudy` for your most recent change. Press `Ctrl+S` (autosave) or
`Ctrl+Shift+S` (file download) to archive it.

## Series and durations

### How many years do I need?

- **Below 10 years**: very uncertain estimates; use only for exercises.
- **10-20 years**: usable with care, prefer Gumbel-moments or L-moment
  methods.
- **>20 years**: all probabilistic families are comparable.
- **>50 years**: even TCEV level 0 (pointwise) becomes reliable.

### Can I use durations other than the standard ones?

Yes. You can add custom durations in the study (e.g. 30′, 45′, 90′). All
analyses use them if there are ≥ 2 values.

### The 60' duration has 5 years and 24h has 30. What happens?

Each duration is analysed independently. The 60' will come out with high
uncertainty, the 24h will be robust. The rainfall curves will have a good
fit at long durations and less so at short ones — watch the \(R^2\).

## Analyses

### Which family should I pick?

Start with **Gumbel-moments**: simple, accepted by almost all authorities.
Add a second family for **comparison** (GEV-Lmoments or TCEV-1) and
document both in the final report.

### Can I compare multiple analyses?

Yes. Add as many as you want in the same study: the page shows a
side-by-side table with each method's \(h(T)\) values.

### TCEV doesn't appear in the menu

The TCEV section is visible only with the interface in **Italian**: the
VA.PI. dataset is specific to Italian regions. Switch the language to IT
from the language menu.

## Rainfall curves

### My curve's \(R^2\) is 0.85 — what do I do?

The law \(h = a \cdot t^n\) doesn't fit well. Possible causes:

- **Sparse series** at some durations → unstable analysis.
- **Climatic discontinuities** or rain-gauge relocation.
- **Mountain basin** where short and long durations follow different regimes.

Try: TCEV level 3 (more parameters); or build separate curves for groups
of durations (short vs long).

### Which return period for design?

Typical Italian standards:

- **Urban sewerage**: T = 5–10 years.
- **Minor culverts and crossings**: T = 25–50 years.
- **Hydraulic mitigation works, detention basins**: T = 100–200 years.
- **Settlement defence (PAI)**: T = 200 years and sometimes T = 500.

## SCS-CN

### What CN for a mixed area?

Use the **CN wizard** in the hydrograph panel: split the basin into
sub-areas, assign soil type (A/B/C/D) and cover to each; the area-weighted
CN is computed automatically.

### How do I estimate Tlag?

Tlag wizard: enter A (km²), L (km, main channel), average slope i (%).
You get \(T_c\) with 4 classical formulas (Kirpich, Giandotti, Pasini,
Pezzoli) and the suggested \(T_{\text{lag}}\) as \(0.6 \cdot T_c\).

### My basin is 500 km², does SCS-CN still work?

Marginally. SCS-CN works best under 250 km² with concentration times
< 24 h. For larger basins use a distributed model (not implemented in
Runoff Lab — use dedicated software like HEC-HMS).

## AI Import

### The AI made a mistake on one value

Open the preview → edit the cell directly → confirm. Manual corrections
survive.

### The PDF is poorly scanned — does it still work?

Generally yes, but inspect the preview carefully. If OCR quality is low,
open the PDF, copy the text manually from the table, and paste in the
modal's "free text" box.

### How many credits does an import cost?

10 credits (\(\text{rainfall.import.ai}\)). Visible on the wallet chip
before confirmation; rejected if the balance isn't enough.

## Export

### Can I export only one section?

For now the report is single and contains the whole study. If you want
only the curves, delete the other sections before export — or trim the
PDF afterwards.

### The formulas look broken in the PDF

All formulas are rendered via MathJax in HTML and converted to SVG in the
PDF. If you see raw code (`\frac{...}` literal), there's a bug:
[report it](mailto:info@geostru.ai?subject=Bug%20Runoff%20Lab%20NX%20-%20formule).

## Common errors

### "No valid item for the computation"

Analyses require ≥ 2 values per duration. Check in the Station section that
at least two non-empty rows exist for each duration you want to use.

### "Curves not available"

To create a curve you need at least **one completed analysis**. First go
to the Analyses panel and add at least one.

### "Hydrograph not available"

The SCS-CN hydrograph requires a **synthetic hyetograph** already built
(or a direct curve + duration). Build a hyetograph first in its dedicated
panel.
