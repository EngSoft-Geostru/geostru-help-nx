# Importazione dal desktop

SPW NX apre i progetti `.spwx` del programma desktop e li converte nel modello nativo. Il progetto originale non viene modificato.

## Come importare

1. Salva il lavoro corrente se vuoi conservarlo.
2. Scegli **File → Apri…** e seleziona il `.spwx`.
3. Attendi la conversione.
4. Leggi il **Rapporto di importazione** nel passo **Progetto**.
5. Controlla i dieci passi e calcola di nuovo.

Puoi aprire un esempio dal menu **File**: passa dallo stesso percorso di importazione e riceve lo stesso rapporto.

## Il rapporto di importazione

Il rapporto conserva nome del file, data, riepilogo e singole note. Resta associato al progetto anche quando lo salvi come `.spwnx`.

| Gruppo | Significato |
|---|---|
| Non importato | dati che non entrano nel modello nativo |
| Assunto | scelta fatta per rappresentare un dato del desktop |
| Nota | informazione sulla conversione, senza una perdita diretta |

Il riepilogo conta fasi, eventi, combinazioni riunite o separate e tronconi letti. Apri ogni gruppo e controlla le voci che riguardano il tuo progetto.

## Cosa cambia nel modello

### Una sola paratia

Il desktop può descrivere tronconi di sezione diversa. SPW NX usa una sola tipologia per tutta l'altezza. In importazione viene scelta una sezione di riferimento e il rapporto elenca i tronconi non mantenuti.

Il peso dei tronconi superiori può diventare un carico in testa. Gli elementi fuori dalla sezione scelta possono non essere importati. Controlla il disegno e la paratia prima del calcolo.

### Una sola stratigrafia

Il modello nativo usa la stratigrafia del progetto per tutte le fasi. Se il desktop contiene varianti per fase, il rapporto segnala le differenze e indica quale stratigrafia è stata mantenuta.

Lo stesso principio vale per inclinazioni di calcolo e moduli di reazione assegnati che cambiano fra le fasi.

### Combinazioni del progetto

Nel desktop i coefficienti possono cambiare da una fase all'altra. In SPW NX le combinazioni appartengono al progetto.

L'importazione riunisce le configurazioni equivalenti. Separa quelle incompatibili e ne limita l'ambito alle fasi pertinenti. Un coefficiente non rappresentabile viene segnalato e non va ricostruito a mano senza averlo verificato.

### Fasi come eventi

Le fasi diventano eventi ordinati. Lo stato di un supporto o di un carico segue installazione, applicazione e rimozione. Non dipende più da un coefficiente usato per accenderlo in una singola combinazione.

La storia è incrementale: un supporto installato entra nella paratia nella condizione raggiunta dalle fasi precedenti.

### Sisma e acqua

I coefficienti sismici sono ricondotti al sito e allo stato limite. Una combinazione statica che contiene dati sismici viene segnalata. Controlla tipo e ambito dopo l'importazione.

Il reticolo di flusso del desktop non viene trasferito come disegno. Il regime e i dati idraulici disponibili sono riportati nel modello nativo.

## Cosa si perde o si ricalcola

- I **risultati salvati** non si importano: il progetto va ricalcolato.
- Le **armature esecutive** del desktop non si importano: si ricavano dalla nuova analisi.
- Viste, zoom, colori e personalizzazioni grafiche non fanno parte del progetto importato.
- Le varianti della stratigrafia per fase non entrano nel modello a stratigrafia unica.
- I tronconi non restano come tronconi: valgono le scelte e gli avvisi del rapporto.
- Tipi di sezione o carichi non rappresentabili possono essere convertiti con un'approssimazione oppure esclusi con una nota.

!!! warning "Attenzione"
    Un'importazione completata non dimostra che il modello sia equivalente al desktop. Il rapporto e un nuovo calcolo fanno parte del controllo.

## Differenze nei risultati

Anche con gli stessi dati principali, i risultati possono cambiare per la storia delle fasi, il modo di applicare i coefficienti, il sisma e le verifiche idrauliche. Le differenze non vanno nascoste né corrette cercando una coincidenza numerica forzata.

Leggi [Validazione](validazione.md) per il significato dei livelli di confronto e [Metodi](metodi.md) per ipotesi e limiti.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/spw/docs/it/importazione-desktop.md).*
