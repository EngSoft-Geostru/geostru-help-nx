# Valores característicos EC7 / NTC §6.2.2

## Por qué los valores característicos

Las normativas geotécnicas europea (EC7 §2.4.5.2) e italiana (NTC 2018 §6.2.2) exigen proyectar sobre los **valores característicos** de los parámetros, no sobre los valores medios. El valor característico tiene en cuenta la variabilidad natural del suelo y la incertidumbre de muestreo.

## Cómo funciona el cálculo

Dynamic Probing NX estima el valor característico de N_SPT para cada estrato aplicando métodos estadísticos a la serie de valores N recogidos en el estrato. Los métodos disponibles son:

| Método | Descripción |
|---|---|
| **Normal** | Estimación basada en media y desviación típica con distribución gaussiana |
| **Lognormal** | Útil cuando N_SPT tiene distribución asimétrica (frecuente con valores bajos) |
| **Student-t** | Corregido para muestras pequeñas (n < 30) — tiene en cuenta la incertidumbre sobre la media |

El nivel de confianza aplicado corresponde al indicado por EC7 para el valor característico inferior (percentil 5, lado conservador).

## Cómo usarlo

En la pestaña **Estimación de parámetros** del Editor:

1. Selecciona el método estadístico (Normal / Lognormal / Student-t).
2. Para cada estrato se muestran: media, desviación típica, tamaño muestral y valor característico calculado.
3. El valor característico de N_SPT se propaga a las correlaciones para obtener los valores característicos de Cu, φ, Mo, Ey, etc.

!!! info "Muestras mínimas"
    Con menos de 3 lecturas por estrato, el cálculo estadístico tiene baja significatividad. La aplicación señala los casos con n < 3 mediante un aviso — en estos casos es preferible usar un enfoque de ingeniería conservador (p. ej. mínimo de los valores observados).

## Valores característicos en el informe

El informe Word exportado incluye la tabla de valores característicos con el método usado, el tamaño muestral y el valor resultante — lista para adjuntar al informe geotécnico.
