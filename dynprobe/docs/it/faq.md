# Domande frequenti

## Generale

??? question "Che differenza c'è tra Dynamic Probing NX e il Dynamic Probing desktop?"
    Il desktop GeoStru Dynamic Probing è la versione storica Windows. Dynamic Probing NX è la versione web, accessibile da qualsiasi browser senza installazione. Le funzionalità principali sono equivalenti; NX aggiunge il supporto multi-prova (gestione di un intero sito con N prove), la mappa interattiva, l'export AGS4 e l'integrazione con GeoSection NX. I dati del desktop si importano in NX tramite il formato `.dypx`.

??? question "I dati vengono salvati sul server?"
    No — Dynamic Probing NX è **local-first**: i dati del progetto risiedono nel tuo browser (localStorage) e vengono salvati sul tuo PC solo quando esporti il file `.dprobe`. Nessun dato di progetto viene inviato ai server GeoStru.

??? question "Posso usarlo offline?"
    Per il caricamento iniziale dell'app è necessaria una connessione. Una volta caricata, l'app funziona anche offline per l'inserimento dati e i calcoli (tranne il calcolo del report Word, che richiede la connessione).

??? question "C'è una versione mobile?"
    L'app è progettata per desktop/tablet. Su smartphone la navigazione funziona ma l'inserimento delle letture su schermi molto piccoli è scomodo.

## Strumenti e letture

??? question "Come aggiungo uno strumento che non è in catalogo?"
    Vai in **Strumenti** dalla barra di navigazione → **+ Aggiungi strumento**. Inserisci: nome, tipo (DPL/DPM/DPH/DPSH), massa del maglio (kg), altezza di caduta (m), diametro punta (mm), angolo punta (°), passo avanzamento (m), e il coefficiente β. Lo strumento viene salvato nel file di progetto.

??? question "Il mio CSV non viene riconosciuto correttamente. Come lo formato?"
    Assicurati che le prime due colonne siano profondità (m) e colpi (intero), separate da virgola, punto e virgola o tab. Rimuovi le righe di intestazione che non seguono questo formato, oppure inseriscile come commenti con `#` a inizio riga. Se le coordinate sono nell'intestazione, usa il formato: `# lat=41.9028 lon=12.4964 quota=120`.

??? question "Posso escludere delle letture dal calcolo?"
    Sì — nel tab Letture, ogni riga ha un checkbox per escluderla. Le letture escluse non entrano nell'aggregazione N_SPT per strato né nelle correlazioni. Utile per scartare valori anomali (rifiuto anticipato, perdita di fango).

## Stratigrafia

??? question "Come scelgo il metodo di aggregazione N_SPT?"
    Dipende dall'obiettivo. Per una stima media conservativa usa **Media − 1σ**. Per il valore caratteristico EC7 usa **RNC** (distribuzione normale) o **RC** (log-normale). Se hai poche letture per strato (< 4), preferisci la Media semplice o il Minimo. Vedi [Stratigrafia →](stratigrafia.md) per la descrizione completa dei 7 metodi.

??? question "Il badge Σ strati è giallo — cosa significa?"
    La somma delle profondità inferiori degli strati non coincide con la profondità della prova. Controlla che l'ultimo strato arrivi esattamente alla profondità di fine prova (es. se la prova è 12,00 m, il limite inferiore dell'ultimo strato deve essere 12,00 m).

## Correlazioni

??? question "Perché alcuni valori di correlazione sono —?"
    Per alcune combinazioni tipo-terreno / autore il parametro non è definito. Ad esempio, Dr (densità relativa) è definita solo per incoerenti: negli strati coesivi la cella mostra —. Analogamente, Cu (coesione non drenata) è definita solo per coesivi.

??? question "Posso inserire i valori di laboratorio invece delle correlazioni?"
    Attualmente l'app usa le correlazioni da N_SPT come fonte primaria. Per il calcolo della portanza puoi inserire direttamente Cu o φ nelle caselle dello strato nella stratigrafia — quei valori sostituiscono quelli correlati.

## Export e report

??? question "Il report Word è modificabile?"
    Sì — è un file `.docx` standard aperto in Word, LibreOffice o Google Docs. Puoi personalizzare l'intestazione, aggiungere il logo del tuo studio e modificare il testo descrittivo. Le tabelle numeriche sono dati statici (non formule Excel).

??? question "Posso esportare in PDF?"
    Non direttamente dall'app. Apri il `.docx` generato in Word e usa **File → Stampa → Salva come PDF**.

??? question "AGS4: quali gruppi vengono esportati?"
    Vengono inclusi i gruppi: TRAN (dati di trasmissione), PROJ (progetto), LOCA (posizione prove), GEOL (stratigrafia), DPRG (parametri della prova dinamica), DPRB (letture colpi). Non vengono esportati correlazioni o portanze — questi risultati elaborati non rientrano nello standard AGS4 per prove dinamiche.
