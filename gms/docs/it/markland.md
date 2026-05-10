# Test di Markland — verifica cinematica

Il **test di Markland** (1972) è la procedura grafico-statistica
classica per stabilire se un pendio roccioso è **cinematicamente
suscettibile** a uno dei tre meccanismi di rottura fondamentali:
**scivolamento planare**, **ribaltamento** (toppling), **scivolamento
di cuneo**.

GMS NX esegue il test in automatico al **Calcola**, restituendo:

- un **banner di sintesi** colorato (verde / giallo / rosso)
- una **strip KPI** con i contatori per categoria
- l'evidenziazione grafica sullo stereonet (poli colorati, ⊗ rossi
  per i cunei instabili)

## Cosa serve in input

3 valori obbligatori (tab **Stabilità**):

- **Dip pendio (α)** — inclinazione del versante in gradi (0–90)
- **Dip direction pendio (β)** — azimut della direzione di
  immersione del versante (0–360)
- **Angolo d'attrito (φ)** — gradi (tipicamente 25–35° per ammassi
  rocciosi sani, 15–25° per ammassi alterati o con riempimenti
  argillosi)

Senza questi valori GMS calcola comunque stereonet e statistica
Fisher, ma il banner di sintesi e le KPI di Markland restano **vuoti**.

## I 3 cinematismi

### 1. Scivolamento planare (Hoek & Bray 1981)

Un giunto è **planare instabile** se:

- **Stesso quadrante** del pendio: `|β_giunto - β_pendio| < 20°`
- **Daylighting**: `α_giunto < α_pendio` (il piano "esce" dal versante,
  non è coperto)
- **Attrito insufficiente**: `α_giunto > φ`

Tutti e tre i criteri devono essere veri.

Sullo stereonet i poli planari instabili cadono nella **mezzaluna**
delimitata da:

- ciclografica del pendio (esterno)
- cono d'attrito (interno)
- arco di ±20° in azimut dal pendio

### 2. Ribaltamento (Goodman & Bray 1976)

Un giunto è **toppling instabile** se:

- **Quadrante opposto** rispetto al pendio: `|β_giunto - (β_pendio + 180°)| < 30°`
- **Inclinazione alta**: il piano si "inarca" verso il versante
- **Test di Goodman**: `(90° - α_giunto) + φ < α_pendio`

I poli toppling instabili cadono in una zona opposta a quella planare
sullo stereonet.

### 3. Scivolamento di cuneo

Una **coppia di famiglie** può formare un cuneo instabile se la **retta
di intersezione** (= prodotto vettoriale dei poli):

- ha **trend** entro ±20° dalla direzione di immersione del pendio
- ha **plunge < α_pendio** (daylighting del cuneo)
- ha **plunge > φ** (attrito insufficiente)

GMS calcola tutte le `(N × (N-1))/2` intersezioni delle famiglie e
marca con `⊗` rosso quelle che soddisfano i criteri.

## I KPI

In cima ai risultati (tab **Risultati**) vedi 5 contatori categorici:

| KPI | Significato | Colore se > 0 |
|---|---|---|
| **Planari** | Numero di poli con `α > φ` nel quadrante del pendio | 🔴 rosso |
| **Toppling** | Numero di poli che soddisfano Goodman & Bray | 🟡 giallo |
| **Stabili** | Tutti gli altri poli (default) | 🟢 verde sempre |
| **Cunei instabili** | Coppie di famiglie con intersezione critica | 🔴 rosso |
| **Pendio · attrito** | Riepilogo geometria pendio (α°/β° · φ°) | 🔘 grigio |

## Il banner di sintesi

In cima alla pagina dei risultati GMS NX restituisce un banner
sintetico che riassume la verifica in 3 livelli:

- 🟢 **Versante stabile** (verde) — nessun cinematismo critico
  rilevato. KPI planari + cunei = 0.
- 🟡 **Attenzione: ribaltamenti rilevati** (giallo) — nessun
  scivolamento ma poli compatibili con toppling. Da approfondire
  caso per caso.
- 🔴 **Versante a rischio** (rosso) — almeno un cinematismo planare o
  cuneo è geometricamente possibile.

!!! warning "Markland è *necessario* ma *non sufficiente*"
    Il test risponde alla domanda *"esiste un meccanismo di rottura
    geometricamente compatibile?"*. **Non** dice *"il versante crollerà"*:
    
    - Un cinematismo possibile può essere **bloccato da un ponte di
      roccia**, da una persistenza limitata del giunto, o dalla
      presenza di un riempimento.
    - Un versante con KPI tutti a zero può comunque **collassare** per
      meccanismi non rappresentati (ribaltamenti flessurali, rotture
      circolari in roccia molto fratturata, fenomeni dinamici, …).
    
    GMS produce **input geometrici** per la perizia. La perizia
    finale resta del professionista.

## Esempio numerico

Configurazione:

- Pendio: α = **60°**, β = **180°** (immersione Sud)
- Attrito: φ = **30°**
- Famiglie rilevate (k-means):
  - F1: α=70°, β=190° (giunto sub-verticale, leggermente a Sud)
  - F2: α=20°, β=350° (sub-orizzontale, con immersione Nord)
  - F3: α=85°, β=270° (sub-verticale, immersione Ovest)

Verifica:

- **F1 vs planare**: stesso quadrante (Δβ = 10° < 20°) ✓; α=70° < α_pendio=60° ✗ — **non daylight, stabile**
- **F2 vs toppling**: quadrante opposto (Δβ ≈ 170° ≈ 180°) ✓; (90°-20°)+30° = 100° > 60° ✗ — **non soddisfa Goodman, stabile**
- **F3 vs planare/toppling**: quadrante laterale, fuori da entrambi
- **F1 ∩ F2**: intersezione plunge ≈ 18°, trend ≈ 195° → trend nel
  quadrante del pendio (✓), plunge < α_pendio (✓), plunge < φ (✗) —
  **cuneo stabile per attrito**
- **F1 ∩ F3**, **F2 ∩ F3**: trend fuori dal quadrante del pendio →
  non considerati

Risultato Markland: 0 planari, 0 toppling, 0 cunei → **banner verde**.

---

## Vedi anche

- [Stereonet](stereonet.md) — gli elementi grafici del test
- [Famiglie di discontinuità](famiglie.md) — la base del test su cunei
- [Workflow completo](workflow.md) — Markland nel ciclo intero
- [Glossario](glossario.md) — definizione di φ, daylighting, …

---

## Riferimenti

- **Markland J.T. (1972)** — *A useful technique for estimating the
  stability of rock slopes when the rigid wedge slide type of failure
  is expected*. Imperial College Rock Mechanics Research Report 19.
- **Hoek E. & Bray J.W. (1981)** — *Rock Slope Engineering*, 3rd ed.,
  IMM London.
- **Goodman R.E. & Bray J.W. (1976)** — *Toppling of rock slopes*.
  ASCE Specialty Conference on Rock Engineering, Boulder.

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20GMS%20NX%20-%20Markland).*
