# Validazione e limiti

Il punto 10.2 delle NTC 2018 chiede al progettista di valutare l'affidabilità del codice. Questa pagina riassume il materiale. L'impianto delle validazioni
GeoStru è descritto su [geostru.ai](https://geostru.ai/en/validation/).

## Campi di impiego

Misure di **rumore ambientale a stazione singola** con sensore a tre componenti. Modello 1D a strati orizzontali, confronto con il modo fondamentale.

## Limiti da valutare

- Il modello è **1D**: valli sepolte, strati inclinati, cavità e topografia non sono rappresentati.
- Si assume un campo d'onde da **sorgenti diffuse**: macchine vicine, vento e cattivo accoppiamento danno picchi non stratigrafici.
- Il misfit usa il **solo modo fondamentale** e confronta la **forma**: l'ampiezza misurata non vincola il contrasto.
- L'inversione **non è unica**: moltiplicando H e V~s~ per lo stesso numero la curva non cambia. Tre modelli con la stessa curva danno categorie E, C e B. **Serve un dato
  indipendente**.
- Un **picco sul bordo** della banda non è un picco, e f~0~ è il massimo assoluto: con due picchi simili può saltare dall'uno all'altro.
- Sotto i **20 minuti** la misura è fuori dalla raccomandazione SESAME.
- ρ e ν sono assunti. Non sono trattati i casi S1 e S2, né l'inversione congiunta con la MASW.

## Casi di prova

**Forme chiuse.** Risonanza V~s~/4H: 20 m a 200 m/s danno 2,5 Hz; il massimo dell'ellitticità vale 2,50 Hz con contrasto 10, 2,65 Hz con contrasto 6, 3,20 Hz con contrasto 4.
V~s,eq~: 6 m a 180 e 14 m a 320 m/s su substrato danno 20 / 0,07708 = 259,46 m/s, categoria E.

**Inversione sintetica.** Una curva generata da un modello noto viene ritrovata: H = 14,000 m, V~s~ = 180,00 e 320,00 m/s, misfit 7,6·10⁻¹⁰. È il caso più favorevole, senza rumore.

**Confronto con Easy HVSR desktop.** Sette registrazioni e nove progetti: curva H/V, σ, spettri e mappe coincidono entro 10⁻⁹ relativo, f~0~ a 12 decimali, i nove esiti SESAME
esattamente, l'ellitticità entro 10⁻⁹, il misfit a 12 decimali. Il riferimento è il desktop di oggi, non i numeri salvati nei progetti del 2011-2015. Questo dimostra che il porting
non ha cambiato il calcolo, non che il metodo sia corretto: per quello valgono le forme chiuse e la letteratura.

| File | Finestre | f~0~ [Hz] | A~0~ | Curva | Picco |
|---|---|---|---|---|---|
| `Example_01.SAF` | 59 | 5,75 | 3,498 | 3/3 | 4/6 |
| `Esempio_02.saf` | 59 | 14,75 (bordo) | 3,299 | 3/3 | 4/6 |
| `Esempio_SEG2.sg2` | 60 | 1,55 | 2,143 | 3/3 | 6/6 |

## Differenze dal desktop

| Desktop | HVSR NX |
|---|---|
| Filtro STA/LTA che, trovata una finestra da scartare in un certo punto, cancellava anche le successive: `Example_01` 0 finestre, `Esempio_02` 16 | ogni finestra è guardata: 30 e 44 |
| Medie su tutte le finestre o sulle incluse, a seconda del comando | sempre sulle incluse |
| V~s,eq~ non estesa a 30 m e con lo spessore del semispazio: 140,43 m/s, categoria D, su 5 m a 100, 5 m a 200, 300 m/s | semispazio infinito: 211,76 m/s, categoria C |
| V~s,eq~ non calcolata con il primo strato ≥ 800 m/s | V~s~ dello strato, categoria A |
| Piano di posa perso nei passaggi; categoria dal piano campagna | salvato; V~s,eq~ e categoria dal piano di posa |
| Etichette dei due lisciamenti triangolari scambiate | etichette corrette |
| Ricerca che poteva consegnare un modello peggiore della partenza | si tiene il migliore |
| Letture non numeriche a 0 in silenzio | errore esplicito |

Restano come nel desktop: 59 finestre invece di 60 su 1200 s, la σ relativa nella banda di fiducia e il rapporto delle medie come curva.

## Criteri SESAME

I criteri del desktop divergono dal testo del 2004 con esiti meno severi: dettagli in [Spettro H/V](spettro-hv.md). Il pulsante **Testo SESAME 2004** li applica come nel testo.

Il documento completo è disponibile su richiesta.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20HVSR%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hvsr/docs/it/validazione.md).*
