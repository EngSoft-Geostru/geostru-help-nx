# Validazione e limiti

Il documento di validazione completo (NTC 2018 §10.2) accompagna il codice: campo d'impiego, basi teoriche, casi di prova risolti e scarti
dal programma desktop. Si chiama validazione, non certificazione: nessun ente terzo è coinvolto. Il §10.2 chiede al **progettista** di
valutare l'affidabilità del codice che usa; questa pagina e quel documento sono il materiale per farlo. La revisione corrente vale per il
**motore di calcolo 1.0.0**, la versione che ogni relazione stampa nel blocco «Codice di calcolo».

## Campo d'impiego

- Muri a mensola in c.a. (con dente, mensola di monte e mensola di valle), muri a gravità, muri su una, due o tre file di pali o su file
  libere, muri con tiranti, muro di cantina (vincolo in testa).
- NTC 2018, NTC 2008 ed Eurocodici, con le combinazioni generate dalla norma o date dal progettista.
- Sisma pseudostatico NTC 2018 con Mononobe-Okabe e β~m~ dei muri dai parametri del sito.
- Terreno a strati (fino a dieci), falda, profilo a tratti, riempimenti, sovraccarichi distribuiti e forze concentrate.
- Sezioni rettangolari in c.a. allo SLU (presso-flessione, taglio senza armatura trasversale) e allo SLE (tensioni, fessure), o alle
  tensioni ammissibili; armature d'inviluppo, ripartitori, distinta.

## Limiti

- Il calcolo è per metro di muro, in deformazione piana: niente effetti tridimensionali, angoli o variazioni di altezza lungo il muro.
- Il carico distribuito sul terrapieno è ridotto a un **sovraccarico uniforme equivalente**: con carichi lontani o in striscia stretta la
  spinta è approssimata.
- La falda è **una sola**; a valle la sottospinta assume la falda al più al piano campagna.
- Con una pendenza di calcolo del terrapieno maggiore di φ~d~ il coefficiente di spinta è convenzionale: il programma lo segnala, la scelta
  del modello spetta al progettista.
- Il sisma verticale ha un solo verso (verso l'alto sulle masse).
- La **stabilità globale** dell'insieme muro-terreno non è calcolata: va verificata a parte con un programma di stabilità dei pendii.
- Spostamenti sismici permanenti e capacità sismica non sono nel risultato.
- Muri a contrafforti, a gabbioni e in pietrame si aprono ma non si calcolano.
- Il taglio delle sezioni del muro è verificato senza armatura trasversale; le armature si progettano sempre (quelle assegnate a mano non
  sono usate).
- Nella prima consegna gli avvisi del motore sono scritti in italiano anche con l'interfaccia in inglese, e i diagrammi delle sollecitazioni
  della fondazione uniscono con una retta i valori delle sezioni di calcolo.

## Casi di prova

| Caso | Riferimento | Esito |
|---|---|---|
| Guida 1, muro a mensola di 3 m su sabbia | calcolo a mano della catena: K~a~ 0,234891, B′ 1,630 m, Q~lim~ 1087,3 kN/m | NX e desktop coincidono alla quarta cifra: F~s~ scorrimento 3,7946, carico limite 8,6067 |
| Coefficienti in forma chiusa | Rankine, Müller-Breslau, Mononobe-Okabe attiva e passiva (Kramer 1996) | 6 decimali |
| Parità con MDC desktop | 22 esempi distribuiti e 8 varianti (sisma, contrafforte, muro di cantina, pali a 1 e 3 file): 30 casi, 87 combinazioni | spinte, forze, verifiche globali, sollecitazioni del paramento 87/87; armature 16/16; verifica SLU 12/12; muri a gravità 5/5; pali 23/23 |
| Correzioni del modo d'uso | un test a mano per ogni difetto corretto | per esempio Guida 1: ribaltamento 6,6597 → 6,5319 con la passiva fra gli stabilizzanti |
| L'app usa il motore così com'è | Guide 1, 2 e 3 aperte dalla pagina e confrontate con il motore chiamato direttamente | coincidenza a 10⁻⁹ |

Le tolleranze della parità sono 10⁻⁴ relativo su forze e coefficienti, 10⁻³ sulle sezioni in c.a., interi esatti per le armature. Un solo
scarto è commentato (0,03 % su una sezione della suola nella Guida 3, per un arrotondamento al mezzo millesimo).

## Differenze dal programma desktop

MDC NX dà gli stessi risultati del desktop dove il desktop è corretto. Dove non lo è, corregge e lo dichiara. Le correzioni principali:

| Desktop | MDC NX |
|---|---|
| nessuna sottospinta sulla base | sottospinta trapezia (falda a monte, al più al piano campagna a valle) |
| il momento della spinta passiva riduceva il momento ribaltante | la passiva è fra gli stabilizzanti |
| γ~R~ della resistenza del terreno a valle mai applicato alla spinta passiva | applicato (E~p~/γ~R,valle~) |
| spinta passiva sismica uguale a quella statica | Mononobe-Okabe passiva × (1 − k~v~) |
| peso del sovraccarico sulla suola con il coefficiente sfavorevole; carico «lineare» con un'estensione sbagliata | peso con γ ≤ 1 per i permanenti, nullo per i variabili; carico lineare come trapezio |
| attrito e adesione di base scritti a mano non ridotti da γ~φ~ e γ~c~ | ridotti; carico limite con i parametri dello strato |
| combinazioni sismiche NTC 2018 create con k~h~ = 0 | k~h~ e k~v~ dal sito |
| nessuna forza d'inerzia verticale | −k~v~·W sulle masse |
| muro a semigravità: resistenza della barra dieci volte troppo alta | corretta |
| sforzo normale preso in valore assoluto nella verifica SLU (una trazione diventava compressione) | col suo segno |
| mensola di valle: l'ultima azione sommata più volte | somma delle azioni |
| pali con modulo crescente: lunghezza caratteristica di Hetényi al posto di quella di Matlock-Reese | $T=(EI/n_h)^{1/5}$ |
| micropali tubolari tesi sempre «non verificati» | interazione N-M corretta |
| tiranti: inclinazione arrotondata a radianti interi; nessuna verifica del tiro; tiranti ignorati senza l'azione TIR | inclinazione esatta, verifica E~d~ ≤ R~d~, γ~TIR~ = 1 |

Restano come nel desktop, perché sono scelte di modello e non errori: il momento resistente di prima plasticizzazione con le NTC 2018 (vedi
[Sezioni in c.a., pali e tiranti](teoria-strutture.md)), la discretizzazione delle sezioni, la pendenza di calcolo del terrapieno, le
correlazioni del carico limite dei pali.

Per questo, sullo stesso progetto, i fattori di sicurezza di MDC NX possono essere diversi da quelli del desktop, quasi sempre in direzione
più cautelativa.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MDC%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mdc/docs/it/validazione.md).*
