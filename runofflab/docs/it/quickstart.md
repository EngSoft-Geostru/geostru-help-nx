# Quickstart — dalla serie pluviometrica all'idrogramma in 5 minuti

Questa guida mostra il flusso minimo per arrivare a un idrogramma di piena
partendo dai valori annui massimi delle piogge brevi.

!!! tip "Vuoi provare subito senza dati tuoi?"
    Apri il modale Info (icona **?** in alto) → tab **Risorse** → clicca su
    "**Cosenza — Metro_Cosenza**". Carica una stazione completa con serie reale
    di ~30 anni. Tutto il resto della guida funziona uguale.

## 1. Apri lo studio

1. Vai su [`nx.geostru.ai/runofflab/`](https://nx.geostru.ai/runofflab/).
2. Se è la prima volta, lo studio è vuoto. Trovi un'**anagrafica** della stazione
   (nome, codice, bacino, coordinate) e una lista di **durate** sotto.
3. La barra superiore mostra `*` accanto al nome quando ci sono modifiche
   non salvate, e `Modifiche non salvate` in piccolo subito sotto.

## 2. Inserisci la serie pluviometrica

Per ogni durata (60', 180', 360', 720', 1440') incolla la serie dei valori
**massimi annui** in millimetri.

- Una riga per anno. Decimali con punto o virgola.
- Servono **almeno 5 valori** perché un'elaborazione probabilistica abbia
  senso statistico; sotto 10-12 i risultati sono molto incerti.
- Le durate con meno di 2 valori vengono ignorate dalle elaborazioni.

!!! example "Esempio"
    Durata 60′ (1 ora), anni 1991-2020, Cosenza: 38.6, 41.2, 36.4, 52.1, …
    (un numero per riga).

Salva in `.hgstudy` con `File → Salva con nome` (o `Ctrl+Shift+S`). Il file è
un JSON portabile, condivisibile per email.

## 3. Calcola una elaborazione probabilistica

Vai nel pannello **Elaborazioni** → "**Aggiungi elaborazione**" → scegli una
famiglia. Per il primo studio, parti da:

- **Gumbel — Metodo dei momenti** (semplice, robusto, default in molti annuari
  italiani).

Il software calcola:

- parametri della distribuzione (\(\mu, \beta\) per Gumbel);
- altezze di pioggia \(h(T)\) per i tempi di ritorno standard (5, 10, 50, 100, 200 anni);
- test di adattamento (KS e χ²).

Per confrontare metodi, aggiungi anche una **GEV (L-moments)** o
**TCEV Livello 1** (se sei in Italia e c'è il dataset VA.PI. per la tua regione).

Vai a [Elaborazioni probabilistiche](elaborazioni.md) per il dettaglio dei metodi.

## 4. Costruisci la curva di pioggia

Pannello **Curve di pioggia** → "**Aggiungi curva**" → scegli l'elaborazione
sorgente e il tempo di ritorno (es. **T = 100 anni**).

Il software stima per regressione log-log i due parametri della legge

$$
h(t) = a \cdot t^{n}
$$

con \(t\) in ore e \(h\) in mm. Tipicamente per il Sud Italia \(n \approx 0.30\text{–}0.45\).

## 5. Pluviogramma sintetico

Dalla curva, costruisci uno **ietogramma di progetto** con il metodo Chicago:

- Pannello **Pluviogrammi sintetici** → "Aggiungi pluviogramma".
- Imposta **durata totale** (es. 60 min) e **posizione del picco** (\(r\),
  tipicamente 0.4).
- Ottieni la sequenza temporale di intensità \(i(t)\) — pioggia "in arrivo" sul bacino.

## 6. Idrogramma di piena con SCS-CN

Pannello **Idrogrammi** → "Aggiungi idrogramma". Inserisci:

- **Area del bacino** (km²);
- **Curve Number CN** (0-100, dipende da suolo e copertura);
- **Tempo di lag Tlag** (ore).

!!! tip "Wizard CN e Tlag"
    Non sai il CN giusto? Apri il **wizard CN** integrato (link nel pannello),
    inserisci tipo idrologico suolo e uso del suolo: il CN viene calcolato
    pesato sull'area.

Lo strumento applica il metodo SCS-CN (pioggia netta) e convolve con
l'idrogramma unitario adimensionale SCS, restituendo:

- volume e durata della pioggia netta;
- **portata al colmo \(Q_p\)** e tempo al picco;
- la curva \(Q(t)\) completa.

## 7. Esporta la relazione

`File → Esporta relazione PDF` produce un documento con:

- anagrafica stazione e serie;
- tabelle parametri di tutte le elaborazioni e h(T);
- grafici delle curve di pioggia;
- pluviogrammi e idrogrammi;
- metodo e formule per ciascuna sezione.

---

**Prossimi passi:**
[Workflow completo](workflow.md) · [Elaborazioni in dettaglio](elaborazioni.md) · [AI Import](ai-import.md)
