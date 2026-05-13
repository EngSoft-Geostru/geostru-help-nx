# Elaborazioni probabilistiche

Le elaborazioni stimano i parametri di una distribuzione di probabilità che
descrive il regime delle piogge intense, e da quella estraggono le altezze
attese per assegnati tempi di ritorno \(T\).

Tutte assumono che i **massimi annui** per durata fissata siano realizzazioni
indipendenti di una stessa variabile aleatoria.

## Gumbel (EV1)

La distribuzione di Gumbel a 2 parametri descrive i massimi di campioni grandi:

\[
F(h) = \exp\!\left[-\exp\!\left(-\frac{h - \mu}{\beta}\right)\right]
\qquad
h(T) = \mu - \beta \ln\!\left[-\ln\!\left(1 - \frac{1}{T}\right)\right]
\]

Due stimatori disponibili:

- **Metodo dei momenti**. Veloce, robusto.
  \(\beta = s \sqrt{6}/\pi\), \(\mu = \bar{h} - \gamma\,\beta\) (\(\gamma \approx 0.5772\) costante di Eulero-Mascheroni).
- **Massima Verosimiglianza (ML)**. Iterativo, leggermente più efficiente.

## GEV — Generalized Extreme Value (L-moments)

Famiglia che generalizza Gumbel: include una **shape \(\kappa\)** che permette
code pesanti (\(\kappa > 0\)) o limitate (\(\kappa < 0\)).

\[
F(h) = \exp\!\left[-\left(1 - \kappa\,\frac{h - \xi}{\alpha}\right)^{1/\kappa}\right]
\]

I tre parametri \((\xi, \alpha, \kappa)\) sono stimati con i **L-moments**
(Hosking 1990) — più robusti dei momenti classici per campioni piccoli.

Le altezze h(T):

\[
h(T) = \xi + \frac{\alpha}{\kappa}\!\left[1 - \left(-\ln(1 - 1/T)\right)^{\kappa}\right]
\]

!!! tip "Quando GEV vs Gumbel?"
    GEV è da preferire se la serie ha pochi anni e valori estremi anomali.
    Per serie >50 anni e niente "code lunghe", Gumbel è di solito sufficiente
    e più semplice da giustificare in relazione.

## Pearson III (metodo dei momenti — Foster/Kite)

Distribuzione a 3 parametri (\(\bar{h}, s, C_s\) = media, deviazione, asimmetria)
storicamente popolare nel mondo anglosassone:

\[
h(T) = \bar{h} + K_T(C_s) \cdot s
\]

con \(K_T\) frequency factor tabulato (formula di Wilson-Hilferty per
calcolarlo analiticamente).

Utile quando la serie ha asimmetria marcata e Gumbel sottostima la coda.

## TCEV — Two-Component Extreme Value (VA.PI. — Italia)

Modello regionale per il territorio italiano basato sul programma **VA.PI.**
(Valutazione delle Piene in Italia, CNR-GNDCI). Distingue **eventi ordinari** e
**eventi straordinari** ammettendo due componenti EV1 sovrapposte.

\[
F(h) = \exp\!\left[-\Lambda_1 e^{-h/\theta_1} - \Lambda_2 e^{-h/\theta_2}\right]
\]

I 4 parametri \((\Lambda_1, \theta_1, \Lambda_2, \theta_2)\) sono difficili da
stimare puntualmente: Runoff Lab NX implementa i **4 livelli** di
regionalizzazione classici:

| Livello | Cosa fissa | Cosa stima |
|---------|------------|------------|
| **0 — puntuale** | nessun parametro regionale | tutti e 4 dalla stazione (poco affidabile sotto 30 anni) |
| **1 — regionale** | \(\Lambda^* = \Lambda_2/\Lambda_1\), \(\Theta^* = \theta_2/\theta_1\) | gli altri 2 dalla stazione |
| **2** | come 1 + \(\Lambda_1\) | resta solo \(\theta_1\) |
| **3** | tutti i parametri di forma regionali; \(\theta_1\) da scala | adimensionale + scala locale |

Il dataset VA.PI. è caricato per le regioni italiane note. Per regioni o paesi
non coperti l'opzione TCEV non è disponibile (il pannello la nasconde quando
la lingua dell'interfaccia è diversa dall'italiano).

!!! note "Quando TCEV ha senso"
    TCEV cattura bene la coda alta degli eventi catastrofici tipici del clima
    italiano (alluvioni convettive su bacini piccoli). È il modello consigliato
    da molte autorità di bacino per Vigilanza idraulica e PAI.

## Test di adattamento

Per ogni elaborazione il software calcola due test:

- **Kolmogorov-Smirnov** (KS): massima distanza fra CDF empirica e teorica.
  Confronto col valore critico al 5%.
- **Pearson χ²**: confronto su classi di frequenza.

Entrambi sono **non rigetto al 5%** se il p-value > 0.05. Una sola distribuzione
che passa entrambi è preferibile a due che ne falliscono uno.

## Bibliografia di riferimento

- Gumbel E.J. (1958), *Statistics of Extremes*, Columbia University Press.
- Hosking J.R.M. (1990), *L-moments: analysis and estimation of distributions
  using linear combinations of order statistics*, J. Royal Stat. Soc. B 52.
- Kite G.W. (1977), *Frequency and Risk Analyses in Hydrology*, Water Resources Publ.
- Rossi F., Versace P. (1982), *Criteri e metodi per l'analisi statistica delle
  piene*, CNR-PFC, Italia.
- Programma VA.PI. — CNR-GNDCI, *Valutazione delle Piene in Italia*, rapporti regionali.
