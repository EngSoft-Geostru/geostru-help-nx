---
title: Cedimenti
---

# Cedimenti

I cedimenti si calcolano con le combinazioni di **servizio (SLE)**. La scheda
**Cedimenti** riporta, per la combinazione selezionata, i contributi elastico ed
edometrico per strato, l'eventuale stima di Burland & Burbidge e il decorso nel
tempo.

!!! note "Con quali carichi"
    A differenza della capacità portante (SLU), i cedimenti si valutano con le
    pressioni **di esercizio**. Il **selettore di combinazione** in cima alla
    scheda permette di passare da una SLE all'altra.

## Cedimenti elastici (Timoshenko-Goodier)

Cedimento immediato di un semispazio elastico, calcolato **al centro** e **al
bordo** della fondazione:

`w = q·B·(1−ν²)·I / E`

dove I è un fattore di influenza che dipende dalla forma (B/L) e dall'eventuale
**profondità del substrato rigido** (bedrock). Servono il **modulo elastico E** e
il **coefficiente di Poisson ν**. Il risultato è in **mm**.

## Cedimenti edometrici

Per gli strati con modulo edometrico **E_ed**, il cedimento di consolidazione
primaria si calcola per sottostrati. Loadcap offre due formulazioni:

- **Monodimensionale**: `w_c = Δσ·H / E_ed`;
- **Logaritmico** (Terzaghi): `w_c = H·RR·log₁₀[(σ′_v0 + Δσ)/σ′_v0]`, con
  `RR = (σ′_v0 + Δσ)/(0,435·E_ed)`.

Scegli la formulazione con il selettore **Metodo edometrico**. Il **cedimento
secondario** (creep) si aggiunge se è definito il coefficiente C_s.

!!! tip "Quale metodo"
    Il metodo logaritmico è coerente con la teoria della consolidazione classica;
    quello monodimensionale è più diretto e conservativo per incrementi tensionali
    piccoli. Per i confronti con calcoli desktop, usa la stessa formulazione.

## Metodo di Schmertmann

Per gli strati con modulo elastico **E** ma senza E_ed, Loadcap applica il metodo
di **Schmertmann** (1970-1978), basato sul fattore di deformazione **I_z**:

- pressione netta `q = q_applicata − σ′_v0(D)`;
- fattore di profondità `C₁ = 1 − 0,5·σ′_v0/q` (minimo 0,5);
- picco `I_z,max = 0,5 + 0,1·√(q/Δp)`;
- distribuzione triangolare di I_z (assialsimmetrica o piana secondo L/B);
- fattore di creep `C₂ = 1 + 0,2·log₁₀(t/0,1)`.

Il cedimento per strato è `w = C₁·q·I_z·H_s/E`, in cm.

## Burland & Burbidge

Stima empirica basata sul numero di colpi **N_SPT**, adatta ai terreni granulari:

`w = f_s·f_h·f_t·(q − ⅔·σ′_v0)·I_c·B^0,7`

con I_c indice di compressibilità funzione di N_SPT, e i fattori correttivi f_s
(forma), f_h (spessore dello strato deformabile) e f_t (tempo). Attivala con la
casella dedicata; richiede N_SPT sugli strati.

## Decorso dei cedimenti nel tempo

Per gli strati con coefficiente di consolidazione **C_v**, Loadcap traccia il
**decorso nel tempo** del cedimento di consolidazione, dalla teoria di Terzaghi:

- cedimento raggiunto al grado di consolidazione U: `w(U) = w_t·U/100`;
- tempo corrispondente: `t(U) = T_v(U)·H²/C_v`.

La tabella riporta la coppia (percentuale di consolidazione, tempo in giorni) fino
al 100%.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/it/cedimenti.md).*
