# Quickstart — il primo progetto in 5 minuti

Obiettivo: aprire l'app, valutare un caso di esempio, capire la lettura del fattore di sicurezza (FS).

## 1. Apri l'app

Vai su [nx.geostru.ai/rockplane](https://nx.geostru.ai/rockplane/). Il software è caricato con un set di **parametri di default** (un versante alto 30 m, β=60°, α=35°) che ti dà subito un cuneo visibile sulla destra.

## 2. Compila i Dati generali (opzionale per il quickstart)

In alto, clicca su **"Dati generali"** per espanderla. Inserisci:

- **Descrizione**: es. *"Versante SS-18 km 42"*
- **Lat / Lon**: lascia 41.9028 / 12.4964 (Roma) per ora
- **Sito**: località
- **Data**: oggi

Non serve nessun altro campo per fare il calcolo.

## 3. Modifica α per vedere FS cambiare

Nella card **Geometria del cuneo**, cambia `α · inclinaz. piano rottura` da 35° a 50°. Sul pannello destro vedrai **FS scendere** in tempo reale (debounce 150 ms). Il colore del numero:

- 🟢 **verde** quando FS ≥ 1.30 (criterio Tensioni Ammissibili)
- 🟡 **arancione** quando 1.0 ≤ FS < 1.30 (marginale)
- 🔴 **rosso** quando FS < 1.0 (instabile)

## 4. Clicca su "α crit" per trovare l'angolo critico

Accanto al campo α c'è il bottone **`α crit`**: clicca per fare uno **sweep** automatico dell'inclinazione α nel range cinematicamente ammissibile. Il software trova l'α che minimizza FS e lo imposta. Vedrai una banner blu con `α crit ≈ XX.X°  ·  FS_min = X.XXX  ·  range […°…°]`.

[Approfondisci →](alfa-critico.md)

## 5. Aggiungi un chiodo passivo

Vai allo **step 3 (Interventi)**:

1. Clicca **"+ aggiungi intervento"**
2. Tipo = **Chiodo passivo**, tipologia = **B** (Barra passiva cementata)
3. Posizione = 15 m (a metà altezza del fronte)
4. Passo orizzontale = 2.5 m
5. Inclinazione Δ = 15° (al ribasso, verso la roccia)

FS sale. Sotto, nel pannello destro, compare la scheda **"Resistenze di progetto · chiodi / tiranti"** con il breakdown completo della capacità del chiodo se hai attivato il calcolo NTC sulla tipologia.

## 6. Cambia normativa

In alto, nella card **Dati generali**, c'è il selettore **Normativa**. Prova le opzioni:

- **Calcolo caratteristico (γ = 1.0)** → vedi tutti i chip verdi (γ unitari, FS_req = 1.30)
- **NTC 2018 — A2+M2+R2** → vedi γ<sub>φ'</sub>=γ<sub>c'</sub>=1.25, γ<sub>R</sub>=1.10
- **EC7 DA2** → vedi γ<sub>G</sub>=1.35 (amplifica il peso)

L'FS si ricalcola con i nuovi coefficienti. La scheda **"γ applicati"** sotto al selettore mostra sempre i valori effettivi.

## 7. Esporta la relazione di calcolo

Menu **File → Esporta → Word**. Il software produce una relazione `.docx` completa di:

- Copertina e quadro normativo
- Dati di input
- Geometria risolta
- **Resistenze di progetto** dei chiodi/tiranti con breakdown e verifiche stile NTC
- Forze sul piano
- Esito con FS confrontato
- Annex A — Validazione del codice (97/97 test)
- Bibliografia

[Approfondisci la sezione Output →](export.md)

---

## Hai capito il flusso?

Bene! Ora vai al [workflow completo](workflow.md) per un caso realistico con acqua, sisma e una serie completa di interventi.
