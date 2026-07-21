# Sistema de vertido

El órgano de vertido determina el caudal saliente del depósito de retención y por
tanto la laminación. HID implementa ocho.

![Sistema de vertido](img/06-calcoli-verifiche.png)

## Los órganos disponibles

| Órgano | Parámetros | Ley |
|---|---|---|
| Caudal constante | Q<sub>u,lim</sub> | Q constante, independiente de la carga hidráulica |
| Vertedero Thomson | ángulo θ | Q ∝ tan(θ/2) · h<sup>5/2</sup> |
| Vertedero Bazin | anchura | Q ∝ L · h<sup>3/2</sup> |
| Vertedero Crump | anchura | Q ∝ L · h<sup>3/2</sup> |
| Orificio sumergido circular | área A | Q = 0,6 · A · √(2gh) |
| Compuerta | apertura, anchura | Q = 0,6 · a · L · √(2gh) |
| Infiltración constante | K, gradiente | Q ∝ K · i · superficie |
| Pozo de infiltración | número, diámetro, longitud | función de la carga hidráulica y de la superficie de infiltración |

## Cómo se elige el caudal máximo de vertido

Es el punto en el que más se falla, por eso HID sigue un orden único:

1. **Si la normativa lo impone**, vale ese. En Lombardia se obtiene a partir del
   área, del coeficiente de escorrentía y de la zona de criticidad.
2. **Si no, lo eliges tú.** Pero el campo "caudal constante saliente" tiene
   sentido solo para un vertido a caudal constante: para un orificio sumergido,
   un vertedero o una compuerta vale el **caudal del órgano a la carga hidráulica
   de proyecto**.

!!! warning "Atención"
    El punto 2 es la razón por la que, al cambiar el tipo de vertido, el volumen
    requerido puede cambiar bastante: el caudal de referencia ya no es el que has
    escrito en el campo, sino el que el órgano vierte realmente.

## Carga hidráulica de proyecto

Para los órganos que dependen de la carga hidráulica, el valor H que introduces
es la carga hidráulica útil máxima. El caudal correspondiente se muestra debajo
del bloque como **caudal a la carga hidráulica de proyecto**.

---

*¿Has encontrado un error en esta página? [Comunícanoslo](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
