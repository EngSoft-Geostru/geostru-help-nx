# Estratigrafía interpretada

## Qué es

La estratigrafía interpretada es el modelo del subsuelo que se obtiene a partir de las lecturas del ensayo. Se define un cierto número de estratos — cada uno con una profundidad inferior, un tipo de suelo y los pesos específicos γ y γ_sat — y el software calcula para cada uno el valor representativo N_SPT, del que derivan a continuación las correlaciones geotécnicas.

## Cómo se introduce

En la pestaña **Estratigrafía interpretada** del Editor:

1. El primer estrato comienza en 0 m. Establece su profundidad inferior (p. ej. 2,50 m).
2. Haz clic en **+ Añadir estrato** para crear el estrato siguiente.
3. Para cada estrato:
   - Establece la **profundidad inferior** (m desde el nivel del terreno).
   - Elige el **tipo de suelo**: `COES` (cohesivo), `INCO` (no cohesivo) o ambos si es mixto — el tipo determina qué correlaciones se aplican.
   - Introduce **γ** (peso específico seco o natural) y **γ_sat** (peso específico saturado) en kN/m³.
   - Si lo deseas, introduce **arcilla (%)** y la **descripción** litológica.

## Los 7 métodos de agregación N_SPT

Para cada estrato, las lecturas que caen dentro de su rango de profundidad se agregan con el método elegido por el usuario. Los métodos disponibles son:

| Método | Cuándo usarlo |
|---|---|
| **Media** | Suelo homogéneo, variabilidad limitada |
| **Mínimo** | Enfoque conservador — se usa el valor más desfavorable |
| **Máximo** | Estimación del límite superior (p. ej. para capacidad portante en punta) |
| **Media − 1σ** | Enfoque estadístico conservador |
| **Media + 1σ** | Enfoque estadístico no conservador |
| **RNC** (distribución normal) | Valor característico en probabilidad según EC7 §2.4.5.2 |
| **RC** (distribución log-normal) | Como RNC pero con distribución log-normal — preferible para N_SPT con valores bajos |

El método se establece en el encabezado de la columna N_SPT de la tabla de estratigrafía y es válido para todos los estratos simultáneamente.

!!! info "¿Cuál es el método correcto?"
    La norma EC7 (y NTC §6.2.2) indica usar el **valor característico** del parámetro, definido como el valor con probabilidad del 5% de ser superado en el lado conservador. Los métodos RNC y RC se aproximan a esta definición estadística. Para muestras pequeñas (< 6 lecturas por estrato) la media sigue siendo la referencia más robusta.

## Conversión N_DPM → N_SPT

Para los ensayos continuos, el N_SPT de estrato se obtiene de N_DPM aplicando el coeficiente β (ver [Instrumentos →](strumenti.md)). El producto N_DPM × β es el N_SPT equivalente para cada lectura; la agregación se aplica posteriormente sobre estos valores equivalentes.

## Indicador Σ estratos / ensayo

En la parte inferior de la pantalla de estratigrafía aparece el indicador:

```
Σ estratos  X,XX m  /  ensayo  Y,YY m
```

- **Verde** (✓): la suma de las profundidades de los estratos coincide con la profundidad del ensayo — la estratigrafía cubre todo el ensayo sin lagunas.
- **Amarillo** (⚠): desviación entre Σ estratos y profundidad del ensayo — comprueba que el último estrato llegue al final del ensayo.
