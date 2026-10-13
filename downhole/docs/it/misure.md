# Misure e geometria della prova

La scheda **Misure** contiene tutto ciò che il calcolo legge: la **geometria della prova** e
la tabella **profondità / T~p~ / T~s~**. I tempi arrivano dalla scheda [Tracce](tracce.md),
oppure li digiti o li incolli qui.

![Scheda Misure: la card Geometria della prova, la tabella Tempi di tragitto e lo Schema della prova](img/10-misure.png)

## Geometria della prova

| Campo | Significato |
|---|---|
| **Offset della sorgente** [m] | Distanza orizzontale d fra la sorgente e l'asse del foro. Entra nella correzione dei tempi. |
| **Numero di ricezioni** | Quante righe deve avere la tabella. |
| **Posizione della prima misura** [m] | Profondità della prima ricezione. |
| **Interdistanza (opzionale)** [m] | Passo fra una ricezione e la successiva. |

Gli ultimi tre campi servono a **generare la colonna delle profondità**; il calcolo legge
le profondità scritte in tabella, non questi campi. L'**offset della sorgente** invece entra
direttamente nel calcolo: controllalo sempre.

**Genera profondità** porta la tabella al numero di ricezioni indicato. La prima riga prende
la posizione della prima misura, le altre la precedente più l'interdistanza. Con
interdistanza zero restano le profondità già scritte. I tempi già presenti non vengono
toccati.

Se il numero di ricezioni è minore delle righe presenti, l'app chiede conferma prima di
eliminare le righe in fondo.

## La tabella dei tempi di tragitto

Una riga per ricezione:

- **Z** [m] — profondità della ricezione dal piano campagna;
- **Tp** [ms] e **Ts** [ms] — tempi di tragitto dalla sorgente al ricevitore, come letti
  sulle tracce (non corretti);
- **γ** [kN/m³] — solo con il peso di volume assegnato (vedi sotto).

Le profondità devono essere **positive e strettamente crescenti**.

**Un tempo pari a zero vale «non misurato»**. La colonna corrispondente esce «--» nei
risultati e il resto si calcola lo stesso: una prova di sole onde S si elabora lasciando a
zero tutti i T~p~.

**Aggiungi riga** aggiunge una riga in fondo, la **×** toglie la riga.

### Incollare da un foglio di calcolo

**Incolla da foglio di calcolo** apre un riquadro di testo. Copia le celle dal foglio e
incollale lì:

- una riga per misura: Z, T~p~, T~s~ e, se vuoi, γ;
- colonne separate da tabulazione o punto e virgola;
- decimali con virgola o con punto.

**Importa** sostituisce la tabella con le righe incollate. Poi premi **Salva**.

![Riquadro Incolla da foglio di calcolo con tre righe di profondità e tempi separati da tabulazione](img/12-misure-incolla.png)

Puoi anche incollare un blocco di celle direttamente in una cella della tabella: le righe
si riempiono a partire da quella.

### Salvare

**Salva**, in alto a destra, registra geometria e tabella. Finché non salvi, accanto al
pulsante compare **Modifiche non salvate**. Se cambi scheda con modifiche in sospeso, l'app
le salva prima di cambiare.

Se una riga ha un errore (una profondità fuori ordine, un tempo negativo), dopo il
salvataggio una striscia rossa sopra la tabella indica la riga da correggere.

## Peso di volume: automatico o assegnato

L'interruttore **Peso di volume dalla correlazione con Vs e profondità** decide da dove
viene γ, che serve per i moduli G, E~d~, E, E~v~.

**Acceso (predefinito).** γ è stimato per ogni strato e intervallo da una correlazione
empirica con V~s~ e profondità. È una stima: la formula è in
[Cenni teorici](teoria.md#peso-di-volume-dalla-correlazione).

**Spento.** Nella tabella compare la colonna **γ** e scrivi tu il peso di volume a ogni
ricezione, per esempio da prove di laboratorio.

- Nel metodo intervallo ogni intervallo usa il γ della sua ricezione.
- Nel metodo diretto ogni sismostrato usa la **media** dei γ delle ricezioni che contiene.
- Dove γ manca, γ e i moduli escono «--». Velocità e coefficiente di Poisson non dipendono
  da γ e si calcolano comunque.

## Schema della prova

A destra, lo **Schema della prova** disegna il foro, la sorgente con il suo offset e le
ricezioni alle profondità della tabella. Si aggiorna quando salvi. Serve a controllare a
colpo d'occhio che geometria e profondità siano quelle volute; lo stesso disegno entra nella
relazione e si esporta in DXF.

![Schema della prova dell'esempio: sorgente a 2,60 m dall'asse del foro e trenta ricezioni da 1 a 30 m](img/11-misure-schema.png)

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Downhole%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/downhole/docs/it/misure.md).*
