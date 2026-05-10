# Dati di input — descrizione di ogni campo

Riferimento campo per campo della pagina **Liquefaction** di LiquiTer NX.
Per il flusso operativo vedi [Workflow](workflow.md).

## Sezione "Dati generali"

### Descrizione

Testo libero, max 200 caratteri. Compare nel frontespizio del Report Word.
Esempio: *"Edificio residenziale 4 piani — Versilia, lotto B"*.

### Indirizzo

Opzionale. Se compilato compare nel report.

### Coordinate (lat / lon)

WGS84 in gradi decimali (es. `41.9028`, `12.4964`). Servono per:

- Geolocalizzare il sito sulla mappa del report
- Pre-compilare a_g e Mw da [Parametri Sismici](https://nx.geostru.ai/parametri-sismici/)
  (se attivi questa funzione)

### Quota falda (Zw)

Profondità della falda in **metri** dal piano campagna.

- Se Zw > Zmax (profondità massima della stratigrafia) → nessun strato
  saturo → **niente liquefazione**
- Se la falda varia stagionalmente → usa il **valore più sfavorevole**
  (più alta) per essere conservativi

## Sezione "Parametri sismici"

### Normativa

| Opzione | Riferimento |
|---|---|
| **NTC 2018** | D.M. 17/01/2018, Cap. 7.11.3.4 (suscettibilità di liquefazione) |
| **EC8 — EN 1998-5** | Eurocodice 8, Annex F |

La scelta determina:
- I fattori di sicurezza limite (NTC default 1.25, EC8 default 1.0)
- Le formule per CSR e fattori correttivi
- I criteri di esclusione (NTC: profondità < 20 m, terreni con > 5% di
  particelle < 5 µm, ecc.)

### Categoria suolo (A · B · C · D · E)

Da Vs,30. Determina i parametri di sito (S_S, S_T) per il calcolo di a_max.

Vedi [workflow.md#categoria-suolo](workflow.md#categoria-suolo-a-b-c-d-e) per la tabella completa.

### Categoria topografica (T1 · T2 · T3 · T4)

Influenza il coefficiente di amplificazione topografica S_T (1.0 – 1.4).

### a_max (accelerazione massima)

Accelerazione di picco al suolo in **g** (per esempio `0.15`).

**Da dove la prendo?**:

- Da [`parametri-sismici.geostru.ai`](https://nx.geostru.ai/parametri-sismici/)
  (gratuito) — inserisci coordinate + periodo di ritorno e ti restituisce a_g
- Da reticolo INGV (`esse1-gis.mi.ingv.it`)
- Da relazioni geologiche del Comune (per microzonazione sismica di
  livello 3)

### Magnitudo Mw

**Magnitudo momento** del terremoto di progetto. Range tipico Italia:
**5.5 – 7.0** a seconda della zonazione INGV.

Per il territorio italiano, si può usare la **magnitudo massima
attesa** della zona sismogenetica (DISS database INGV):

| Zona INGV | Mw tipica |
|---|---|
| Calabria/Sicilia/Friuli | 6.5 – 7.0 |
| Appennino Centrale | 6.0 – 6.7 |
| Pianura Padana | 5.5 – 6.5 |
| Sardegna | < 5.5 (bassa sismicità) |

## Sezione "Metodo di analisi"

Vedi [Metodi di calcolo](metodi.md) per dettagli su ciascuno.

### Sabbie pulite vs limose

- **Sabbie pulite**: contenuto fine (< 0.075 mm) **< 5%**
- **Sabbie limose**: contenuto fine **5–35%**
- > 35% di fine: il terreno è argilloso, non liquefacibile (verifica
  comunque con criterio Boulanger 2014 sulla plasticità)

Influenza la formula di correzione di N1,60 → N1,60,cs (clean-sand
equivalent).

### Sabbie sciolte vs medio-dense

Influenza il fattore di scala K_σ per le tensioni. Sabbie sciolte hanno
maggiore riduzione di CRR all'aumentare di σ'_v.

### Modalità di passo

- **MetaStrato** (default): un punto di calcolo per ogni cambio di strato
- **PassoFisso**: un punto ogni `Δz` (es. ogni 0.5 m)

Il PassoFisso restituisce un grafico FSL(z) più "pulito" ma può
sovrastimare i contributi di strati sottili. MetaStrato è più rappresentativo.

### Fattore di sicurezza limite

Default `1.25` (NTC 2018). Soglia sotto cui un punto è considerato
"liquefacibile". Il calcolo usa questo valore per:

- Codificare l'esito (verde/rosso) in tabella
- Includere/escludere lo strato dall'IPL e dai cedimenti

Per analisi più conservative usa `1.5`. Per analisi al limite (calcolo
del rischio reale, non normativo) usa `1.0`.

## Sezione "Stratigrafia"

Tab dedicata, gestita per **strato**. Per ogni strato:

| Campo | Unità | Significato |
|---|---|---|
| **Profondità top** | m | quota del tetto |
| **Profondità base** | m | quota del letto (la base di uno strato è il top del successivo) |
| **Litologia** | — | descrittiva, non entra nel calcolo |
| **γ** | kN/m³ | peso unità di volume; **totale** sopra falda, **saturo** sotto |
| **N-SPT** | colpi/30cm | dal Standard Penetration Test (UNI EN ISO 22476-3) |
| **qc** | MPa | resistenza alla punta CPT (UNI EN ISO 22476-1). Opzionale. |
| **Vs** | m/s | velocità onde S. Opzionale. |
| **% argilla** | % | frazione < 5 µm; > 35% esclude la liquefazione (NTC) |

### Importazione stratigrafia

Tab **Stratigrafia** ha funzioni di:

- **Importa CSV** (stratigrafia esportata da altri software GeoStru o da Excel)
- **AI Import** (foto del log di sondaggio, l'AI estrae i parametri)
- **Stratigraphy adapter** (compatibilità con altri formati GeoStru)

---

## Vedi anche

- [Workflow completo](workflow.md) — il flusso di tutto il processo
- [Metodi di calcolo](metodi.md) — formule per ogni metodo
- [FAQ](faq.md) — domande sui parametri di input

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20LiquiTer%20NX%20-%20Dati%20input).*
