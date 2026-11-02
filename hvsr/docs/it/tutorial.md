# Tutorial: analisi completa

Il tutorial ripete un'analisi dall'inizio alla fine, con i numeri che devi ritrovare a ogni passo. Usa la registrazione del progetto d'esempio, 1200 s a
128 Hz, che apri dall'app senza alcun file.

!!! note "Con il tuo file"
    La sequenza è la stessa. Importa il file nella scheda **Tracce**, vedi [Tracce](tracce.md), e riparti dal passo 2: un progetto nuovo ha già durata 20 s,
    periodo breve 1 s, banda 0,5–15 Hz e passo 0,15, quindi quelle caselle non vanno cambiate. I numeri saranno i tuoi.

## 1. Apri l'esempio

Scegli **File → Apri l'esempio**, oppure il pulsante **Apri l'esempio** nella scheda **Tracce** vuota. Se il progetto aperto ha modifiche non salvate, una
striscia ti chiede **Salva prima**, **Continua senza salvare** o **Annulla**.

Nella scheda **Tracce** trovi F~s~ = 128 Hz, 153.600 campioni, 1200 s. Il progetto ha già finestre, parametri e un modello, ottenuti con scelte
diverse da queste: nei passi seguenti li sostituisci.

## 2. Crea le finestre

Nella scheda **Selezione** scrivi **Durata della finestra** = 20 e lascia **Sovrapposizione** = 0, **Tempo iniziale** = 0 e **Tempo finale** vuoto. Premi
**Seleziona**: ottieni **59 finestre**.

Nella scheda **Analisi spettrale** scrivi **f min** = 0,5 e **Passo** = 0,15, poi premi **Aggiorna**. Il resto va già bene: f max 15, lisciamento
**Triangolare a banda proporzionale**, **Ampiezza** 10 %, **Media aritmetica**.

Con queste finestre la curva dà **f~0~ = 5,75 Hz** e **A~0~ = 3,498**. Nella scheda **Spettro H/V**, con **Come il desktop**, la curva è affidabile (3 su 3) e il
picco non è chiaro (4 su 6).

## 3. Applica il filtro

Torna alla scheda **Selezione**. Nel **Filtro STA/LTA** scrivi **Periodo breve (STA)** = 1, lascia **Limite superiore** = 3, **Limite inferiore** = 0,1 e
**Considera le finestre residuali** attiva, poi premi **Filtra**. Il messaggio dice «Tolte 29 finestre, ne restano 30»: restano **30 finestre**.

Molte finestre cadono. Guarda dove sono i vuoti sui sismogrammi e sulla mappa di stazionarietà, e decidi se vuoi recuperare un tratto con **Aggiungi**.

## 4. Leggi lo spettro

Nella scheda **Analisi spettrale** i parametri restano quelli del passo 2. Nella scheda **Spettro H/V** ora trovi:

| Grandezza | Valore |
|---|---|
| f~0~ | 5,75 Hz |
| A~0~ | 4,140 |
| Curva, **Come il desktop** | 3 su 3 |
| Picco, **Come il desktop** | 6 su 6 |
| Picco, **Testo SESAME 2004** | 4 su 6, su curva geometrica con A~0~ = 3,633 |

Premi **Testo SESAME 2004** e guarda quali criteri cadono: il filtro ha reso il picco chiaro per il desktop, non per il testo. In relazione dovrai dire quali hai
usato. Per proseguire torna a **Come il desktop**.

## 5. Scrivi il modello

Il primo strato si suppone noto da un sondaggio. Nel **Modello stratigrafico** premi **Ricerca automatica**, così compaiono limiti e blocchi, e controlla la
tabella. L'esempio ha già limiti e blocchi di questa tabella: devi riscrivere soltanto H e V~s~ di partenza.

| Strato | H | V~s~ | Limiti |
|---|---|---|---|
| 1 | 2 m, bloccato | 120 m/s, bloccata | – |
| 2 | 5 m | 200 m/s | H fino a 20 m, V~s~ fino a 500 m/s |
| 3, semispazio | – | 500 m/s | V~s~ da 400 a 900 m/s |

Attiva **Normalizza l'ellitticità** sopra la curva, così le due curve si confrontano sulla stessa scala. Premi **Sintetizza**: il misfit iniziale è **0,4180**.

## 6. Lancia la Ricerca

Lascia **Iterazioni** = 1000 e **Seme fisso** attivo, poi premi **Ricerca**. Il risultato:

| Grandezza | Valore |
|---|---|
| Strato 2 | 11,51 m a 274,4 m/s |
| Semispazio | 721,2 m/s |
| Misfit | 0,1954 |
| Massimo ellitticità | 6,05 Hz |

Il massimo dista il 5 % da f~0~, sotto la soglia del 15 % oltre la quale l'app lo segnala. Fra i **Suggerimenti** resta quello sulla lunghezza del modello, che
arriva a 13,5 m.

## 7. Leggi la categoria

Nel riquadro **Risultati**: **V~s,eq~ = 368,23 m/s**, H = 30 m, **categoria B**.

Fermati qui prima di scriverlo. V~s,eq~ sta a poco più del 2 % dal confine con la categoria C e dipende dalla V~s~ del semispazio, prolungato da 13,5 a
30 m senza che la misura la vincoli. Premi **Memorizza**, cambia i limiti del semispazio, ripeti la Ricerca e confronta: se i modelli spiegano ugualmente la
curva e cambiano categoria, serve un dato indipendente.

## 8. Genera la relazione

Nella scheda **Relazione** controlla l'**Anteprima** e premi **Genera Word**. Con **Esporta DXF** ottieni la tavola con colonna, profilo e curva.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20HVSR%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hvsr/docs/it/tutorial.md).*
