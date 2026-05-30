# Guida rapida — il primo progetto in 5 minuti

Obiettivo: caricare un file di esempio, leggere la stratigrafia e le correlazioni principali, esportare il report.

## 1. Apri l'app e crea un nuovo progetto

Vai su [nx.geostru.ai/dynprobe](https://nx.geostru.ai/dynprobe/). Clicca **Nuovo file** dal menu File.  
Dai un nome al progetto (es. "Sito via Roma") e clicca **Crea**.

In alternativa, usa un **file di esempio** dalla schermata iniziale — scoprirai subito tutte le sezioni già popolate.

## 2. Aggiungi una prova

Nel **Dashboard** clicca **+ Prova continua** (oppure **+ Prova in foro** per le SPT). Inserisci:

- **Sigla**: codice identificativo della prova (es. `DP-1`)
- **Strumento**: seleziona dal catalogo (DPM, DPSH, DPH, DPL…). Lo strumento definisce il peso del maglio, l'altezza di caduta e il passo di avanzamento — tutti i parametri energetici sono già tabulati internamente.
- **Coordinate**: inserisci lat/lon per posizionare la prova sulla mappa (opzionale ma utile per l'export planimetria).

## 3. Inserisci le letture

Vai nel tab **Letture**. Hai tre modalità:

- **Manuale**: digita il numero di colpi riga per riga.
- **Importa CSV**: incolla o carica un file da datalogger — il sistema riconosce automaticamente profondità e colpi.
- **Importa .dypx**: carica direttamente un file esportato dal desktop GeoStru Dynamic Probing.

Il grafico N/profondità si aggiorna in tempo reale.

## 4. Interpreta la stratigrafia

Vai nel tab **Stratigrafia interpretata**. L'app propone un primo strato sull'intera profondità.

- Clicca **+ Aggiungi strato** per suddividere il profilo.
- Per ogni strato imposta la profondità inferiore, il **tipo di terreno** (coesivo / incoerente / misto) e il **peso di volume** γ.
- Il metodo di aggregazione N_SPT per strato si sceglie nell'header della colonna (default: media). Vedi [Stratigrafia →](stratigrafia.md) per i 7 metodi disponibili.

!!! tip "Colori e badge"
    Il badge **Σ strati / prova** in basso mostra se la somma delle profondità degli strati coincide con la profondità della prova (spunta verde = coerente, triangolo giallo = scarto da controllare).

## 5. Leggi le correlazioni

Tab **Correlazioni geotecniche**: per ogni strato compare una tabella con i parametri stimati (Cu, φ, Mo, Ey, Vs, γ, Dr …) calcolati dalle formule di riferimento della letteratura geotecnica. Vedi [Correlazioni →](correlazioni.md).

!!! note
    Le correlazioni sono stime empiriche. Usale come punto di partenza — integrale sempre con dati di laboratorio quando disponibili.

## 6. Controlla la categoria di sottosuolo

Tab **Cat. suolo**: l'app calcola la velocità equivalente V_s,30 e assegna automaticamente la categoria NTC 2018. Vedi [Categoria →](categoria.md).

## 7. Esporta il report

Menu **File → Salva** per scaricare il file `.dprobe`. Menu **Esporta → Report Word** per la relazione completa.

In 5 minuti hai:

- ✅ una prova con letture
- ✅ una stratigrafia interpretata
- ✅ i parametri geotecnici per ogni strato
- ✅ la categoria di sottosuolo
- ✅ il file di progetto scaricato
