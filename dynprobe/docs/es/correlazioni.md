# Correlaciones geotécnicas

## Qué son

Las correlaciones geotécnicas transforman N_SPT en parámetros de resistencia y deformabilidad del suelo. Son fórmulas empíricas derivadas de la literatura internacional — su uso está consolidado en la práctica geotécnica, pero siguen siendo estimaciones: complementa siempre con datos de laboratorio cuando estén disponibles.

## Cómo se leen

En la pestaña **Correlaciones** del Editor, para cada estrato de la estratigrafía aparece una tabla con los valores calculados. La columna de la izquierda indica el parámetro; las siguientes muestran los valores según los distintos autores de referencia. Puedes activar o desactivar autores individuales con los interruptores en la parte superior de cada columna.

El **valor preferido** (⭐) alimenta la pestaña **Resumen de parámetros** y el informe Word.

## Parámetros para suelos cohesivos (COES)

| Parámetro | Significado |
|---|---|
| **Cu** | Resistencia al corte no drenada (kPa) |
| **Mo** | Módulo edométrico (MPa) |
| **Ey** | Módulo de Young (MPa) |
| **Vs** | Velocidad de ondas de corte (m/s) |
| **γ** | Peso específico (kN/m³) |
| **Clasificación** | Consistencia (muy blanda → muy rígida) |

Autores de referencia citados en la literatura geotécnica italiana e internacional: Terzaghi-Peck, Schmertmann, Ohta-Goto y otros.

## Parámetros para suelos no cohesivos (INCO)

| Parámetro | Significado |
|---|---|
| **Dr** | Densidad relativa (%) |
| **φ** | Ángulo de rozamiento interno (°) |
| **φ_160** | Ángulo de rozamiento sobre N_1,60 normalizado (°) |
| **Mo** | Módulo edométrico (MPa) |
| **Ey** | Módulo de Young (MPa) |
| **Vs** | Velocidad de ondas de corte (m/s) |
| **ν** | Coeficiente de Poisson |
| **G** | Módulo de corte (MPa) |

Autores de referencia: Meyerhof, Peck, Hanson, Thornburn, Ohta-Goto, Seed-Idriss y otros.

!!! warning "Límites de validez"
    Cada correlación fue desarrollada para un rango específico de N_SPT y tipos de suelo concretos. Cuando N_SPT es muy bajo (< 3) o muy alto (> 50), los resultados deben interpretarse con cautela. La aplicación resalta los valores fuera de rango.

## Envolvente de parámetros

Cuando dispones de varios ensayos en el mismo sitio, la pestaña **Envolvente** muestra para cada estrato el rango min-máx de los parámetros entre todos los ensayos, con el **criterio de diseño** seleccionable (mínimo / media / máximo / valor preferido ⭐). El valor de diseño alimenta automáticamente el Resumen.

## Resumen de parámetros

La pestaña **Resumen** reúne en una sola tabla los valores geotécnicos característicos de cada estrato — útil como tabla de síntesis para incluir en el informe geotécnico. El informe Word la incluye automáticamente.
