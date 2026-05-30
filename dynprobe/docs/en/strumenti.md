# Instruments — DPL · DPM · DPH · DPSH · Borehole SPT

## Continuous dynamic tests

In a continuous dynamic test the hammer falls repeatedly and the number of blows required to advance the cone by a fixed step (typically 10 or 20 cm) is counted. The blow count / depth sequence is the raw material of all processing.

Dynamic Probing NX supports the four types standardised by **UNI EN ISO 22476-2**:

| Code | Type | Energy per blow |
|---|---|---|
| **DPL** | Light | low |
| **DPM** | Medium | medium |
| **DPH** | Heavy | high |
| **DPSH** | Super heavy | very high |

Each type has hammer mass, drop height and cone diameter defined by the standard. The instrument library in the app includes the most widely used models on the market already tabulated — you can also add a custom instrument with your own calibration data.

### The correlation coefficient β

The coefficient β converts the blow count from the dynamic test (N_DPM, N_DPSH…) into the equivalent N_SPT. The value depends on the instrument and is determined by comparative in-situ tests. Each instrument in the catalogue has a default β; you can override it with the value from your specific calibration.

## Borehole SPT tests

The SPT (Standard Penetration Test, **UNI EN ISO 22476-3**) is performed inside a boring. The sampler is driven 45 cm in three 15 cm increments:

- **N1**: first increment (seating) — not counted
- **N2** + **N3**: second and third increments → **N_SPT = N2 + N3**

Add a borehole SPT test from the Dashboard with the **+ Borehole test** button. Define the start depths of each drive (e.g. 1.0 m — 2.5 m — 4.0 m) and for each enter N1, N2, N3. The app automatically computes N_SPT and builds the profile.

### Stratigraphy of borehole tests

For borehole SPT tests the stratigraphy is entered manually in the **Interpreted stratigraphy** section, layer by layer, exactly as for continuous tests. Mean N_SPT per layer is computed from the drives that fall within the depth range of the layer.

## Instrument library

Go to **Instruments** from the navigation bar to access the library. You can:

- View the parameters of each instrument (mass, drop height, cone diameter, cone angle, step, β)
- Add a custom instrument
- Modify the β of an existing model for your specific datalogger

Instruments are saved in the `.dprobe` project file — the file is self-contained and portable to another PC without losing calibration data.
