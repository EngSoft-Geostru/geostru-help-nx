# Dimensionamiento del depósito de retención

## Hietograma de proyecto

El hietograma distribuye en el tiempo la altura de lluvia dada por la curva.

| Tipo | Cuándo usarlo |
|---|---|
| **Chicago** | El más difundido: pico posicionable con el coeficiente r |
| **Uniforme** | Intensidad constante durante toda la duración |
| **Sifalda** | Tres tramos, forma trapecial |
| **Triangular** | Subida y bajada lineales |

Para el Chicago el **coeficiente de posición r** indica dónde cae el pico: 0,4
significa al 40 % de la duración.

![Hietograma y pérdidas hidrológicas](img/05-depurazione-piogge.png)

## Pérdidas hidrológicas

Transforman la lluvia bruta en lluvia neta, es decir, la que se convierte en
escorrentía.

- **Porcentual** — multiplica por el coeficiente de escorrentía φ de la
  superficie. Es el modelo más sencillo y el más usado.
- **Horton** — infiltración decreciente en el tiempo según la clase de suelo.
- **SCS-CN** — método del curve number, con condición de humedad antecedente
  AMC I, II o III.

!!! warning "Lombardia"
    El método SCS-CN no está admitido por el reglamento regional.

## Hidrograma

Transforma la lluvia neta en caudal:

- **Tiempo de concentración** — usa el tiempo de concentración de la superficie.
- **Nash** — cascada de n embalses lineales con constante K, para cuencas más
  articuladas.

## Laminación

El depósito de retención se enruta paso a paso resolviendo el balance de masa
entre caudal entrante, caudal saliente por el órgano de vertido y volumen
acumulado. El máximo del volumen es el resultado del procedimiento detallado.

![Cálculos y verificaciones](img/06-calcoli-verifiche.png)

## Las verificaciones finales

| Verificación | Condición |
|---|---|
| Altura útil | H de proyecto ≥ altura requerida |
| Volumen útil | V de proyecto ≥ volumen admisible |
| Tiempo de vaciado | T ≤ tiempo admitido (por norma 48 h) |

El tiempo de vaciado se calcula solo para los vertidos a caudal constante y para
la infiltración constante: para los demás órganos el caudal depende de la carga
hidráulica y varía durante el vaciado.

---

*¿Has encontrado un error en esta página? [Comunícanoslo](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
