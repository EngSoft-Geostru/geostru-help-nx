# Exportación e informe

## Informe Word (.docx)

El informe Word es el informe de cálculo completo, listo para adjuntar a la documentación del proyecto. Se genera desde el menú **Exportar → Informe**.

El documento incluye:

- Encabezado con datos del sitio (nombre, cliente, coordenadas, fecha)
- Ficha del instrumento: tipo, parámetros técnicos, β utilizado
- Perfil de lecturas de golpes N/profundidad (gráfico)
- Tabla de estratigrafía: estratos, profundidades, tipo de suelo, N_SPT por estrato
- Tabla de correlaciones geotécnicas para cada estrato (autores seleccionados)
- Categoría de subsuelo: V_s,eq, categoría asignada, tabla de estratos
- Capacidad portante de cimentaciones (si se ha calculado): tabla comparativa de métodos
- Valores característicos EC7 / NTC §6.2.2 (si se han calculado)

## AGS4 (.ags)

El formato **AGS4** es el estándar abierto para el intercambio de datos geotécnicos (AGS Data Format v4.2). Expórtalo desde **Exportar → AGS4** para compartir los datos del ensayo con otros programas o con el cliente.

Grupos incluidos en el export AGS4: TRAN, PROJ, LOCA, GEOL, DPRG (parámetros del ensayo dinámico), DPRB (lecturas).

## GeoSection (.geosection)

Exporta los ensayos con su estratigrafía interpretada hacia **GeoSection NX** para construir la sección geológica. Desde **Exportar → GeoSection**: selecciona los ensayos a incluir (los que tienen coordenadas), haz clic en **Exportar**. El archivo `.geosection` se abre directamente en la aplicación GeoSection.

## Plano de situación (imagen PNG)

Si los ensayos tienen coordenadas asignadas, desde **Exportar → Plano de situación (imagen)** se obtiene una imagen PNG del plano de situación con la posición de los ensayos, las cotas y las distancias entre ensayos. Disponible solo con al menos 2 ensayos georreferenciados.

## KMZ (Google Earth)

El menú **Exportar → KMZ** genera un archivo visualizable en Google Earth con la posición de todos los ensayos georreferenciados del proyecto.

## Archivo de proyecto (.dprobe)

El archivo `.dprobe` es el formato nativo de Dynamic Probing NX — un JSON legible que contiene toda la información del proyecto (ensayos, instrumentos, estratigrafía, correlaciones, datos del sitio). Se guarda desde **Archivo → Guardar** y se vuelve a abrir desde la Página principal con **Abrir archivo…**.

!!! tip "Compatibilidad con escritorio"
    Puedes importar un archivo `.dypx` (formato texto del escritorio GeoStru Dynamic Probing) desde la Página principal de Dynamic Probing NX. El archivo NX `.dprobe` no puede abrirse con la versión de escritorio.
