# Fattori di amplificazione ICMS

I **fattori di amplificazione** quantificano in modo sintetico quanto il
sito amplifica lo scuotimento sismico rispetto alla bedrock di riferimento.
Sono il principale output di una **microzonazione sismica di Livello 3**
secondo gli **Indirizzi e Criteri per la Microzonazione Sismica**
(ICMS 2008/2018, Dipartimento della Protezione Civile).

## I 3 fattori

ICMS richiede **tre fattori** calcolati su intervalli specifici di periodo:

| Fattore | Intervallo | Significato |
|---|---|---|
| **FA** | 0.1 – 0.5 s | Brevi periodi — strutture rigide (edifici fino a 5 piani) |
| **FH** | 0.4 – 0.8 s | Periodi medio-lunghi — edifici 5-10 piani |
| **FT** | tutti | Spettro completo (uno scalare riassuntivo) |

Ogni fattore è il rapporto tra l'integrale dello spettro di risposta del
sito (output RSL) e l'integrale dello spettro NTC della categoria A
(bedrock di riferimento), sull'intervallo di periodo specifico:

$$
F = \frac{\int_{T_1}^{T_2} \text{PSA}_{\text{site}}(T) \, dT}{\int_{T_1}^{T_2} \text{PSA}_{\text{bedrock}}(T) \, dT}
$$

(formulazione semplificata — la versione ICMS usa l'integrazione sui valori
discreti del PSA al passo specificato dalle norme).

## Interpretazione

- **F = 1.0** → il sito si comporta come una bedrock standard (nessuna
  amplificazione)
- **F = 1.0–1.5** → amplificazione modesta, comune
- **F = 1.5–2.0** → amplificazione importante, sito sensibile
- **F > 2.0** → amplificazione molto alta, terreno problematico (bacini
  sedimentari, terreni soffici di grande spessore)

I valori di F sono il **principale input** per le **carte di
microzonazione sismica** comunali e per le decisioni urbanistiche
(zone instabili, zone stabili amplificate, zone stabili non amplificate).

## Quale fattore usare per cosa

### Per progettazione di edifici

Dipende dal **periodo proprio** dell'edificio T₁:

- **Edifici bassi** (1-3 piani, T₁ ≈ 0.1-0.3 s): usa **FA**
- **Edifici medi** (4-7 piani, T₁ ≈ 0.4-0.7 s): usa **FH**
- **Edifici alti** (10+ piani, T₁ > 1 s): usa direttamente lo spettro RSL,
  perché ICMS standard non copre periodi alti

### Per microzonazione comunale

Si producono **carte di FA** e **carte di FH** sovrapposte alla cartografia
geologica del Comune. Le aree con stesso intervallo di F sono
**microzone sismiche omogenee**.

### Per studi di vulnerabilità

FT (singolo scalare) è il modo più veloce di confrontare diverse
combinazioni stratigrafia-input.

## Procedura ICMS Livello 3 in pratica

1. **Identifica le sezioni geologiche** rappresentative del Comune
   (tipicamente 3-10 sezioni)
2. **Definisci la stratigrafia** lungo ogni sezione (Vs da MASW + sondaggi
   geognostici)
3. **Scegli 7 accelerogrammi** spectro-compatibili con NTC della zona
4. Per ogni colonna stratigrafica significativa, lancia RSL III in
   **multi-input** con i 7 accelerogrammi
5. Calcola FA, FH, FT come **medi** sui 7 accelerogrammi
6. Crea le **carte tematiche** sovrapponendo i valori di F sulle micro-aree
7. Pubblica la **relazione di microzonazione** secondo la struttura ICMS

RSL III include il calcolo automatico di FA, FH, FT — vedi tab **Risultati**
→ scheda **Fattori di amplificazione**.

## Output di RSL III per ICMS

Il **Report Word** include automaticamente:

- Tabella dei 3 fattori per ogni accelerogramma di input
- **Statistica** (media, deviazione standard) se modalità multi-input
- Grafico spettro PSA medio + envelope max/min
- Confronto con spettro NTC standard (cat. A) → linea di riferimento

Per un **progetto di microzonazione** completo, esporta anche:

- CSV dello spettro PSA punto-per-punto (per cartografia GIS)
- Profili γ, a, σ vs profondità (per relazione tecnica)

## Riferimenti normativi

- **ICMS 2008/2018** — Indirizzi e Criteri per la Microzonazione Sismica,
  Dipartimento della Protezione Civile (DPC)
- **NTC 2018** — D.M. 17/01/2018, capitolo 7.11.3 (azione sismica)
- **EC8 — EN 1998-5** — Eurocodice 8, Annex F (effetti locali)
- **OPCM 3274/2003** e **3519/2006** — istituzione della microzonazione
  sismica obbligatoria nei comuni italiani

---

## Vedi anche

- [Metodo lineare equivalente](metodo.md) — come si calcolano i fattori
- [Workflow completo](workflow.md) — la microzonazione end-to-end
- [FAQ](faq.md) — domande sull'ICMS

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20RSL%20III%20-%20ICMS).*
