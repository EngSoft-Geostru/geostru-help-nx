# Quick start — first project in 5 minutes

Objective: load a sample file, read the stratigraphy and main correlations, export the report.

## 1. Open the app and create a new project

Go to [nx.geostru.ai/dynprobe](https://nx.geostru.ai/dynprobe/). Click **New file** from the File menu.  
Give the project a name (e.g. "Rome Street Site") and click **Create**.

Alternatively, use a **sample file** from the home screen — you will immediately see all sections already populated.

## 2. Add a test

In the **Dashboard** click **+ Continuous test** (or **+ Borehole test** for SPT). Enter:

- **Label**: identification code for the test (e.g. `DP-1`)
- **Instrument**: select from the catalogue (DPM, DPSH, DPH, DPL…). The instrument defines the hammer mass, drop height and advancement step — all energy parameters are already tabulated internally.
- **Coordinates**: enter lat/lon to position the test on the map (optional but useful for site plan export).

## 3. Enter the readings

Go to the **Readings** tab. You have three modes:

- **Manual**: type the blow count row by row.
- **Import CSV**: paste or load a file from a datalogger — the system automatically recognises depth and blow count.
- **Import .dypx**: load a file exported directly from the GeoStru Dynamic Probing desktop.

The N/depth chart updates in real time.

## 4. Interpret the stratigraphy

Go to the **Interpreted stratigraphy** tab. The app proposes a first layer over the entire depth.

- Click **+ Add layer** to subdivide the profile.
- For each layer set the lower depth, the **soil type** (cohesive / non-cohesive / mixed) and the **unit weight** γ.
- The N_SPT aggregation method per layer is chosen in the column header (default: mean). See [Stratigraphy →](stratigrafia.md) for the 7 available methods.

!!! tip "Colours and badges"
    The **Σ layers / test** badge at the bottom shows whether the sum of layer depths matches the test depth (green tick = consistent, yellow triangle = discrepancy to check).

## 5. Read the correlations

**Geotechnical correlations** tab: for each layer a table appears with the estimated parameters (Cu, φ, Mo, Ey, Vs, γ, Dr …) computed from reference formulas in geotechnical literature. See [Correlations →](correlazioni.md).

!!! note
    Correlations are empirical estimates. Use them as a starting point — always supplement with laboratory data when available.

## 6. Check the subsoil category

**Subsoil cat.** tab: the app computes the equivalent velocity V_s,30 and automatically assigns the NTC 2018 category. See [Category →](categoria.md).

## 7. Export the report

**File → Save** to download the `.dprobe` file. **Export → Word Report** for the complete report.

In 5 minutes you have:

- ✅ a test with readings
- ✅ an interpreted stratigraphy
- ✅ geotechnical parameters for each layer
- ✅ the subsoil category
- ✅ the project file downloaded
