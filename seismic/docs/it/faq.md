# FAQ

## I parametri sono diversi da quelli di un altro strumento. Perché?

Nella quasi totalità dei casi la causa è una di queste:

- **Coordinate diverse** — anche poche centinaia di metri, vicino a un bordo di
  zona, cambiano i valori interpolati.
- **Datum non convertito** — coordinate ED50 usate come WGS84 (o viceversa).
  Usa la [conversione integrata](localizzazione.md#datum-e-conversione-delle-coordinate).
- **Arrotondamenti** — alcuni strumenti troncano i valori intermedi.

PS Advanced interpola direttamente i nodi ufficiali del reticolo con le formule
dell'Allegato alle NTC. Vedi [Interpolazione](parametri.md#interpolazione).

## Il mio sito è su un'isola minore e non trovo il punto sulla mappa

Le isole minori fuori dal reticolo continentale hanno **valori dedicati**:
selezionale dall'elenco delle isole invece di cliccare sulla mappa. Vedi
[Localizzazione del sito](localizzazione.md#isole-minori).

## Che differenza c'è tra spettro elastico e spettro di progetto?

Lo **spettro elastico** rappresenta l'azione sismica su una struttura che
resta in campo elastico. Lo **spettro di progetto** lo riduce con il **fattore
di comportamento** $q$ per tener conto della capacità dissipativa/duttilità.
Dettagli in [Spettri di risposta](spettri.md).

## Quale fattore di comportamento $q$ devo usare?

Dipende dalla tipologia strutturale e dalla classe di duttilità (Cap. 7 NTC).
Per le **verifiche geotecniche** allo SLV si usa spesso $q = 1.5$; per le
strutture può essere molto maggiore. Il valore di default in app è 1.5,
cautelativo: adattalo al tuo caso.

## Come scelgo la categoria di sottosuolo?

In base alla velocità equivalente delle onde di taglio nei primi 30 m
($V_{S,eq}$), da indagini geofisiche o geotecniche. La
[tabella delle categorie](categorie.md#categoria-di-sottosuolo) riporta gli
intervalli. Se serve un'analisi della risposta sismica locale più accurata,
usa [RSL III](https://help.nx.geostru.ai/rsl/).

## A cosa servono $k_h$ e $k_v$?

Sono i **coefficienti sismici** per le verifiche geotecniche pseudo-statiche
(spinte, stabilità, portanza, scorrimento). Vedi
[Coefficienti sismici](coefficienti.md).

## Il PDF non si genera / segnala "dati non disponibili" { #crediti }

Il report usa l'ultimo calcolo in sessione. Dopo ogni modifica di sito o
parametri, **ricalcola gli spettri** prima di esportare.

## Il calcolo consuma crediti?

Sì: il calcolo dei parametri, la generazione degli spettri, l'export della
relazione e l'assistente AI consumano **crediti NX** secondo il listino
dell'app. Il saldo è visibile nell'interfaccia. Per acquistare crediti o
gestire l'abbonamento vai su [geostru.ai](https://www.geostru.ai/).

## Posso salvare e riprendere un progetto?

Sì, con il pulsante **GeoDropbox**: salva sito e impostazioni nello spazio
cloud GeoStru e li riapri quando vuoi. Vedi [Formati ed export](formati.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20PS%20Advanced%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/seismic/docs/it/faq.md).*
