# Pluviogrammi sintetici (Chicago design storm)

Un **pluviogramma sintetico** è la distribuzione temporale dell'altezza di
pioggia all'interno di un evento di progetto. Mentre la curva IDF dice solo
*quanto* pioveva in un certo intervallo, il pluviogramma dice *come* si
distribuiva nel tempo: questa è l'informazione che serve per applicare la
trasformazione afflusso-deflusso.

Runoff Lab NX usa il **Chicago Design Storm** (Keifer & Chu, 1957), il
metodo standard per costruire ietogrammi sintetici partendo da una curva IDF.

## Idea del metodo

L'intensità istantanea ai due lati del picco si ricava direttamente
dall'inversione della curva IDF:

$$
i(t_b) = a \cdot \left(\frac{t_b}{r}\right)^{\!n-1}
\qquad
i(t_a) = a \cdot \left(\frac{t_a}{1-r}\right)^{\!n-1}
$$

con:

- \(r\) posizione del picco (\(r = 0.4\) tipico);
- \(t_b\) tempo prima del picco;
- \(t_a\) tempo dopo il picco;
- \(a\), \(n\) parametri della curva di partenza.

Risultato: una sequenza di intensità centrata sul picco, decrescente in
modo asimmetrico verso testa e coda.

## Come si costruisce in Runoff Lab

1. Vai nel pannello **Pluviogrammi sintetici** → *Aggiungi*.
2. Imposta:
   - **Curva sorgente** (es. Gumbel — T=100 anni);
   - **Durata totale** \(D\) dell'evento in minuti (60, 120, 360, …);
   - **Posizione del picco** \(r\) in \([0, 1]\);
   - **Passo temporale** \(\Delta t\) (1, 5, 10 min — default 1 min).
3. Conferma → il grafico mostra l'ietogramma a barre, la tabella i valori
   \(\big(t_i, i(t_i)\big)\).

## Scelta di \(r\)

| \(r\) | Interpretazione |
|------|-----------------|
| **0.0** | Picco all'inizio — pioggia decrescente. Bacini urbani saturi. |
| **0.3** | Picco anticipato. |
| **0.4** (default) | Compromesso adottato nelle linee guida italiane (PAI, autorità di bacino). |
| **0.5** | Simmetrico — sovrastima la portata al colmo su bacini ordinari. |
| **1.0** | Picco alla fine — pioggia crescente. |

## Quando usarlo

Il pluviogramma sintetico serve per:

- alimentare il **modello afflusso-deflusso** (vedi [Idrogrammi SCS-CN](scs-cn.md));
- documentare l'ietogramma di progetto nelle relazioni idrauliche;
- testare la sensibilità dell'opera a diversi scenari (\(D\), \(r\)).

!!! note "Pluviogrammi alternativi"
    Il metodo Chicago è uno standard ma esistono alternative (Huff,
    Sifalda, blocchi alternati). Runoff Lab NX al momento implementa solo
    Chicago; per quasi tutti gli usi pratici è sufficiente.

## Bibliografia

- Keifer C.J., Chu H.H. (1957), *Synthetic Storm Pattern for Drainage Design*,
  ASCE Hydraulic Division 83.
- Watt W.E., Chow K.C.A. (1985), *A general expression for basin lag time*,
  Canadian Journal of Civil Engineering 12(2).
