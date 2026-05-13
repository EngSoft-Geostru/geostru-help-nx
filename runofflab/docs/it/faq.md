# FAQ — domande frequenti

## Generali

### Cosa serve per cominciare?

Almeno una serie di **massimi annui** per una durata (idealmente 5 durate
e ≥ 15 anni di dati). Se non hai dati, carica uno degli esempi della
Calabria dal modale Info → Risorse.

### Posso usare Runoff Lab senza connessione a Internet?

Per l'**uso operativo** sì: l'app gira nel browser e salva su localStorage.
Solo l'**AI Import** richiede connessione (chiama un modello sul backend).

### I miei dati restano privati?

Sì. Lo studio è salvato nel tuo browser (localStorage) e nel file `.hgstudy`
locale. Niente viene trasmesso al server **eccetto**:
- l'AI Import che invia il file al backend (non lo conserva);
- l'export PDF se contiene immagini generate server-side.

## Salvataggio e crash recovery

### Ho chiuso il tab senza salvare. Posso recuperare?

Sì. Riapri l'app: l'autosave del browser ripristina la sessione automaticamente.
Per essere sicuro, salva un `.hgstudy` con `Ctrl+Shift+S`: è un JSON portabile.

### Il badge "modifiche non salvate" sta sempre acceso

Significa che l'autosave del browser è aggiornato ma non hai ancora scaricato
il `.hgstudy` definitivo dell'ultima modifica. Premi `Ctrl+S` (autosave) o
`Ctrl+Shift+S` (download file) per archiviare.

## Serie e durate

### Quanti anni servono?

- **Sotto 10 anni**: stime molto incerte; usa solo per esercitazioni.
- **10-20 anni**: usabile con cautela, preferisci Gumbel-momenti o
  metodi L-moments.
- **>20 anni**: tutte le famiglie probabilistiche sono confrontabili.
- **>50 anni**: anche TCEV livello 0 (puntuale) diventa attendibile.

### Posso usare durate diverse dalle standard?

Sì. Nello studio puoi aggiungere durate custom (es. 30′, 45′, 90′). Tutte le
elaborazioni le useranno se hanno ≥ 2 valori.

### La durata 60' ha 5 anni e quella 24h ne ha 30. Cosa succede?

Le elaborazioni usano ciascuna durata separatamente. La 60' uscirà con
incertezza alta, la 24h sarà robusta. Le curve di pioggia avranno un
buon fit nelle code lunghe e meno nelle brevi: occhio al \(R^2\).

## Elaborazioni

### Quale famiglia scegliere?

Inizia con **Gumbel-momenti**: semplice, accettata da quasi tutti gli enti.
Aggiungi una seconda famiglia per **confronto** (GEV-Lmoments o TCEV-1)
e nella relazione finale documenta entrambe.

### Posso confrontare più elaborazioni?

Sì. Aggiungi tutte quelle che vuoi nello stesso studio: la pagina mostra una
tabella affiancata con i valori \(h(T)\) di ciascuna.

### TCEV non compare nel menu

La sezione TCEV è visibile solo con interfaccia in **italiano**: il dataset
VA.PI. è specifico per regioni italiane. Cambia lingua → IT dal menu lingua.

## Curve di pioggia

### \(R^2\) della mia curva è 0.85 — che faccio?

La legge \(h = a \cdot t^n\) non si adatta bene. Possibili cause:

- **Serie con pochi anni** su alcune durate → elaborazione poco stabile.
- **Discontinuità climatiche** o spostamento del pluviometro.
- **Bacino di montagna** dove valori brevi e lunghi seguono regimi diversi.

Prova: TCEV livello 3 (più parametri); oppure costruisci curve separate per
gruppi di durate (brevi vs lunghe).

### Quale tempo di ritorno per il dimensionamento?

Standard tipici per l'Italia:

- **Fognature urbane**: T = 5–10 anni.
- **Tombini e attraversamenti minori**: T = 25–50 anni.
- **Opere di mitigazione idraulica, vasche di laminazione**: T = 100–200 anni.
- **Difesa abitato (PAI)**: T = 200 anni e talora T = 500.

## SCS-CN

### Che valore di CN per un'area mista?

Usa il **wizard CN** nel pannello idrogrammi: dividi il bacino in subaree,
assegna a ciascuna suolo (A/B/C/D) e copertura, il CN pesato sull'area
viene calcolato automaticamente.

### Come stimo il Tlag?

Wizard Tlag: inserisci A (km²), L (km, asta principale), pendenza media i (%).
Ottieni \(T_c\) con 4 formule classiche (Kirpich, Giandotti, Pasini, Pezzoli)
e il \(T_{\text{lag}}\) suggerito come \(0.6 \cdot T_c\).

### Il bacino è di 500 km², va ancora bene SCS-CN?

Marginalmente. SCS-CN funziona meglio sotto 250 km² e con tempi di
concentrazione < 24 h. Per bacini più grandi conviene un modello distribuito
(non implementato in Runoff Lab — usa software dedicati come HEC-HMS).

## AI Import

### L'AI ha sbagliato un valore

Apri l'anteprima → modifica direttamente la cella → conferma. Le correzioni
manuali sopravvivono.

### Il PDF è scannerizzato male — funziona lo stesso?

In generale sì, ma controlla l'anteprima con attenzione. Se la qualità
dell'OCR è bassa, conviene aprire il PDF, copiare il testo a mano dalla
tabella, e incollare nella casella "testo libero" del modale.

### Quanti crediti consuma un import?

10 crediti (\(\text{rainfall.import.ai}\)). Visibile nel chip del wallet
prima della conferma; rifiutato se il saldo non è sufficiente.

## Export

### Posso esportare solo una sezione?

Per ora la relazione è unica e contiene tutto lo studio. Se vuoi solo le
curve, eliminale dalle altre sezioni prima dell'export — o ritaglia il
PDF a posteriori.

### Le formule nel PDF si vedono male

Tutte le formule sono renderizzate via MathJax in HTML e convertite in
SVG nel PDF. Se vedi codice grezzo (`\frac{...}` letterale), c'è un bug:
[segnalacelo](mailto:info@geostru.ai?subject=Bug%20Runoff%20Lab%20NX%20-%20formule).

## Errori comuni

### "Nessun elemento valido per il calcolo"

L'elaborazione richiede ≥ 2 valori per ciascuna durata. Verifica nella
sezione Stazione che ci siano almeno due righe non vuote per ciascuna
durata che vuoi usare.

### "Curve non disponibili"

Per creare una curva serve almeno **una elaborazione completata**. Vai
prima nel pannello Elaborazioni e aggiungine almeno una.

### "Idrogramma non disponibile"

L'idrogramma SCS-CN richiede un **pluviogramma sintetico** già costruito
(o una curva diretta + durata). Crea prima un pluviogramma nel suo
pannello dedicato.
