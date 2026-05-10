# LiquiTer NX — Analisi della liquefazione

**LiquiTer NX** è il software web GeoStru per l'**analisi della liquefazione**
dei terreni saturi sotto sollecitazione sismica. Inserisci la stratigrafia,
i parametri sismici e scegli un metodo (Seed, Tokimatsu, Boulanger-Idriss,
Andrus-Stokoe) per ottenere il **fattore di sicurezza FSL** per ogni profondità,
l'indice del potenziale di liquefazione (IPL) e i cedimenti post-sismici.
Conforme NTC 2018 e Eurocodice 8.

[**Apri LiquiTer NX**](https://nx.geostru.ai/liquiter/){ .md-button .md-button--primary }
[Quickstart in 5 minuti](quickstart.md){ .md-button }

---

## Cosa fa, in sintesi

- **Input**: stratigrafia (γ, N-SPT, qc, frazione argillosa, Vs), parametri sismici
  (a_g, Mw), profondità falda, normativa (NTC 2018 / EC8).
- **Metodi di calcolo**: Seed (1971), Tokimatsu (1983), Boulanger-Idriss (2014),
  Andrus-Stokoe (Vs), Ishihara-Yoshimine (cedimenti post-sismici).
- **Output**: fattore di sicurezza FSL per profondità, indice IPL,
  cedimenti, report Word `.docx`, export CSV.

## Per chi

- **Geologi e ingegneri geotecnici** che valutano la suscettibilità di
  liquefazione di un sito in conformità NTC 2018 (cap. 7.11.3.4) o EC8 (EN 1998-5).
- **Studi di consulenza** che producono pareri tecnici per progettazione di
  fondazioni, opere di sostegno, edilizia in zona sismica.

## Come iniziare

1. Apri [`nx.geostru.ai/liquiter/`](https://nx.geostru.ai/liquiter/)
2. Carica un dataset di esempio o inserisci la stratigrafia
3. Imposta parametri sismici (a_g · Mw · normativa)
4. Scegli il metodo di calcolo
5. Premi **Esegui calcolo** → FSL per profondità + IPL + cedimenti
6. Esporta in Word / CSV

[Vedi il workflow completo →](workflow.md)

## Capitoli del manuale

### Iniziare

- [**Quickstart**](quickstart.md) — 5 minuti dal primo accesso al primo report
- [**Workflow completo**](workflow.md) — sequenza dettagliata input → calcolo → export

### Input

- [**Dati di input**](dati-input.md) — descrizione di ogni campo (sito, falda,
  sismica, stratigrafia)

### Calcolo

- [**Metodi di calcolo**](metodi.md) — Seed · Tokimatsu · Boulanger-Idriss ·
  Andrus-Stokoe · Ishihara-Yoshimine. Quando usare quale, formule, riferimenti.

### Output

- [**Esportazioni**](esportazioni.md) — Report Word, CSV, interpretazione FSL/IPL

### Riferimento

- [**FAQ**](faq.md) — domande frequenti

---

*Hai trovato un errore o vuoi suggerire un contenuto?
[Scrivici](mailto:info@geostru.ai?subject=Help%20LiquiTer%20NX) — grazie!*
