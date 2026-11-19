# SPW NX

**SPW NX** è l'app GeoStru per il progetto e la verifica delle **paratie**. Gestisce pali in calcestruzzo armato, micropali e diaframmi, con tiranti, puntoni, carichi e falda. La sequenza costruttiva è descritta per fasi.

Il disegno al centro mostra il modello mentre lo componi. I risultati includono diagrammi, inviluppi, condizione governante, verifiche e armature.

[**Apri SPW NX**](https://nx.geostru.ai/spw/){ .md-button .md-button--primary }

## A chi serve

Serve al progettista geotecnico e strutturale che deve studiare uno scavo sostenuto da una paratia. Puoi partire da un progetto nuovo, da un esempio o da un file `.spwx` del programma desktop.

## Cosa fa

- definisce il sito e i parametri sismici secondo le NTC 2018;
- organizza le combinazioni prima delle fasi, con coefficienti normativi ed eccezioni motivate;
- descrive una stratigrafia unica e una sola tipologia di paratia per tutto il progetto;
- segue scavi, rinterri, installazioni, tesature, carichi e cambi di falda come eventi;
- offre il modello all'equilibrio limite (LEM) e il modello a elementi finiti su molle (FEM);
- mostra spostamenti, momento, taglio, sforzo normale, pressioni e reazione del terreno;
- verifica sezioni, tiranti, puntoni e condizioni geotecniche, idrauliche e di esercizio;
- produce la relazione Word e le tavole DXF e passa i dati a Computo NX, PDM NX e CAD Tools;
- riceve la posizione del sito da Atlante NX.

!!! note "Due metodi di calcolo"
    Nel passo **Calcolo** scegli il **FEM** (paratia su molle, con spostamenti e storia delle fasi) o il **LEM** (equilibrio limite, per infissione e sollecitazioni di schemi semplici). Il calcolo a video è gratuito con entrambi i metodi.

## I dieci passi

| Passo | Cosa contiene |
|---|---|
| 1. Progetto | dati dell'opera, studio, sito, normative e sisma |
| 2. Combinazioni | matrice dei coefficienti, ambito delle verifiche ed eccezioni |
| 3. Terreno | piano campagna, stratigrafia, modulo di reazione e falda iniziale |
| 4. Paratia | tipologia, geometria, materiali, armatura e trave di coronamento |
| 5. Elementi | tiranti, puntoni e carichi, ciascuno con il proprio identificativo |
| 6. Fasi | eventi costruttivi in ordine temporale |
| 7. Calcolo | metodo, teorie di spinta, opzioni FEM e avvio |
| 8. Risultati | dettagli, diagrammi, inviluppi e condizioni governanti |
| 9. Verifiche e armature | esiti STR, GEO, HYD, UPL, SLE e armatura esecutiva |
| 10. Relazione ed export | anteprima e relazione Word, tavole DXF, collegamenti con Computo NX, PDM NX e CAD Tools |

## Gratuito e a crediti

Modellazione, **calcolo a video**, disegni, risultati e anteprima della relazione non consumano crediti. La relazione Word, il DXF e l'apertura in CAD Tools consumano **10 crediti**. Ogni messaggio all'assistente ne consuma **3**. Un'operazione fallita non si paga.

Leggi [Crediti](crediti.md) per il dettaglio.

## Sessione e salvataggio

Il progetto resta nella sessione per **30 minuti di inattività**. Salva il lavoro con **File → Salva** o **Salva con nome…** in un file `.spwnx`. Puoi anche usare **GeoDropbox**.

!!! warning "Attenzione"
    «Salvato» nella scheda significa salvato nella sessione. Non significa che il progetto sia già in un file sul tuo computer.

## Mappa del manuale

| Capitolo | Contenuto |
|---|---|
| [Guida rapida](quickstart.md) | un esempio importato, il calcolo e i risultati |
| [Flusso di lavoro](workflow.md) | i dieci passi, uno per uno |
| [Combinazioni](combinazioni.md) | matrice, ambiti, eccezioni e coefficienti da confermare |
| [Fasi](fasi.md) | eventi, persistenza dello stato e miniature |
| [Metodi](metodi.md) | LEM, FEM, spinte, sisma, acqua, supporti e verifiche |
| [Importazione dal desktop](importazione-desktop.md) | file `.spwx`, rapporto e differenze di modello |
| [Formati](formati.md) | `.spwnx`, `.spwx`, Word, DXF e GeoDropbox |
| [Crediti](crediti.md) | azioni gratuite, tariffe e operazioni fallite |
| [Assistente](assistente.md) | lettura del manuale e del progetto, modifiche e limiti |
| [Validazione](validazione.md) | riferimenti, confronti e limiti d'impiego |
| [Glossario](glossario.md) | i termini delle paratie |
| [Domande frequenti](faq.md) | risposte ai dubbi più comuni |

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/spw/docs/it/index.md).*
