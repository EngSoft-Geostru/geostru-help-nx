# Preguntas frecuentes

## General

??? question "¿Cuál es la diferencia entre Dynamic Probing NX y el Dynamic Probing de escritorio?"
    El escritorio GeoStru Dynamic Probing es la versión histórica para Windows. Dynamic Probing NX es la versión web, accesible desde cualquier navegador sin instalación. Las funcionalidades principales son equivalentes; NX añade soporte multi-ensayo (gestión de un sitio completo con N ensayos), el mapa interactivo, el export AGS4 y la integración con GeoSection NX. Los datos del escritorio se importan en NX mediante el formato `.dypx`.

??? question "¿Los datos se guardan en el servidor?"
    No — Dynamic Probing NX es **local-first**: los datos del proyecto residen en tu navegador (localStorage) y se guardan en tu PC solo cuando exportas el archivo `.dprobe`. Ningún dato del proyecto se envía a los servidores de GeoStru.

??? question "¿Puedo usarlo sin conexión?"
    Se necesita conexión a internet para la carga inicial de la aplicación. Una vez cargada, la aplicación funciona también sin conexión para la introducción de datos y los cálculos (excepto para generar el informe Word, que requiere conexión).

??? question "¿Existe versión móvil?"
    La aplicación está diseñada para escritorio/tableta. En smartphones la navegación funciona pero la introducción de lecturas en pantallas muy pequeñas resulta incómoda.

## Instrumentos y lecturas

??? question "¿Cómo añado un instrumento que no está en el catálogo?"
    Ve a **Instrumentos** desde la barra de navegación → **+ Añadir instrumento**. Introduce: nombre, tipo (DPL/DPM/DPH/DPSH), masa del martinete (kg), altura de caída (m), diámetro de la punta cónica (mm), ángulo de la punta (°), paso de avance (m) y el coeficiente β. El instrumento se guarda en el archivo de proyecto.

??? question "Mi CSV no se reconoce correctamente. ¿Cómo debo formatearlo?"
    Asegúrate de que las dos primeras columnas sean profundidad (m) y golpes (número entero), separadas por coma, punto y coma o tabulador. Elimina las filas de encabezado que no sigan este formato, o introdúcelas como comentarios con `#` al inicio de la línea. Si las coordenadas están en el encabezado, usa el formato: `# lat=41.9028 lon=12.4964 cota=120`.

??? question "¿Puedo excluir lecturas del cálculo?"
    Sí — en la pestaña Lecturas, cada fila tiene una casilla de verificación para excluirla. Las lecturas excluidas no entran en la agregación N_SPT por estrato ni en las correlaciones. Útil para descartar valores anómalos (rechazo anticipado, pérdida de lodos).

## Estratigrafía

??? question "¿Cómo elijo el método de agregación N_SPT?"
    Depende del objetivo. Para una estimación media conservadora usa **Media − 1σ**. Para el valor característico EC7 usa **RNC** (distribución normal) o **RC** (log-normal). Si tienes pocas lecturas por estrato (< 4), prefiere la Media simple o el Mínimo. Ver [Estratigrafía →](stratigrafia.md) para la descripción completa de los 7 métodos.

??? question "El indicador Σ estratos está en amarillo — ¿qué significa?"
    La suma de las profundidades inferiores de los estratos no coincide con la profundidad del ensayo. Comprueba que el último estrato llegue exactamente a la profundidad de final del ensayo (p. ej. si el ensayo es de 12,00 m, el límite inferior del último estrato debe ser 12,00 m).

## Correlaciones

??? question "¿Por qué algunos valores de correlación aparecen como —?"
    Para algunas combinaciones tipo de suelo / autor el parámetro no está definido. Por ejemplo, Dr (densidad relativa) solo está definida para suelos no cohesivos: en los estratos cohesivos la celda muestra —. De forma análoga, Cu (cohesión no drenada) solo está definida para suelos cohesivos.

??? question "¿Puedo introducir valores de laboratorio en lugar de las correlaciones?"
    Actualmente la aplicación usa las correlaciones de N_SPT como fuente primaria. Para el cálculo de la capacidad portante puedes introducir directamente Cu o φ en los campos del estrato en la estratigrafía — esos valores sustituyen a los correlacionados.

## Exportación e informe

??? question "¿El informe Word es editable?"
    Sí — es un archivo `.docx` estándar que se abre en Word, LibreOffice o Google Docs. Puedes personalizar el encabezado, añadir el logotipo de tu estudio y modificar el texto descriptivo. Las tablas numéricas son datos estáticos (no fórmulas de Excel).

??? question "¿Puedo exportar a PDF?"
    No directamente desde la aplicación. Abre el `.docx` generado en Word y usa **Archivo → Imprimir → Guardar como PDF**.

??? question "AGS4: ¿qué grupos se exportan?"
    Se incluyen los grupos: TRAN (datos de transmisión), PROJ (proyecto), LOCA (posición de los ensayos), GEOL (estratigrafía), DPRG (parámetros del ensayo dinámico), DPRB (lecturas de golpes). Las correlaciones y la capacidad portante no se exportan — estos resultados elaborados no forman parte del estándar AGS4 para ensayos dinámicos.
