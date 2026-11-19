# Calculation methods

This page explains what the methods do, when to use them and their limits. It does not report the engine equations. For the full theory use the bibliographic references at the end.

## LEM: limit equilibrium

The limit equilibrium method studies wall equilibrium under ground, water, load and support actions. It is mainly intended for selecting or checking embedment and for the internal forces of simple schemes.

**When to use it**

- to assess embedment;
- for cantilever walls or walls with one level of supports;
- for a preliminary comparison with FEM.

**Assumptions and limits**

Ground behaviour is represented through limiting earth pressure conditions. The method does not fully describe wall deformability and soil-structure interaction. It is not the appropriate choice when displacements and deformation history govern the design.

**What it returns**

- bending moment, shear and axial force along the wall;
- the design embedment;
- support forces.

LEM does not compute displacements: the deflection diagram shows “Data unavailable” and the SLS check stays not calculated. The FEM options of the Calculation step have no effect.

## FEM: wall on springs

The finite element method represents the wall as a flexural member and the ground as a set of yielding reactions. Anchors, struts and other restraints contribute to the response according to their stiffness and installation stage.

**What it returns**

- displacements along the wall;
- bending moment, shear and axial force;
- pressures and ground mobilisation;
- support forces;
- response to individual stages and combinations.

**Linear and nonlinear analysis**

In linear analysis, ground response does not change with displacement level. Nonlinear analysis limits the reaction when the ground reaches the condition expected by the model. Use it when you want a more realistic representation of resistance mobilisation.

**Discretisation and convergence**

The number of elements controls detail along the wall. Maximum iterations and tolerance control convergence. The linear-range limit, excavation-base spring reduction and displacement associated with subgrade reaction describe ground response.

Change these data with care. A non-converged calculation or inadequate discretisation is not a sufficient basis for design.

## Earth pressure

Available options include Coulomb, Müller–Breslau, Caquot–Kérisel, Rankine and Jaky's at-rest condition where applicable.

- **Coulomb** considers wedge equilibrium and soil-wall friction.
- **Müller–Breslau** is a formulation of the same family for more general geometric conditions.
- **Caquot–Kérisel** uses an established treatment and tables for passive pressure and soil-wall friction.
- **Rankine** suits simpler assumptions for the wall and ground surface.
- **Jaky** describes at-rest pressure in the applicable cases.

The choice must be consistent with geometry, soil-wall friction, drainage and expected displacements. Passive resistance is particularly sensitive to these assumptions.

## Seismic action

The **Mononobe–Okabe** option extends the earth pressure model to pseudo-static action. The **Structures without displacement** option concerns schemes where the deformation mechanism associated with active pressure is not permitted.

The seismic increment point can be placed at one third, one half or two thirds of the height according to the selected scheme.

Site parameters derive from location, nominal life, use class, subsoil and topography. The specific NTC 2018 provisions for retaining structures apply. The seismic model is applied only to combinations that include it.

**Limits:** check that the method is compatible with soil type, water and allowable displacements. Do not automatically extend a model for free walls to a strongly restrained structure.

## Water table, piping and uplift

Groundwater changes effective soil weight and introduces water pressures. Different elevations on the two sides can produce flow through the ground.

- The **hydrostatic** regime considers levels without describing the flow field.
- The **seepage** regime represents flow effects with the approximations stated by the program.
- The **HYD · piping** check assesses safety against internal erosion associated with flow.
- The **UPL · uplift** check concerns excavation-base equilibrium under water pressure.

A hydraulic combination may have no structural diagrams: in that case it returns the hydraulic check factors. Always check permeability data and the assigned regime.

## Anchors and struts

An **active anchor** receives preload. A **passive anchor** reacts to displacements after installation. Free length, bulb, reinforcement, spacing and duration affect response and checks.

A **strut** works mainly in compression. Stiffness can be assigned or proposed from geometric and material data.

Anchor checks cover pull-out and steel resistance. Strut resistance is available; buckling is not checked and requires a separate assessment.

## Structural checks and reinforcement

STR checks concern bending and shear of RC sections and the supported composite sections. Forces per metre of wall are referred to the element through spacing or width.

The project retains concomitant actions from the same condition. Final reinforcement derives from demand along the wall and from the entered geometric rules.

Strut buckling, global stability, vertical bearing capacity and section SLE checks are outside the current scope.

## Essential bibliography { #bibliografia-essenziale }

- Blum, H., *Einspannungsverhältnisse bei Bohlwänden*, 1931.
- Coulomb, C. A., *Essai sur une application des règles de maximis et minimis*, 1776.
- Rankine, W. J. M., *On the Stability of Loose Earth*, 1857.
- Caquot, A.; Kérisel, J., *Tables for the Calculation of Passive Pressure, Active Pressure and Bearing Capacity of Foundations*, 1948.
- Mononobe, N.; Matsuo, H., 1929; Okabe, S., 1926, for the pseudo-static earth pressure method.
- Winkler, E., *Die Lehre von der Elasticität und Festigkeit*, 1867, for the yielding reaction model.
- NTC 2018, in particular Sections 6.5, 6.6 and 7.11.6.3.
- EN 1997-1, Eurocode 7, for geotechnical verification approaches.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/spw/docs/en/metodi.md).*
