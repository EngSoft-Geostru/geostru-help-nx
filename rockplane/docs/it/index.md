# RockPlane NX

> Verifica di stabilità di pendii rocciosi soggetti a **meccanismo di rottura planare** — singola discontinuità persistente con daylighting (Hoek-Bray / RocPlane).

[**Apri l'app**](https://nx.geostru.ai/rockplane/){ .md-button .md-button--primary }
[Quickstart in 5 minuti](quickstart.md){ .md-button }

---

## In sintesi

- **Cosa fa**: verifica all'equilibrio limite (LEM) di un cuneo planare in roccia, con calcolo automatico della resistenza di progetto NTC §6.6 dei tiranti, §6.7 dei chiodi (Variante A SoilNail), criterio di Clouterre per l'interazione N-V su chiodi passivi, reti corticali R1 e pannelli a fune R2.
- **Per chi**: geologi e ingegneri progettisti che devono validare la sicurezza di un fronte roccioso a rottura planare, dimensionare un intervento di consolidamento (chiodatura + rete) e produrre la relazione di calcolo conforme NTC 2018 / Eurocodice 7.
- **In quanti minuti**: 5 (caso da esempio) → 30 (caso reale con interventi).

## Workflow tipico

1. Apri l'app: `nx.geostru.ai/rockplane/`
2. Compila i **Dati generali** (Descrizione, Lat/Lon, Data, Sito).
3. Inserisci la **geometria del cuneo**: H, β, α, ψ, B; eventuale tension crack T/θ.
4. Inserisci il **materiale**: γ, c, φ (Mohr-Coulomb sul piano).
5. Inserisci le **azioni** opzionali: acqua (Hw/Zw/Zt), sisma kh/Ω, forza esterna E/δ.
6. Aggiungi **interventi** dal catalogo: chiodi/tiranti con dimensionamento NTC, reti R1/R2.
7. Scegli l'**approccio normativo**: Caratteristico (γ=1) · NTC 2018 (A2+M2+R2) · EC7 (DA1/DA2/DA3).
8. Leggi il **FS** in alto e le **verifiche** (R<sub>i</sub> ≥ E<sub>d</sub>) per ogni elemento.
9. Esporta la **relazione Word** e/o il **DXF** della sezione.

[Vedi il workflow completo →](workflow.md)

## Capitoli del manuale

### Input del modello
- [Geometria del cuneo](geometria.md) — H, β, α, ψ, B, fessura di trazione
- [Materiale](materiale.md) — peso volume γ, coesione c, angolo d'attrito φ
- [Acque](acque.md) — Hw esterna ponded, Zw nella discontinuità, Zt nella fessura
- [Sisma pseudostatico](sisma.md) — kh, kv, direzione Ω
- [Forza esterna E](forze-esterne.md) — modulo, inclinazione δ, tipo carico G/Q

### Interventi
- [Chiodi passivi](chiodi.md) — NTC §6.7, Variante A SoilNail, Clouterre N-V
- [Tiranti attivi](tiranti.md) — NTC §6.6, ξ Tab. 6.6.III, γ<sub>Ra,t</sub>
- [Reti](reti.md) — R1 corticale (pressione normale), R2 caging (τ resistente)

### Calcolo
- [Modello teorico](modello-teorico.md) — equazioni Hoek-Bray (1)–(30)
- [Approccio normativo](verifica.md) — coefficienti TA · NTC · EC7
- [α critico](alfa-critico.md) — sweep dell'inclinazione del piano

### Output
- [Esportazione Word/DXF](export.md) — relazione di calcolo completa
- [Formati file](formati.md) — `.rockplane` (JSON)

### Reference
- [Risorse](risorse.md) — file di esempio scaricabili
- [Glossario](glossario.md) — simboli, terminologia
- [FAQ](faq.md) — domande frequenti

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20RockPlane%20NX).*
