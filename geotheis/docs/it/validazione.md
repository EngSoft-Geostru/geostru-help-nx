# Validazione e differenze dal desktop

Il codice di calcolo di GeoTheis NX è accompagnato da un documento di validazione, come chiede il punto 10.2 delle NTC 2018: campi
d'impiego, basi teoriche, casi di prova risolti e scarti dal programma desktop. Si chiama validazione, non certificazione: nessun ente
terzo è coinvolto.

Questa pagina riassume il documento per la versione **1.0.0** del motore di calcolo (16/11/2026). La versione del motore è stampata
nel blocco «Codice di calcolo» di ogni relazione Word, così sai con quale codice è stato fatto ogni documento.

## Riferimenti della validazione

GeoTheis NX nasce dal programma desktop GeoTheis, ma il riferimento più forte della validazione è la **letteratura**: forme chiuse,
tabelle pubblicate, identità matematiche che non dipendono dal codice. Il desktop serve a dimostrare che le differenze fra i due
programmi sono le correzioni elencate più sotto, e nient'altro.

Il motore ha due modalità:

- la modalità **corretta**, l'unica che usi nell'app, con le formule di letteratura; coincide con il desktop corretto il 15/11/2026;
- una modalità che **riproduce il desktop** com'era prima delle correzioni, che esiste solo nelle prove automatiche per il confronto.

Al 16/11/2026 le prove automatiche sono 840 sul motore di calcolo, 304 sull'app con il motore collegato e 23 sulla guardia della
versione del motore: tutte superate.

## Che cosa è stato controllato

| Controllo | Riferimento | Esito |
|---|---|---|
| Funzione di pozzo W(u) di Theis | integrale esponenziale E~1~ e tabella pubblicata (Wenzel; Kruseman & de Ridder) | 10⁻¹³ relativo su E~1~; entro le 3 cifre della tabella |
| Funzione di Hantush W(u, r/B) | limite stazionario 2·K~0~(r/B), identità di simmetria di Hantush, tabella di Hantush (1956) su circa 2 080 celle | identità a 10⁻¹¹; tabella entro 0,6·10⁻⁴ assoluto o 2·10⁻⁴ relativo, salvo refusi della tabella del desktop |
| Parità con il desktop di prima | 12 esempi del desktop + 8 varianti dei pozzi singoli, nella modalità che riproduce il desktop | tutti entro 10⁻⁵ relativo |
| Modalità corretta contro il desktop corretto | gli stessi 20 casi | 10⁻⁵ relativo (5·10⁻⁵ su C dei gradini, che il desktop calcola in precisione singola) |
| Modalità corretta contro le formule di letteratura | gli stessi dati, formule in doppia precisione | entro 10⁻⁹ |
| Fitting di Theis e Hantush | dati sintetici con valori noti | T e S ritrovati a 10⁻⁶ relativo, r/B a 10⁻⁵; con rumore del 2 % l'intervallo al 95 % contiene il valore vero |
| Rorabaugh | dati sintetici s = BQ + CQⁿ con n = 1,5; 2; 2,8 | B, C, n ritrovati |
| Coordinate | PROJ (pyproj) su città italiane e su un caso reale in Gauss-Boaga | entro 2 cm; andata e ritorno sotto 1 cm |

## Caso di prova: CELICO

L'esempio **CELICO** (pozzo completo in falda confinata, tre gradini, due piezometri, prova a portata costante con risalita) è il caso
di riferimento. Valori della modalità corretta, uguali al desktop corretto:

| Grandezza | GeoTheis NX | Desktop prima delle correzioni |
|---|---|---|
| B, C dei gradini | 2,3894·10⁻³ h/m², 3,2486·10⁻⁶ h²/m⁵ | uguali |
| Efficienza alla portata ottimale (989,6 m³/h) | 42,64 % | 0 % |
| T Cooper-Jacob P1 / P2 | 4,231·10⁻³ / 1,058·10⁻² m²/s | 1,98·10⁻⁴ / 4,96·10⁻⁴ m²/s |
| S Cooper-Jacob P1 / P2 | 7,32·10⁻³ / 5,61·10⁻³ | 2,22·10⁻⁴ / 1,70·10⁻⁴ |
| T risalita P1 / P2 | 4,69·10⁻³ / 1,17·10⁻² m²/s | calcolata sui tempi sbagliati |
| T, R Dupuit-Thiem | 3,91·10⁻³ m²/s, R = 76,5 m | R = 1,21 m |
| T, K, R dai gradini (retta in distanza) | 5,41·10⁻² m²/s, 7,72·10⁻³ m/s, 443 m | 5,79·10⁻² m²/s, 8,27·10⁻³ m/s, 558 m |
| T pozzo singolo (R = 150 m) | 4,23·10⁻² m²/s | uguale entro lo 0,07 % |

**Fitting di Theis contro il punto scelto a mano nel desktop.** Il desktop non aveva un fitting: T e S di Theis venivano dal punto
trascinato col mouse su una curva tipo sbagliata. Su CELICO il fitting di GeoTheis NX dà T = 4,34·10⁻³ m²/s e S = 7,03·10⁻³ su P1, con
uno scarto tipico dai dati del 7 %, e concorda con Cooper-Jacob entro il 3 % su T e il 4 % su S. Il punto salvato nel file del desktop
dà T = 2,50·10⁻³ m²/s e S = 1,97·10⁻², con uno scarto tipico del 190 %. Per questo il punto importato compare come *non affidabile*.

**Pozzi singoli con la portata critica nota.** Sugli otto esempi con la sola geometria del pozzo, con Q~c~ = 100 m³/h, s~c~ = 5 m e
R = 150 m, il programma calcola gli stessi 29 metodi del desktop corretto, entro 1,1·10⁻⁷ relativo. Pozzo completo in falda
confinata: T = 5,043·10⁻³ m²/s, K = 8,405·10⁻⁴ m/s.

!!! note "Nota"
    Gli esempi del desktop **non sono prove reali**: in CELICO le letture di P2 sono quelle di P1 × 0,4, e due esempi riusano le stesse
    letture con i piezometri spostati. Dimostrano che il calcolo è corretto, non che un metodo descrive un acquifero vero. Per questo
    su CELICO i metodi della prova a gradini (T ≈ 5·10⁻² m²/s) e quelli della portata costante (4–11·10⁻³ m²/s) non concordano, e il
    programma lo segnala.

## Differenze dal programma desktop

GeoTheis NX usa le formule di letteratura dove il desktop, prima della correzione del 15/11/2026, se ne discostava. Sugli stessi dati i
numeri possono quindi essere diversi da quelli che leggevi nel desktop.

| Desktop prima delle correzioni | GeoTheis NX |
|---|---|
| W(u) di Theis calcolata con −0,7552 al posto della costante di Eulero (0,5772): curva tipo spostata | W(u) esatta |
| T di Cooper-Jacob = 0,183·(Q/3600)/C: su CELICO 24 volte più piccola | T = ln10·Q/(4π·Δs) |
| Retta di Cooper-Jacob su tutti i punti, anche a u ≈ 0,5 | solo il tratto con u < 0,05, scelto in automatico |
| Risalita regredita sui tempi dell'abbassamento | s′ contro log(t/t′), con il tempo d'arresto dichiarato |
| S di Hantush = 4·T·t/(u·r) | S = 4·T·u·(t/r²) |
| R di Dupuit-Thiem ricavato dal pozzo, con π al posto di 2π | R dalla retta dei piezometri, dove s = 0 |
| Raggio d'azione dai gradini: retta pozzo – R cliccato | retta di Thiem sui piezometri, un R per gradino |
| Efficienza dei gradini salvata come 0 % | efficienza alla portata ottimale |
| Muskat con una parentesi sbagliata; tabella ξ di Chiesa interpolata al contrario, con due refusi | formule e tabella corrette |
| Medie divise per il numero di righe, anche vuote | medie dei soli valori presenti |
| Theis e Hantush solo con il punto scelto col mouse | fitting automatico con intervalli al 95 %, più il ritocco |
| Falda libera e pozzo incompleto rifiutati dai metodi transitori | calcolati con un avviso |
| Tabella di Hantush con refusi | integrale numerico |
| Solo Jacob (n = 2) sulla prova a gradini | in più Rorabaugh (n libero), indicativo |

Restano **come nel desktop**, segnate *da verificare*, cinque formule dei pozzi incompleti (Halek, Muskat, Girinski, «L/b − L/2r» e il termine
ξ/2 dei tipi B e C): vedi [Cenni teorici](teoria.md#pozzo-incompleto-pozzo-parzialmente-penetrante).

## Campo d'impiego e limiti

- Prove a gradini di portata e prove a portata costante con risalita, sul pozzo e sui piezometri, in falda libera, confinata e
  semiconfinata, con pozzo completo o incompleto.
- Theis e Cooper-Jacob presuppongono la falda confinata; in falda libera valgono per abbassamenti piccoli rispetto allo spessore
  saturo (nessuna correzione di Jacob, nessun modello di Neuman).
- Hantush senza immagazzinamento dello strato semipermeabile.
- S dal pozzo di emungimento non è affidabile; per S servono i piezometri.
- I pozzi singoli e i metodi in distanza sui gradini sono indicativi.
- Non modellati: immagazzinamento nel pozzo e skin, derivata dell'abbassamento, drenaggio ritardato, limiti alimentanti o
  impermeabili, anisotropia, portate variabili diverse dai gradini, interferenza di più pozzi.
- Coordinate: le trasformazioni di datum a 7 parametri (Roma40) hanno un errore dell'ordine del metro, fino a qualche metro; ED50 fino a
  una decina di metri. La relazione dichiara la trasformazione usata.
- I pozzi censiti vengono dall'archivio ISPRA (L. 464/84), che è incompleto; la quota del piano campagna da modello digitale non entra
  nel calcolo.

Un confronto incrociato a video fra desktop e NX su un caso reale è previsto e sarà aggiunto al documento quando saranno disponibili
le letture di una prova reale.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/it/validazione.md).*
