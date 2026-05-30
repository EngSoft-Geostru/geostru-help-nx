# Formato file

## .dprobe — formato nativo NX

Il file `.dprobe` è il formato di progetto di Dynamic Probing NX. È un file **JSON** in chiaro, leggibile con qualsiasi editor di testo. Contiene:

- Metadati del progetto (nome, sito, committente, coordinate)
- Elenco delle prove con tutte le letture
- Libreria strumenti embeddati nel file
- Stratigrafia interpretata (strati, profondità, tipo, γ)
- Impostazioni correlazioni (autori preferiti)
- Risultati calcolati (correlazioni, categoria suolo, portanze, stima parametri)

Il file è **autonomo e portabile**: copialo su un altro PC, aprilo su Dynamic Probing NX — tutto funziona senza configurazione aggiuntiva.

## .dypx — formato desktop GeoStru (importazione)

Il file `.dypx` è il formato di esportazione testuale del desktop GeoStru Dynamic Probing. Dynamic Probing NX può importarlo dalla schermata iniziale con **Importa .dypx…**. Durante l'import vengono letti:

- Tutte le prove con le letture colpi
- I dati dello strumento (tipo, β se presente)
- Le coordinate delle prove (se salvate nel file desktop)

La stratigrafia e le correlazioni non vengono importate dal desktop — vanno reinserite in NX.

## CSV datalogger

Molti datalogger per prove dinamiche esportano i dati in formato CSV o TXT. Dynamic Probing NX riconosce automaticamente il formato se le colonne sono strutturate come:

```
profondità, colpi
0.10, 8
0.20, 9
0.30, 11
...
```

Le colonne possono essere separate da virgola, punto e virgola o tab. Se il file ha un'intestazione con le coordinate del sito (lat, lon, quota), vengono lette automaticamente.

Per importare: nel tab **Letture** dell'editor, clicca **Importa letture da file…** e seleziona il CSV. In alternativa, incolla il contenuto direttamente nel campo testo del modale.

## AGS4 (.ags)

Dynamic Probing NX esporta in formato AGS4 (v4.2) ma non importa da AGS4. Vedi [Esportazione →](export.md).
