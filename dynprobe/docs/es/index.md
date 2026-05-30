# Dynamic Probing NX

> Procesamiento de **ensayos de penetración dinámica** (DPL · DPM · DPH · DPSH) y **SPT en sondeo** — estratigrafía automática, correlaciones geotécnicas, categoría de subsuelo NTC 2018, capacidad portante de cimentaciones superficiales y profundas, valores característicos EC7 / NTC §6.2.2.

[**Abrir la aplicación**](https://nx.geostru.ai/dynprobe/){ .md-button .md-button--primary }
[Guía rápida (5 minutos)](quickstart.md){ .md-button }

---

## Resumen

- **Qué hace**: lee las lecturas de campo de un ensayo dinámico continuo o de una serie de ensayos SPT en sondeo, devuelve la estratigrafía interpretada con los parámetros geotécnicos característicos y las verificaciones de capacidad portante, todo conforme a las normativas vigentes (NTC 2018, NTC 2008, EC8, Eurocódigo 7).
- **Para quién**: geólogos e ingenieros geotécnicos que necesitan procesar sondeos dinámicos, clasificar el perfil estratigráfico y producir el informe de cálculo.
- **En cuántos minutos**: 5 (caso con archivo .dypx de ejemplo) → 30 (caso real completo con estratigrafía, correlaciones y capacidad portante).

## Flujo de trabajo típico

1. Abre la aplicación: `nx.geostru.ai/dynprobe/`
2. Crea un archivo nuevo o importa un `.dypx` desde el escritorio GeoStru o un CSV desde un datalogger.
3. Ve a **Datos generales** y completa la información del sitio (nombre, coordenadas, instrumento, cliente).
4. Introduce (o comprueba) las **lecturas de golpes** en la pestaña Lecturas: la aplicación las visualiza inmediatamente en el gráfico N/profundidad.
5. Pasa a la **Estratigrafía interpretada**: define el número de estratos, los límites y el tipo de suelo (cohesivo / no cohesivo). La aplicación calcula el N_SPT medio por estrato con el método elegido.
6. Consulta las **Correlaciones geotécnicas** — para cada estrato, una tabla con los parámetros derivados (Cu, φ, Mo, Ey, Vs, γ …).
7. Verifica la **Categoría de subsuelo** según NTC 2018 / NTC 2008 / EC8.
8. Si es necesario, calcula la **Capacidad portante** de una cimentación superficial o profunda (pilote hincado Meyerhof).
9. Lee los **Valores característicos** EC7 / NTC §6.2.2 en la pestaña dedicada.
10. Exporta el **informe Word** (Informe) o el archivo de proyecto `.dprobe`.

## Capítulos del manual

| Capítulo | Contenido |
|---|---|
| [Guía rápida](quickstart.md) | Desde la carga del archivo hasta el primer resultado en 5 minutos |
| [Instrumentos](strumenti.md) | DPL, DPM, DPH, DPSH, SPT en sondeo — cómo introducirlos y los parámetros relevantes |
| [Estratigrafía interpretada](stratigrafia.md) | Cómo definir los estratos, los 7 métodos de agregación N_SPT |
| [Correlaciones geotécnicas](correlazioni.md) | Parámetros derivados para suelos cohesivos y no cohesivos, autores de referencia |
| [Categoría de subsuelo](categoria.md) | NTC 2018, NTC 2008, EC8 — datos de entrada, lógica de cálculo, lectura del resultado |
| [Capacidad portante de cimentaciones](portanze.md) | Cimentaciones superficiales (6 métodos) y profundas (Meyerhof pilote hincado) |
| [Valores característicos](caratter.md) | EC7 §2.4.5.2 / NTC §6.2.2 — normal, lognormal, Student-t |
| [Exportación e informe](export.md) | Informe Word, AGS4, GeoSection, plano de situación, KMZ |
| [Formatos de archivo](formati.md) | `.dprobe` (JSON NX) · `.dypx` (escritorio) · CSV datalogger |
| [Recursos y ejemplos](risorse.md) | Archivos de ejemplo descargables |
| [Preguntas frecuentes](faq.md) | Preguntas frecuentes |
