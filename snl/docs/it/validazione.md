# Validazione e limiti

La validazione documenta campo d'impiego, basi teoriche, casi di prova e scarti noti del codice di calcolo. Serve al progettista per valutare l'affidabilità del programma, come chiede il punto 10.2 delle NTC 2018.

Non è una certificazione: nessun ente terzo è coinvolto. Non sostituisce il controllo del modello, dei dati e dei risultati da parte di chi firma il progetto.

Il riferimento generale è la pagina [Validazione del codice di calcolo](https://geostru.ai/en/validation/). La versione del motore di calcolo è stampata nel blocco «Codice di calcolo» di ogni relazione.

## Come è stato controllato il motore

- **Casi risolti a mano** con le formule di letteratura riportate in [Cenni teorici](teoria.md): terreno omogeneo asciutto, un solo chiodo, carico uniforme, carico lineare, coefficienti di spinta;
- **confronto con esempi di calcolo già risolti**, su progetti che coprono le normative, il sisma, la falda, i carichi, le scelte di β e Bl e chiodi diversi fra loro;
- **scarti dichiarati**: dove il risultato differisce da un riferimento, la differenza è spiegata, non nascosta.

## Che cosa copre

- pareti chiodate costruite dall'alto per fasi di scavo, una fase per chiodo;
- paramento inclinato di θ dal verticale (0–90°) e terreno a monte inclinato di ε (0–90°);
- terreno stratificato; lo strato sotto la base è il terreno di fondazione;
- chiodi con profondità, lunghezza, inclinazione, diametri, fy e kn propri; interasse orizzontale unico;
- carichi a monte uniformi, a striscia e lineari, ciascuno con il proprio coefficiente A;
- falda orizzontale a quota assegnata;
- sisma pseudostatico con kh e kv;
- verifiche di rottura e sfilamento dei chiodi, stabilità interna per fase, scorrimento del blocco, diagrammi del rivestimento.

## Che cosa non copre

- la **stabilità globale** per superfici che passano dietro o sotto i chiodi: serve un programma di stabilità dei pendii, come GeoStru Slope;
- la **verifica della sezione del rivestimento** e della testa del chiodo: SNL NX dà solo i diagrammi;
- spostamenti e stati limite di esercizio, moto di filtrazione, condizioni non drenate;
- la ricerca della superficie critica: β è assegnata oppure 45° + φ̄'/2, non cercata al minimo del fattore di sicurezza.

## Ipotesi del metodo da tenere presenti

- **Cuneo piano** per ogni fase, con origine al fondo dello scavo della fase; i parametri del terreno sono medie pesate sugli spessori scavati.
- **Una sola combinazione** A/M/R per progetto, con un coefficiente R per verifica. Per applicare approcci diversi a verifiche diverse si calcola il progetto più volte. Scegliendo «Eurocodice 7» tutti i coefficienti valgono 1.
- La **forza nei chiodi** si calcola una volta, sulla parete finita: la verifica a rottura è la stessa in ogni fase, lo sfilamento cambia con la lunghezza efficace.
- La **pressione dell'acqua** entra nella forza del chiodo come la spinta del terreno, con kn e il fattore 1/cos α.
- La **resistenza tangenziale τlim** usa l'attrito δ dello strato del bulbo e un'aderenza pari a una frazione della coesione; la tensione verticale è quella del terreno sopra il centro del tratto efficace, senza falda né pendio. Non si può assegnare da prove di sfilamento.
- Il **coefficiente A** di ogni carico si scrive a mano: non viene dalla categoria.
- **Pendio a monte indefinito** con l'inclinazione ε.
- **Falda orizzontale** nelle tensioni e nella spinta dell'acqua sul blocco, parallela al pendio nella spinta sulla superficie di rottura e nella sottospinta; **paramento impermeabile**: l'acqua grava tutta sui chiodi.
- **Sisma**: con kh > 0 la spinta è sempre di Coulomb / Mononobe-Okabe; l'incremento sismico agisce sui carichi uniformi, non su strisce e carichi lineari; nello scorrimento sismico non c'è la forza d'inerzia del blocco. Il segno di kv va scelto con attenzione.
- **Scorrimento**: Q è il carico sul cuneo dell'ultima fase; con Bl automatica la base è la proiezione del primo chiodo.
- **Rivestimento**: i diagrammi sono indicativi; il momento al piede non torna esattamente a zero.
- Con ε > 0 il coefficiente di Rankine non contiene il fattore cos ε sulla spinta: per la forza nei chiodi il risultato è a favore di sicurezza (circa +3 % con ε = 10°).

## Differenze rispetto ai file .snl

I risultati salvati in un file `.snl` possono differire da quelli di SNL NX perché il calcolo è stato corretto in alcuni punti (fattori di sicurezza negativi nello scorrimento, spinte degli strati, falda nella verifica interna, chiodi non in ordine di profondità). Nello scorrimento con più strati SNL NX integra la spinta di ogni strato una volta sola: il fattore di sicurezza può risultare più alto di quello salvato nel file.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/snl/docs/it/validazione.md).*
