# Glossario

Elenco dei simboli e dei termini usati nel software, nella relazione di calcolo e nel manuale.

## Geometria

| Simbolo | Nome esteso                                    | Unità  |
|---------|------------------------------------------------|--------|
| H       | altezza del versante                            | m      |
| β       | inclinazione del fronte (slope face)            | °      |
| α       | inclinazione del piano di rottura               | °      |
| ψ       | inclinazione del piano sommitale (bench)        | °      |
| B       | profondità del blocco (⟂ alla sezione)          | m      |
| T       | distanza fessura di trazione dal ciglio         | m      |
| θ       | inclinazione della fessura di trazione          | °      |
| N       | lunghezza fronte versante                       | m      |
| L       | lunghezza piano di rottura                      | m      |
| M       | lunghezza piano sommitale                       | m      |
| Q       | lunghezza fessura di trazione                   | m      |
| A       | area del cuneo per metro                        | m²     |
| O, B, C, D | vertici del cuneo                            | (m, m) |
| G       | baricentro del cuneo                            | (m, m) |

## Materiale

| Simbolo  | Nome esteso                                  | Unità  |
|----------|----------------------------------------------|--------|
| γ        | peso volume del blocco                       | kN/m³  |
| c, c'    | coesione efficace sul piano                  | kPa    |
| φ, φ'    | angolo d'attrito efficace                    | °      |
| τ        | resistenza al taglio mobilitata              | kN/m   |
| σ<sub>n</sub> | tensione normale efficace sul piano      | kPa    |

## Forze e equilibrio

| Simbolo                      | Nome esteso                                     | Unità  |
|------------------------------|-------------------------------------------------|--------|
| W                            | peso del cuneo per metro                        | kN/m   |
| F<sub>x</sub>, F<sub>y</sub> | risultanti delle azioni                          | kN/m   |
| N                            | normale al piano di rottura                     | kN/m   |
| S                            | taglio motore lungo il piano                    | kN/m   |
| τ                            | resistenza al taglio sul piano (eq. 30)         | kN/m   |
| FS                           | fattore di sicurezza = τ / \|S\|                | -      |
| FS<sub>req</sub>             | FS richiesto dalla normativa                    | -      |

## Acqua

| Simbolo  | Nome esteso                                      | Unità  |
|----------|--------------------------------------------------|--------|
| γ<sub>w</sub> | peso volume dell'acqua                       | kN/m³  |
| Hw       | livello acqua al piede (ponded esterna)          | m      |
| Zw       | livello acqua nella discontinuità                | m      |
| Zt       | livello acqua nella fessura di trazione          | m      |
| U        | sottospinta uplift sul piano                     | kN/m   |
| U<sub>p</sub> | spinta acqua ponded sul fronte              | kN/m   |
| V        | forza acqua nella tension crack                  | kN/m   |
| u(s)     | pressione interstiziale distribuita sul piano    | kPa    |

## Sisma e azioni esterne

| Simbolo                        | Nome esteso                                  | Unità  |
|--------------------------------|----------------------------------------------|--------|
| k<sub>h</sub> = α<sub>s</sub>  | coefficiente sismico orizzontale             | -      |
| k<sub>v</sub>                  | coefficiente sismico verticale               | -      |
| Ω                              | direzione del sisma dall'orizzontale         | °      |
| E                              | modulo della forza esterna                   | kN/m   |
| δ                              | inclinazione di E dall'orizzontale           | °      |

## Interventi

| Simbolo                       | Nome esteso                                   | Unità  |
|-------------------------------|-----------------------------------------------|--------|
| J<sub>x</sub>, J<sub>y</sub>  | componenti chiodi attivi (tiranti)            | kN/m   |
| K<sub>x</sub>, K<sub>y</sub>  | componenti chiodi passivi                     | kN/m   |
| F                             | capacità singola del chiodo/tirante           | kN     |
| Δ                             | inclinazione del chiodo sotto-orizzontale     | °      |
| Φ = α + Δ                     | angolo bar-piano (Clouterre)                  | °      |
| T<sub>max</sub>               | capacità assiale del chiodo                   | kN     |
| V<sub>max</sub>               | capacità a taglio della barra (Tresca)        | kN     |
| R<sub>acciaio</sub>           | resistenza rottura armatura                   | kN     |
| R<sub>aderenza</sub>          | resistenza aderenza barra-malta               | kN     |
| R<sub>estrazione</sub>        | resistenza sfilamento bulbo                   | kN     |
| R<sub>min</sub>               | min dei 3 limiti                              | kN     |
| R<sub>k</sub>                 | resistenza caratteristica = R<sub>min</sub>/ξ | kN     |
| R<sub>d</sub>                 | resistenza di progetto = R<sub>k</sub>/γ<sub>Ra,t</sub> | kN |
| q                             | pressione rete corticale R1                   | kN/m²  |
| τ<sub>R2</sub>                | capacità rete caging R2                       | kN/m   |

## Coefficienti parziali

| Simbolo                | Nome esteso                                       | Range tipico |
|------------------------|---------------------------------------------------|--------------|
| γ<sub>G</sub>          | coefficiente azioni permanenti                    | 1.00 – 1.35  |
| γ<sub>Q</sub>          | coefficiente azioni variabili                     | 1.30 – 1.50  |
| γ<sub>E</sub>          | coefficiente azioni sismiche                       | 1.00         |
| γ<sub>φ'</sub>         | coefficiente parziale su tan φ'                   | 1.00 – 1.25  |
| γ<sub>c'</sub>         | coefficiente parziale su c'                       | 1.00 – 1.25  |
| γ<sub>γ</sub>          | coefficiente parziale sul peso volume             | 1.00         |
| γ<sub>R</sub>          | coefficiente sulla resistenza globale             | 1.00 – 1.20  |
| γ<sub>Ra,t</sub>       | coefficiente sulla resistenza tiranti             | 1.10 – 1.20  |
| ξ                      | coefficiente di correlazione Tab. 6.6.III         | 1.10 – 1.40  |
| η                      | tasso di lavoro dell'acciaio                      | 0.90 – 1.00  |

## Riferimenti normativi

| Sigla            | Documento                                                                |
|------------------|--------------------------------------------------------------------------|
| NTC 2018         | Decreto Ministeriale 17 gennaio 2018 — Norme Tecniche per le Costruzioni |
| Circolare 7/2019 | Istruzioni per l'applicazione delle NTC 2018                            |
| EC7              | EN 1997-1 Eurocodice 7: Progettazione geotecnica                         |
| EC8              | EN 1998-5 Eurocodice 8: Geotecnica sismica                              |

## Approcci di calcolo (RockPlane)

| Codice  | Nome                                                          |
|---------|---------------------------------------------------------------|
| 0       | Calcolo caratteristico (γ = 1.0)                              |
| 1       | NTC 2018 — A2+M2+R2 (Approccio 1 Combinazione 2)              |
| 2       | EC7 DA1 Comb. 1 — A1+M1+R1                                    |
| 3       | EC7 DA1 Comb. 2 — A2+M2+R2                                    |
| 4       | EC7 DA2 — A1+M1+R2                                            |
| 5       | EC7 DA3 — A2+M2+R3                                            |

## Termini tecnici

| Termine                  | Definizione                                                     |
|--------------------------|-----------------------------------------------------------------|
| **Daylighting**          | Condizione cinematica α < β: il piano di rottura emerge sul fronte |
| **Tension crack (TC)**    | Fessura di trazione subverticale alle spalle del cuneo          |
| **Bench**                | Piano sommitale orizzontale o inclinato dietro il ciglio        |
| **Pull-out**             | Prova di estrazione su tirante installato in opera              |
| **LEM**                  | Limit Equilibrium Method, metodo dell'equilibrio limite         |
| **Caging**               | Sistema a pannelli di funi che attraversa il piano di rottura   |
| **Soil nail / Rock nail** | Chiodo passivo cementato                                       |
| **SLU**                  | Stato Limite Ultimo                                              |
| **SLE**                  | Stato Limite di Esercizio (non considerato in RockPlane)        |
