---
title: Stratigrafia e falda
---

# Stratigrafia e falda

La stratigrafia descrive il terreno sotto il piano di posa, strato per strato. La
qualità del calcolo dipende in modo diretto dalla bontà di questi parametri.

## Parametri per strato

Ogni riga della tabella **Stratigrafia** ha i campi principali sempre visibili e
i parametri di deformabilità nel pannello di dettaglio (freccia a sinistra).

| Simbolo | Unità | Significato |
|---|---|---|
| **s** | m | Spessore dello strato |
| **γ** | kN/m³ | Peso di volume naturale |
| **γ_sat** | kN/m³ | Peso di volume saturo (sotto falda) |
| **φ′** | ° | Angolo di resistenza al taglio efficace |
| **c′** | kPa | Coesione efficace |
| **c_u** | kPa | Coesione non drenata (analisi in tensioni totali) |
| **E** | kPa | Modulo elastico (cedimenti elastici e Schmertmann) |
| **E_ed** | kPa | Modulo edometrico (cedimenti edometrici) |
| **ν** | – | Coefficiente di Poisson |
| **C_s** | – | Coefficiente di consolidazione secondaria |
| **C_v** | – | Coefficiente di consolidazione primaria (decorso nel tempo) |
| **N_SPT** | – | Numero di colpi SPT (metodo di Burland & Burbidge) |

!!! warning "Unità SI, sensibili al maiuscolo/minuscolo"
    I simboli sono in unità SI e rispettano le convenzioni scientifiche: **kPa**,
    **MPa**, **kN/m³**. Attenzione a non confondere γ (peso di volume, kN/m³) con
    le pressioni (kPa).

### Quali parametri servono a cosa

- **Carico limite**: γ, φ′, c′ (drenata) oppure c_u (non drenata).
- **Cedimenti elastici**: E, ν.
- **Cedimenti edometrici**: E_ed (e C_v per il decorso, C_s per il secondario).
- **Cedimenti di Burland & Burbidge**: N_SPT.

Se uno strato ha `E_ed > 0` viene trattato con il metodo edometrico; in assenza di
E_ed, se `E > 0`, con il metodo di **Schmertmann**. Vedi [Cedimenti](cedimenti.md).

## Incolla e importa

Compilare la stratigrafia a mano non è l'unica strada:

- **Incolla** — copia una tabella da un foglio Excel (o dalla griglia del
  desktop) e incollala: una finestra ti fa **mappare le colonne** sui campi. I
  colori degli strati vengono assegnati con un **gradiente terroso** dall'alto
  (chiaro) verso il basso (scuro).
- **Importa** — carica una stratigrafia in formato JSON, tipicamente **esportata
  da Dynamic Probing NX** («Esporta per Loadcap»), oppure un file `.lcnx`.

!!! tip "Dal dato di prova alla stratigrafia"
    Per una stratigrafia derivata da prove penetrometriche, l'interpretazione
    rigorosa appartiene a **Dynamic Probing NX**: da lì esporti gli strati già
    caratterizzati (γ, φ′, c_u, E, N_SPT) pronti per Loadcap.

## Falda

Nella card **Falda** indichi:

- **Presenza falda** — assente o presente;
- **Profondità dal piano campagna** — positiva sotto il piano campagna.

La falda governa il calcolo delle tensioni efficaci (spinta idraulica) e, quindi,
sia la capacità portante sia i cedimenti. Sotto falda si usa il peso di volume
**γ_sat**.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/it/stratigrafia.md).*
