# PS Advanced NX — Pericolosità sismica NTC 2018

**PS Advanced NX** è il software web GeoStru per il calcolo della
**pericolosità sismica di base** secondo le **NTC 2018** (D.M. 17/01/2018) e
la relativa Circolare applicativa. Scegli un punto sul territorio italiano —
da mappa, da indirizzo o da coordinate — e l'app restituisce i **parametri
sismici** ($a_g$, $F_0$, $T_C^*$) per i quattro stati limite, gli **spettri di
risposta** elastici e di progetto, e i **coefficienti sismici** orizzontale e
verticale ($k_h$, $k_v$) pronti per le verifiche geotecniche e strutturali.

[**Apri PS Advanced**](https://nx.geostru.ai/seismic/){ .md-button .md-button--primary }
[Quickstart in 5 minuti](quickstart.md){ .md-button }

---

## Cosa fa, in sintesi

- **Input**: posizione del sito (mappa / indirizzo / coordinate, isole
  comprese), **vita nominale** $V_N$ e **classe d'uso** ($C_U$), categoria di
  **sottosuolo** (A–E) e categoria **topografica** (T1–T4)
- **Calcolo**: interpolazione dei **4 nodi** della griglia di pericolosità
  sismica più vicini al sito, per i periodi di ritorno $T_R$ derivati da
  $V_R = V_N \cdot C_U$
- **Output**:
  - **Parametri sismici** $a_g$, $F_0$, $T_C^*$ per **SLO · SLD · SLV · SLC**
  - **Spettri di risposta** elastici (orizzontale e verticale) e **di
    progetto** (con fattore di comportamento $q$)
  - **Coefficienti sismici** $k_h$ e $k_v$ per spinte e verifiche
  - **Categorie di sottosuolo e topografiche**: $S_S$, $C_C$, $S_T$, $a_{max}$
- **Export**: report **TXT** e **PDF**, salvataggio del progetto su
  **GeoDropbox**

## Per chi

- **Ingegneri strutturali** che definiscono l'azione sismica di progetto per
  edifici e opere
- **Geologi e ingegneri geotecnici** che calcolano spinte sismiche, verifiche
  di stabilità e portanza con i coefficienti $k_h$, $k_v$
- **Studi di consulenza** che allegano i parametri sismici di sito alla
  relazione geologica o geotecnica

## Come iniziare

1. Apri [`nx.geostru.ai/seismic/`](https://nx.geostru.ai/seismic/)
2. Individua il sito su **mappa**, o cercalo per **indirizzo** / **coordinate**
3. Imposta **vita nominale** e **classe d'uso** (→ periodo di riferimento $V_R$)
4. Scegli la **categoria di sottosuolo** e la **categoria topografica**
5. Leggi **parametri**, **spettri** e **coefficienti sismici**
6. Esporta il **report** (TXT / PDF) o salva il progetto

[Vedi il workflow completo →](workflow.md)

## Capitoli del manuale

### Iniziare

- [**Quickstart**](quickstart.md) — 5 minuti dal primo accesso ai parametri
- [**Workflow completo**](workflow.md) — sequenza dettagliata input → output →
  export

### Input

- [**Localizzazione del sito**](localizzazione.md) — mappa, indirizzo,
  coordinate, datum, isole
- [**Vita nominale e classe d'uso**](vita-nominale.md) — $V_N$, $C_U$, $V_R$,
  periodi di ritorno $T_R$

### Output

- [**Parametri sismici e stati limite**](parametri.md) — $a_g$, $F_0$, $T_C^*$,
  interpolazione della griglia
- [**Categorie di sottosuolo e topografia**](categorie.md) — $S_S$, $C_C$,
  $S_T$, $a_{max}$
- [**Spettri di risposta**](spettri.md) — elastici e di progetto
- [**Coefficienti sismici**](coefficienti.md) — $k_h$, $k_v$

### Riferimento

- [**Formati ed export**](formati.md) — TXT, PDF, GeoDropbox
- [**Glossario**](glossario.md) — termini e simboli
- [**FAQ**](faq.md)

## Riferimenti normativi

- **D.M. 17/01/2018** — «Aggiornamento delle *Norme tecniche per le
  costruzioni*» (NTC 2018)
- **Circolare 21/01/2019 n. 7** C.S.LL.PP. — Istruzioni per l'applicazione
  delle NTC 2018
- **Allegati A e B** alle NTC 2008 — reticolo di riferimento e pericolosità
  sismica di base (INGV)

!!! note "Base dati di pericolosità"
    I valori di $a_g$, $F_0$ e $T_C^*$ derivano dal **reticolo di riferimento**
    nazionale della pericolosità sismica (studio INGV *MPS04*, adottato dalle
    NTC). PS Advanced ne interpola i nodi: non è una stima, è il dato ufficiale
    della normativa per il punto scelto.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20PS%20Advanced%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/seismic/docs/it/index.md).*
