# Stratigrafia e terreni

La sezione **Geotecnica** definisce i parametri dei due terreni principali e
la stratigrafia multistrato del terreno spingente.

## Terreno spingente (a tergo)

È il terreno **a monte** del muro, che esercita la spinta attiva.

### Stratigrafia multistrato

Inserisci da 1 a N strati, dall'**alto verso il basso** (dalla sommità del
muro al piede). Per ogni strato:

| Campo | Significato | Unità | Valori tipici |
|---|---|---|---|
| Descrizione | Nome libero | — | "Sabbia ghiaiosa" |
| Colore | Hex (per il disegno) | — | `#d9ed92` |
| Altezza | Spessore dello strato | m | 1.0 ÷ 5.0 |
| Angolo resistenza taglio φ | Attrito interno | ° | 28 ÷ 40 |
| Peso unità volume γ | Naturale | kN/m³ | 17 ÷ 21 |
| Peso unità volume saturo γ_sat | Sotto falda | kN/m³ | 19 ÷ 22 |
| Coesione c | Apparente | kPa | 0 (ghiaie/sabbie) ÷ 25 (limi/argille) |

L'altezza totale degli strati dovrebbe coprire **almeno l'altezza del muro
più 1÷2 m** (per evitare di non avere terreno fino al piede).

### Spinta multistrato

Per ogni strato GDW calcola un proprio Ka tramite la formula di Coulomb (o
Mononobe-Okabe in sismica) con φ, c, δ specifici di quello strato. Le spinte
elementari vengono sommate, e i punti di applicazione computati con baricentro
trapezoidale della distribuzione di pressioni σ_h(z).

### Coefficienti riduttivi M

I parametri ridotti per il calcolo sono:

$$
\varphi_{red} = \arctan\left(\frac{\tan \varphi}{\gamma_{M\varphi}}\right) \quad ; \quad c_{red} = \frac{c}{\gamma_{Mc}}
$$

Con NTC 2018 A1·M1·R3 (statico): γ_M = 1.0 (non riduce). Con A2·M2·R3
(sismico): γ_M = 1.25.

[Dettagli coefficienti →](coefficienti.md)

## Terreno di fondazione

È il terreno **sotto** la fondazione, che resiste a scorrimento e capacità
portante.

| Campo | Significato | Valori tipici |
|---|---|---|
| Peso unità volume γ_fond | kN/m³ | 18 ÷ 22 |
| Angolo resistenza taglio φ_fond | gradi | 28 ÷ 40 |
| Coesione c_fond | kPa | 0 (granulari) ÷ 30+ (argille) |

Questi valori entrano in:

- **Verifica scorrimento esterno**: φ_fond e c_fond all'interfaccia base muro-terreno (se interfaccia = "terreno")
- **Capacità portante**: Brinch-Hansen / Meyerhof con N_q, N_γ, N_c calcolati da φ_fond
- **Verifica interna fila 0** (senza fondazione c.a.): φ_fond e c_fond come parametri di scorrimento sul terreno

## Falda

Sezione **Dati progetto**:

- **Profondità falda** (m dalla sommità del muro)
- Vuoto o 0 → niente falda
- Valore > 0 → la falda è posizionata a quella profondità

Effetti del calcolo:

- **γ_sat** sostituisce γ negli strati sotto falda
- **Sottospinta idrica** (γ_w = 10 kN/m³) viene sottratta al peso effettivo
- **Spinta idrostatica** S_w = ½·γ_w·h_w² viene aggiunta orizzontalmente alla spinta del terreno

## Interfaccia alla base (scorrimento)

Sezione **Geotecnica**, in fondo:

- **Terreno naturale (φ e c pieni)**: usa i parametri del terreno di fondazione (φ_fond, c_fond).
- **Fondazione c.a./cls (δ = 2/3 φ, c = 0)**: caso di getto in calcestruzzo armato sul gabbione. Attrito ridotto a 2/3 dell'angolo di attrito del terreno, coesione nulla.
- **Personalizzato (valori a scelta)**: l'utente inserisce δ_custom e c_custom in due campi separati. Utile per dati sperimentali (es. test su gabbioni su calcestruzzo: δ ~ 35÷40°).

## Geometria del terreno (profilo)

Sezione **Geometria terreno**:

- **Inclinazione e lunghezza monte 1**: il primo tratto di terrapieno a partire dal top del muro. ε₁ è l'angolo (0÷45° tipico), L₁ in metri.
- **Inclinazione e lunghezza monte 2**: secondo tratto (opzionale, per terrapieni a gradoni).
- **Inclinazione e lunghezza valle**: terreno a valle del muro. Tipicamente 0° (orizzontale) o leggermente pendente.

ε₁ entra nella formula di Coulomb come **angolo di pendenza del terrapieno**:
maggiore ε₁ → maggiore Ka → maggiore spinta.

## Riempimento a tergo (solo allineamento a sinistra)

Quando l'allineamento è "A sinistra" (gradoni verso monte), il muro è
appoggiato contro un riempimento a tergo. GDW richiede parametri **separati**
per il riempimento:

- **Peso specifico riempimento** γ_riemp (kN/m³)
- **Angolo resistenza taglio riempimento** φ_riemp (°)
- **Colore riempimento** (per disegno)

Il peso del riempimento contribuisce al baricentro stabilizzante del sistema
"muro + riempimento", a patto di applicare il coefficiente parziale `A_riemp`
(G2 favorevole, tipicamente 0.8 in statico e 1.0 in sismico).

---

## Vedi anche

- [Coefficienti parziali NTC](coefficienti.md) — γ_M, γ_R, γ_G, γ_Q
- [Sovraccarichi e spinta](sovraccarichi.md)
- [Verifiche esterne](verifiche.md) — capacità portante con γ_fond, φ_fond
