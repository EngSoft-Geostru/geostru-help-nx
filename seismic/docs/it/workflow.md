# Workflow completo

Questa pagina segue un progetto reale dall'inizio alla fine, con tutte le
opzioni. Per la versione rapida vedi il [Quickstart](quickstart.md).

## Il flusso in breve

```text
Localizzazione → Vita nominale + Classe d'uso → Parametri sismici (4 SL)
      → Categoria sottosuolo + topografia → Spettri elastico/progetto
      → Coefficienti sismici → Report / Salvataggio
```

## 1. Localizzazione del sito

La pericolosità sismica di base dipende **solo dalla posizione geografica**: il
primo passo è individuare il punto con precisione.

- **Mappa interattiva** — pan/zoom, clic per posizionare il marcatore.
- **Ricerca per indirizzo** — geocodifica di indirizzo o toponimo.
- **Coordinate manuali** — WGS84 in gradi decimali; conversione da ED50 e da
  gradi/primi/secondi disponibile.
- **Isole minori** — per i siti fuori dal reticolo continentale si usa
  l'elenco delle isole con reticolo dedicato.

Dettagli e casi limite in [Localizzazione del sito](localizzazione.md).

## 2. Vita nominale e classe d'uso

Definiscono per **quanto tempo** e con quale **importanza** l'opera deve
resistere:

$$ V_R = V_N \cdot C_U $$

- $V_N$ — vita nominale (≥ 10, 50 o ≥ 100 anni secondo il tipo di opera)
- $C_U$ — coefficiente d'uso legato alla **classe d'uso** (I → 0.7, II → 1.0,
  III → 1.5, IV → 2.0)

Dal periodo di riferimento $V_R$ discendono i **periodi di ritorno** $T_R$ dei
quattro stati limite, con le probabilità di superamento $P_{V_R}$ di normativa.
Tabella completa in [Vita nominale e classe d'uso](vita-nominale.md).

## 3. Parametri sismici per i 4 stati limite

Per ciascuno stato limite (SLO, SLD, SLV, SLC) l'app interpola dal reticolo i
tre parametri di base:

| Parametro | Significato |
|---|---|
| $a_g$ | accelerazione orizzontale massima al suolo rigido orizzontale |
| $F_0$ | valore massimo del fattore di amplificazione dello spettro in accelerazione |
| $T_C^*$ | periodo di inizio del tratto a velocità costante dello spettro |

L'[interpolazione](parametri.md#interpolazione) usa i **quattro nodi** del
reticolo che racchiudono il sito, pesati con le distanze e sui due periodi di
ritorno che racchiudono $T_R$.

## 4. Categoria di sottosuolo e topografia

L'azione sismica al sito reale si ottiene amplificando quella su suolo rigido:

- **Categoria di sottosuolo** A, B, C, D, E → coefficienti $S_S$ (stratigrafico)
  e $C_C$ (che modifica $T_C$)
- **Categoria topografica** T1, T2, T3, T4 → coefficiente $S_T$

L'accelerazione massima al sito è:

$$ a_{max} = S \cdot a_g = S_S \cdot S_T \cdot a_g $$

Vedi [Categorie di sottosuolo e topografia](categorie.md).

## 5. Spettri di risposta

Con parametri + categorie l'app costruisce:

- lo **spettro elastico** in accelerazione (orizzontale e verticale),
- lo **spettro di progetto**, ottenuto riducendo l'elastico con il **fattore di
  comportamento** $q$ (imposti $q_h$ e $q_v$, valore tipico 1.5 per le verifiche
  geotecniche allo SLV).

Puoi impostare lo **smorzamento** $\xi$ (che definisce il fattore $\eta$) e
scegliere lo stato limite di progetto. Tutti i dettagli in
[Spettri di risposta](spettri.md).

## 6. Coefficienti sismici

Per le verifiche geotecniche (spinte, stabilità, portanza) l'app calcola i
**coefficienti sismici** orizzontale e verticale:

$$ k_h = \beta_s \cdot \frac{a_{max}}{g} \qquad k_v = \pm 0.5 \, k_h $$

dove $\beta_s$ è il coefficiente di riduzione dell'accelerazione massima.
Approfondimento in [Coefficienti sismici](coefficienti.md).

## 7. Report e salvataggio

- **Report TXT** — riepilogo testuale di input e parametri.
- **Report PDF** — documento formattato con parametri dei 4 SL, categorie,
  coefficienti e spettro dello stato limite selezionato.
- **GeoDropbox** — salva il progetto (sito + impostazioni) nello spazio cloud
  GeoStru per riaprirlo o condividerlo tra le app NX.

!!! warning "Rigenera gli spettri prima del PDF"
    Il PDF usa i dati dell'ultimo calcolo in sessione. Se cambi sito o
    parametri, **rigenera gli spettri** prima di esportare, altrimenti l'app
    ti avvisa che i dati sismici non sono disponibili.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20PS%20Advanced%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/seismic/docs/it/workflow.md).*
