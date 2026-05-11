# GDW NX — Muri di sostegno in gabbioni

**GDW NX** è il software web per il **dimensionamento e la verifica geotecnica
di muri di sostegno in gabbioni** secondo NTC 2018. Configuri geometria, terreni
e carichi nel browser; ottieni in pochi clic spinta multistrato (Coulomb /
Mononobe-Okabe), verifiche esterne, verifiche interne fila per fila e analisi
di stabilità globale con metodo di Bishop semplificato.

[**Apri GDW NX**](https://nx.geostru.ai/gdw/){ .md-button .md-button--primary }
[Quickstart in 5 minuti](quickstart.md){ .md-button }

---

## Cosa fa, in sintesi

- **Input**: geometria del muro (n. file di gabbioni, blocchi per fila, spostamenti, inclinazione globale), fondazione (base, spessore valle, inclinazione β verso monte), stratigrafia multistrato, falda, sovraccarichi G/Q, sisma NTC 2018.
- **Calcolo**: spinta attiva multi-strato con Coulomb (statico) o Mononobe-Okabe (sismico), verifiche esterne ribaltamento/scorrimento/capacità portante, verifiche interne ad ogni giunto gabbione-gabbione, stabilità globale con Bishop semplificato su superficie circolare passante sotto il muro.
- **Output**: report Word `.docx`, disegni di sezione (con tensioni interne e diagramma pressioni), pannello debug calcoli, file progetto `.gabbioni`.

## Per chi

- **Ingegneri geotecnici** che dimensionano muri a gravità in gabbioni per regimazione idraulica, protezione versanti, sostegno stradale.
- **Studi di consulenza** che producono relazioni tecniche conformi NTC 2018.
- **Tecnici di cantiere** che vogliono verificare rapidamente l'adeguatezza di un'opera già posata.

## Come iniziare

1. Apri [`nx.geostru.ai/gdw/`](https://nx.geostru.ai/gdw/).
2. Imposta **Numero file** e blocchi per fila (es. 5-4-3-2-1 per un muro a piramide a destra).
3. Scegli **Allineamento** ("A destra" = paramento valle verticale, gradoni a monte).
4. In **Fondazione**: imposta `base`, `spessore valle h_v` e l'**inclinazione β** (0÷15°, verso monte, migliora resistenza allo scorrimento).
5. Compila **Geotecnica** con la stratigrafia (γ, φ, c) del terreno spingente e di fondazione.
6. **Calcola**. Leggi i 3 FS principali e le verifiche interne fila per fila.
7. **Report → Word** per la relazione tecnica.

[Vedi il workflow completo →](workflow.md)

## Capitoli del manuale

### Iniziare

- [**Quickstart**](quickstart.md) — 5 minuti dal primo accesso al primo report.
- [**Workflow completo**](workflow.md) — sequenza dettagliata input → calcolo → export.

### Geometria

- [**Muro e gabbioni**](geometria.md) — file, blocchi, spostamenti, allineamento, prima fila interrata.
- [**Inclinazione del muro**](inclinazione-muro.md) — muro battuto verso monte (α 0÷15°): cosa cambia su Ka di Coulomb e direzione spinta.
- [**Fondazione**](fondazione.md) — base, spessore valle, **inclinazione β** della faccia inferiore per migliorare scorrimento.

### Materiali

- [**Rete metallica**](rete.md) — rete a **doppia torsione Maccaferri** (catalogo: 6×8, 8×10, con/senza PVC) vs rete elettrosaldata; verifiche diverse, σ_adm di Gawac, coesione apparente c_g del gabbione.
- [**Stratigrafia e terreni**](geotecnica.md) — strati multipli, terreno di fondazione, falda, interfaccia base.

### Carichi

- [**Sovraccarichi e spinta**](sovraccarichi.md) — sovraccarichi permanenti G e variabili Q sul terrapieno; coefficiente Ψ₂ in combinazione sismica.
- [**Sisma**](sisma.md) — combinazione sismica NTC, k_h/k_v, Mononobe-Okabe automatico, R_rib amplificato.
- [**Coefficienti parziali**](coefficienti.md) — A1·M1·R3 (statico) e A2·M2·R3 (sismico), tabelle e default.

### Verifiche

- [**Esterne**](verifiche.md) — ribaltamento, scorrimento (con base inclinata β), capacità portante (Brinch-Hansen).
- [**Interne fila per fila**](verifiche-interne.md) — σ_max ≤ σ_adm Maccaferri Gawac per rete DT, scorrimento e ribaltamento ad ogni giunto.
- [**Stabilità globale**](bishop.md) — Bishop semplificato, 3 punti del cerchio editabili, validazione del cerchio sotto fondazione.

### Riferimento

- [**Report e disegni**](report.md) — Word `.docx`, sezione SkiaSharp, debug log.
- [**Glossario**](glossario.md) — definizioni dei termini chiave (Ka, δ, β, α, γ_R, ecc.).
- [**Formati file**](formati.md) — il file `.gabbioni` (testo a sezioni, backward-compatible).
- [**FAQ**](faq.md)

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GDW%20NX) — grazie!*
