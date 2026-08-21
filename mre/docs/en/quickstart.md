# Quick start (5 minutes)

1. **General data** — description, site coordinates (lat/lon/elevation), design code
   (NTC 2018, Eurocodes or User) and approach: **Design** (the program works out the
   anchorage lengths) or **Check** (you impose them).
2. **Seismic action** — enter k~h~ and k~v~, or use **Import from GeoStru PS (.txt)**: the
   GeoStru PS report fills in hazard data and coefficients for the four limit states (SLV
   applied automatically) and copies the coordinates into General data.
3. **Geometry** — height H, base B, inclination of the outer facing α, optional inner
   excavation α~s~, backfill slope β and foundation depth D. The preview on the right
   follows every change.
4. **Surcharge** — load strip q with start/end abscissas and **type** (permanent, crowd,
   traffic, …): it drives γ~Q~ in the static combination and ψ₂ in the seismic one.
5. **Geotechnical parameters** — the three soils: reinforced, retained, foundation.
6. **Reinforcements** — spacing s, nominal strength t~ult~ and reduction factors RF, or
   pick a product from the **Archive**. With L~rip~ > 0 you draw the wrap-around facing.
7. Press **Calculate** and read the results in the **Checks**, **Reinforcements** and
   **Global stability** tabs; generate the **Report** in DOCX.

Data goes into the cards on the left; the preview on the right follows every change.

![General data card with the section preview](img/01-parametri.png)

After the calculation the **Checks** tab sums up overturning, sliding and bearing
capacity, with the factor of safety of each combination.

![Checks tab with the factors of safety per combination](img/09-verifiche.png)

!!! note "Saving"
    A project is saved as an **.mre** file (File → Save) or on **GeoDropbox**; the state
    of the page is kept in the session at every change anyway.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MRE%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mre/docs/en/quickstart.md).*
