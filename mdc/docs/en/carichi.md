# Loads

The self-weight of the wall and of the soil is computed by the program. In step 5 you add the **distributed surcharges on the backfill** and
the **point loads**. In a new project both lists are empty: **+ Load** and **+ Force** add a row, the bin removes it.

## Distributed surcharges

| Field | Unit | Notes |
|---|---|---|
| Description | | free text |
| Type | | Uniform, Strip, Trapezoidal |
| Category | | Not assigned, Generic, Structural permanent, Non-structural permanent, Crowd, Traffic, Railway, Buildings |
| Start abscissa, End abscissa | m | measured from the top of the wall towards the backfill |
| Start intensity, End intensity | kPa | equal for the uniform load |
| Depth | m | |

The load enters the earth pressure as an **equivalent uniform surcharge**, as in the desktop: the part of the load that falls within a
distance from the top of the wall equal to the wall height plus the heel is spread over that whole length. With distant loads or narrow
strips the earth pressure is therefore approximate (see [Validation and limits](validazione.md)).

The **category** decides how the load weighs on the foundation: a **permanent** load (structural or non-structural) above the heel counts as
stabilising weight with a factor not greater than 1; a **variable** load (all other categories) does not count as stabilising weight, only
as earth pressure.

!!! note "Note"
    The desktop program weighed the surcharge on the heel with the unfavourable factor of the combination, making it more stabilising just
    when it should be more severe. MDC NX corrects this.

The factor with which each load enters a combination belongs to the combination (1.5 in the A1 combinations generated from the code, 1 in
the seismic ones): see [Combinations and checks](verifiche.md).

## Point loads

Forces and moments **per metre of wall**, applied at a point of the wall system (x from the toe edge of the foundation, y from the founding
plane).

| Field | Unit | Positive direction |
|---|---|---|
| Abscissa x, Level y | m | |
| Horizontal force F~x~ | kN/m | towards the toe (to the left in the drawing) |
| Vertical force F~y~ | kN/m | downwards |
| Moment M~z~ | kN·m/m | overturning, i.e. rotating the wall towards the toe (anticlockwise in the drawing) |

It is the same convention as the resultants in the report (F~x~ > 0 towards the toe, F~y~ > 0 downwards, M > 0 overturning). Point loads are
used for actions coming from other structures: a parapet, a barrier, the reaction of a slab. Loads applied to the **front shelf** are
entered here, with the point on the shelf: the program uses them to design its reinforcement.

## Ground anchors

Anchors are not loads to be entered here: they are described in the [Piles and anchors](pali-tiranti.md) step and the program derives
their force.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MDC%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mdc/docs/en/carichi.md).*
