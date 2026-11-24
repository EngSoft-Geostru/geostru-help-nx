# Validation and limits

Validation documents the scope, theoretical basis, test cases and known differences of the calculation code. It helps the designer assess the reliability of the program, as required by point 10.2 of NTC 2018.

It is not a certification: no third party is involved. It does not replace the check of the model, data and results by whoever signs the design.

The general reference is the page [Validation of the calculation code](https://geostru.ai/en/validation/). The version of the calculation engine is printed in the «Calculation code» block of every report.

## How the engine was checked

- **Cases solved by hand** with the literature formulas given in [Theory](teoria.md): homogeneous dry soil, a single nail, uniform load, line load, earth pressure coefficients;
- **comparison with worked examples**, on projects covering the design codes, seismic action, water table, loads, the choices of β and Bl and different nails;
- **declared differences**: where the result differs from a reference, the difference is explained, not hidden.

## What it covers

- soil nail walls built from the top down by excavation stages, one stage per nail;
- facing inclined by θ from the vertical (0–90°) and backslope inclined by ε (0–90°);
- layered soil; the layer below the base is the foundation soil;
- nails with their own depth, length, inclination, diameters, fy and kn; one horizontal spacing;
- uniform, strip and line surcharges, each with its own factor A;
- horizontal water table at a given depth;
- pseudo-static seismic action with kh and kv;
- checks of nail failure and pull-out, internal stability by stage, sliding of the block, facing diagrams.

## What it does not cover

- **global stability** for surfaces passing behind or below the nails: use a slope stability program, such as GeoStru Slope;
- the **structural check of the facing section** and of the nail head: SNL NX gives only the diagrams;
- displacements and serviceability, seepage, undrained conditions;
- the search for the critical surface: β is assigned or 45° + φ̄'/2, not searched for the minimum safety factor.

## Method assumptions to keep in mind

- **Planar wedge** for each stage, starting at the bottom of the stage excavation; soil parameters are thickness-weighted means over the excavated layers.
- **One combination** A/M/R per project, with one R factor per check. To apply different approaches to different checks, calculate the project more than once. Choosing «Eurocode 7» sets all factors to 1.
- The **nail force** is computed once, on the finished wall: the failure check is the same in every stage, pull-out changes with the effective length.
- The **water pressure** enters the nail force like the soil thrust, with kn and the factor 1/cos α.
- The **limit shear resistance τlim** uses the friction δ of the bond-length layer and an adhesion equal to a fraction of the cohesion; the vertical stress is that of the soil above the middle of the effective length, without water table or slope. It cannot be assigned from pull-out tests.
- The **factor A** of each load is typed by hand: it does not come from the category.
- **Infinite backslope** with inclination ε.
- **Horizontal water table** in the stresses and in the water thrust on the block, parallel to the slope in the thrust on the failure surface and in the uplift; **impermeable facing**: the water weighs entirely on the nails.
- **Seismic action**: with kh > 0 the thrust is always Coulomb / Mononobe-Okabe; the seismic increment acts on uniform loads, not on strip and line loads; seismic sliding has no inertia force of the block. Choose the sign of kv carefully.
- **Sliding**: Q is the load on the wedge of the last stage; with automatic Bl the base is the projection of the first nail.
- **Facing**: the diagrams are indicative; the moment at the toe does not return exactly to zero.
- With ε > 0 the Rankine coefficient has no cos ε factor on the thrust: for the nail force the result is on the safe side (about +3 % with ε = 10°).

## Differences from .snl files

The results saved in a `.snl` file may differ from those of SNL NX because the analysis was corrected in some points (negative safety factors in sliding, layer thrusts, water table in the internal check, nails not in order of depth). In sliding with several layers SNL NX integrates the thrust of each layer only once: the safety factor may come out higher than the one saved in the file.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/snl/docs/en/validazione.md).*
