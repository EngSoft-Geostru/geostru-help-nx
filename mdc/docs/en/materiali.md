# Materials

Step 7 has a panel for the **wall materials**, one for the **pile materials** (only with a piled foundation), one for **factors and covers**
and, for the gravity wall, one for the **gravity wall**. Strengths and moduli are in **MPa**, unit weights in **kN/m³**, covers in
**metres**.

## Concrete and steel

**Class** picks from the archive and fills in the properties; the values can still be changed.

| Material | Classes | Fields |
|---|---|---|
| Concrete | C20/25, C25/30, C28/35, C30/37, C32/40, C35/45, C40/50, C45/55, C50/60 | Cube strength R~ck~, Cylinder strength f~ck~, Elastic modulus E~c~, Design strength f~cd~, Mean tensile strength f~ctm~, Design tensile strength f~ctd~ (MPa); Unit weight (kN/m³) |
| Steel | B450C, B450A | Yield strength f~yk~, Design yield strength f~yd~, Elastic modulus E~s~ (MPa); Ultimate strain ε~uk~ |

The archive properties follow NTC 2018 (f~cd~ = 0.85·f~ck~/1.5, f~ctd~ = 0.7·f~ctm~/1.5). A project opened from the desktop carries the
classes of its archive ("from file"). Wall and piles can have different materials.

## Factors and covers

| Field | Unit | Notes |
|---|---|---|
| Wall unit weight | kN/m³ | used when the concrete class gives no weight |
| Concrete γ~c~ | | 1.5 as a rule |
| Steel γ~s~ | | 1.15 as a rule |
| Environmental conditions | | Ordinary, Aggressive, Very aggressive |
| Concrete covers: Stem, Foundation, Shear key, Starter bars | m | they enter the effective depth of the sections and the crack width |

The environmental conditions (NTC 2018 §4.1.2.2.4) set the crack width limits in the serviceability combinations.

## Gravity wall

| Field | Unit |
|---|---|
| Design compressive strength | MPa |
| Design tensile strength | MPa |
| Unit weight | kN/m³ |
| Starter bar diameter | mm |

The stresses in the wall body are compared with these strengths: see [Sections, reinforcement and bar schedule](armature.md#gravity-wall).

## Design reinforcement

The diameters and number of bars used to design the reinforcement are in the [Reinforcement](armature.md#design-reinforcement) step.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MDC%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mdc/docs/en/materiali.md).*
