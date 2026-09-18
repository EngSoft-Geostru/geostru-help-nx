# MP NX — Piles and micropiles

**MP NX** analyses and designs a **single foundation pile** or a **single micropile**:
ultimate vertical and lateral load, design resistances to NTC 2018 and EN 1997-1, internal
forces along the shaft from a finite-element model, reinforced-concrete section check,
reinforcement cage and settlement. The calculation engine is that of MP, the GeoStru desktop
program for piles, brought to the web.

[**Open the app**](https://nx.geostru.ai/mp/){ .md-button .md-button--primary }

## Who it is for

Geotechnical and structural engineers, geologists, design offices and contractors who need
to size a pile or a micropile and deliver a calculation report. Interface and report are
available in **Italian** and **English**.

## What it does

- **Ultimate vertical load** (base + shaft) for each investigation vertical, in compression
  and in tension, with multiple stratigraphies, water table, undrained layers, rock layers,
  negative skin friction and tapered piles.
- **Characteristic and design resistances** with the correlation factors ξ~3~ and ξ~4~ and
  the factors γ~b~, γ~s~: NTC 2018, EN 1997-1 (also with the Romanian national annex) or
  global factors.
- **Ultimate lateral load** with Broms' method.
- **Micropiles**, Tubifix and Radice, with bulb, bar or tubular reinforcement.
- **FEM analysis** of the pile as a beam on Winkler elastic soil, linear or non-linear.
- **ULS check** in bending with axial force and in shear of the circular section, node by
  node, with the N-M interaction domain, the **cage shop drawing** and the **bar schedule**.
- **Settlement** of the single pile with the Poulos and Davis method.
- **Calculation report** in Word and PDF, DXF drawing, 2D and 3D views.

You enter the data in the cards of the **Parameters** tab; the preview on the right follows
every change.

![MP NX Parameters tab: project tree on the left, data cards in the middle, section preview on the right](img/01-parametri.png)

## What it does not do

MP NX covers the single pile and the single micropile. It does **not** cover:

- pile groups and group efficiency;
- screw piles, jet grouting, stone columns, steel or timber piles;
- micropile networks, raked micropiles, critical buckling load of the micropile;
- node-by-node ULS check of the composite tube + grout section of the tubular micropile;
- settlement with Fleming's hyperbolic method, dynamic formulae, pressuremeter tests as a
  pile input;
- the full NTC seismic hazard and kinematic bending moments: seismic action enters as a
  correction of the ultimate load, starting from a/g.

The limits of the model are discussed in [Code validation](validazione.md).

## How you pay

MP NX runs on **credits**, charged only when an operation succeeds.

| Operation | Credits |
|---|---|
| **Calculate** | 8 |
| FEM analysis and section design, when enabled | + 5 |
| DXF drawing or cage DXF | 10 |
| Report (Word or PDF) | 10 |
| Message to the AI assistant | 3 |

Preview, drawings, 3D view, report preview, saving the project and the PNG image of the
section cost no credits. If an operation fails, nothing is charged. Changing the rules of
the cage shop drawing redraws it at no charge.

## Where to start

1. [Quick start](quickstart.md) — from the opening project to the report in 5 minutes.
2. [Pile and footing](palo.md), [Micropiles](micropali.md), [Materials](materiali.md) — geometry and section.
3. [Stratigraphies and water table](stratigrafia.md) — the ground and the investigation verticals.
4. [Loads, combinations and design code](combinazioni.md) — actions, signs and factors.
5. [Ultimate load](carico-limite.md), [FEM analysis](fem.md), [Sections and reinforcement](armature.md), [Settlements](cedimenti.md) — the results.
6. [Report, exports and assistant](relazione.md), [Example projects](esempi.md), [Code validation](validazione.md), [FAQ](faq.md).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MP%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mp/docs/en/index.md).*
