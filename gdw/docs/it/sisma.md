# Sisma — combinazione sismica NTC 2018

GDW gestisce la combinazione sismica seguendo NTC 2018 con il metodo di
**Mononobe-Okabe** per la spinta sismica del terrapieno.

## Attivazione

Sezione **Dati progetto** → **Normativa**:

- `NTC 2018 (statica)` — Approccio 1, combinazione A1·M1·R3
- `NTC 2018 (sismica)` — Approccio 1, combinazione A2·M2·R3 (richiesta in zone sismiche)

Quando selezioni "sismica" GDW chiama automaticamente l'endpoint
`UpdateNormativa` che ricalcola i coefficienti parziali in base ai parametri
sismici della tua app (PGA, S, tipo terreno, ecc. — gestiti a livello di
account/configurazione).

## Coefficienti sismici

I valori risultanti vengono mostrati nella sezione **Sisma**:

- **k_h** — coefficiente sismico orizzontale (in genere 0.05 ÷ 0.25)
- **k_v** — coefficiente sismico verticale (= 0.5 · k_h per terreni granulari)

In combinazione sismica i coefficienti A sulle azioni diventano **tutti 1.0**
(NTC 2018 § 7.11.6.2): non si amplifica più con γ_G1=1.3 perché l'azione
sismica è già amplificata da PGA. I campi A_PesoMuro, A_Spinta, A_Q diventano
readonly e mostrano "1".

## Mononobe-Okabe (spinta sismica)

L'angolo sismico equivalente è:

$$
\theta = \arctan\left(\frac{k_h}{1 - k_v}\right)
$$

Questo θ entra nella formula di Coulomb sostituendo l'orizzontale:

$$
K_{a,sismico} = \frac{\cos^2(\varphi - \beta - \theta)}{\cos\theta \cdot \cos^2 \beta \cdot \cos(\delta + \beta + \theta) \cdot [1 + \sqrt{R}]^2}
$$

dove R è il termine di Mononobe (vedi [Inclinazione del muro](inclinazione-muro.md)
per la formula completa).

Effetto: per k_h ≈ 0.15 e φ = 35°, K_a sismico ≈ 0.55 (vs 0.36 statico) → spinta
sismica ~50% maggiore della statica.

## Forza inerziale del muro

Il muro stesso subisce una forza inerziale orizzontale:

$$
F_{inerz} = W \cdot k_h \cdot A_{sismica}
$$

dove W è il peso del muro e A_sismica = 1.0. F_inerz è applicato al
baricentro del muro e contribuisce al momento ribaltante (Mr).

## Combinazione ribaltamento sismica

Per la verifica di **ribaltamento** in sismica, NTC 7.11.7 richiede di
considerare le **due combinazioni** kv positivo e kv negativo, prendendo la
più sfavorevole.

GDW automatizza: ricalcola la spinta `thrustRib` con `kv → ±kv`, ricalcola
K_a corrispondente, e usa il valore peggiore.

## R_ribaltamento amplificato

Nella combinazione sismica, il coefficiente R_R per il ribaltamento è
amplificato a **R_rib = 1.2** (vs 1.0 in statica) per NTC § 7.11.

## Effetto pratico sui FS

Per un muro tipo 5 m, terrapieno 25°, φ 35°:

| | Statico | Sismico (k_h=0.15) |
|---|---|---|
| K_a | 0.362 | 0.553 |
| Spinta totale | 85.9 kN/m | 131.2 kN/m |
| F_inerz muro | 0 | 26.4 kN/m |
| FS_ribaltamento | 2.60 | 1.45 |
| FS_scorrimento | 1.85 | 1.10 |

→ I FS scendono significativamente. Spesso in sismica diventa **critica** la
verifica di scorrimento: rimedi tipici sono **inclinazione fondazione β** (vedi
[Fondazione](fondazione.md)) e **base muro più larga**.

## Vedi anche

- [Coefficienti parziali NTC](coefficienti.md) — A2·M2·R3 sismico
- [Inclinazione del muro](inclinazione-muro.md) — β nella formula di Coulomb-MO
- [Verifiche esterne](verifiche.md) — formula scorrimento con base inclinata
- [Sovraccarichi](sovraccarichi.md) — Ψ₂ in combinazione sismica
