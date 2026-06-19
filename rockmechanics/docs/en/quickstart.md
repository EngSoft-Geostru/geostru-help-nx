# Quickstart (5 minutes)

The goal: from a survey of just a few discontinuities to your **first geomechanical classification** with the characteristic rock-mass parameters. No theory — that is in the pages dedicated to the individual methods.

## 1. Open the app

Go to [nx.geostru.ai/rockmechanics](https://nx.geostru.ai/rockmechanics/) and create a **New file** from the File menu. Fill in the **General data** (site description, location, date, operator).

## 2. Enter the joint survey

For each **discontinuity set** surveyed on site, specify at least:

- **attitude**: dip direction and dip;
- mean **spacing** $s$;
- **persistence, aperture, roughness, weathering, infilling**;
- **hydraulic conditions** (dry → heavy inflow).

Also specify the **orientation of the face** (dip direction and dip) of the slope or excavation: this is needed for the orientation correction factor and for the Slope Mass Rating.

!!! tip "Where the data come from"
    The survey is carried out with compass and clinometer according to ISRM recommendations. If you use **eGeo Compass** or **GMS (GeoMechanical Survey)**, the joint sets and attitudes are imported ready to use (see [File formats](formati.md)).

## 3. Define strength and fracturing

- **$S_u$** — uniaxial compressive strength of the intact rock: enter it from a Point Load test, from a Schmidt hammer or with the ISRM estimate (see [common parameters](classificazioni.md#resistenza-a-compressione-uniassiale-su)).
- **RQD** — from borehole cores, or estimated from the number of joints per cubic metre $J_v$.

## 4. Choose the classification

Open the **Classifications** tab and select the method that suits your case:

| If you need… | Use |
|---|---|
| General characterisation or underground works | [Barton (Q)](barton.md) |
| Stability of a **slope** | [Romana (SMR)](rmr-romana.md) or [Robertson (SRMR)](robertson.md) |
| Tunnels | [Singh & Goel (N)](singh-goel.md) |
| Carbonate rock mass | [Jašarević (n)](jasarevic.md) |

The app immediately computes the **index** (Q, RMR, SMR, N…), the **class** and the **quality** of the rock mass.

## 5. Read the characteristic parameters

In the same tab you will find the derived parameters, ready for the calculation:

- cohesion $c$,
- friction angle $\varphi$,
- deformation modulus $E$,
- (for RMR) the **GSI**.

## 6. (Optional) Check stability

If you have a recognised kinematic mechanism, move to [Planar sliding](scivolamento-planare.md) or [Sliding 3D](sliding-3d.md): enter the face geometry, water, seismic action and any external forces, and read the safety factor.

## 7. Export

Generate the **calculation report** with tables and charts from the Report tab (see [Export](export.md)).

---

➡️ Continue with the [full workflow](workflow.md) for the details of each step.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
