# Frequently asked questions

## Why does the volume change if I change the discharge type?

Because the reference flow changes. The "constant outflow" field applies only to
the constant-flow discharge; for a submerged orifice or a weir, HID uses the flow
the device actually discharges at the design head. See
[Discharge system](scarico.md).

## Which method should I use?

The one the reviewing authority asks for. When in doubt, keep more than one
active: HID adopts the highest, which is the most conservative condition.

## Why can't I use SCS-CN in Lombardia?

The regional regulation does not allow it, and it requires the GEV curve. HID
applies the constraint and blocks the calculation, explaining the reason.

## I can't find my municipality

The database covers Italian municipalities. For other countries enter the region
and the coordinates manually: the generic profile does not need the municipality.

## How do I work outside Italy?

Choose **Other / international** as the country, or tick **Ignore territorial
regulation**. You set the discharge limit and the minimum volume yourself, based
on what the local authority prescribes.

## The emptying time is empty

It is calculated only for the constant-flow discharge and for constant
infiltration. For the other devices the flow depends on the head and changes
during emptying.

## What is the difference between the direct method and the regional direct method?

The direct method uses the coefficients you enter. The regional one, prescribed
in Emilia-Romagna and Marche, uses the fixed coefficients of the regulation (0.9
and 0.2) and the exponent 0.48, and asks for the pre- and post-development areas.

## Can I change language once work has started?

Yes. The labels are translated, not the data: the project values stay as you
entered them.

## The report comes out in Italian even though the app is in German

It should not: the report follows the selected language. If it happens,
[let us know](mailto:info@geostru.ai?subject=Help%20HID%20NX) stating the
language and the format.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
