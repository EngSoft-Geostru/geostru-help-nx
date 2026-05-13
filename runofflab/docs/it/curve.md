# Curve di pioggia

Una **curva di pioggia** (o curva IDF — Intensity-Duration-Frequency) lega
l'altezza di pioggia attesa \(h\) a una durata \(t\), per un fissato tempo di
ritorno \(T\):

$$
h(t, T) = a(T) \cdot t^{\, n(T)}
\qquad
i(t, T) = a(T) \cdot t^{\, n(T) - 1}
$$

con:

- \(h\) in mm, \(i\) in mm/h, \(t\) in ore;
- \(a(T)\) e \(n(T)\) ricavati per fit log-log dai valori \(h(t_i, T)\)
  forniti dalle elaborazioni probabilistiche.

## Come la calcola Runoff Lab

1. Nel pannello **Curve** → *Aggiungi* selezioni:
   - **Elaborazione sorgente** (es. Gumbel-momenti);
   - **Tempo di ritorno** (5, 10, 50, 100, 200 anni o custom).
2. Per ciascuna durata della stazione viene preso il valore \(h(t_i, T)\) dalla
   distribuzione adattata.
3. Si applica la regressione lineare in log-log fra \(\ln h\) e \(\ln t\):

$$
\ln h = \ln a + n \cdot \ln t
$$

   ricavando \(a\) e \(n\).
4. Il pannello mostra:
   - \(a\), \(n\), coefficiente di determinazione \(R^2\);
   - tabella valori osservati vs valori della curva;
   - grafico log-log con punti e retta.

## Interpretazione di \(a\) e \(n\)

- \(\boldsymbol{a}\) = altezza di pioggia per **\(t = 1\) ora** (per quel \(T\)).
  Più grande in zone climatiche piovose o per T alti.
- \(\boldsymbol{n}\) = esponente della legge, sempre in \([0, 1]\).
  Tipicamente:
  - \(n \approx 0.20\text{–}0.30\) per piogge molto convettive (brevi e intense);
  - \(n \approx 0.40\text{–}0.55\) per piogge frontali persistenti.

Bassi \(n\) → la pioggia "si concentra" nelle durate brevi → bacini piccoli
soggetti a piene rapide.

## Più tempi di ritorno

Crea una curva per ciascun \(T\) che ti interessa: tipicamente 5, 50, 200 anni
per opere idrauliche. Confronta su un unico grafico le curve sovrapposte per
mostrare il "fattore di crescita" tra fasi di ritorno.

!!! tip
    Conservare in studio almeno le curve per T = 50 e T = 200 è quasi sempre
    richiesto da una relazione idrologica per opere pubbliche.

## Quando il fit log-log non basta

Se \(R^2 < 0.95\) la legge a 2 parametri non rappresenta bene la stazione.
Cause tipiche:

- **Discontinuità nella serie** (pluviometro spostato, periodo storico vs
  recente). Splittare la serie e rifare l'elaborazione su sotto-periodi.
- **Effetto di scala**: per stazioni a quota molto alta o vicinissime al mare,
  la singola legge a 2 parametri può fallire. Usa modelli a 3 parametri
  (TCEV livello 3) che vincolano meglio la coda.

## Esportazione

Ogni curva entra automaticamente nella relazione PDF con:

- parametri \(a\), \(n\), \(R^2\);
- tabella punti osservati vs predetti;
- grafico h-t (log-log) e i-t (lin-lin) per il T scelto;
- formula con i valori numerici sostituiti.
