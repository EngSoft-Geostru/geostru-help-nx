# Guida rapida (5 minuti)

Alla prima apertura MP NX mostra un progetto già pronto da calcolare: un **palo trivellato
Ø 0,80 m, L = 15 m**, con plinto, una verticale d'indagine di due strati (sabbia limosa e
argilla sabbiosa) e due combinazioni di carico. Lo usi per fare il giro completo, poi lo
sostituisci con i tuoi dati.

## 1. Apri l'app

Vai su [nx.geostru.ai/mp](https://nx.geostru.ai/mp/) con il tuo account GeoStru. La
finestra ha tre parti: a sinistra l'albero del progetto, al centro le schede (**Parametri**,
**Sezione 2D**, **Vista 3D**, **Carico limite**, **Analisi FEM**, **Sezioni e armature**,
**Cedimenti**, **Relazione**), in alto la barra con i menu **File**, **Dati**, **Relazione**,
**Esporta** e il pulsante **Calcola**.

Nella scheda **Parametri** ogni voce dell'albero porta alla sua card. L'anteprima a destra
ridisegna palo, strati, falda e carichi a ogni modifica; le due tendine sopra il disegno
scelgono la verticale e la combinazione mostrate.

![Scheda Parametri con il progetto d'apertura: palo trivellato Ø 0,80 m e anteprima della sezione](img/01-parametri.png)

## 2. Controlla i dati

Scorri le card senza cambiare nulla: **Dati generali** (tipologia, normativa, vincolo in
testa), **Fondazione di collegamento**, **Palo**, **Materiali e armatura**, **Stratigrafie e
verticali d'indagine**, **Falda**, **Carichi e combinazioni**. La combinazione «A1+M1+R3»
porta in testa F~y~ = 900 kN, F~x~ = 60 kN e M = 40 kNm; la «SLE» 600 kN verticali.

!!! note "Quanto costa il primo calcolo"
    Nel progetto d'apertura l'analisi FEM è **attiva**: **Calcola** addebita 8 + 5 crediti.
    Per il solo carico limite (8 crediti) togli la spunta a **Esegui l'analisi FEM e il
    progetto della sezione con Calcola**, nella card **Armatura e analisi FEM**.

## 3. Calcola

Premi **Calcola**, in alto a destra. La pagina si ricarica con i risultati; accanto alle
schede compare il distintivo **FS min**, verde se tutte le verifiche sono soddisfatte.

## 4. Leggi il carico limite

Apri la scheda **Carico limite**. In alto trovi l'esito e la **combinazione governante**,
poi quattro riquadri: **Resistenza di progetto R~d~**, **Azione di progetto E~d~**,
**Resistenza caratteristica R~k~** e **Fattore di sicurezza**. Sotto, una card per ogni
combinazione con N~q~, N~c~, Q~p~, Q~s~, il peso W, il carico limite Q e H~max~ di Broms.
La lettura completa è in [Carico limite](carico-limite.md).

![Scheda Carico limite: esito, riquadri di sintesi e tabella delle verticali per la combinazione A1+M1+R3](img/10-carico-limite.png)

Con il FEM attivo guarda anche **Analisi FEM** (diagrammi e tabella per nodo) e **Sezioni e
armature** (verifiche SLU, gabbia, distinta). La scheda **Sezione 2D** mostra il disegno
quotato, con i pulsanti **PNG** e **DXF**.

![Scheda Sezione 2D: palo, plinto, stratigrafia e schema delle azioni in testa](img/08-sezione-2d.png)

## 5. Genera la relazione

Apri la scheda **Relazione**: l'anteprima è gratuita e si aggiorna con il progetto. Con
**DOCX** (o **PDF**) scarichi il documento; l'addebito avviene solo a file prodotto.

## 6. Salva il progetto

**File → Salva** scarica il progetto come file **`.mpnx`**; **File → Apri** lo ricarica.
In alternativa usa il pulsante **GeoDropbox** per tenerlo nel cloud. Finché non salvi, in
barra compare **Modifiche non salvate**.

## E poi

Per partire da un caso diverso, **File → Nuovo progetto** crea un progetto vuoto. Oppure
scarica uno degli otto [progetti di esempio](esempi.md) dal pulsante **?** (scheda
**Risorse**) e aprilo con **File → Apri**.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MP%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mp/docs/it/quickstart.md).*
