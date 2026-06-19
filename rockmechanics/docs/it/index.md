# Rock Mechanics NX

> Elaborazione del **rilievo geostrutturale** di ammassi rocciosi eseguito in sito con bussola e clinometro secondo le raccomandazioni **ISRM** — classificazioni geomeccaniche, parametri caratteristici dell'ammasso e verifiche di stabilità per scivolamento planare e a cuneo.

[**Apri l'app**](https://nx.geostru.ai/rockmechanics/){ .md-button .md-button--primary }
[Guida rapida (5 minuti)](quickstart.md){ .md-button }

---

## In sintesi

- **Cosa fa**: rappresenta ed elabora il rilievo di discontinuità di un ammasso roccioso, esegue le principali **classificazioni geomeccaniche** (Barton, Bieniawski/Romana, Jašarević, Sen, Robertson, Singh & Goel), ne deriva i parametri caratteristici (coesione, angolo d'attrito, modulo di deformazione) e verifica la stabilità per i cinematismi di **scivolamento lungo un piano** e **a cuneo (Sliding 3D)**.
- **Per chi**: geologi e ingegneri geotecnici che caratterizzano un ammasso roccioso, classificano la qualità della roccia e producono la relazione geomeccanica.
- **In quanti minuti**: 5 (prima classificazione su un rilievo già pronto) → 45 (caso reale con più famiglie di giunti, classificazioni multiple e verifica di stabilità).

Il rilievo segue il procedimento descritto nelle raccomandazioni ISRM *"Suggested Methods for the Quantitative Description of Discontinuities in Rock Masses"*.

## Workflow tipico

1. Apri l'app: `nx.geostru.ai/rockmechanics/`
2. Inserisci i **dati del rilievo geostrutturale**: famiglie di discontinuità, giacitura (immersione/inclinazione), spaziatura, persistenza, apertura, rugosità, alterazione, riempimento, condizioni idrauliche.
3. Determina la **resistenza della roccia intatta** $S_u$ (Point Load, sclerometro o stima ISRM) e l'**RQD**.
4. Scegli una o più **classificazioni geomeccaniche**: l'app calcola l'indice di qualità e la classe dell'ammasso.
5. Leggi i **parametri caratteristici** derivati (coesione $c$, angolo d'attrito $\varphi$, modulo $E$, GSI).
6. Se serve, esegui la **verifica di stabilità** per scivolamento planare o a cuneo, con acqua, sisma e forze esterne.
7. Usa le **utility** per la forza d'impatto di un masso o la suscettibilità sismica al crollo.
8. Esporta la **relazione di calcolo** e gli elaborati grafici.

[Vedi il workflow completo →](workflow.md)

## Capitoli del manuale

### Per iniziare
- [Guida rapida](quickstart.md) — dalla giacitura dei giunti alla prima classificazione in 5 minuti
- [Workflow completo](workflow.md) — il rilievo ISRM e la sequenza input → calcolo → export

### Classificazioni geomeccaniche
- [Panoramica e parametri comuni](classificazioni.md) — $S_u$, RQD, spaziatura, $J_n/J_r/J_a/J_w$/SRF
- [Barton (indice Q)](barton.md) — sotterraneo e caratterizzazione generale
- [Bieniawski & Romana (RMR · SMR)](rmr-romana.md) — gallerie, fondazioni e versanti
- [Jašarević & Kovačević (indice n)](jasarevic.md) — ammassi carbonatici
- [RMR modificato (Sen)](sen.md) — formulazione continua semplificata
- [SRMR (Robertson)](robertson.md) — versanti in roccia tenera
- [Singh & Goel (indice N)](singh-goel.md) — gallerie, derivazione da Q

### Verifiche di stabilità
- [Scivolamento planare](scivolamento-planare.md) — equilibrio limite su un singolo piano
- [Sliding 3D](sliding-3d.md) — scivolamento di un cuneo tetraedrico

### Utility
- [Forza d'impatto · crollo sismico](utility.md) — Paronuzzi e Harp & Noble

### Output e reference
- [Esportazione e report](export.md) — relazione di calcolo ed elaborati
- [Formati file](formati.md) — progetto e dati di rilievo
- [Risorse](risorse.md) — figure e file di esempio scaricabili
- [Glossario](glossario.md) — simboli e terminologia geomeccanica
- [Bibliografia](bibliografia.md) — riferimenti scientifici
- [Geoapp](geoapp.md) — calcoli online complementari
- [FAQ](faq.md) — domande frequenti

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
