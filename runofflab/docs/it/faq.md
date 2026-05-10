# FAQ — domande frequenti

## Generali

### Runoff Lab NX è gratuito?

Runoff Lab NX è incluso nella suite **GeoStru NX** con piano *freemium*.
Calcolo base e export CSV nel piano Free; report PDF e AI Import richiedono
Subscription. Per dettagli aggiornati visita
[`geostru.ai`](https://www.geostru.ai/).

### Devo installare qualcosa?

No — è una web app accessibile da
[`nx.geostru.ai/runofflab/`](https://nx.geostru.ai/runofflab/).

## Curve di pioggia

### Quale dei 4 metodi uso?

| Situazione | Metodo |
|---|---|
| Hai stazione pluviometrica vicina | **PLV da Hydrogeo NX** (più rigoroso) |
| Hai parametri IDF da letteratura | **IDF tradizionale** |
| Studio in zona VAPI nota | **VAPI** (rapido, standardizzato) |
| Studi specifici / sensibilità | **Custom** |

### Come converto da IDF a Curva 3-parametri?

La forma `i = a · d^(n-1)` ha **2 parametri** (a, n). La curva
*3-parametri* `h = a · d^n / (1 + d/c)^m` (CNR) ha 3 parametri ed è
usata in alcuni studi italiani classici. Runoff Lab supporta entrambe;
per la conversione la app fornisce il **fit numerico** automatico.

## Bacino

### Dove trovo il CN?

Tabelle SCS-CN sono integrate nel **wizard CN**. Selezioni:

1. **Tipo idrologico di suolo** (A/B/C/D) — da carta geologica
2. **Copertura** — da carta uso del suolo / Corine Land Cover

Output: **CN per condizione AMC II** (umidità media). Per AMC I (asciutto)
o AMC III (saturo) ci sono formule di correzione.

### Quale formula per il Tc?

In Italia:

- **Bacini < 1 km²**: Kirpich
- **Bacini 1-10 km²**: Pasini, Ventura
- **Bacini 10-1000 km²**: Giandotti

In dubbio, calcola con 2-3 formule diverse e media i risultati. Se il
range è ampio (es. Tc da 1h a 5h) il bacino ha caratteristiche
geometriche complesse — meglio una analisi 2D.

### L'AI Import ha capito male i parametri

Verifica sempre i parametri estratti — l'AI può sbagliare a leggere
unità di misura, virgole vs punti, o confondere parametri simili (Tc
vs Tlag). Modifica a mano dove serve.

## Trasformazione

### SCS-CN vs Cinematico — quando usare cosa?

- **Cinematico (Razionale)**: bacini piccoli (< 5 km²) urbani o
  semi-urbani con Tc breve (< 1 h). Il modello è semplice ma
  conservativo per il **dimensionamento di fognature**.
- **SCS-CN**: bacini medi (5-1000 km²) misti rurali/urbani. È lo
  **standard internazionale** ed è raccomandato dalla NTC per opere
  importanti.
- **Idrogramma unitario triangolare (Mockus)**: alternativa al SCS,
  più semplice ma meno accurata sulle code dell'idrogramma.

### Il Q_max che ho ottenuto è troppo basso

Cause comuni:

- **CN troppo basso** → poco runoff. Verifica la copertura del suolo.
- **Tlag troppo alto** → idrogramma più piatto e lungo. Verifica formula
  scelta.
- **Tempo di ritorno T sottostimato** — riguarda le NTC per la
  classificazione dell'opera.

## Esportazione

### Quale formato per la relazione tecnica?

PDF impaginato è il più diffuso per pareri tecnici. Excel se il
committente vuole un formato editabile. PLV se serve interscambio
con altri software.

## Manca la mia domanda

[Scrivici](mailto:info@geostru.ai?subject=Help%20Runoff%20Lab%20NX%20-%20FAQ)
e la aggiungiamo qui.
