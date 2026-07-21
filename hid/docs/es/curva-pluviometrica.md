# Curva intensidad-duración-frecuencia

La curva relaciona la altura de lluvia con la duración del evento para un
determinado periodo de retorno. Es la entrada de todo método de dimensionamiento.

![Curva intensidad-duración-frecuencia](img/03-curva-pluviometrica.png)

## Curva de dos parámetros

La forma clásica:

$$h(t) = a \cdot t^{n}$$

con `h` en mm y `t` en horas. Introduce `a` (coeficiente pluviométrico horario) y
`n` (coeficiente de escala). El parámetro **n₁** gobierna las duraciones
inferiores a la hora, donde la curva tiene una pendiente distinta; el valor
habitual es 0,5.

!!! example "Ejemplo"
    Con a = 46,49 y n = 0,364 la lluvia de 3 horas vale
    46,49 × 3^0,364 = 69,35 mm; la de 24 horas vale 147,83 mm.

## Curva GEV

La distribución generalizada de valores extremos obtiene el coeficiente `a` a
partir del coeficiente horario `a₁` y del factor de crecimiento ligado al periodo
de retorno:

$$a = a_1 \cdot K_T$$

Introduce los parámetros α (alfa), k (kappa) y ε (épsilon) y el periodo de
retorno. HID calcula K_T y lo muestra junto a la curva.

!!! warning "Lombardia"
    El reglamento regional impone la curva GEV. Los parámetros se obtienen del
    servicio regional de referencia. Con la curva de dos parámetros HID bloquea
    el cálculo.

## Tabla y gráfico

Tras el cálculo la tabla muestra las alturas en las 28 duraciones estándar: 0,
0,25, 0,50, 0,75, 1 hora, luego cada hora hasta 24. El gráfico inferior muestra
la misma serie.

!!! note "Redondeos"
    Los valores se calculan en doble precisión y se redondean solo para la
    visualización. Pequeñas diferencias en la última cifra respecto a otros
    programas dependen del sentido del redondeo, no del cálculo.

---

*¿Has encontrado un error en esta página? [Comunícanoslo](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
