# Formati e scambio dei dati

## Progetto SPW NX: `.spwnx`

Il `.spwnx` è il file nativo del progetto. Contiene gli ingressi: dati generali, sito, terreno, paratia, elementi, combinazioni, fasi, opzioni e rapporto di importazione.

Non conserva i risultati del calcolo. All'apertura devi calcolare di nuovo. Una versione più recente del programma può quindi produrre risultati diversi secondo la validazione documentata.

Usa **File → Salva** per aggiornare il file corrente. Usa **Salva con nome…** per crearne uno nuovo.

## Progetto desktop: `.spwx`

Il `.spwx` si apre in sola lettura con **File → Apri…**. SPW NX crea un progetto nativo e un rapporto delle scelte effettuate.

Per conservare il risultato dell'importazione salva un `.spwnx`. Il file desktop resta invariato. Dettagli in [Importazione dal desktop](importazione-desktop.md).

## Relazione Word

La relazione è un documento `.docx` con dati del progetto, risultati aggiornati, verifiche, armature e blocco «Codice di calcolo». Comprende le eccezioni delle combinazioni e il rapporto di importazione quando presente. Il file porta nelle proprietà del documento l'autore e l'impronta dei dati.

Si genera dal passo **Relazione ed export** solo con un calcolo completo e aggiornato e costa 10 crediti. L'**Anteprima gratuita** mostra a video lo stesso contenuto. La relazione è nella lingua dell'interfaccia.

## Tavola DXF

Il `.dxf` trasferisce il disegno della paratia o dei risultati a un programma CAD. Dal passo **Relazione ed export** scegli la tavola completa (sezione, fasi e inviluppi) o la sola sezione della paratia. Il pulsante **DXF · 10 crediti** del passo Risultati esporta il diagramma a video.

Una vista senza contenuto non produce un file e non consuma crediti. Controlla che il disegno si riferisca alla combinazione e alla fase desiderate.

## CAD Tools

Il pulsante **CAD Tools** del passo Relazione ed export porta le viste della paratia nell'ambiente di editing, in una nuova scheda. L'operazione usa la stessa tariffa del DXF.

## Computo NX e PDM NX

I pulsanti **Computo NX** e **PDM NX** del passo Relazione ed export portano il progetto verso il computo delle quantità e verso il piano di manutenzione. Prima del trasferimento a Computo NX puoi aprire **Parametri e anteprima computo**, controllare le quantità e togliere le voci che non servono. I collegamenti non sostituiscono il controllo dei dati trasferiti.

## Ingresso da Atlante NX

Dal fascicolo di Atlante NX puoi aprire SPW NX con la posizione del sito già scelta. Se il progetto non ha una posizione, la riceve subito con un avviso. Se ne ha già una diversa, il passo Relazione ed export chiede se sostituirla o mantenerla. Dopo la sostituzione richiedi di nuovo i parametri sismici del sito.

## GeoDropbox

Il pulsante **GeoDropbox** permette di aprire e salvare il `.spwnx` in un progetto GeoDropbox. Il salvataggio del progetto è gratuito. Se scegli di allegare una relazione a pagamento, vale la tariffa della relazione.

## Unità e contenuti

Il progetto usa unità SI. Quote e lunghezze sono in metri, forze in kN, pressioni in kPa e pesi dell'unità di volume in kN/m³. Barre e tubolari hanno le dimensioni in millimetri dove indicato.

Le quote sono assolute e positive verso l'alto. Molti risultati sono riferiti a un metro di paratia. Le verifiche delle sezioni riportano invece i valori per elemento.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/spw/docs/it/formati.md).*
