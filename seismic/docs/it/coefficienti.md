# Coefficienti sismici

Per le **verifiche geotecniche** con il metodo pseudo-statico — spinte sui muri,
stabilità dei pendii, capacità portante e scorrimento delle fondazioni — l'azione
sismica si rappresenta con due coefficienti adimensionali: $k_h$ (orizzontale) e
$k_v$ (verticale). PS Advanced li calcola direttamente dai parametri del sito.

## Coefficiente orizzontale $k_h$

$$ k_h = \beta_s \cdot \frac{a_{max}}{g} $$

dove:

- $a_{max} = S_S \cdot S_T \cdot a_g$ è l'[accelerazione massima al sito](categorie.md#accelerazione-massima-al-sito)
- $g$ è l'accelerazione di gravità
- $\beta_s$ è il **coefficiente di riduzione** dell'accelerazione massima attesa

Il coefficiente $\beta_s$ (< 1) tiene conto della capacità dell'opera di
subire spostamenti senza cadere in condizioni di collasso; dipende dalla
categoria di sottosuolo e dal valore di $a_g$, secondo le tabelle di normativa
per muri di sostegno e per fronti/pendii.

## Coefficiente verticale $k_v$

$$ k_v = \pm 0.5 \, k_h $$

Il coefficiente verticale è assunto pari a metà di quello orizzontale, con
segno da valutare nella combinazione più sfavorevole.

## Uso nelle verifiche

I coefficienti alimentano, ad esempio:

- la spinta sismica dei terreni (metodo di Mononobe-Okabe),
- le verifiche di **stabilità globale** dei pendii in condizioni sismiche,
- le verifiche di **scorrimento** e **capacità portante** delle fondazioni.

!!! note "Coerenza con lo stato limite"
    $k_h$ e $k_v$ vengono calcolati per lo **stato limite** e per lo
    smorzamento/periodo impostati nel calcolo degli spettri. Verifica che lo
    stato limite selezionato sia quello richiesto dalla tua verifica
    (di norma SLV per gli stati limite ultimi geotecnici).

## Da PS Advanced alle altre app NX

I coefficienti calcolati qui sono l'input sismico di molte verifiche
geotecniche della suite. Per il dimensionamento dei muri in gabbioni con
spinta sismica vedi [GDW NX](https://help.nx.geostru.ai/gdw/); per l'analisi
1D della risposta sismica locale (quando la categoria di sottosuolo non basta)
vedi [RSL III](https://help.nx.geostru.ai/rsl/).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20PS%20Advanced%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/seismic/docs/it/coefficienti.md).*
