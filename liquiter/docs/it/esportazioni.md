# Esportazioni — Word, CSV

A fine analisi LiquiTer NX produce 2 output, accessibili dalla toolbar:

## Report Word (.docx)

Il **Report Word** è una relazione tecnica pre-impaginata, conforme alle
indicazioni della NTC 2018 cap. 7.11.3.4.

### Cosa contiene

1. **Frontespizio** con: titolo, descrizione, sito, operatore, data, mappa GPS
2. **Riepilogo dati di input**:
   - Tabella della stratigrafia (γ, N-SPT, qc, Vs, % argilla)
   - Parametri sismici (a_g, Mw, normativa, categoria suolo, S_S, S_T)
   - Profondità falda
3. **Metodologia di calcolo**:
   - Riferimento normativo
   - Metodo selezionato + formule
   - Valori dei coefficienti correttivi (r_d, MSF, K_σ)
4. **Risultati**:
   - Tabella per profondità (z, σ_v, σ'_v, CSR, CRR, FSL, esito)
   - Grafico FSL vs z
   - IPL e classificazione del rischio
   - Cedimenti per strato + cedimento totale
5. **Conclusioni**:
   - Sintesi suscettibilità del sito
   - Eventuali raccomandazioni (mitigazione, approfondimenti)

### Apertura

Compatibile con:

- **Microsoft Word** 2016+
- **LibreOffice Writer** 6+
- **Google Docs** (caricato su Drive)
- **Pages** (macOS)

I grafici sono PNG embedded a 300 DPI.

### Personalizzare il template

Se serve un layout aziendale custom (logo studio, font specifici), contatta
[info@geostru.ai](mailto:info@geostru.ai) — possiamo configurare un template
dedicato per il tuo studio.

## CSV — dati grezzi

Esportazione tabellare in CSV (encoding UTF-8 BOM, separatore virgola)
compatibile Excel / LibreOffice / Google Sheets / Python.

### Colonne incluse

```
z, sigma_v, sigma_v_eff, r_d, CSR, CRR, FSL, MSF, K_sigma, esito, IPL_contrib, settlement_cm
```

### Quando ha senso

- **Analisi di sensibilità** — esportare CSV con i risultati di Seed,
  Tokimatsu, Boulanger e fare grafici comparativi in Excel
- **Combinare con altri rilievi** — confronto liquefazione su più siti
- **Re-calcolo custom** in Python (per esempio: calcolo cedimenti con
  metodi alternativi tipo Cetin)
- **Archiviazione long-term** in formato leggibile a vita

---

## Interpretazione FSL e IPL

Il valore di FSL e IPL **non è una sentenza**: vanno letti con criterio.

### FSL — fattore di sicurezza per profondità

| FSL | Significato | Azione |
|---|---|---|
| > 1.5 | Stabile con margine | Nessuna |
| 1.25 – 1.5 | Stabile (margine NTC) | Nessuna |
| 1.0 – 1.25 | Vicino al limite | Approfondisci, considera mitigazione |
| < 1.0 | Liquefacibile | Mitigazione necessaria |

### IPL — indice complessivo del sito

Iwasaki et al. (1982):

| IPL | Rischio | Tipica decisione |
|---|---|---|
| 0 | Trascurabile | Costruzioni standard |
| 0–5 | Basso | Costruzioni standard, attenzione fondazioni |
| 5–15 | Medio | Mitigazione consigliata o platea rigida |
| > 15 | Alto | Mitigazione obbligatoria (jet grouting, drenaggi, palificate) |

!!! warning "Decisione finale al professionista"
    LiquiTer produce **input geometrico-statistico** per la perizia. La
    decisione finale (sito ok / mitigazione necessaria / quale tipo di
    mitigazione) è dell'ingegnere/geologo che firma il progetto. La
    suscettibilità di liquefazione si combina con valutazioni di rischio
    sismico, classe di vita nominale dell'opera, criticità delle fondazioni.

---

## Vedi anche

- [Workflow completo](workflow.md) — l'esportazione nel ciclo intero
- [Metodi di calcolo](metodi.md) — interpretazione di FSL e IPL
- [FAQ](faq.md) — domande sulle esportazioni

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20LiquiTer%20NX%20-%20Esportazioni).*
