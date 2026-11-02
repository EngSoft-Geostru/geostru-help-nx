# HVSR NX — Rapporto spettrale H/V

**HVSR NX** elabora nel browser le misure di **rumore ambientale a stazione singola**: dalle tracce NS, EO e V alla curva H/V, dalla
frequenza di risonanza f~0~ con le verifiche SESAME al modello a strati, fino a V~s,eq~, categoria di sottosuolo e relazione Word. È
il programma desktop Easy HVSR di GeoStru portato sul web.

[**Apri l'app**](https://nx.geostru.ai/hvsr/){ .md-button .md-button--primary }
[Guida rapida](quickstart.md){ .md-button }

## A chi serve

A geologi, geofisici, ingegneri geotecnici e imprese di indagini che eseguono la misura con un tromografo e devono consegnarne
l'elaborazione: frequenza di risonanza del sito, sua affidabilità, profilo V~s~ stimato e categoria di sottosuolo secondo NTC 2018.

## Come si lavora

Le schede orizzontali seguono l'ordine del lavoro, da sinistra a destra. La descrizione completa è in
[Flusso di lavoro](workflow.md).

1. **Dati generali** — committente, cantiere, operatore, posizione.
2. [**Tracce**](tracce.md) — importi la registrazione a tre componenti.
3. [**Selezione**](selezione.md) — dividi la registrazione in finestre, escludi quelle disturbate.
4. [**Analisi spettrale**](analisi-spettrale.md) — banda, lisciamento, somma delle orizzontali, mappe.
5. [**Spettro H/V**](spettro-hv.md) — f~0~, A~0~ e verifiche SESAME; poi [modello e ricerca](modello.md) e
   [V~s,eq~ e categoria](categoria.md).
6. [**Relazione**](relazione.md) — Word, DXF e CSV.

Il calcolo avviene sul server: nel browser restano il disegno e i gesti sui grafici.

## Da dove cominciare

Con la [Guida rapida](quickstart.md) arrivi alla curva H/V in pochi minuti. Il [Tutorial](tutorial.md) ripete un'analisi completa
sul progetto che apri con **File → Apri l'esempio**, con i numeri che devi ritrovare. Prima di usare i risultati in un progetto leggi [Validazione e limiti](validazione.md): la curva H/V
da sola non determina il profilo V~s~.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20HVSR%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hvsr/docs/it/index.md).*
