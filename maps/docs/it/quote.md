# Quote e modello del terreno

Un numero sullo schermo ha lo stesso aspetto che valga un centimetro o dieci
metri. Conta sapere quale dei due hai in mano.

## Da dove vengono

Le quote sono lette da un **modello digitale del terreno** a copertura globale,
con passo tipico di circa **30 metri** (classe SRTM / Copernicus). Sono quote del
**terreno**, non della superficie: edifici e chiome degli alberi non ci sono.

## A che cosa servono

- studi di fattibilità e progettazione preliminare;
- profili longitudinali di un tracciato;
- una superficie di partenza per una stima di volumi;
- l'input altimetrico di un modello geotecnico, quando il rilievo non è ancora
  stato commissionato.

## Che cosa non sostituiscono

!!! danger "Non sono un rilievo topografico"
    Fra due punti distanti pochi metri il modello non ha nulla di nuovo da dire.
    Una griglia più fitta della risoluzione del modello aggiunge nodi, non
    informazione. Per il progetto esecutivo serve un rilievo.

## Come ottenerle

**A richiesta** — il pulsante **Quote** in alto quota tutti i punti presenti
sulla mappa.

**Automatica** — la casella **Quota automatica sui nuovi punti**, in barra
laterale, fa arrivare ogni nuovo punto già quotato.

## Quando qualcosa non arriva

Il servizio quote può non rispondere. In quel caso:

- **compare un avviso**, che dice quanti punti su quanti non hanno ricevuto la
  quota;
- i punti coinvolti **restano com'erano** — non vengono scritti a zero;
- la barra di stato riporta *"Quote aggiornate: N di M punti"*.

Se invece è andato tutto bene, non compare alcun popup: il risultato è già nella
colonna *Quota* e nell'escursione altimetrica in barra laterale.

!!! warning "Lo zero è ambiguo"
    Un punto mai quotato mostra `0.00`, esattamente come un punto realmente al
    livello del mare. Se hai un dubbio, ricalcola le quote e leggi il messaggio
    in barra di stato: dice quanti punti sono stati effettivamente aggiornati.

## Riconoscere un valore che non torna

- **Un picco isolato** di decine di metri fra due vertici vicini su un tracciato
  breve è quasi sempre un artefatto del modello o un vertice cliccato male, non
  terreno.
- **Una quota molto diversa dall'attesa** su un punto in area urbana può
  dipendere dal fatto che il modello descrive il terreno, non gli edifici.
- **Tutte le quote a zero** significa che il calcolo non è mai stato eseguito, o
  che è fallito.

L'assistente AI, se glielo chiedi, controlla proprio queste cose.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Maps%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/maps/docs/it/quote.md).*
