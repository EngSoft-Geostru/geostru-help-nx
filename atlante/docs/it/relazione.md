# Testo dell'assistente e Word

## Il testo dell'assistente

**Genera il testo** chiede all'assistente di scrivere la base documentale in forma leggibile:
una **sintesi**, una **sezione per tema** e l'elenco **da verificare**. Il modello riceve
soltanto le evidenze numerate del fascicolo — mai le tavole, mai i campi tecnici — e deve
rispettare regole precise:

- ogni frase che afferma un dato termina con il riferimento **[n]** all'evidenza;
- niente valori, classificazioni, formazioni o conclusioni che non siano nelle evidenze; niente
  categoria di sottosuolo o giudizi di idoneità dedotti;
- un'evidenza «nulla al punto» si scrive con cautela («non risultano … nella cartografia
  consultata [n]»), mai come assenza di pericolo;
- un'evidenza «non disponibile» va dichiarata tale;
- le evidenze «documento fornito» (le tue indagini) si citano dicendo da dove vengono.

Al ritorno il testo viene **validato**: i riferimenti a evidenze inesistenti si tolgono, una
sezione senza alcun [n] si scarta. Il testo resta nel fascicolo con data e modello e si
**rigenera** solo a richiesta — per esempio dopo aver aggiunto le tue indagini.

!!! warning "È una bozza da rivedere"
    Il testo è generato sulle evidenze, non sul sito. Rileggilo come rileggeresti la bozza di
    un collaboratore: il fascicolo lo dice in testa a ogni sezione e nel Word.

### Quota

L'assistente è compreso nell'app gratuita con una **quota mensile per utente**, dimensionata
per un uso professionale normale (un testo o un'analisi PDF costa circa un centesimo). Se la
quota è esaurita, il pulsante lo dice e indica la data in cui si rinnova; il fascicolo, le
tavole e il Word restano disponibili.

## Il Word

**Scarica Word** produce un `.docx` in forma di relazione, pronto da completare:

| Capitolo | Contenuto |
|---|---|
| Indice | campo di Word, aggiornato all'apertura (o con F9) |
| Premessa | cosa contiene il documento, **metodo** (come sono state interrogate le fonti, cosa significano gli esiti, come sono fatte le tavole), avvertenza |
| Oggetto e limiti dell'incarico | titolo, committente, profilo, descrizione dell'intervento (o l'avviso che manca), i limiti della base documentale |
| Sintesi | la sintesi dell'assistente e l'elenco «da verificare», se il testo è stato generato |
| Ubicazione del sito | tabella con Comune, Provincia, Regione, ISTAT, indirizzo, coordinate, raggio, perimetro, particella; tavole di inquadramento e satellite |
| Un capitolo per tema | il testo dell'assistente per il tema, poi ogni evidenza con esito e [n], le **tabelle** dei record per colonne, le tavole |
| Verifiche da completare | «da verificare» dell'assistente, fonti non disponibili, perimetro e indagini mancanti, scala ed edizione delle carte |
| Conclusioni | il capitolo esiste e resta **tuo**: modello del sottosuolo, compatibilità, prescrizioni |
| Prosegui con le app NX | le app pertinenti al profilo con i link al sito |
| Fonti consultate | tabella con numero, fonte, ente e licenza, data e ora (UTC), esito; sotto, i **portali** degli enti con i numeri delle evidenze |

Il file porta nelle proprietà l'autore e un'impronta di provenienza GeoStru. Le tavole sono
incorporate: con sei tavole il file pesa 5–9 MB.

!!! tip "Lingua"
    Il Word segue la lingua dell'interfaccia (IT/EN). Il testo dell'assistente viene generato
    nella lingua attiva al momento della richiesta.
