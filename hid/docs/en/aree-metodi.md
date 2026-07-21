# Areas and calculation methods

## Drainage areas

Each row of the table is a surface that is homogeneous in use and permeability.
You need a description, the type, the area in m² and the post-development runoff
coefficient φ.

![Defining the areas](img/02-aree-metodi.png)

The area type (impervious, semi-impervious, pervious) is a descriptive label that
suggests the order of magnitude of φ; the value used in the calculation is always
the one you type.

HID calculates the **weighted runoff coefficient**:

$$\varphi_{pond} = \frac{\sum \varphi_i \cdot S_i}{\sum S_i}$$

and the **weighted area** $S_{pond} = S_{tot} \cdot \varphi_{pond}$, which is the
equivalent impervious area.

## The sizing methods

HID distinguishes **universal** methods, valid everywhere, from **jurisdiction**
methods, which exist only where the regulation prescribes them.

### Minimum requirements

Specific volume per hectare imposed by the regulation as a function of the
hydraulic criticality zone. In Lombardia it is 800, 500 or 400 m³/ha depending on
zone A, B or C and on the regulation version. Where the regulation does not
prescribe it, you set the minimum volume yourself.

### Rain-only method

It balances the inflow volume against the volume discharged at constant flow,
looking for the duration that maximises the storage. It is the most widely used
method for quick checks.

!!! note "Durations shorter than one hour"
    When the critical duration drops below one hour, HID uses the exponent n₁ of
    the curve, as required. It does not round the duration up to one hour: doing
    so underestimates the volume, and it is an error we corrected while
    validating the app against the previous version.

### Time-of-concentration method

It introduces the catchment time of concentration, so it accounts for the shape
of the hydrograph. It returns the critical duration and the volume.

### Direct method

It compares the specific pre- and post-development storage volumes through the
ratio of the runoff coefficients. In Emilia-Romagna and Marche the regulation
prescribes a variant with fixed coefficients, which HID exposes as a separate
method, **Regional direct method**, visible only in those regions.

### Detailed procedure

This is the full simulation: design hyetograph, losses, flood hydrograph and
step-by-step attenuation of the storage facility. It is the most demanding method
and the most defensible.

## How the volume is chosen

HID calculates all the selected methods and adopts the **highest** result as the
allowable volume. The method proposed by the regulation is shown below the
checkboxes, but it does not limit which methods you can calculate.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
