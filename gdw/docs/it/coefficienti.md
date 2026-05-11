# Coefficienti parziali NTC 2018

GDW segue il **D.M. 17 gennaio 2018** (NTC 2018) per la verifica geotecnica
dei muri di sostegno, con l'**Approccio 1** + le combinazioni A·M·R indicate
per i muri a gravità.

## Combinazioni adottate

| Normativa | Combinazione | Quando |
|---|---|---|
| `NTC 2018 (statica)` | **A1 · M1 · R3** | Tutte le verifiche statiche (rib, scorr, q_lim) |
| `NTC 2018 (sismica)` | **A2 · M2 · R3** | Combinazione sismica (NTC § 7.11.6) |

Le combinazioni vengono settate automaticamente dal combo Normativa.

## Coefficienti sulle azioni (A)

| Azione | Simbolo | A1 (statico) | A2 (sismico) |
|---|---|---|---|
| Peso muro (G1 favorevole) | γ_W = A_PesoMuro | 1.0 | 1.0 |
| Spinta terreno (G1 sfavorevole) | γ_S = A_SpintaTerreno | 1.3 | 1.0 |
| Spinta falda | A_SpintaFalda | 1.3 | 1.0 |
| Spinta sismica | A_SpintaSismica | — | 1.0 |
| Sovraccarico permanente (G2) | A_G | 1.3 | 1.0 |
| Sovraccarico variabile (Q) | A_Q | 1.5 | 1.0 |
| Peso riempimento (G2 favorevole) | A_PesoRiempimento | 0.8 | 1.0 |

NB: in sismica i coefficienti A diventano tutti 1.0 perché l'azione sismica è
già amplificata dalla PGA. I campi diventano readonly.

## Coefficienti sui parametri (M)

| Parametro | Simbolo | M1 (statico) | M2 (sismico) |
|---|---|---|---|
| tan φ (angolo attrito) | γ_Mφ = MGFi | 1.0 | 1.25 |
| c (coesione) | γ_Mc = MGC | 1.0 | 1.25 |
| c_u (coesione non drenata) | γ_Mcu = MGCU | 1.0 | 1.4 |

I parametri ridotti entrano nella formula di Coulomb:

$$
\varphi_{red} = \arctan\left(\frac{\tan\varphi}{\gamma_{M\varphi}}\right)
\quad ; \quad
c_{red} = \frac{c}{\gamma_{Mc}}
$$

Per φ = 35° con γ_Mφ = 1.25 → φ_red = 29.5° (riduzione effettiva di 5.5°).

## Coefficienti sulle resistenze (R3)

| Verifica | Simbolo | Valore |
|---|---|---|
| Capacità portante | γ_R3_qlim = RQLim | **2.3** (NTC tab. 6.5.I) |
| Scorrimento sulla base | γ_R3_scorr = RScorrimento | **1.1** (statico) / **1.1** (sismico) |
| Resistenza passiva | γ_R3_passiva = RSpintaPassiva | **1.4** |
| Ribaltamento (EQU) | γ_R_rib = RRibaltamento | **1.0** (statico) / **1.2** (sismico, NTC 7.11.7) |

Le verifiche sono soddisfatte quando:

$$
FS \ge \gamma_R
$$

In GDW i FS visualizzati hanno già γ_R nel denominatore, quindi la verifica è
**FS ≥ 1**.

## Esempio numerico

Verifica scorrimento con base **non** inclinata, in statica:

- F_x (orizzontale sollecitante) = A_S · spinta + A_Q · sovr = 1.3·85 + 1.5·5 = 118 kN/m
- F_y (verticale stabilizzante) = A_W · peso = 1.0·176 = 176 kN/m
- φ_red = arctan(tan(32°)/1.0) = 32°
- R_resistenza = F_y · tan(φ_red) = 176 · 0.625 = 110 kN/m
- FS = R / (γ_R3_scorr · F_x) = 110 / (1.1 · 118) = **0.85** ⚠️ Non verificato

→ Servirebbero: aumentare base muro, o inclinare la fondazione (β > 0), o
aumentare il peso (riempimento, gabbioni più larghi).

## Personalizzazione dei coefficienti

Sezione **Coefficienti di sicurezza** (collassabile): puoi modificare a mano
ogni singolo coefficiente. Caso d'uso:

- Verifica con un'altra normativa (Eurocodice, normative estere)
- Approccio 2 (A1+M1+R2 oppure A2+M2+R1)
- Analisi parametrica (sensibilità ai coefficienti)

Quando cambi normativa dal combo, i valori vengono ricalcolati e sovrascrivono
le modifiche manuali.

## Spinta passiva

Nel caso di **prima fila interrata** (checkbox in Geometria), la spinta
passiva del terreno di fondazione contribuisce alla resistenza allo scorrimento:

$$
S_{p,red} = \frac{1}{2} \cdot \gamma_{fond} \cdot K_p \cdot H_{interrato}^2 / \gamma_{R3,passiva}
$$

Il coefficiente di partecipazione spinta passiva (default 50%) la riduce
ulteriormente per tener conto delle deformazioni necessarie a mobilitarla.

## Vedi anche

- [Verifiche esterne](verifiche.md) — applicazione pratica dei coefficienti
- [Sisma](sisma.md) — A2·M2·R3, R_rib amplificato a 1.2
- [Sovraccarichi](sovraccarichi.md) — γ_G2 e γ_Q
