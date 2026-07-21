# HID NX — Invariancia hidráulica

HID dimensiona los sistemas de laminación para la **invariancia hidráulica e
hidrológica**: verifica que una actuación de transformación del suelo no aumente
el caudal vertido al receptor respecto a la condición anterior.

La aplicación compara en paralelo los métodos de cálculo que selecciones y adopta
como volumen de retención el **máximo de los resultados**, de modo que la
verificación sigue siendo válida sea cual sea el método exigido por quien tramita
el expediente.

[**Abre la app**](https://nx.geostru.ai/hid/){ .md-button .md-button--primary }

![Interfaz de HID NX, sección Datos generales](img/01-dati-generali.png)

## A quién sirve

A quien proyecta obras de laminación de aguas pluviales: ingenieros hidráulicos,
geólogos y proyectistas que deben adjuntar un informe de invariancia hidráulica a
una licencia de obra, a un plan parcial o a una autorización de vertido.

## Qué calcula

| Ámbito | Contenido |
|---|---|
| Lluvias | Curva intensidad-duración-frecuencia (IDF) GEV o de dos parámetros |
| Hietogramas | Chicago, uniforme, Sifalda, triangular |
| Pérdidas hidrológicas | Coeficiente de escorrentía, Horton, SCS-CN |
| Hidrogramas | Tiempo de concentración y Nash |
| Dimensionamiento | Requisitos mínimos, método de las lluvias, método directo, método del tiempo de concentración, procedimiento detallado |
| Vertido | Ocho órganos, desde los orificios sumergidos hasta los pozos de infiltración |
| Verificaciones | Altura útil, volumen útil, tiempo de vaciado |

## Normativa

HID aplica **perfiles normativos** elegidos en función del país y de la región.
El perfil determina qué métodos están admitidos, qué datos hacen falta, y si el
caudal máximo de vertido y el volumen mínimo los impone la normativa o los eliges
tú.

- **Lombardia** — R.R. 7/2017, integración 2019, R.R. 3/2025: curva GEV
  obligatoria, SCS-CN excluido, criticidad y caudal máximo de vertido derivados
  del municipio.
- **Emilia-Romagna y Marche** — método directo regional con n = 0,48.
- **Cualquier otro país o región** — perfil genérico: métodos libremente
  combinables, caudal máximo de vertido y volumen mínimo elegidos por ti.

!!! note "Fuera de Italia"
    Donde no existe un callejero de municipios, la región y las coordenadas se
    introducen a mano. No es un error: es la forma prevista de trabajar en los
    países todavía no cubiertos por un perfil dedicado.

## Por dónde empezar

- [Guía rápida](quickstart.md) — el primer dimensionamiento en cinco minutos
- [Flujo de trabajo completo](workflow.md) — un proyecto real desde el inicio hasta el informe
- [Glosario](glossario.md) — los términos del dominio, con los símbolos usados en la app

---

*¿Has encontrado un error en esta página? [Comunícanoslo](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
