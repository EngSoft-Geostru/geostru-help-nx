# Chiodi passivi

I **chiodi** (rock nails / soil nails) sono elementi di rinforzo **passivi**: non vengono pretensionati ma sviluppano la loro azione stabilizzante solo quando il cuneo prova a scivolare. RockPlane segue la formulazione **Variante A GeoStru SoilNail** secondo NTC 2018 §6.7 e prassi italiana (FHWA-NHI-09-035).

## Capacità del singolo chiodo

Il chiodo ha **3 limiti assiali** + **1 limite a taglio**:

| Limite                              | Simbolo  | Formula                                              |
|-------------------------------------|----------|------------------------------------------------------|
| Rottura dell'armatura               | T<sub>a1</sub> | η · f<sub>y</sub> · π·(D−4)² / 4                          |
| Aderenza barra ↔ malta              | T<sub>a2</sub> | β · √f<sub>ck</sub> · π · (D−4) · L<sub>mm</sub> · FS⁻¹     |
| Sfilamento foro (in roccia)         | T<sub>a3</sub> | π · D<sub>foro</sub> · L<sub>mm</sub> · τ<sub>ult</sub> · FS⁻¹  con τ<sub>ult</sub> = 0.1·σ<sub>c</sub> |
| Sfilamento foro (in terreno)        | T<sub>a3</sub> | (π·D·c' + 2·D<sub>foro</sub>·K<sub>α</sub>·σ<sub>v</sub>·tan φ) · L · FS⁻¹ |
| **Taglio della barra (Tresca)**     | T<sub>a4</sub> | 0.5 · f<sub>y</sub> · A<sub>net</sub>                       |

Capacità assiale: $T_{max} = \min(T_{a1}, T_{a2}, T_{a3})$. T<sub>a4</sub> entra separatamente nell'interazione N-V.

Per chiodi NTC §6.7 (Variante A) **non si applicano ξ né γ<sub>Ra,t</sub>**: la capacità di progetto = T<sub>max</sub> (eventualmente divisa per un FS locale aggiuntivo se il capitolato lo richiede).

## Parametri di input (catalogo tipologia)

### Geometria armatura

| Simbolo                | Significato                                   | Unità | Default |
|------------------------|-----------------------------------------------|-------|---------|
| D (φ arm)              | diametro barra                                | mm    | 32      |
| L (L efficace)         | lunghezza efficace del chiodo                 | m     | 8       |
| D<sub>foro</sub> (φ foro) | diametro del foro                          | mm    | 150     |

!!! note "Sezione netta D−4"
    Per chiodi filettati la sezione resistente è ridotta di ~4 mm (D<sub>net</sub> = D − 4). RockPlane lo applica automaticamente in Ta1 e Ta2.

### Acciaio e aderenza

| Simbolo            | Significato                                | Unità  | Default |
|--------------------|--------------------------------------------|--------|---------|
| f<sub>y</sub>      | resistenza armatura (yield)                | N/mm²  | 391     |
| f<sub>ck</sub> malta | resistenza cubica malta                  | N/mm²  | 32      |
| β barre            | coeff. aderenza barra (Geostru SoilNail)   | -      | 0.5 (ribbed) / 0.7 (autoperforante) |

η è forzato a 100% (yield pieno) per chiodi passivi.

### Ancoraggio

Toggle **"in roccia"** (default) vs **"in terreno"**.

In roccia:
- σ<sub>c</sub> resistenza a compressione monoassiale [MPa]

In terreno:
- γ<sub>terreno</sub>, φ<sub>terreno</sub>, c<sub>terreno</sub>, profondità media z<sub>med</sub>
- α<sub>rif</sub> (per K<sub>α</sub> Caquot)

## Interazione N-V (Clouterre 1993)

Quando il cuneo scivola, il chiodo subisce simultaneamente **trazione T** (lungo l'asse della barra) e **taglio V** (perpendicolare all'asse, attraverso il piano). Le due capacità interagiscono secondo il criterio di Clouterre **lineare**:

$$ \frac{T}{T_{max}} + \frac{V}{V_{max}} \leq 1 $$

con V<sub>max</sub> = 0.5·f<sub>y</sub>·A<sub>net</sub> (Tresca).

**Mobilizzazione ottima**: RockPlane calcola la modalità che massimizza il contributo a τ resistente del cuneo, considerando sia il contributo diretto lungo il piano (T·cos Φ + V·sin Φ) sia l'incremento di N che attiva attrito:

```
contrib_axial = T_max · (cos Φ + sin Φ · tan φ_des)
contrib_shear = V_max · (sin Φ − cos Φ · tan φ_des)
```

dove Φ = α + Δ è l'angolo bar-piano. Si sceglie il maggiore.

Per configurazioni tipiche (Φ moderato, V<sub>max</sub> ≈ 0.5·T<sub>max</sub>, tan φ moderato), **vince l'assiale** → comportamento identico al modello classico "solo trazione". Il taglio diventa governante solo per Φ → 90° (chiodo perpendicolare al piano).

## UI catalogo

Per ogni tipologia hai **due modalità**:

### Modalità manuale (footer ambra)

Inserisci direttamente F [kN], la capacità singola del chiodo. Utile per:
- Tipologie certificate da fornitore con scheda tecnica
- Casi sperimentali con prove di pull-out specifiche
- Pre-dimensionamento rapido

### Modalità NTC (footer verde)

Spunti **"Calcola Resistenza di progetto"**. Il software calcola tutto:
- T<sub>a1</sub>, T<sub>a2</sub>, T<sub>a3</sub> (assiali)
- T<sub>a4</sub> (taglio)
- min = governante
- R<sub>d</sub> = T<sub>min</sub> (per chiodi non si applica ξ né γ<sub>Ra,t</sub>)

Nel pannello destro **"Resistenze di progetto · chiodi / tiranti"** vedi il breakdown completo + le verifiche stile NTC R.2/R.3/R.4/R.5.

## Intervento posizionato

Per piazzare i chiodi sul cuneo, vai allo step "Interventi":

| Campo              | Significato                                                |
|--------------------|------------------------------------------------------------|
| Tipo               | Chiodo passivo                                             |
| Tipologia          | codice del catalogo                                        |
| Posizione (Y)      | quota verticale sul fronte [m]                             |
| Passo orizzontale  | interasse ⟂ alla sezione [m]                              |
| Inclinazione Δ     | sotto-orizzontale, verso la roccia [°]                    |
| Etichetta          | label visibile sul disegno                                 |

**Forza per metro** applicata = CapacitàSingola / PassoOrizzontale.

## Esempio numerico

| Parametro          | Valore        |
|--------------------|---------------|
| Tipo               | Barra φ32 B450C |
| D, L, D<sub>foro</sub> | 32mm · 8m · 150mm |
| f<sub>y</sub>, f<sub>ck</sub>, β | 391, 32, 0.5 |
| Ancoraggio in roccia, σ<sub>c</sub> = 30 MPa |              |
| Passo orizzontale  | 2.5 m         |

Risultati attesi:
- T<sub>a1</sub> ≈ 215 kN (sezione netta φ28)
- T<sub>a2</sub> ≈ 1990 kN (aderenza barra-malta, L=8m)
- T<sub>a3</sub> ≈ 1131 kN (sfilamento foro, τ<sub>ult</sub>=3 MPa)
- T<sub>a4</sub> ≈ 123 kN (taglio Tresca φ28)
- R<sub>d</sub> = min(215, 1990, 1131) = **215 kN** (limite armatura)
- Forza per metro = 215 / 2.5 = **86 kN/m**

## Riferimenti

- NTC 2018 §6.7 — Tiranti di ancoraggio e chiodi
- FHWA-NHI-09-035 — Soil Nail Walls Reference Manual
- Clouterre 1991/1993 — Recommandations pour le clouage des sols
- Bustamante-Doix 1985 — Calcul des tirants et des micropieux injectés
