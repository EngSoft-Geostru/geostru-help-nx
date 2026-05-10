# Dati di input — descrizione di ogni campo

Riferimento campo per campo dell'app RSL III. Per il flusso operativo vedi
[Workflow](workflow.md).

## Stratigrafia

Tab **Stratigrafia** — definisci la colonna 1D dal piano campagna verso il
basso, fino a raggiungere la **bedrock** (substrato di riferimento sismico,
Vs ≥ 800 m/s).

### Per ogni strato

| Campo | Unità | Descrizione |
|---|---|---|
| **Spessore (h)** | m | Spessore dello strato. Somma totale ≥ profondità della bedrock di riferimento. |
| **Vs** | m/s | Velocità delle onde di taglio in piccolo deformazioni (γ < 10⁻⁴%). Da prove sismiche dirette: cross-hole, down-hole, MASW, ReMi, sismica passiva (microtremor HVSR). |
| **ρ** (densità) | kN/m³ | Peso dell'unità di volume. Per terreni sopra falda ρ_d (secco), sotto falda ρ_sat (saturo). |
| **G_max** | MPa | Modulo di taglio in piccolo deformazioni. RSL III lo calcola in automatico come `G_max = ρ · Vs²` se non lo inserisci. |
| **ξ_min** | % | Smorzamento minimo (in piccolo). Tipico: 0.5-1% (sabbie addensate), 1-3% (argille), 2-5% (riempimenti antropici). |
| **Curva G/Gmax-γ** | — | Funzione di degradazione del modulo. Scelta dalla libreria (vedi sotto). |
| **Curva ξ-γ** | — | Funzione di smorzamento. Stessa libreria della curva G. |
| **Litologia** | — | Descrittiva, non entra nel calcolo. |

### Criteri per definire la bedrock

L'ultimo strato deve essere la bedrock di riferimento sismico. Caratteristiche:

- **Vs ≥ 800 m/s** (definizione NTC 2018 cat. A)
- **Comportamento elastico lineare** atteso per il livello di sismicità del
  sito (γ < 10⁻³ %)
- Sia abbastanza profonda da catturare la **prima frequenza propria** del
  sito: T₀ = 4H/Vs_media → tipicamente H = 30-100 m

!!! warning "Profondità della bedrock"
    Se la bedrock è troppo superficiale (es. 5-10 m sopra Vs > 800 m/s), il
    sito **non amplifica** in maniera significativa e RSL III restituisce
    output simili allo spettro NTC standard. In questi casi non vale la pena
    fare SRA di dettaglio.

## Curve di degradazione

RSL III viene fornito con la **libreria standard**. Per ogni strato puoi
assegnare:

### Argille (Vucetic-Dobry 1991)

Famiglia di curve in funzione dell'**indice di plasticità IP**:

- **IP = 0** (argille non plastiche / sabbie limose)
- **IP = 15-30** (argille mediamente plastiche)
- **IP = 30-50** (argille molto plastiche)
- **IP > 50** (argille con alta plasticità)

All'aumentare di IP, la curva G/Gmax è "più lenta a degradare" e ξ è più
piccolo. Argille molto plastiche sono il caso meno dissipativo.

### Sabbie (Seed-Idriss 1970)

Famiglia *upper / mean / lower* per sabbie. Per default si usa la **mean**.
Le upper e lower coprono la dispersione naturale delle sabbie.

### Darendeli (2001) — formula generale

Curve sintetiche di letteratura, dipendenti da IP, OCR e σ'_v (pressione di
confinamento). Più moderne, raccomandate per studi avanzati.

### EPRI (1993)

Famiglia di curve per profondità (tipica di studi nucleari). Differenzia per
range di profondità (0-15 m, 15-50 m, 50-150 m, >150 m).

### Curve custom

Carica una tabella `γ [%], G/Gmax [-], ξ [%]` dal tuo studio specifico
(prove di laboratorio: triassiale ciclica, colonna risonante, taglio
torsionale ciclico). Formato CSV con header.

## Accelerogramma di input

Tab **Input sismico**. Caricare l'accelerogramma di accelerazione orizzontale
alla **bedrock**.

### Formati supportati

| Formato | Origine tipica |
|---|---|
| **PEER** | NGA-West / NGA-Subduction, archivio mondiale di accelerogrammi |
| **ITACA** | Italian Accelerometric Archive (INGV, registrazioni italiane) |
| **CSV / TXT** | header `time, accel` (o `t, a`) — generico |
| **GeoStru ACC** | export da [Spectra](https://www.geostru.ai/) o altro software GeoStru |

### Cosa serve sapere dell'accelerogramma

- **Δt** (passo di campionamento): tipicamente 0.005-0.01 s
- **Durata totale**: 20-40 s per registrazioni reali, può arrivare a 80 s
  per accelerogrammi sintetici con coda lunga
- **a_max**: accelerazione di picco (PGA), in g o m/s²
- **Magnitudo Mw e distanza R**: utili nella relazione tecnica (compatibilità
  spettrale con NTC)

### Outcrop vs within

⚠️ Punto critico:

- Se l'accelerogramma è registrato su **bedrock affiorante** (es. roccia
  esposta in superficie), sceglie *"Outcrop"* nell'app. RSL III applicherà la
  deconvoluzione spettrale dimezzando l'ampiezza all'interno della colonna.
- Se l'accelerogramma è già definito **all'interno** della colonna (es. da un
  modello SHAKE precedente), scegli *"Within"*. Nessuna deconvoluzione.

Per le registrazioni di archivio (PEER, ITACA): **outcrop** è l'opzione
giusta nel 99% dei casi.

### Spettro compatibile con NTC

Per analisi conformi NTC 2018, gli accelerogrammi devono essere
**spectro-compatibili** col sito (vita nominale, classe d'uso, periodo di
ritorno). Generalmente si usano:

- **7 accelerogrammi reali** (raccomandazione NTC 2018, paragrafo 7.3.5)
- Modificati con tecniche di scaling o spectral matching per essere
  compatibili con lo spettro target

RSL III in modalità **multi-input** elabora i 7 accelerogrammi e produce lo
spettro **medio** (più envelope/std) — formato pronto per la verifica
strutturale.

## Parametri di iterazione

Tab **Avanzate**:

- **Tolleranza convergenza**: default `0.5%` (variazione massima di γ_eff
  tra iterazioni successive)
- **Max iterazioni**: default `30` (di solito si converge in 4-8)
- **γ_eff/γ_max**: default `0.65` (formulazione Idriss). Alcune
  letterature usano 0.5 o 0.85 per casi particolari.
- **Frequenza massima f_max**: default `25 Hz` (limita la discretizzazione
  e l'aliasing). Per studi con accelerometri high-frequency aumenta.

I valori default sono raccomandati. Modifica solo se sai cosa stai facendo.

## Riepilogo: cosa serve come minimo per partire

1. **Stratigrafia**: 3-10 strati con spessore, Vs, ρ
2. **Curve dinamiche**: scelta dalla libreria (anche default Seed-Idriss)
3. **Accelerogramma**: 1 file PEER o ITACA, durata > 20 s

Tutto il resto è raffinamento.

---

## Vedi anche

- [Workflow completo](workflow.md) — uso pratico dei dati di input
- [Metodo lineare equivalente](metodo.md) — come RSL III usa questi dati
- [FAQ](faq.md) — domande sui parametri di input

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20RSL%20III%20-%20Dati%20input).*
