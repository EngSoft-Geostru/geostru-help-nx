---
title: Pendio e substrato
---

# Pendio e substrato

SRS NX modella il pendio come una **coltre** (lo strato superficiale
potenzialmente instabile) appoggiata su un **substrato** (terreno o roccia)
in cui si ancorano i chiodi. Questa pagina spiega i parametri delle sezioni
**Pendio** e **Substrato** e come SRS li usa per calcolare il coefficiente di
sicurezza pre-intervento **FS₀**.

## Schema geometrico

Lo schema seguente riassume la geometria dei dati di input: pendio inclinato
di **α**, coltre di spessore **S** (misurato perpendicolarmente al pendio),
falda interna alla coltre (**S′ = m·S**), ancoraggio inclinato di **β**
sotto l'orizzontale con lunghezza totale **L_a = L_nc + L_b**, dove
**L_nc = S / sin(α+β)** è il tratto non collaborante nella coltre e **L_b**
il bulbo ancorato nel substrato.

<figure markdown="span">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400" font-family="sans-serif" font-size="13" role="img" aria-label="Schema geometrico sezione"><polygon points="97.9,364.1 450.1,117.4 480.1,147.4 480.1,394.0 97.9,394.0" fill="#cbbfa5" stroke="#43403a" stroke-width="1" fill-opacity="0.75"/><polygon points="60.0,310.0 412.2,63.4 450.1,117.4 97.9,364.1" fill="#e8dcc3" stroke="#43403a" stroke-width="1.4" fill-opacity="0.95"/><line x1="78.9" y1="337.0" x2="431.2" y2="90.4" stroke="#3c8dd6" stroke-width="1.6" stroke-dasharray="7 5"/><text x="143.9" y="309.9" fill="#3c8dd6" font-size="12" font-style="italic" font-weight="600" transform="rotate(-35.0 143.9 309.9)">S′ = m·S</text><line x1="353.7" y1="144.7" x2="334.7" y2="117.6" stroke="#8a5a00" stroke-width="1.1"/><polygon points="334.7,117.6 340.7,121.2 336.1,124.5" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><line x1="353.7" y1="144.7" x2="372.6" y2="171.7" stroke="#8a5a00" stroke-width="1.1"/><polygon points="372.6,171.7 366.6,168.1 371.3,164.8" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><text x="353.7" y="138.7" fill="#8a5a00" text-anchor="middle" font-size="12" font-weight="600" transform="rotate(55.0 353.7 144.7)">S</text><line x1="346.5" y1="219.4" x2="431.1" y2="250.2" stroke="#1e5fa8" stroke-width="7"/><line x1="243.2" y1="181.7" x2="431.1" y2="250.2" stroke="#1e5fa8" stroke-width="2.2"/><line x1="238.0" y1="174.4" x2="248.3" y2="189.1" stroke="#43403a" stroke-width="3.5"/><line x1="243.2" y1="181.7" x2="353.2" y2="181.7" stroke="#43403a" stroke-width="1" stroke-dasharray="4 3"/><path d="M 287.2 181.7 A 44 44 0 0 1 284.5 196.8" fill="none" stroke="#43403a" stroke-width="1.1"/><text x="297.2" y="175.7" fill="#43403a" font-size="13" font-style="italic" font-weight="600">β</text><line x1="288.7" y1="217.5" x2="237.0" y2="198.7" stroke="#8a5a00" stroke-width="1.1"/><polygon points="237.0,198.7 244.0,198.2 242.0,203.5" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><line x1="288.7" y1="217.5" x2="340.4" y2="236.3" stroke="#8a5a00" stroke-width="1.1"/><polygon points="340.4,236.3 333.4,236.8 335.3,231.4" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><text x="288.7" y="211.5" fill="#8a5a00" text-anchor="middle" font-size="12" font-weight="600" transform="rotate(20.0 288.7 217.5)">L<tspan font-size="9" dy="2">nc</tspan></text><line x1="382.7" y1="251.7" x2="340.4" y2="236.3" stroke="#8a5a00" stroke-width="1.1"/><polygon points="340.4,236.3 347.4,235.8 345.4,241.2" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><line x1="382.7" y1="251.7" x2="424.9" y2="267.1" stroke="#8a5a00" stroke-width="1.1"/><polygon points="424.9,267.1 418.0,267.6 419.9,262.2" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><text x="382.7" y="245.7" fill="#8a5a00" text-anchor="middle" font-size="12" font-weight="600" transform="rotate(20.0 382.7 251.7)">L<tspan font-size="9" dy="2">b</tspan></text><line x1="323.5" y1="253.5" x2="229.5" y2="219.3" stroke="#8a5a00" stroke-width="1.1"/><polygon points="229.5,219.3 236.5,218.8 234.5,224.2" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><line x1="323.5" y1="253.5" x2="417.4" y2="287.7" stroke="#8a5a00" stroke-width="1.1"/><polygon points="417.4,287.7 410.4,288.2 412.4,282.9" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><text x="323.5" y="247.5" fill="#8a5a00" text-anchor="middle" font-size="12" font-weight="600" transform="rotate(20.0 323.5 253.5)">L<tspan font-size="9" dy="2">a</tspan></text><line x1="177.6" y1="264.0" x2="177.6" y2="312.0" stroke="#43403a" stroke-width="1.8"/><polygon points="177.6,312.0 174.7,305.6 180.4,305.6" fill="#43403a" stroke="#43403a" stroke-width="1"/><text x="184.6" y="308.0" fill="#43403a" font-size="13" font-style="italic" font-weight="600">W</text><line x1="177.6" y1="268.0" x2="129.6" y2="268.0" stroke="#43403a" stroke-width="1.8"/><polygon points="129.6,268.0 135.9,265.1 135.9,270.8" fill="#43403a" stroke="#43403a" stroke-width="1"/><text x="91.6" y="262.0" fill="#43403a" font-size="13" font-style="italic" font-weight="600">k<tspan font-size="9" dy="2">h</tspan><tspan dy="-2">·W</tspan></text><line x1="60.0" y1="310.0" x2="156.0" y2="310.0" stroke="#43403a" stroke-width="1" stroke-dasharray="4 3"/><path d="M 128.0 310.0 A 68 68 0 0 0 115.7 271.0" fill="none" stroke="#43403a" stroke-width="1.1"/><text x="138.0" y="296.0" fill="#43403a" font-size="13" font-style="italic" font-weight="600">α</text></svg>
<figcaption>Sezione tipo: coltre, substrato, falda e ancoraggio.</figcaption>
</figure>

## Pendio (coltre)

| Simbolo | Parametro | Unità |
|---|---|---|
| I.1 α | Inclinazione del pendio | ° |
| I.2 S | Spessore della coltre | m |
| I.3 γ_col | Peso per unità di volume | kN/m³ |
| I.4 φ_col | Angolo d'attrito | ° |
| I.5 c'_col | Coesione drenata | kPa |
| I.6 m | Spessore adimensionalizzato del moto di filtrazione | — |

**m** rappresenta la posizione della falda all'interno della coltre: **m = 0**
significa falda assente, **m = 1** falda a piano campagna, valori intermedi
falda a profondità intermedia. Incide sulla sottospinta idraulica e riduce la
resistenza al taglio disponibile.

## Substrato

Scegli **Terreno** o **Roccia** con i due pulsanti radio: la card mostra i
campi pertinenti alla scelta.

### Terreno

| Simbolo | Parametro | Unità |
|---|---|---|
| I.8 ad_soil | Tensione di aderenza malta-terreno | MPa |
| I.9 α_iniez | Coefficiente di modalità di iniezione | — |

Il menu a tendina accanto a **ad_soil** propone valori tipici per litologia
(basalto, calcare, arenaria, dolomia, scisto, scisto alterato, gesso,
ardesia, oppure terreni sciolti come argille, sabbie e ghiaie), da usare come
riferimento e correggere in base ai dati di sito. Il coefficiente
**α_iniez** distingue iniezione ripetuta (valori più alti) da iniezione
semplice, per la stessa gamma di litologie sciolte.

### Roccia

| Simbolo | Parametro | Unità |
|---|---|---|
| I.10 ad_rock | Tensione di aderenza malta-roccia | MPa |

Stesso principio di preset per litologia della tensione di aderenza in
terreno.

!!! note "Valori indicativi, non sostituiscono l'indagine geognostica"
    I preset per litologia sono valori di riferimento tipici della
    letteratura tecnica. La tensione di aderenza malta-substrato da usare in
    progetto deve sempre essere confermata da prove di estrazione in sito o
    da indicazioni del produttore della malta e dell'ancoraggio.

## Come SRS calcola FS₀

Premendo **Calcola FS₀** (card **Parametri di Progetto**, passo 1), SRS
determina l'equilibrio del cuneo di coltre associato a un singolo ancoraggio,
di area in pianta pari all'interasse **i_x × i_y**:

1. **Volume agente** `V = i_x · i_y · S`
2. **Peso** `W = V · γ_col`
3. **Sottospinta idraulica** `U = 10 · m · V · cos(α)`
4. **Forza sismica orizzontale** `F_h = W · K_h` (0 se K_h = 0)
5. **Forza sismica verticale** `F_v = F_h / 2`
6. **Forza di taglio resistente** — dalla coesione e dall'attrito sulla
   superficie di scorrimento, al netto delle componenti sismiche
7. **Forza di taglio agente** — la componente del peso e delle forze sismiche
   lungo il pendio
8. **FS₀ = forza resistente / forza agente**

Se **FS₀** risulta negativo, il pendio è già instabile anche prima di
qualunque intervento: verifica i dati inseriti.

!!! warning "Aggiorna FS₀ dopo ogni modifica al pendio"
    FS₀ è calcolato una volta e resta memorizzato finché non lo ricalcoli. Se
    cambi inclinazione, spessore o parametri geotecnici della coltre dopo
    averlo determinato, premi di nuovo **Calcola FS₀** prima di lanciare la
    verifica completa.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20SRS%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/it/pendio.md).*
