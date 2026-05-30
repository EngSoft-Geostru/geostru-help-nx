# Categoría de subsuelo

## Para qué sirve

La categoría de subsuelo determina la amplificación sísmica esperada para el emplazamiento y condiciona el valor del parámetro **S** (coeficiente de amplificación estratigráfica) en los espectros de respuesta NTC 2018.

Dynamic Probing NX calcula automáticamente la categoría a partir de las velocidades V_s de los estratos, derivadas de las correlaciones N_SPT → Vs.

## Normativas soportadas

| Normativa | Parámetro de referencia | Notas |
|---|---|---|
| **NTC 2018** (D.M. 17/01/2018) | V_s,30 | Método principal para edificios y obras |
| **NTC 2008** (D.M. 14/01/2008) | V_s,30 | Compatibilidad con proyectos anteriores |
| **Eurocódigo 8** (EN 1998-1) | V_s,30 | Referencia europea |

## Cómo se calcula V_s,30

V_s,30 es la velocidad media de las ondas de corte en los primeros 30 m de profundidad, ponderada por los espesores de los estratos. Para profundidades de sondeo menores de 30 m, la aplicación utiliza un substrato sísmico por defecto (roca) para los metros que faltan — este valor es configurable en la pestaña **Cat. suelo**.

## Cómo leer el resultado

En la pestaña **Cat. suelo** del Editor encontrarás:

- **V_s,eq**: velocidad equivalente calculada (m/s)
- **Categoría**: letra A / B / C / D / E (NTC 2018) con descripción textual
- **Tabla de estratos**: contribución de cada estrato al cálculo de V_s,30

El cálculo se actualiza automáticamente cada vez que modificas la estratigrafía o las velocidades V_s de los estratos.

!!! info "Vs desde ensayos de laboratorio"
    Si dispones de medidas directas de V_s (MASW, down-hole, cross-hole), puedes sobrescribir el valor V_s de cada estrato en la columna dedicada de la tabla — el cálculo de V_s,30 usa los valores introducidos manualmente en lugar de los estimados a partir de las correlaciones.

## Categorías NTC 2018

| Categoría | Descripción |
|---|---|
| **A** | Afloramientos rocosos o suelos muy rígidos (V_s,30 > 800 m/s) |
| **B** | Depósitos de arenas, gravas compactas o arcillas rígidas (360 < V_s,30 ≤ 800 m/s) |
| **C** | Depósitos de arenas, gravas medianamente compactas o arcillas de consistencia media (180 < V_s,30 ≤ 360 m/s) |
| **D** | Depósitos de suelos granulares sueltos o suelos cohesivos blandos (V_s,30 ≤ 180 m/s) |
| **E** | Perfiles con estratos superficiales aluviales con V_s < 360 m/s y espesor comprendido entre ciertos límites sobre substrato de categoría A o B |
