# Instrumentos — DPL · DPM · DPH · DPSH · SPT en sondeo

## Ensayos dinámicos continuos

En el ensayo dinámico continuo el martinete cae repetidamente y se cuenta el número de golpes necesarios para hacer avanzar la punta cónica un paso fijo (típicamente 10 o 20 cm). La secuencia golpes/profundidad es la materia prima de todo el procesamiento.

Dynamic Probing NX soporta los cuatro tipos normalizados por **UNI EN ISO 22476-2**:

| Código | Tipo | Energía por golpe |
|---|---|---|
| **DPL** | Ligero | baja |
| **DPM** | Medio | media |
| **DPH** | Pesado | alta |
| **DPSH** | Superpesado | muy alta |

Cada tipo tiene masa del martinete, altura de caída y diámetro de la punta cónica definidos por la norma. En la biblioteca de instrumentos de la aplicación encontrarás los modelos más difundidos en el mercado ya tabulados — también puedes añadir un instrumento personalizado con tus propios datos de calibración.

### El coeficiente de correlación β

El coeficiente β convierte el número de golpes del ensayo dinámico (N_DPM, N_DPSH…) en el N_SPT equivalente. El valor depende del instrumento y se determina mediante ensayos comparativos in situ. Cada instrumento del catálogo tiene un β por defecto; puedes sobreescribirlo con el valor de tu calibración específica.

## Ensayos SPT en sondeo

El ensayo SPT (Standard Penetration Test, **UNI EN ISO 22476-3**) se realiza dentro de un sondeo. Se hinca el tomamuestras 45 cm en tres tramos de 15 cm:

- **N1**: primer tramo (asentamiento) — no entra en el recuento
- **N2** + **N3**: segundo y tercer tramo → **N_SPT = N2 + N3**

Añade un ensayo SPT en sondeo desde el Dashboard con el botón **+ Ensayo en sondeo**. Define las cotas de inicio de cada hinca (p. ej. 1,0 m — 2,5 m — 4,0 m) y para cada una introduce N1, N2, N3. La aplicación calcula automáticamente N_SPT y construye el perfil.

### Estratigrafía de los ensayos en sondeo

Para los ensayos SPT en sondeo la estratigrafía se introduce manualmente en la sección **Estratigrafía interpretada**, estrato por estrato, exactamente igual que para los ensayos continuos. El N_SPT medio por estrato se calcula a partir de las hincas que caen dentro del rango de profundidad del estrato.

## Biblioteca de instrumentos

Ve a **Instrumentos** desde la barra de navegación para acceder a la biblioteca. Puedes:

- Ver los parámetros de cada instrumento (masa, altura de caída, diámetro de la punta cónica, ángulo de la punta, paso, β)
- Añadir un instrumento personalizado
- Modificar el β de un modelo existente para tu datalogger específico

Los instrumentos se guardan en el archivo de proyecto `.dprobe` — el archivo es autónomo y portátil a otro PC sin perder los datos de calibración.
