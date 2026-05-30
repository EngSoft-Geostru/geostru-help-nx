# Capacidad portante de cimentaciones

## Cimentaciones superficiales

Dynamic Probing NX calcula la **presión admisible** para cimentaciones superficiales sobre suelos granulares y cohesivos según los métodos de referencia de la literatura geotécnica. Los resultados se expresan en kPa.

### Métodos disponibles

| Método | Tipo de suelo | Notas |
|---|---|---|
| **Terzaghi-Peck** | Arenas, gravas | Clásico desde N_SPT, incluye corrección por asiento |
| **Meyerhof** | Arenas, gravas | Tiene en cuenta forma y profundidad de la cimentación |
| **Bazaraa** | Arenas, gravas | Alternativa conservadora a Meyerhof |
| **Peck-Hanson-Thornburn** | Arenas, gravas | Con límite de asiento admisible |
| **Meigh-Hobbs** | Arcillas | Desde N_SPT para suelos cohesivos |
| **De Beer-Martens** | Arenas | Método europeo |

### Datos de entrada requeridos

En la pestaña **Capacidad portante** establece:

- **Ancho de cimentación B** (m)
- **Profundidad de empotramiento D** (m desde el nivel del terreno)
- **Asiento admisible** (mm) — típicamente 25 mm para cimentaciones corridas, 25–50 mm para zapatas aisladas
- **Estrato de cálculo**: el método usa N_SPT del estrato en el que está empotrada la cimentación

### Lectura del resultado

La tabla muestra la presión admisible q_adm para cada método. El informe presenta todos los métodos comparados — elige el más adecuado al contexto estratigráfico.

!!! warning "Cimentaciones sobre arcillas"
    Para cimentaciones sobre arcillas, el cálculo se basa en Cu derivado de la correlación N_SPT → Cu. Complementa con ensayos de laboratorio (triaxial, consolidación) para los proyectos definitivos.

## Cimentaciones profundas — pilote hincado (Meyerhof)

Para pilotes hincados, la aplicación implementa el método de **Meyerhof** que estima por separado:

- **Q_p**: capacidad portante en punta (contribución del estrato por debajo de la punta del pilote)
- **Q_l**: capacidad portante por fuste (contribución de los estratos atravesados por el pilote)
- **Q_tot = Q_p + Q_l − W_p**: capacidad portante total neta del peso propio del pilote

### Datos de entrada requeridos

- **Diámetro del pilote** D (m)
- **Longitud del pilote** L (m)
- **Tipo de pilote**: el método Meyerhof distingue entre pilotes hincados en arena y en arcilla

El cálculo usa los valores N_SPT de los estratos según la distribución de profundidad definida en la estratigrafía. La capacidad portante total se reporta en kN.

!!! info "Coeficiente de seguridad"
    La capacidad portante admisible se obtiene dividiendo la capacidad portante última por el coeficiente de seguridad global. Dynamic Probing NX reporta la capacidad portante última — la aplicación del coeficiente de seguridad es responsabilidad del proyectista según la normativa aplicable.
