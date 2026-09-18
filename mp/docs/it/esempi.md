# Progetti di esempio

MP NX distribuisce otto progetti pronti: tre esempi di progetto e cinque casi di
validazione, confrontati numero per numero con il programma desktop MP.

## Come si aprono

1. Nell'app premi il pulsante **?** in alto a destra e apri la scheda **Risorse**.
2. Sotto **Progetti di esempio** e **Casi di validazione** fai clic sul progetto: il browser
   scarica un file `.mpnx`.
3. **File → Apri** e scegli il file scaricato. L'app torna sulla scheda **Parametri** con i
   dati dell'esempio.
4. Premi **Calcola**.

Un esempio è un progetto come gli altri: lo modifichi e lo salvi con un altro nome.

## Esempi di progetto

### Palo trivellato — NTC 2018

`palo-trivellato-ntc2018.mpnx` — Palo trivellato Ø 0,80 m, L = 15 m, con plinto e piano di
posa a 1 m. **Due verticali d'indagine** (sondaggi S1 e S2, tre strati ciascuno) e falda a
4,5 m. Combinazioni «SLU A1+M1+R3» e «SLE rara», M~y~ = 350 kNm assegnato.

Mostra la catena NTC con più verticali: ξ~3~ e ξ~4~ per n = 2, minimo e media, R~k~ e R~d~.
Il cedimento è calcolato sulla combinazione di esercizio.

### Palo infisso in argilla con falda

`palo-infisso-argilla.mpnx` — Palo infisso Ø 0,50 m, L = 18 m, cerniera in testa. Due strati
di argilla in **condizione non drenata**, il primo in **attrito negativo**, sopra una sabbia
densa; falda a 1 m. Tre combinazioni, di cui una in **trazione** (F~y~ = −150 kN), e
**correzione sismica di Okamoto** con a/g = 0,15. N~q~ di Terzaghi.

Mostra come si leggono l'attrito negativo sottratto da Q, la verifica a trazione e la
riduzione sismica.

### Palo intestato in roccia

`palo-in-roccia.mpnx` — Palo Ø 1,00 m, L = 12 m, con trave di collegamento posata a 1,5 m.
Detrito di versante sopra due **strati rocciosi** (R~c~ = 5 e 15 MPa, RQD = 45 e 85 %).
Normativa **Eurocodice 7**, N~q~ di Hansen, M~y~ = 900 kNm, sovraccarico q~pc~ = 10 kN/m².

Mostra la resistenza laterale τ = α·R~c~ᵏ e la punta in roccia con k~sq~ dall'RQD.

## Casi di validazione

Sono trascrizioni di file del programma desktop MP. Usano la **Teoria classica** con
coefficienti globali 2,5. I risultati attesi sono nella pagina
[Validazione del codice](validazione.md).

### Esempio 16.3 di Bowles

`ex16-3-bowles.mpnx` — Palo trivellato Ø 0,30 m, 23 m nel terreno e 7 m di sporgenza, in
argilla molle non drenata (c~u~ = 12 kPa, α = 1). N~q~ imposto nullo, K = 0,8 assegnato.

Non ha azioni di progetto: serve al confronto sul carico limite. Per questo la scheda
Cedimenti resta vuota. Punta e fusto coincidono con il desktop; il peso del palo differisce
del 2 % per il peso di volume del calcestruzzo nei due archivi.

### Esempio 16.10 di Bowles

`ex16-10-bowles.mpnx` — Palo trivellato Ø 0,40 m, L = 15,9 m, in sabbia densa (φ = 32°).
N~q~ di Berezantsev con angolo corretto ¾ φ + 10°, forza orizzontale di 140 kN in testa,
cedimento di Poulos e Davis con Q = 100 kN. Il file porta il K~s~ assegnato del testo
(A~s~ = 4 927, B~s~ = 58 620, n = 1, 16 elementi).

Nel file l'analisi FEM è spenta: attivala nella card **Armatura e analisi FEM** per
riprodurre momenti, tagli e spostamenti nodo per nodo.

### Example1 del desktop

`example1-desktop.mpnx` — Palo trivellato Ø 0,60 m, L = 12 m, tre strati di argilla, trave
posata a 1 m. Forza orizzontale a z = 1 m, **FEM attivo** con K~s~ di Bowles costante e 9
elementi, **verifica SLU** con 8 Ø 16 e staffe Ø 10, normativa strutturale «NTC (a rottura)».

È il caso più completo: carico limite, FEM nodo per nodo, verifica della sezione. L'archivio
dei materiali del progetto riproduce quello tecnico del desktop.

### Pile immersed del desktop

`pile-immersed-desktop.mpnx` — Lo stesso palo, con **4 m fuori terra** e il livello
dell'acqua **2 m sopra il piano campagna** (profondità della falda −2 m). Argille in
condizione non drenata con c~u~ = 196 kPa. Tre forze orizzontali sul tratto libero; FEM
spento.

Mostra la tensione totale alla punta con la colonna d'acqua e la sporgenza.

### DPHS1 micropiles del desktop

`dphs1-micropiles-desktop.mpnx` — **Micropalo Tubifix** con tubolare 114,3 × 10 mm:
perforazione Ø 0,20 m, fusto di 2 m e bulbo Ø 0,40 × 6 m, iniezione IRS, portata laterale
con **Mayer modificato**. Tre strati, due non drenati, falda a 2,9 m. M~y~ = 39,68 kNm
assegnato, carico assiale di 100 kN.

!!! note "Peso dell'armatura"
    Il file riproduce il desktop, che ha il peso dell'armatura a 0. Se scegli il tubo dalla
    serie, il campo **Peso dell'armatura** si riempie dalla geometria (0,252 kN/m), W sale
    da 20,42 a 22,44 kN e Q scende da 383,79 a 381,77 kN.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MP%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mp/docs/it/esempi.md).*
