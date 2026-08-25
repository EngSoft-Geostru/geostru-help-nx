# Domande frequenti

### Quanto sono precise le quote?

Vengono da un modello digitale del terreno a copertura globale, con passo tipico
di circa 30 metri. Servono per la fattibilità e il preliminare; non sostituiscono
un rilievo topografico. Vedi [Quote e modello del terreno](quote.md).

### Un punto mostra quota 0.00: è a livello del mare?

Non necessariamente. Lo zero è anche il valore di un punto **mai quotato** o la
cui quota non è stata recuperata. Rilancia il calcolo delle quote e leggi il
messaggio in barra di stato: dice quanti punti sono stati davvero aggiornati.

### In che sistema di riferimento ottengo i dati?

La mappa lavora in WGS84 geografiche. Le esportazioni NEZ e DXF proiettano in
UTM. Vedi [Esportazione e coordinate](esportazione.md).

### Posso importare un tracciato che ho già?

Sì. Incolla o allega una lista di coordinate, oppure passa all'assistente un
documento che le contiene: le estrae e le disegna. I progetti salvati nel cloud
si riaprono esattamente come li avevi lasciati.

### Che differenza c'è fra i due modi di fare una sezione?

Il profilo dai punti mette in progressiva i vertici che hai cliccato. La sezione
dalla traccia ricampiona la linea a passo regolare, quindi segue il terreno anche
fra i vertici, e porta con sé passo e sorgente delle quote. Vedi
[Sezioni e profili](sezioni.md).

### Quanto fitta conviene fare la griglia della mesh?

Non più fitta del dato che sta sotto. Cambiando righe e colonne, Maps NX mostra
il passo risultante in metri: quando scende ben sotto la risoluzione del modello,
i nodi in più non aggiungono informazione.

### Il DXF si apre nel mio CAD?

Sì: l'esportazione scrive punti e polilinee come entità reali, non come immagine.

### Il disegno non compare sulla mappa

Cambia mappa base o sposta leggermente la vista: il disegno viene ridisegnato non
appena la mappa è pronta. Se il problema persiste, ricarica la pagina — il lavoro
non si perde, perché la sessione viene conservata.

### Come viene fatturato?

Maps NX funziona a **crediti** GeoStru NX: si acquista un pacchetto e ogni azione
a pagamento vi attinge. Se l'azione fallisce non viene addebitato nulla.

### In quali lingue è disponibile?

L'interfaccia è in italiano, inglese, tedesco, francese, spagnolo, rumeno e
danese. Si cambia dal selettore in alto a destra.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Maps%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/maps/docs/it/faq.md).*
