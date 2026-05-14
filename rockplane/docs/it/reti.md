# Reti

RockPlane modella due tipologie di reti, con meccanismi di resistenza **distinti**:

## R1 · Rete corticale aderente

"Buccia" di rete tesa contro il fronte del versante, fissata da chiodi corti. Modello: pressione normale uniforme `q` [kN/m²] applicata sul fronte.

**Effetto sul cuneo**:
- Forza risultante R1 = q · N (con N = H/sin β lunghezza fronte)
- Direzione: ⟂ al fronte, verso l'interno
- Componenti: R1<sub>x</sub> = q·H, R1<sub>y</sub> = −q·H·cot β
- Entra come **azione attiva** in F<sub>x</sub>/F<sub>y</sub>
- Aumenta N (normale al piano) → aumenta attrito mobilitato N·tan φ
- **Non** contribuisce direttamente a τ (non attraversa il piano)

**Uso tipico**: contenimento del distacco superficiale di degrado spessore ≤ 1 m, dove la roccia ha buon φ.

## R2 · Pannello a fune (caging)

Pannelli a fune (es. cavi d'acciaio φ8 mm, interasse 600 mm) che **attraversano** il piano di scorrimento, ancorati a chiodi profondi. Modello: capacità di taglio mobilizzata `τ_R2` [kN/m] applicata direttamente al piano.

**Effetto sul cuneo**:
- Sommata direttamente a τ resistente nell'equazione di Mohr-Coulomb
- Non passa attraverso N (è una membrana in trazione)
- Frena lo scorrimento sul piano in maniera indipendente da φ

**Uso tipico**: roccia degradata di spessore significativo che vuole scorrere come blocco. Richiede chiodatura profonda associata.

## Catalogo reti

Le tipologie sono definite nel **catalogo reti** dello step Interventi:

| Campo                              | Significato                                | Default |
|------------------------------------|--------------------------------------------|---------|
| Codice                             | identificatore (es. N1, N2)                | N1      |
| Categoria                          | Corticale aderente / Pannello a fune       | 0       |
| Calcola capacità                   | toggle automatico                          | true    |
| Diametro filo                      | φ del filo della maglia [mm]               | 3       |
| Maglia (orizz/vert)                | dimensioni della maglia [mm]               | 80 × 80 |
| Resistenza trazione filo           | f<sub>tk</sub> del filo [kN/cavo]          | 30      |
| Passo chiodi (orizz/vert)          | interasse dei chiodi di fissaggio [m]      | 3 × 3   |
| Capacità singolo chiodo            | F del chiodo fisso [kN]                    | 100     |
| Interasse funi (caging)            | passo dei cavi nella griglia [mm]          | 600     |
| Numero funi                        | n. cavi nella griglia                      | 1       |
| Resistenza trazione fune           | f<sub>tk</sub> della fune [kN/cavo]        | 60      |
| Capacità override                  | forzatura manuale [kN/m² o kN/m]           | 0       |

La capacità (`q` per corticale, `τ` per caging) viene calcolata automaticamente dai parametri, ma è possibile sovrascriverla con un valore da datasheet del fornitore.

!!! note "Verifica strutturale interna delegata al fornitore"
    RockPlane **non** duplica le verifiche di punzonamento del singolo nodo (R_punz) né di trazione globale del pannello (R_tr,rete) come fa SRS. Queste sono verifiche strutturali interne tipicamente certificate dal fornitore della rete. RockPlane usa la capacità dichiarata e la inserisce come azione nel calcolo di stabilità planare.

## Intervento posizionato

Lo step "Interventi" permette di assegnare una rete al cuneo:

| Campo              | Significato                                         |
|--------------------|-----------------------------------------------------|
| Tipo               | Rete corticale / Rete caging                        |
| Tipologia          | codice del catalogo reti (N1, N2, …)               |
| q oppure τ         | derivata dal catalogo, modificabile come override   |

L'intervento si applica a tutto il fronte (non è puntuale come per chiodi/tiranti).

## Confronto sintetico

| Aspetto                  | R1 Corticale            | R2 Caging                       |
|--------------------------|-------------------------|----------------------------------|
| Parametro                | q [kN/m²]               | τ [kN/m]                         |
| Direzione                | ⟂ al fronte, verso monte | lungo il piano (tangente)       |
| Effetto su N             | **+** (aumenta)         | nessuno                          |
| Effetto su τ resistente  | indiretto (via N·tan φ) | **diretto** (somma a τ)         |
| Funzione fisica          | "stappa" il cuneo       | resiste a taglio sul piano      |
| Tipico uso               | superficie esposta      | spessore di degrado significativo |

## Sul disegno 2D

- **R1**: zona di pressione sul fronte con freccette verso il cuneo
- **R2**: indicazione di linee in trazione sul piano di rottura

## ΔFS apportato dalle reti

Quando ci sono reti nel progetto, RockPlane calcola **automaticamente** anche l'FS **senza reti** (esclude solo R1/R2 dal calcolo, lascia chiodi/tiranti) e mostra il **ΔFS** apportato dalle reti. Utile per giustificare il dimensionamento al cliente:

```
FS = 1.34          (con reti)
FS senza reti = 1.18
Δ FS = +0.16
```

Compare nel pannello FS in alto.

## Riferimenti

- ETAG 027 — Guidelines for European Technical Approval of falling rock protection kits
- UNI EN 1090-2 — Esecuzione di strutture di acciaio e di alluminio
- Cataloghi fornitori: Maccaferri, Geobrugg, Officine Maccaferri
