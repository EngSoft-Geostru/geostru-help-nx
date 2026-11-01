# Tracce

La scheda **Tracce** prepara i dati che entrano nello spettro.

## Importare

Trascina i file sul riquadro o sceglili: **SEG-2** (`.sg2`, `.seg2`, `.dat`), **SEG-Y** (`.sgy`, `.segy`), **SU** (`.su`), **Ambrogeo** (`.dta`), **SARA DoReMi** (`.drm`),
**Dolang** e **ASCII** (`.txt`, `.asc`, `.csv`). Con **Aggiungi** decidi se le tracce vanno **in testa**, **in coda**, **interposte** o
**sommate** a quelle presenti.

Il file ASCII non dichiara il passo di campionamento: indica **Passo ASCII** e **Prima riga dati**. Ogni riga è un
campione, ogni colonna una traccia, separate da `;`, tabulazione, virgola o spazi.

!!! note "Ampiezze SEG-Y"
    I campioni in virgola mobile IBM (codice 1) sono convertiti correttamente. La versione desktop li leggeva come IEEE.

## Acquisizione

Imposta **dt** (passo di campionamento), **dx** (interdistanza dei geofoni) e **Distanza sorgente** dal primo geofono.
Il passo di campionamento decide la frequenza di Nyquist; dx decide il limite di aliasing spaziale.

## Il sismogramma

Una colonna per geofono, tempo verso il basso, lobi positivi pieni. **Amplificazione** ingrandisce le oscillazioni,
la rotella del mouse fa zoom sul tempo, **Tutto** torna alla vista intera. Ogni traccia è normalizzata sul proprio massimo.

![Sismogramma ed elenco delle tracce](img/02-tracce.png)

## Elenco delle tracce

Per ogni traccia puoi:

- togliere la spunta **Usa nello spettro**: la traccia resta nel progetto ma non entra nel calcolo. Lo spettro tiene
  conto della posizione reale dei geofoni rimasti;
- **Inverti polarità**, **Sposta su**, **Sposta giù**, **Elimina traccia**;
- con **Inverti ordine** rovesciare tutto lo stendimento, se la sorgente era dall'altro lato.

## Ritaglio e filtro

**Ritaglia** disegna sul sismogramma la zona utile: trascina il poligono e premi **Applica ritaglio**. Fuori dalla zona
il segnale si smorza in 20 campioni, senza gradini. **Togli ritaglio** riporta tutto com'era.

Il **Filtro passa-basso** è Butterworth o Chebyshev: scegli **Taglio** e **Attenuazione**. Il filtro è una passata
sola, quindi ritarda un poco il segnale, come nella versione desktop.

Filtro, ritaglio e polarità non toccano i campioni letti: si possono togliere in qualunque momento. Se li cambi dopo aver
calcolato, una striscia ti dice che lo spettro va rifatto.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MASW%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/it/tracce.md).*
