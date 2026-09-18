# Carico limite

MP NX calcola il carico limite verticale con le **formule statiche**, per ogni verticale
d'indagine e per ogni combinazione, poi applica i fattori ξ e i coefficienti γ~R~. Questa
pagina spiega le scelte della card **Palo** e come leggere la scheda **Carico limite**.

## Carico limite netto

In **compressione**:

Q = Q~p~ + Q~s~ − W − Q~neg~

con Q~p~ resistenza di punta, Q~s~ resistenza laterale, W peso del palo e Q~neg~ aderenza
degli strati in attrito negativo. In **trazione** la punta non lavora: Q = Q~s~ + W.

## Resistenza di punta

Q~p~ = A·(σ′~v~·N~q~ + c·N~c~), con σ′~v~ tensione verticale efficace alla punta, compreso
il sovraccarico q~pc~. N~q~ e N~c~ dipendono dal **Metodo per N~q~**:

| Metodo | N~q~ | N~c~ |
|---|---|---|
| **Berezantsev** | funzione di φ e di L/D; per D > 0,8 m interpolazione su L/D | (N~q~ − 1)/tan φ; 9 per φ = 0 |
| **Berezantsev (L/D = 32)** | 0,48·exp(4,97·tan φ) | come sopra |
| **Terzaghi** | formula di Terzaghi (1943) | (N~q~ − 1)/tan φ, minimo 5,7 |
| **Janbu** | funzione di φ e della densità relativa D~r~ (ψ = 60° + 0,45·D~r~) | (N~q~ − 1)/tan φ; 5,74 per φ = 0 |
| **Hansen** | exp(π·tan φ)·tan²(45° + φ/2) con fattori di forma e profondità | con gli stessi fattori; 5,14 per φ = 0 |
| **Vesic** | funzione di φ e dell'indice di rigidezza I~r~ = 1,7·D~r~ | (N~q~ − 1)/tan φ |
| **N~q~ utente** | il valore del campo **N~q~ imposto** | (N~q~ − 1)/tan φ; 9 per φ = 0 |

Con Janbu e Vesic compare il campo **D~r~**, la densità relativa in %. Le formule complete e
i valori di controllo a φ = 30° sono nel [documento di validazione](validazione.md).

Il campo **Angolo d'attrito per la resistenza laterale** corregge φ prima del calcolo: φ,
φ − 3° (trivellati), ¾ φ + 10° (battuti) oppure (φ + 40°)/2. L'angolo corretto entra anche
in N~q~: nell'esempio 16.10 di Bowles φ = 32° diventa 34° alla punta.

## Resistenza laterale

Q~s~ = π·D·Σ (K·tan δ·σ′~v,med~ + α·c)·t, sommata sugli strati di spessore t.

- **Coefficiente di spinta K**: 0,5; 1; 1 − sin φ; 1 − tan² φ; oppure **Valore utente**.
- **Angolo di attrito terra-palo**: δ = φ, ⅔ φ, ¾ φ, 20° o 25°.
- **α** e **c** (o **c~u~**) vengono dallo [strato](stratigrafia.md).

Negli strati rocciosi il termine attritivo è nullo e τ = α·R~c~ᵏ. L'aderenza sopra il piano
di posa della fondazione è sottratta. Per i pali infissi tronco-conici si applica il fattore
di conicità F~w~.

!!! note "K è calcolato con φ non ridotto"
    Con K = 1 − sin φ o 1 − tan² φ il programma usa l'angolo d'attrito dello strato, non
    quello ridotto dai coefficienti M o corretto per l'infissione. È il comportamento del
    programma desktop, dichiarato nel documento di validazione.

## Da Q a R~k~ e R~d~

Per ogni combinazione il programma calcola Q~p~ e Q~s~ su tutte le verticali, poi:

1. prende minimo e media, e con ξ~3~ e ξ~4~ ricava **R~k,p~** e **R~k,s~**;
2. divide per γ~b~ e γ~s~ e sottrae il peso: **R~d~ = R~k,p~/γ~b~ + R~k,s~/γ~s~ − W**;
3. confronta con l'azione: **FS~v~ = R~d~/|E~d,v~|**.

Il peso W è quello della prima verticale. I coefficienti sono descritti in
[Carichi, combinazioni e normativa](combinazioni.md).

## Carico limite orizzontale (Broms)

H~max~ è calcolato con il metodo di **Broms**, nella formulazione di Viggiani: terreni
coesivi (con c~u~) e incoerenti (con K~p~ di Rankine), **testa libera o incastrata** secondo
il **Vincolo in testa** dei Dati generali. Il meccanismo dipende dal momento ultimo della
sezione M~y~ e compare in tabella come **Palo corto**, **Palo medio** o **Palo lungo**.

Da dove viene M~y~:

- se scrivi **M~y~** nella card Materiali e armatura, prevale il tuo valore;
- se M~y~ = 0 e l'**analisi FEM è attiva**, entra il momento ultimo della sezione armata a
  N = 0, calcolato dal programma;
- per il **micropalo tubolare** con M~y~ = 0 entra il momento della sezione mista tubo +
  malta;
- se M~y~ = 0 e il FEM è spento, la verifica orizzontale non viene fatta.

La resistenza di progetto è R~d,h~ = R~k,h~/γ~T~ e la verifica FS~h~ = R~d,h~/E~d,h~.

## Correzione sismica

Con a/g > 0 nella card **Azione sismica** il carico limite è ridotto con uno di tre metodi:

| Metodo | Correzione |
|---|---|
| **Vesic** | φ ridotto di 2° |
| **Okamoto** | punta e termine coesivo laterale moltiplicati per 1 − a/g |
| **Sano** | φ ridotto di atan(a/(g·√2)) |

Vesic e Sano ripartono dall'angolo φ non ridotto: con i coefficienti M2 la riduzione di φ
non si somma. Anche questo è dichiarato nel documento di validazione.

## Leggere la scheda Carico limite

In alto c'è l'esito, **Verifica soddisfatta** o **Verifica NON soddisfatta**, con la
**Combinazione governante**, cioè quella con il fattore di sicurezza più basso. I quattro
riquadri riportano R~d~, E~d~, R~k~ e il **Fattore di sicurezza** su una scala da 1 a 3.

Segue una card per combinazione. L'intestazione dice se è **Compressione** o **Trazione** e
riporta E~d,v~ ed E~d,h~. La tabella ha una riga per verticale:

| Colonna | Significato |
|---|---|
| N~q~, N~c~ | fattori di capacità portante usati |
| φ~p~, c~p~ | angolo d'attrito e coesione alla punta, dopo correzioni e coefficienti |
| σ′~v,p~ | tensione verticale alla punta |
| Q~p~, Q~s~, W | punta, laterale, peso del palo |
| Q | carico limite netto; fra parentesi l'attrito negativo sottratto |
| H~max~, Meccanismo | carico limite orizzontale di Broms e meccanismo |

Sotto la tabella, quattro gruppi: **Verticali d'indagine** (n, ξ~3~, ξ~4~, minimo, media e
massimo di Q~p~ e Q~s~), **Resistenze caratteristiche**, **Resistenze di progetto** con γ~b~,
γ~s~ e FS~v~, e **Carico limite orizzontale (Broms)** con FS~h~. In fondo compaiono gli
eventuali messaggi del calcolo.

![Scheda Carico limite: esito, combinazione governante, riquadri R_d, E_d, R_k, FS e tabella delle verticali](img/10-carico-limite.png)

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MP%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mp/docs/it/carico-limite.md).*
