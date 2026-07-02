---
title: Metodo razionale di Ivanov (deflessione)
---

# Metodo razionale di Ivanov (deflessione)

Il metodo della **massima deflessione** (o di Ivanov) è un metodo razionale che imposta il problema elastico nei terreni secondo Boussinesq. Il criterio di verifica limita la **massima deflessione** che si produce in superficie al termine della vita utile della pavimentazione.

## Principio di verifica

Si confrontano due deflessioni:

- **f_adm** — deflessione ammissibile, funzione del traffico;
- **f_d** — deflessione calcolata sotto il carico dei pneumatici.

Il **fattore di sicurezza** è:

`FS = f_adm / f_d`

La sovrastruttura è **verificata** quando `FS ≥ 1`.

## Come RPD calcola

1. **Modulo elastico equivalente (E_eq)** — l'ammasso multistrato viene ricondotto a un unico modulo equivalente, iterando **dal basso verso l'alto** (fondazione → base → collegamento → usura). Il modulo di partenza del sottofondo è stimato dal CBR: `E₀ = 65 · CBR^0,65`. Ogni strato attivo modifica E_eq in funzione del proprio modulo elastico **E**, dello spessore e del raggio dell'impronta del pneumatico.
2. **Deflessione ammissibile** — `f_adm = 0,17 − 0,026 · log₁₀(N)`, dove **N** è il numero di assi standard al giorno nell'ultimo anno di vita utile.
3. **Deflessione calcolata** — `f_d = p · Dp / E_eq`, con **p** pressione di gonfiaggio dei pneumatici e **Dp** diametro dell'impronta.

!!! note "Strato di usura"
    Nel calcolo razionale puoi **escludere lo strato di usura** (opzione in *Stratigrafia*): in molti approcci l'usura non è considerata portante.

## Dati richiesti in RPD

| Sezione | Dato |
|---|---|
| Sollecitazioni meccaniche | Diametro impronta pneumatici (Dp), pressione di gonfiaggio (p) |
| Caratteristiche sottofondo | CBR (per E₀) |
| Stratigrafia | Per ogni strato: spessore e **modulo elastico E** (kg/cm²) |
| Traffico di progetto | Serve per f_adm (assi/giorno a fine vita utile) |

!!! tip "Sollecitazioni meccaniche"
    I campi *Sollecitazioni meccaniche* sono usati solo dai metodi razionali (Ivanov e Westergaard). Con il metodo AASHTO restano visibili ma non attivi.

## Risultati

Nella scheda **Risultati** vedi la deflessione ammissibile, quella calcolata, il modulo equivalente E_eq, il numero di assi/giorno e il fattore di sicurezza, con la condizione di verifica.

!!! tip "Approfondimento teorico"
    Il documento del metodo razionale è scaricabile dall'app (menu **?** → *Risorse* → "Metodo razionale — Ivanov").

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20RPD%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rpd/docs/it/ivanov.md).*
