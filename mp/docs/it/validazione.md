# Validazione del codice

Il punto **10.2 delle NTC 2018** chiede al **progettista** di valutare l'affidabilità del
codice di calcolo che usa. Non è un adempimento di chi produce il software: è un giudizio
tuo. Il nostro compito è darti il materiale per formarlo.

Per MP NX quel materiale è il **documento di validazione**: campi d'impiego e limiti, basi
teoriche con bibliografia, casi di prova risolti e riproducibili. Questa pagina ne è la
sintesi. È una **validazione**, fatta da chi sviluppa il programma e verificabile da
chiunque: nessun ente terzo è coinvolto.

## Campi d'impiego e limiti

MP NX calcola un **palo singolo in calcestruzzo armato**, trivellato o infisso, e un
**micropalo singolo**. Le funzioni sono elencate nella [home](index.md).

Non copre: gruppi di pali ed efficienza della palificata; pali a elica; jet grouting; pali
in acciaio o legno; reticoli di micropali, micropali inclinati e carico critico
d'instabilità; verifica della sezione mista tubolare; sezioni non circolari nella verifica
strutturale; prove pressiometriche e formule dinamiche; cedimento di Fleming; pericolosità
sismica NTC completa e momenti cinematici.

Il modello alla Winkler non coglie l'interazione fra le molle né la plasticizzazione del
terreno oltre l'esclusione delle molle: per pali con grandi spostamenti servono analisi p-y
o continue.

## Basi teoriche

Berezantsev et al. (1961), Terzaghi (1943), Janbu (1976), Hansen (1970) e Vesic (1977) per
N~q~ e N~c~; Broms (1964) nella formulazione di Viggiani (1999) per il carico orizzontale;
Poulos e Davis (1980) per il cedimento; Bowles (1996) e Chiarugi-Maia (1970) per il modulo
di reazione; NTC 2018 con la Circolare 7/2019, EN 1997-1 ed EN 1992-1-1 per i coefficienti e
la verifica della sezione.

## Casi di prova

Il documento contiene **18 casi**, tutti ripetuti come test automatici a ogni versione.

| Casi | Oggetto | Riferimento | Scarto |
|---|---|---|---|
| 1 | N~q~ e N~c~ a φ = 30° per tutti i metodi | formule di letteratura | < 1 % (< 2 % Berezantsev con D = 1 m) |
| 2–4 | palo in sabbia, in argilla non drenata, in roccia | calcolo a mano | entro ± 1 % |
| 5 | Broms, sei casi (coesivo e incoerente, testa libera e incastrata) | forme chiuse | ± 1 % |
| 6 | Poulos e Davis | tabella del metodo | 6,1 mm attesi, 6,0–6,25 calcolati |
| 7 | catena NTC: ξ, γ~b~, γ~s~, trazione, coefficiente globale | NTC 2018 tab. 6.4.II e 6.4.IV | esatto |
| 8–10 | i tre esempi di progetto | si caricano e si calcolano | — |
| 11–12 | FEM dell'esempio 16.10 di Bowles; K~s~ di Bowles a mano | desktop e calcolo a mano | 0,0 % sul solutore; 0,4 % attraverso l'archivio |
| 13 | momento ultimo Ø 80 cm, 12 Ø 20 | abachi adimensionali | 455 kNm attesi e calcolati |
| 14–18 | cinque file del desktop MP | programma desktop | vedi sotto |

Dove esiste, il riferimento è la **forma chiusa di letteratura** ricalcolata a mano: è
verificabile da chiunque e non dipende da noi. Il confronto con il desktop si aggiunge, non
lo sostituisce.

## Scarti commentati

Gli scarti non sono nascosti: ognuno ha una causa dichiarata.

- **Peso del palo, + 2 % (caso 14).** Il desktop, nel sistema in kg, usa 2 500 kg/m³ per il
  C20/25 (24,52 kN/m³); l'archivio SI riporta 25 kN/m³. Punta e fusto coincidono; tolta la
  differenza di peso, Q e R~d~ tornano entro lo 0,1 %. Lo scarto è conservativo.
- **Modulo elastico, 0,4 % (caso 11).** Stessa origine: i due archivi del desktop hanno E
  diversi per la stessa classe. Con lo stesso modulo il solutore coincide alla quarta cifra.
- **Resistenze a taglio, − 2 % (caso 16).** V~Rcd~ e V~Rsd~ sono più basse del desktop a
  tutti i nodi. Corrisponde a un'altezza utile minore di un diametro di staffa: il desktop
  usa una versione compilata del solutore, MP NX i sorgenti. Lo scarto è conservativo.
- **Casi 15, 17 e 18: 0,0 %** su carico limite e resistenze di progetto; nel caso 15 anche
  sul cedimento, nel caso 18 anche su Broms.

Per riprodurre un file del desktop in sistema tecnico, metti nell'archivio del progetto i
valori dell'archivio tecnico (per il C20/25: E~c~ = 29 380,7 MPa, γ = 24,52 kN/m³). Così lo
scarto che resta è del calcolo, non degli archivi.

## Scelte dichiarate

Alcuni comportamenti del programma desktop sono stati **mantenuti** e sono elencati nel
documento: il fattore di conicità F~w~ per φ ≥ 30°, la correzione sismica di Vesic e Sano a
partire da φ non ridotto, l'aderenza non sottratta quando il piano di posa cade nel primo
strato, R~d~ con il peso del palo della prima verticale. Un errore del desktop nella
descrizione del meccanismo di Broms è stato invece corretto; H~max~ non cambia.

## Dove trovarlo

I cinque casi di validazione si scaricano dall'app: vedi [Progetti di esempio](esempi.md).
La pagina sulla validazione dei codici GeoStru si apre dal pulsante **?**, scheda
**Risorse**, voce **Validazione del codice di calcolo**.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MP%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mp/docs/it/validazione.md).*
