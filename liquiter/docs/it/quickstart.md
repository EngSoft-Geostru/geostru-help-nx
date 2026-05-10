# Quickstart — il tuo primo calcolo in 5 minuti

In 5 minuti vedi LiquiTer NX al lavoro su un dataset di esempio.

## 1. Apri l'app

Vai su [`nx.geostru.ai/liquiter/`](https://nx.geostru.ai/liquiter/).

## 2. Carica il dataset di esempio

Toolbar in alto → **File → Apri** → **"Dati di esempio"**.

LiquiTer carica subito una stratigrafia tipica (sabbia limosa satura su strato
ghiaioso) con parametri sismici realistici (zona 2 italiana).

## 3. Esamina i risultati

In pochi secondi LiquiTer:

- Calcola **CSR** (Cyclic Stress Ratio) e **CRR** (Cyclic Resistance Ratio)
  per ogni profondità
- Calcola il **fattore di sicurezza FSL = CRR / CSR** strato per strato
- Calcola l'**indice del potenziale di liquefazione IPL**
  ([Iwasaki et al. 1982](metodi.md#ipl-indice-del-potenziale-di-liquefazione))
- Stima i **cedimenti post-sismici** con Ishihara-Yoshimine

Vedi:

- **Tabella risultati**: per ogni passo di profondità mostra σ_v, σ'_v, r_d, CSR, CRR, FSL e
  l'esito (liquefacibile / non liquefacibile)
- **Grafico FSL vs z**: profilo verticale del fattore di sicurezza, con
  evidenziata la soglia FSL = 1
- **Banner IPL**: 0 (nessun rischio) — 5 (rischio basso) — 15 (medio) — >15 (alto)

## 4. Cambia metodo e confronta

In alto, sezione **Metodo di analisi**, prova:

- **Seed** (1971) — il classico, su SPT
- **Tokimatsu** (1983) — su SPT, distingue sabbie pulite/limose
- **Boulanger-Idriss** (2014) — su CPT (qc), il più recente
- **Andrus-Stokoe** — su Vs (velocità onde di taglio)

Ogni metodo restituisce un FSL leggermente diverso: confrontarli aiuta a
capire quanto è robusta la conclusione.

## 5. Esporta

Toolbar in alto → **Esporta**:

- **Report Word (.docx)** — relazione tecnica con tabelle, grafici, parametri
  e conclusioni
- **CSV** — dati grezzi (profondità, CSR, CRR, FSL) per analisi ulteriori in
  Excel/Python

---

## Prossimi passi

- [**Workflow completo**](workflow.md) — un progetto reale dall'inizio alla fine
- [**Metodi di calcolo**](metodi.md) — quando usare quale metodo, formule
- [**Dati di input**](dati-input.md) — descrizione completa di ogni campo

---

*Pagina utile? Hai dubbi? [Scrivici](mailto:info@geostru.ai?subject=Help%20LiquiTer%20NX%20-%20Quickstart).*
