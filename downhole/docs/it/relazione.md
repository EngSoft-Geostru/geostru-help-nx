# Relazione, DXF e crediti

Dalla scheda **Relazione** escono i due elaborati della prova: la **relazione in Word** e le
**tavole DXF** dei grafici. Sono le due azioni dell'app che, insieme ai messaggi
all'assistente, consumano crediti. L'**anteprima** della relazione, a destra, è gratuita.

![Scheda Relazione: a sinistra le cinque sezioni attivabili e il riepilogo di ciò che entrerà nel documento, a destra l'anteprima impaginata che si apre con i dati generali](img/21-relazione.png)

## Prima di generare

Controlla tre cose, tutte gratuite:

1. i campi della scheda **Dati generali** (committente, cantiere, località, data, operatore,
   responsabile, descrizione, note, coordinate WGS84 e altitudine): aprono il documento;
2. i sismostrati e la V~s,eq~ nella scheda [Elaborazione](elaborazione.md);
3. il riquadro **Che cosa entrerà nella relazione**: numero di misure, sismostrati dei due
   metodi, strati descrittivi, figure e V~s,eq~ dei due metodi.

Poi guarda l'**anteprima**: è il documento come uscirà.

Se le misure mancano o contengono errori, **Genera Word** è disattivato e una nota dice che
cosa correggere.

## L'anteprima

La card **Anteprima della relazione** mostra il documento impaginato, pagina per pagina,
con gli stessi testi, tabelle e figure del Word: lo compone il server con lo stesso codice.
Segue gli interruttori delle sezioni appena li cambi, prima ancora di salvarli.

Rispetto al Word mancano solo i **numeri di pagina** e il blocco **Codice di calcolo**, che
esiste solo nel documento emesso (vedi sotto). L'anteprima non consuma crediti.

## Com'è fatta la relazione

Il documento non ha copertina. Nell'ordine:

1. **Dati generali** — la tabella con i campi della scheda Dati generali, comprese
   latitudine e longitudine (WGS84) e altitudine in m s.l.m. I campi vuoti non compaiono; se
   sono tutti vuoti, il documento comincia dal capitolo successivo;
2. le **sezioni** scelte (tabella sotto) e l'**elaborazione delle misure**, la tabella dei
   tempi corretti, che c'è sempre;
3. **Codice di calcolo (NTC 2018 §10.2)** — il blocco che identifica il software e il
   documento;
4. l'**indice**, in fondo.

## Sezioni della relazione

Cinque interruttori scelgono che cosa includere.

| Sezione | Contenuto |
|---|---|
| **Cenni teorici** | La prova, la procedura, i due metodi, i parametri elastici, la V~s,eq~, i limiti e la bibliografia. |
| **Dati di input (geometria, misure, schema della prova)** | Geometria, tabella dei tempi misurati, schema della prova. |
| **Metodo diretto (sismostrati, parametri, dromocrone)** | V~s,eq~, sismostrati, parametri per strato, dromocrone. |
| **Metodo intervallo (valori per ricezione, medie, cinque profili)** | V~s,eq~, parametri per intervallo di misura, sismostrati e valori medi, i cinque profili (velocità, γ, ν, G·E~d~, E·E~v~). |
| **Stratigrafia (falda, strati, colonna)** | Falda, strati e colonna. Entra solo se la scheda Stratigrafia ha almeno uno strato. |

Le opzioni si salvano con il progetto: **Salva le opzioni**, oppure cambia scheda e l'app le
salva da sé.

## Genera Word

**Genera Word** produce un file `.docx` e il browser lo scarica.

- La relazione è scritta **nella lingua dell'interfaccia**: per averla in inglese, cambia
  lingua dal selettore in alto prima di generarla.
- Le figure sono gli stessi disegni che vedi a video.
- All'apertura Word può chiedere di aggiornare i campi: accetta, e l'indice prende i numeri
  di pagina. In alternativa, tasto destro sull'indice → **Aggiorna campo**.
- I valori non calcolabili restano «--», come a video; gli avvisi del calcolo sono riportati
  nel documento.

Il documento è un file Word normale: puoi modificarlo, aggiungere il tuo logo, convertirlo
in PDF dal tuo programma di scrittura.

### Il blocco «Codice di calcolo»

L'ultimo capitolo della relazione, **Codice di calcolo (NTC 2018 §10.2)**, è una tabella
scritta dal software con ciò che il punto 10.2 chiede di dichiarare:

- titolo del software e produttore;
- versione dell'app, versione del **motore di calcolo** e revisione del codice;
- licenza d'uso, intestata a chi ha generato il documento;
- **codice del documento**, nella forma `NX-…-XXXX-XXXX`, e l'indirizzo dove verificarlo;
- il rimando alla [validazione](validazione.md) del motore;
- l'impronta dei dati di ingresso.

Il codice è registrato su geostru.ai quando generi il Word: chiunque riceva la relazione
può verificare, all'indirizzo stampato nel blocco, che il documento è stato emesso da
Downhole NX con quella versione. La verifica dice che il documento è stato **emesso**, non
che i dati di partenza sono corretti: quelli restano responsabilità di chi firma.

Se il registro dei documenti non risponde, la relazione **non esce** e non viene addebitato
nulla: riprova fra qualche minuto.

## Tavola DXF

Nella card **Tavola DXF** scegli il **Disegno da esportare** e premi **Esporta DXF**:

- Schema della prova
- Dromocrone e sismostrati del metodo diretto
- Profilo delle velocità d'intervallo
- Profilo del peso di volume d'intervallo
- Profilo del coefficiente di Poisson d'intervallo
- Profilo dei moduli G ed Ed d'intervallo
- Profilo dei moduli E ed Ev d'intervallo
- Colonna stratigrafica

Ogni esportazione produce **un** disegno, con i layer per ruolo (assi, griglia, punti,
dromocrone, strati, quote, testi), nelle stesse unità e con gli stessi colori che vedi a
video. I testi sono nella lingua dell'interfaccia.

Se il disegno scelto è vuoto (per esempio la colonna stratigrafica senza strati), l'app lo
dice e non esporta nulla.

## Crediti

### Che cosa li consuma

| Azione | Quando viene addebitata |
|---|---|
| **Genera Word** | A documento prodotto. |
| **Esporta DXF** | A file prodotto. |
| **Messaggio all'assistente** | Quando la risposta arriva. |

### Che cosa è gratuito

Caricare le tracce, scegliere i tempi, compilare le misure, elaborare, inserire e spostare i
sismostrati, guardare tutti i grafici e le tabelle a video, compilare la stratigrafia,
guardare l'anteprima della relazione, salvare e aprire il progetto, aprire gli esempi.

### Quanto costano

Questo manuale non riporta i prezzi: cambiano con il listino, pubblicato su
[geostru.ai](https://www.geostru.ai/). Il tuo **saldo** è nel menu utente, in alto a destra.

Se il saldo non basta, l'app non genera nulla e mostra una striscia con i **crediti
necessari**, il **saldo** e il pulsante **Acquista crediti**. Il progetto resta in sessione:
ricarica i crediti e riprova.

### Se qualcosa va storto

**Se un'operazione non va a buon fine, non viene addebitato nulla.** Vale per ogni caso che
l'app può incontrare:

- errore durante la generazione del Word o del DXF;
- misure non valide o disegno vuoto;
- sessione scaduta: l'app lo dice e non scrive né addebita nulla;
- servizio dei crediti o registro dei documenti non raggiungibile: riprova fra qualche
  minuto;
- assistente non disponibile o risposta non arrivata.

Le condizioni complete (validità dei crediti, rimborsi) sono nei
[Termini di servizio](https://geostru.ai/it/terms-of-service/).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Downhole%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/downhole/docs/it/relazione.md).*
