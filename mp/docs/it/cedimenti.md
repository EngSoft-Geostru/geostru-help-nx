# Cedimenti

MP NX calcola il cedimento del **palo singolo** con il metodo di **Poulos e Davis** (1980),
per un carico assiale Q:

s = Q/(D·E~t~)·I

con D diametro del palo, E~t~ modulo elastico del terreno e I coefficiente d'influenza. Il
metodo assume un mezzo elastico con coefficiente di Poisson ν = 0,5.

## Dati richiesti

- **E** dello strato che contiene la **punta** del palo, in MPa: è la colonna E della
  [stratigrafia](stratigrafia.md). Senza un valore di E il cedimento non ha senso.
- Il modulo elastico del palo E~p~, preso dalla classe di calcestruzzo
  nell'[archivio dei materiali](materiali.md).
- Diametro e lunghezza del palo.
- Un **carico verticale**.

Il coefficiente I è interpolato da tabella in funzione di **L/D** (otto classi) e della
rigidezza relativa **K = E~p~/E~t~** (interpolazione lineare fra 10, 100, 1 000, 10⁴ e 10⁵).

## Opzioni cedimenti

Nella card **Opzioni cedimenti** della scheda Parametri scegli:

- la **Combinazione** da cui prendere il carico. Di solito è una combinazione di esercizio:
  nel progetto d'apertura è selezionata la prima, «A1+M1+R3», e la «SLE» va scelta a mano;
- il **Carico**, in kN. Con 0 il programma usa la risultante verticale della combinazione
  scelta; con un valore diverso da zero usa quello.

Il cedimento si calcola con **Calcola**, insieme al resto, senza crediti aggiuntivi.

## Leggere la scheda Cedimenti

La scheda mostra la combinazione e il carico usati, poi tre riquadri: il **Cedimento** in
mm, il coefficiente **I** e il carico **Q**.

!!! example "Esempio"
    Q = 1 000 kN, D = 0,8 m, L = 10 m, E~p~ = 31 475 MPa, E~t~ = 30 MPa. L/D = 12,5 e
    K = 1 049 danno I = 0,147. Il cedimento è s = 1 000/(0,8·30 000)·0,147 = 6,1 mm. È il
    caso 6 del [documento di validazione](validazione.md).

![Scheda Cedimenti: combinazione e carico usati, e i riquadri con cedimento in millimetri, coefficiente I e carico Q](img/14-cedimenti.png)

## Perché a volte il cedimento manca

Se la scheda dice **Nessun cedimento calcolato** dopo un calcolo riuscito, la combinazione
scelta **non ha carico verticale**: E~d,v~ = 0 e il metodo richiede un carico assiale. Il
messaggio a video indica la combinazione interessata.

Hai due rimedi:

1. assegna una forza verticale **F~y~** nei carichi di quella combinazione, oppure scegli
   un'altra combinazione nelle **Opzioni cedimenti**;
2. scrivi direttamente il **Carico** Q nelle Opzioni cedimenti.

Succede, per esempio, con l'esempio 16.3 di Bowles, che ha solo il carico limite e nessuna
azione di progetto.

## Limiti

- Il cedimento è quello del palo **singolo**: non c'è l'effetto di gruppo.
- Il metodo usa un solo modulo E~t~, quello dello strato della punta: in terreni molto
  stratificati il risultato è un ordine di grandezza da valutare con giudizio.
- Il cedimento con il metodo iperbolico di Fleming, presente nel programma desktop, non è
  in MP NX.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MP%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mp/docs/it/cedimenti.md).*
