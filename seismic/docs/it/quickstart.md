# Quickstart — 5 minuti

Obiettivo: dai parametri sismici di un sito reale a un report esportato, in
cinque minuti. Nessuna teoria qui — solo i passi. La spiegazione di ogni
grandezza è nei capitoli [Output](parametri.md).

## 1. Apri l'app

Vai su [`nx.geostru.ai/seismic/`](https://nx.geostru.ai/seismic/) e accedi con
il tuo account GeoStru. Il calcolo dei parametri e la generazione degli spettri
consumano **crediti NX** (vedi [FAQ](faq.md#crediti)).

## 2. Individua il sito

Hai tre modi, tutti equivalenti:

- **Mappa** — clicca il punto esatto sulla mappa. Il marcatore si posiziona e
  le coordinate WGS84 si aggiornano.
- **Indirizzo** — apri il pannello di ricerca e digita un indirizzo o un
  Comune; seleziona il risultato.
- **Coordinate** — inserisci latitudine e longitudine (WGS84 in gradi
  decimali). Per le **isole minori** non coperte dal reticolo continentale,
  scegli l'isola dall'elenco dedicato.

!!! tip "Coordinate da un altro datum"
    Se hai le coordinate in **ED50** o in gradi/primi/secondi, usa la
    conversione integrata: PS Advanced riporta il punto a WGS84 prima di
    interrogare il reticolo.

## 3. Vita nominale e classe d'uso

Imposta:

- **Vita nominale** $V_N$ dell'opera (es. 50 anni per costruzioni ordinarie)
- **Classe d'uso** (I, II, III, IV) → coefficiente d'uso $C_U$

L'app calcola il **periodo di riferimento** $V_R = V_N \cdot C_U$ e, da questo,
i **periodi di ritorno** $T_R$ dei quattro stati limite. Il dettaglio è in
[Vita nominale e classe d'uso](vita-nominale.md).

## 4. Leggi i parametri sismici

Compare la scheda dei quattro **stati limite** — **SLO**, **SLD**, **SLV**,
**SLC** — ciascuno con:

- $a_g$ — accelerazione orizzontale massima su sito di riferimento rigido
- $F_0$ — fattore di amplificazione dello spettro
- $T_C^*$ — periodo di inizio del tratto a velocità costante

I valori sono **interpolati** dai quattro nodi del reticolo più vicini
([come funziona](parametri.md#interpolazione)).

## 5. Sottosuolo, topografia e spettri

Scegli la **categoria di sottosuolo** (A–E) e la **categoria topografica**
(T1–T4). L'app calcola $S_S$, $C_C$, $S_T$ e l'accelerazione di sito
$a_{max}$, poi disegna lo **spettro di risposta elastico** e lo **spettro di
progetto** (imposta il fattore di comportamento $q$). Vedi
[Spettri di risposta](spettri.md).

Nella scheda coefficienti trovi $k_h$ e $k_v$ pronti per le verifiche
geotecniche.

## 6. Esporta

- **Report TXT / PDF** — tabelle dei parametri, categorie, coefficienti e
  spettri per lo stato limite selezionato
- **Salva progetto** — con il pulsante **GeoDropbox** archivi sito e impostazioni
  per riaprirli o condividerli

[Approfondisci con il workflow completo →](workflow.md)

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20PS%20Advanced%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/seismic/docs/it/quickstart.md).*
