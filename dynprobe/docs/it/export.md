# Esportazione e report

## Report Word (.docx)

Il report Word è la relazione di calcolo completa, pronta per essere allegata alla documentazione di progetto. Si genera dal menu **Esporta → Report**.

Il documento include:

- Intestazione con dati del sito (nome, committente, coordinate, data)
- Scheda strumento: tipo, parametri tecnici, β utilizzato
- Profilo letture colpi N/profondità (grafico)
- Tabella stratigrafia: strati, profondità, tipo terreno, N_SPT per strato
- Tabella correlazioni geotecniche per ogni strato (autori selezionati)
- Categoria di sottosuolo: V_s,eq, categoria assegnata, tabella strati
- Portanza fondazioni (se calcolata): tabella metodi a confronto
- Valori caratteristici EC7 / NTC §6.2.2 (se calcolati)

## AGS4 (.ags)

Il formato **AGS4** è lo standard aperto per lo scambio di dati geotecnici (AGS Data Format v4.2). Esportalo dal menu **Esporta → AGS4** per condividere i dati di prova con altri software o con il committente.

I gruppi inclusi nell'export AGS4: TRAN, PROJ, LOCA, GEOL, DPRG (parametri prova dinamica), DPRB (letture).

## GeoSection (.geosection)

Esporta le prove con la stratigrafia interpretata verso **GeoSection NX** per costruire la sezione geologica. Dal menu **Esporta → GeoSection**: seleziona le prove da includere (quelle con coordinate), clicca **Esporta**. Il file `.geosection` si apre direttamente nell'app GeoSection.

## Planimetria (immagine PNG)

Se le prove hanno coordinate assegnate, dal menu **Esporta → Planimetria (immagine)** si ottiene un'immagine PNG della planimetria con la posizione delle prove, le quote e le distanze tra prove. Disponibile solo con almeno 2 prove georeferenziate.

## KMZ (Google Earth)

Il menu **Esporta → KMZ** genera un file visualizzabile in Google Earth con la posizione di tutte le prove georeferenziate del progetto.

## File di progetto (.dprobe)

Il file `.dprobe` è il formato nativo di Dynamic Probing NX — un JSON leggibile che contiene tutte le informazioni del progetto (prove, strumenti, stratigrafia, correlazioni, dati del sito). Si salva dal menu **File → Salva** e si riapre dalla Home con **Apri file…**.

!!! tip "Compatibilità desktop"
    Puoi importare un file `.dypx` (formato testo del desktop GeoStru Dynamic Probing) dalla Home di Dynamic Probing NX. Il file `.dprobe` NX non è invece apribile con la versione desktop.
