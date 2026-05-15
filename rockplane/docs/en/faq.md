# FAQ

## General

### Is RockPlane NX free?

Yes. The app is available **free of charge in the geostru.ai free plan**. Just sign up at [geostru.ai](https://geostru.ai) and open RockPlane from your dashboard.

### Do I need to install anything?

No. RockPlane NX is a **web app**: it runs in the browser. No local install, no licence key, no dongle. Recommended browsers: Chrome, Edge, Safari, Firefox (latest version).

### Does it work offline?

The app needs an internet connection to load and to compute (the calculation runs on the server). The 2D section and 3D viewport run in the browser and are interactive even with intermittent connection.

### Is my data secure?

Project data lives in your browser session. Files are saved as `.rockplane` (JSON) on your local disk via the File System Access API. The server processes calculations but does not persist project data.

## Model

### What failure mechanisms does RockPlane analyse?

**Planar failure only** (Hoek-Bray): single persistent discontinuity with daylighting, 2D rigid wedge. For other mechanisms:

- **Wedge failure** (two intersecting discontinuities) → different software
- **Toppling** (Goodman-Bray) → different software
- **Circular failure** (slope stability with Bishop / Spencer / Morgenstern-Price) → different software

### Mohr-Coulomb or Barton-Bandis — which one should I use?

- **Mohr-Coulomb**: simple, classical, good for preliminary design or when cohesion is known from tests.
- **Barton-Bandis**: more representative for **rough rock joints at low confining stress** (typical in rock slopes). Includes roughness dilation i_eff which can be significant.

In practice, use **Barton-Bandis** for rock slope projects whenever you can characterise the joint with JRC and JCS (Schmidt hammer + roughness profile).

### Can I model a wedge formed by two discontinuities?

No. RockPlane NX models **only planar failure** (one discontinuity). For 2-discontinuity wedge failure see **WedgeFail** (different GeoStru tool).

## Reinforcement

### Active anchor vs passive nail?

- **Active anchor** (tirante): pre-stressed during installation. Pre-load applied as **action**. Reduces driving shear S directly. Typical for permanent works requiring controlled stabilisation.
- **Passive nail** (chiodo): no pre-load. Mobilises force only when the wedge moves. Adds **resistance** via friction increase + Clouterre N-V interaction. Simpler and cheaper.

For the same single capacity F, active anchors are slightly more effective; passive nails are simpler to install and don't need tensioning equipment.

### How does the Clouterre N-V interaction work?

A passive nail crossing the failure plane works in both axial T and shear V. The Clouterre 1993 linear envelope is:

\[ T/T_{max} + V/V_{max} \le 1 \]

The optimum is on one of the two axes (axial mode T=T_max,V=0 or shear mode T=0,V=V_max). The software picks the one that maximises the stabilising contribution to τ.

### What's the difference between mesh nails and structural nails?

- **Mesh fixing nails** (short, in the R1 corticale): only hold the mesh against the rock. Already represented by `T_nail / mesh_area = q`. **Don't** add them as separate reinforcement.
- **Structural nails** (long, cross the failure plane): contribute to wedge stability directly. **Do** add them as `PassiveNail` reinforcement.

Rule of thumb: if nail length ≥ 1.5× depth of the failure plane → structural.

## Code

### Which code should I select?

- **Characteristic (γ = 1.0)**: pre-design, comparison, didactic. NOT for executive design.
- **NTC 2018 (A2+M2+R2)**: standard for Italian projects.
- **EC7 DA1/DA2/DA3**: for European projects following Eurocode 7.

### What is FS_required for NTC 2018?

In NTC 2018 §6.8 A2+M2+R2 set, FS_required = 1.00 (the partial factors already incorporate the safety margin). Equivalent characteristic FS ≈ 1.30 with all γ=1.0.

### What about the seismic in NTC §3.2 / §7.11.3?

NTC pseudo-static slope analysis uses k<sub>h</sub> = β<sub>s</sub> · a<sub>max</sub> / g (NTC Tab. 7.11.I). RockPlane takes the final k<sub>h</sub> as input — you calculate it from the site classification yourself.

## Practical use

### Why does FS not change when I add seismic if c = 0?

With c = 0 and E ≈ vertical, N and S increase proportionally, so FS = tan φ / tan α is invariant. This is a known result in granular planar slopes. Add some cohesion or a horizontal external load to see FS change.

### Why does the 3D view "jump" when I change a parameter?

That bug is fixed in the latest version: the camera position stays where you left it (after the first user interaction). If you see it resetting, hard-refresh the page (Ctrl+Shift+R).

### The α critical search returns a negative FS — bug?

Pre-fix behaviour. The latest version filters degenerate cases (thin sliver wedges with reinforcement) and shows a warning when no physically valid α exists in the admissible range.

## Export

### Can I open the DXF in AutoCAD?

Yes, the DXF is R12 format compatible with AutoCAD, BricsCAD, DraftSight, Trispace.

### Why is there a 5-minute limit on the Trispace handoff token?

The token URL is publicly fetchable while valid. A short TTL (5 min) minimises the exposure window. The token is also use-and-discard: once consumed, it's removed from the cache.

### Why don't I see RockPlane in the help.nx.geostru.ai landing?

The deployment workflow rebuilds the landing index every push. If RockPlane is missing, check that `.github/workflows/deploy.yml` includes the product in its `products` array.
