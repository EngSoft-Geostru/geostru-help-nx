---
title: Pendio e substrato
---

# Pendio e substrato

SRS NX modella il pendio come una **coltre** (lo strato superficiale
potenzialmente instabile) appoggiata su un **substrato** (terreno o roccia)
in cui si ancorano i chiodi. Questa pagina spiega i parametri delle sezioni
**Pendio** e **Substrato** e come SRS li usa per calcolare il coefficiente di
sicurezza pre-intervento **FS₀**.

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
