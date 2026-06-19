# FAQ

Quick answers to the most common questions about Rock Mechanics NX: which classification to choose, how to estimate missing parameters and how to produce the report.

### Which classification should I choose?

It depends on the problem. For a **general characterisation** or for **underground** works, start from Barton's Q-index ([Barton](barton.md)) or from Singh & Goel's N-index ([Singh & Goel](singh-goel.md)). For **slope** stability use Romana's SMR ([Romana](rmr-romana.md)); if the slope is in **soft rock** (RMR < 40) turn to Robertson's SRMR ([Robertson](robertson.md)). For **carbonate rock masses**, Jašarević's n-index is calibrated ([Jašarević](jasarevic.md)). There is nothing stopping you from computing more than one on the same survey and comparing the classes.

### What is the difference between the Q-index and RMR?

They are two different systems. Bieniawski's **RMR** is a sum of ratings on a 0–100 scale (see [RMR](rmr-romana.md)); Barton's **Q-index** ([Barton](barton.md)) is a product/ratio of six joint parameters and varies on a logarithmic scale, typically from $0{,}001$ to $1000$. They measure the same quality with different quantities and are linked by empirical correlations; the most widely used is $RMR = 9 \ln Q + 44$.

### How do I estimate RQD if I have no borehole cores?

From the discontinuity survey. With the **Palmström** relation you derive it from the *volumetric joint count*: $RQD = 115 - 3{,}3\,J_v$. Alternatively, with the **Priest and Hudson** formula, from the average number of joints per linear metre $\lambda$. Both are described in [RQD](classificazioni.md#rqd-rock-quality-designation).

### Can I import the survey from GMS or eGeo Compass?

Yes. Rock Mechanics NX reads geostructural survey data coming from **GMS** and from **eGeo Compass**, so you do not have to re-enter the attitudes by hand. Supported formats and import procedures are described in [File formats](formati.md).

### What is the difference between planar and wedge sliding?

**Planar sliding** is the movement of a block along a *single* discontinuity that daylights on the slope face: it is a 2D limit-equilibrium check (see [Planar sliding](scivolamento-planare.md)). **Wedge sliding**, on the other hand, concerns a tetrahedral wedge bounded by *two* intersecting discontinuities, and is analysed in 3D along their line of intersection (see [Sliding 3D](sliding-3d.md)).

### When do I use Rock Mechanics and when RockPlane?

Use **Rock Mechanics** for the *geomechanical classification* of the rock mass, the derivation of the characteristic parameters and the basic checks of the kinematics (planar and wedge sliding). Switch to **[RockPlane](https://help.nx.geostru.ai/rockplane/en/)** when you need to *design the remedial measures* (bolts, anchors, meshes) on a planar failure with a tension crack and two joints, with verification according to NTC/Eurocodes.

### How do I obtain cohesion, friction angle and modulus of the rock mass?

These are the **characteristic parameters** that the app derives automatically from the classifications. Once the quality index (RMR, Q or GSI) has been computed, Rock Mechanics applies the known correlations to return the cohesion $c$, friction angle $\varphi$ and deformation modulus $E$ of the rock mass, ready to be entered into the stability checks.

### How do I export the report?

From the export function: the app generates the **calculation report** with the survey data, the indices, the classes and the characteristic parameters, together with the graphical outputs. The procedure, formats and customisations are described in [Export and report](export.md).

### Where do I find the figures and the CAD drawing cited in the manual?

On the [Resources](risorse.md) page: you can download the kinematics figures in PDF, the planar-sliding drawing in DWG and the historical manual of the desktop version.

### How do I report an error or a bug?

Write to [info@geostru.ai](mailto:info@geostru.ai?subject=Bug%20Rock%20Mechanics%20NX) describing the problem and, if possible, attaching a screenshot and the project file that reproduces it.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
