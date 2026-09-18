# Stratigrafie e falda

Il terreno si descrive nella card **Stratigrafie e verticali d'indagine**; la falda ha una
card sua. Il sovraccarico sul piano campagna q~pc~ sta nella card **Palo**.

## Verticali d'indagine

Ogni stratigrafia è una **verticale**: un sondaggio, una prova, un profilo di progetto. Con
il pulsante **Verticale** ne aggiungi quante ne servono.

La casella **Verticale d'indagine** decide se la stratigrafia entra nel calcolo. Per ogni
verticale marcata il programma calcola il carico limite; il numero n di verticali fissa i
fattori di correlazione ξ~3~ e ξ~4~, e la resistenza caratteristica è
R~k~ = min(Q~med~/ξ~3~, Q~min~/ξ~4~). Le stratigrafie non marcate servono solo al disegno.

Se nessuna stratigrafia è marcata, il programma usa la prima e lo segnala fra i messaggi.

## Parametri di strato

Ogni riga è uno strato, dall'alto verso il basso. Le frecce spostano la riga, poi ci sono
**Duplica** ed **Elimina**; il quadratino colorato sceglie il colore nel disegno.

| Colonna | Significato | Unità |
|---|---|---|
| **s** | spessore | m |
| **γ** | peso di volume | kN/m³ |
| **γ~sat~** | peso di volume saturo, usato sotto falda | kN/m³ |
| **φ** | angolo di attrito | ° |
| **c** | coesione efficace c′ | kPa |
| **α** | adesione: moltiplica la coesione nella resistenza laterale (α·c) | – |
| **E** | modulo elastico del terreno, usato dal cedimento di Poulos e Davis | MPa |

La freccia a inizio riga apre le **Proprietà dello strato**: il coefficiente di Poisson ν e
il modulo edometrico E~ed~ (servono al modulo di reazione di Chiarugi-Maia nel
[FEM](fem.md)), la coesione non drenata c~u~, la resistenza R~c~ e l'RQD della roccia, e
tre caselle.

![Card Stratigrafie e verticali d'indagine con una verticale di due strati, e sotto la card Falda](img/04-stratigrafie.png)

### Condizione non drenata

Con **Condizione non drenata** lo strato è calcolato con φ = 0, c = c~u~ e il peso saturo.
Alla punta N~q~ = 1 e N~c~ è quello del metodo scelto per φ = 0 (9 con Berezantsev); lungo
il fusto la resistenza è α·c~u~.

**c′ e c~u~ sono due campi distinti.** La colonna **c** è la coesione efficace, usata in
condizione drenata; **c~u~** sta nelle proprietà dello strato e si abilita con la casella.
Così uno stesso strato conserva entrambi i valori e puoi passare da una condizione
all'altra senza riscriverli.

!!! note "File salvati prima di settembre 2026"
    In uno strato non drenato con c~u~ = 0 il programma usa il valore della colonna **c**.
    Serve ai progetti salvati quando il campo era unico, che altrimenti cambierebbero
    risultato da soli. Nei progetti nuovi scrivi c~u~ nel suo campo.

### Strato roccioso

Con **Strato roccioso** si abilitano **R~c~** (resistenza a compressione monoassiale, in
MPa) e **RQD** (in %). Il termine attritivo è annullato e la resistenza laterale vale
τ = α·R~c~ᵏ, con l'esponente k scritto nella card **Normativa e coefficienti parziali**
(campo **k roccia**). Se la punta è in roccia, Q~p~ = A·R~c~·k~sq~·d~r~, con d~r~ fattore di
profondità e k~sq~ dall'RQD:

| RQD [%] | > 90 | 75–90 | 50–75 | 25–50 | ≤ 25 |
|---|---|---|---|---|---|
| k~sq~ | 1,00 | 0,75 | 0,30 | 0,10 | 0,05 |

### Attrito negativo

Con **Attrito negativo** lo strato trascina il palo verso il basso: non contribuisce alla
resistenza laterale e la sua aderenza è sottratta dal carico limite netto. Nella scheda
**Carico limite** il valore sottratto compare fra parentesi accanto a Q.

## Falda

Nella card **Falda** scegli **Presente** e scrivi la **Profondità della falda** dal piano
campagna. Sotto falda il programma usa γ′ = γ~sat~ − γ~w~: se in uno strato immerso manca
γ~sat~, il calcolo si ferma con un messaggio.

Una profondità **negativa** mette il livello dell'acqua **sopra il piano campagna**: tutti
gli strati sono immersi e alla tensione si aggiunge la colonna d'acqua γ~w~·|z|. È il caso
dei pali in alveo o in banchina; l'esempio «Pile immersed» lo mostra con 2 m d'acqua.

!!! warning "Falda su una quota di strato"
    La profondità della falda non deve coincidere con il passaggio fra due strati: il
    calcolo si ferma. Sposta la falda di un centimetro o spezza lo strato.

## Sovraccarico

**q~pc~**, nella card **Palo**, è un sovraccarico uniforme sul piano campagna, in kN/m². Si
somma alla tensione verticale efficace alla punta, σ′~v~, da cui dipende la resistenza di
punta.

## Incolla strati

Se hai la stratigrafia in un foglio di calcolo, usa il pulsante con gli appunti
nell'intestazione della verticale. Si apre la finestra **Incolla strati**: incolla le righe
copiate, una per strato, con le colonne in quest'ordine.

```text
descrizione; spessore [m]; γ [kN/m³]; γsat [kN/m³]; φ [°]; c [kPa]; α; E [MPa]
```

Le colonne possono essere separate da tabulazione, punto e virgola o virgola; i decimali
possono avere la virgola. La descrizione è facoltativa e le colonne mancanti restano ai
valori della prima riga. La finestra mostra le **Righe rilevate** prima di confermare, e
scegli se **aggiungi in coda** o **sostituisci** gli strati esistenti. Le proprietà non
presenti nell'elenco (c~u~, R~c~, RQD, caselle) si completano poi a mano.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MP%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mp/docs/it/stratigrafia.md).*
