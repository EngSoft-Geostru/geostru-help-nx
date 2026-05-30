# Guía rápida — primer proyecto en 5 minutos

Objetivo: cargar un archivo de ejemplo, leer la estratigrafía y las correlaciones principales, exportar el informe.

## 1. Abre la aplicación y crea un proyecto nuevo

Ve a [nx.geostru.ai/dynprobe](https://nx.geostru.ai/dynprobe/). Haz clic en **Nuevo archivo** en el menú Archivo.  
Dale un nombre al proyecto (p. ej. "Sitio calle Roma") y haz clic en **Crear**.

Como alternativa, usa un **archivo de ejemplo** desde la pantalla inicial — verás de inmediato todas las secciones ya rellenas.

## 2. Añade un ensayo

En el **Dashboard** haz clic en **+ Ensayo continuo** (o **+ Ensayo en sondeo** para SPT). Introduce:

- **Código**: código identificativo del ensayo (p. ej. `DP-1`)
- **Instrumento**: selecciona del catálogo (DPM, DPSH, DPH, DPL…). El instrumento define la masa del martinete, la altura de caída y el paso de avance — todos los parámetros energéticos ya están tabulados internamente.
- **Coordenadas**: introduce lat/lon para posicionar el ensayo en el mapa (opcional pero útil para el export del plano de situación).

## 3. Introduce las lecturas

Ve a la pestaña **Lecturas**. Dispones de tres modos:

- **Manual**: escribe el número de golpes fila a fila.
- **Importar CSV**: pega o carga un archivo desde un datalogger — el sistema reconoce automáticamente la profundidad y los golpes.
- **Importar .dypx**: carga directamente un archivo exportado desde el escritorio GeoStru Dynamic Probing.

El gráfico N/profundidad se actualiza en tiempo real.

## 4. Interpreta la estratigrafía

Ve a la pestaña **Estratigrafía interpretada**. La aplicación propone un primer estrato en toda la profundidad.

- Haz clic en **+ Añadir estrato** para subdividir el perfil.
- Para cada estrato establece la profundidad inferior, el **tipo de suelo** (cohesivo / no cohesivo / mixto) y el **peso específico** γ.
- El método de agregación N_SPT por estrato se elige en el encabezado de la columna (por defecto: media). Ver [Estratigrafía →](stratigrafia.md) para los 7 métodos disponibles.

!!! tip "Colores e indicadores"
    El indicador **Σ estratos / ensayo** en la parte inferior muestra si la suma de las profundidades de los estratos coincide con la profundidad del ensayo (marca verde = coherente, triángulo amarillo = desviación a verificar).

## 5. Lee las correlaciones

Pestaña **Correlaciones geotécnicas**: para cada estrato aparece una tabla con los parámetros estimados (Cu, φ, Mo, Ey, Vs, γ, Dr …) calculados a partir de las fórmulas de referencia de la literatura geotécnica. Ver [Correlaciones →](correlazioni.md).

!!! note
    Las correlaciones son estimaciones empíricas. Úsalas como punto de partida — complementa siempre con datos de laboratorio cuando estén disponibles.

## 6. Comprueba la categoría de subsuelo

Pestaña **Cat. suelo**: la aplicación calcula la velocidad equivalente V_s,30 y asigna automáticamente la categoría NTC 2018. Ver [Categoría →](categoria.md).

## 7. Exporta el informe

Menú **Archivo → Guardar** para descargar el archivo `.dprobe`. Menú **Exportar → Informe Word** para el informe completo.

En 5 minutos has obtenido:

- ✅ un ensayo con lecturas
- ✅ una estratigrafía interpretada
- ✅ los parámetros geotécnicos para cada estrato
- ✅ la categoría de subsuelo
- ✅ el archivo de proyecto descargado
