# Workflow completo

Sequenza di un'analisi tipica in Runoff Lab NX, partendo da una serie pluviometrica
e arrivando all'idrogramma di piena per una sezione di bacino.

## Schema

```
┌────────────────────┐
│ Stazione + serie   │  serie annuali h_max per 60′, 3h, 6h, 12h, 24h
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ Elaborazione       │  Gumbel / GEV / Pearson III / TCEV
│ probabilistica     │  → h(T) per T = 5, 10, 50, 100, 200 anni
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ Curva di pioggia   │  fit log-log:  h = a · t^n  per T fissato
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ Pluviogramma       │  ietogramma sintetico (Chicago design storm)
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ Idrogramma SCS-CN  │  CN, Tlag, area → Q(t), Q_peak
└────────────────────┘
```

Ognuno dei pannelli laterali corrisponde a un riquadro qui sopra.
I dati fluiscono verso il basso: cambia una serie, ricalcola sopra,
le elaborazioni e tutto il resto a valle si rigenerano.

---

## 1. Stazione e serie

Nel pannello **Stazione** inserisci:

- **Anagrafica**: nome, codice, bacino di appartenenza, comune/provincia/regione.
- **Coordinate**: latitudine/longitudine + altitudine. Servono solo per
  documentare nella relazione finale.
- **Periodo di osservazione**: anni di inizio e fine della serie storica.
- **Strumento**: tipologia (pluviometro registratore, ecc.).

In basso, per ogni **durata** (60′, 3h, 6h, 12h, 24h, o personalizzate)
incolli i valori massimi annui in mm. Suggerimenti pratici:

- copia dalla colonna Excel e incolla nella casella: il parser separa
  ogni riga in un valore;
- supporta `.` e `,` come separatore decimale;
- una durata con meno di 2 valori non viene usata in elaborazione e
  appare con badge "ignorata".

## 2. Elaborazioni probabilistiche

Dal pannello **Elaborazioni** clicca *Aggiungi* → scegli una famiglia.
Le 4 famiglie disponibili:

| Famiglia | Metodo | Quando usarla |
|----------|--------|---------------|
| **Gumbel** | Momenti, Massima Verosimiglianza | Default in molti annuari italiani; semplice e ben validato per valori estremi. |
| **GEV** | L-moments (Hosking) | Più flessibile di Gumbel; copre code pesanti (eventi catastrofici). |
| **Pearson III** | Momenti (Foster/Kite) | Tradizione anglosassone; utile per serie con asimmetria marcata. |
| **TCEV** | Livelli 0-3, regionalizzato VA.PI. | Italia; il livello 3 sfrutta tutta la regionalizzazione VA.PI. |

Per ogni elaborazione il software calcola:

- parametri della distribuzione;
- altezze \(h(T)\) per T standard;
- test di adattamento KS e χ²;
- grafico **Quantile-Quantile** osservato vs teorico.

[Dettaglio matematico →](elaborazioni.md)

!!! note "Confronto fra metodi"
    Aggiungi più elaborazioni alla stessa stazione. La tabella di output
    affianca i valori h(T) per ciascun metodo: confronti immediati,
    discrimini visivamente l'incertezza.

## 3. Curve di pioggia

Dal pannello **Curve** → *Aggiungi*. Seleziona:

- l'**elaborazione** sorgente (es. *Gumbel-momenti — 60′/3h/6h/12h/24h*);
- il **tempo di ritorno** (T = 5, 10, 50, 100, 200 anni o custom).

Il fitting log-log restituisce:

$$
h(t) = a \cdot t^n
\qquad
i(t) = a \cdot t^{n-1}
$$

con \(t\) in ore. La pagina mostra la curva sovrapposta ai punti
osservati \((d_i, h(d_i, T))\) per occhio.

[Dettagli →](curve.md)

## 4. Pluviogrammi sintetici

Dal pannello **Pluviogrammi** → *Aggiungi*. Seleziona:

- la **curva** sorgente;
- la **durata totale** dell'evento (es. 60, 120, 360 min);
- la **posizione del picco** \(r \in [0, 1]\) (Chicago design storm).

Esce un ietogramma rettangolare con risoluzione configurabile (default 1 min).

[Dettagli →](pluviogrammi.md)

## 5. Idrogrammi SCS-CN

Dal pannello **Idrogrammi** → *Aggiungi*. Inserisci:

- **Pluviogramma** o curva di partenza;
- **Area del bacino** (km²);
- **Curve Number CN** (0–100);
- **Tempo di lag Tlag** (ore).

L'algoritmo:

1. calcola le **perdite iniziali** \(I_a = 0.2 S\) (con \(S = 25400/\text{CN} - 254\));
2. ottiene la **pioggia netta** \(P_e = (P - I_a)^2 / (P - I_a + S)\) per ogni intervallo;
3. convolve la sequenza con l'**idrogramma unitario SCS** adimensionale (forma a triangolo, picco a 0.375 Tp);
4. somma → idrogramma totale \(Q(t)\) con portata al colmo \(Q_p\) e tempo al picco.

[Dettagli + wizard CN/Tlag →](scs-cn.md)

## 6. Export

`File → Esporta relazione PDF`: una sola relazione con tutto:

- anagrafica e serie;
- per ogni elaborazione: parametri, h(T), test;
- per ogni curva: \(a\), \(n\), \(R^2\);
- pluviogrammi e idrogrammi con grafico;
- metodologia e fonti bibliografiche standard;
- copertina con logo e dati progetto.

## Salvataggio e ripristino

- `Ctrl+S` → salva nel browser (autosave attivo in continuazione).
- `Ctrl+Shift+S` → scarica un file `.hgstudy` (JSON portabile).
- `Ctrl+O` → apri un `.hgstudy` salvato in precedenza.
- Se chiudi il tab con modifiche non salvate, il browser mostra il prompt
  nativo "Vuoi davvero uscire?"; in più la sessione resta in localStorage
  e viene riproposta alla prossima apertura.
