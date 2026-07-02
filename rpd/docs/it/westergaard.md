---
title: Metodo razionale di Westergaard (rigida)
---

# Metodo razionale di Westergaard (pavimentazioni rigide)

Il metodo di **Westergaard** si basa sulla soluzione dell'equazione di Lagrange per le **lastre sottili**. La pavimentazione viene modellata come una **piastra multistrato su suolo elastico**: il metodo calcola la massima deflessione della lastra sotto carico. È indicato in particolare per le **pavimentazioni rigide**.

## Principio di verifica

Come per Ivanov, si confronta la deflessione ammissibile con quella calcolata:

`FS = f_adm / f_d`

La sovrastruttura è **verificata** quando `FS ≥ 1`. La deflessione ammissibile ha la stessa forma del metodo di Ivanov: `f_adm = 0,17 − 0,026 · log₁₀(N)`.

## Come RPD calcola

RPD risolve la piastra multistrato con una **doppia serie di Fourier**, strato per strato, sommando i contributi:

- ogni strato è caratterizzato da modulo elastico **E**, spessore, coefficiente di Poisson **ν** (assegnato per posizione: 0,2 al 1° strato, 0,3 al 2°, 0,4 ai successivi) e coefficiente **αK** che lega il modulo al modulo di reazione (`K = E / αK`);
- il carico dei pneumatici è ripartito su un'area quadrata equivalente all'impronta;
- il modulo di reazione del sottofondo **K** chiude il modello alla base.

La deflessione di verifica è quella calcolata **in superficie** (primo strato).

## Dati richiesti in RPD

| Sezione | Dato |
|---|---|
| Sollecitazioni meccaniche | Diametro impronta pneumatici, pressione di gonfiaggio |
| Caratteristiche sottofondo | **Costante di sottofondo K** (kg/cm³) |
| Stratigrafia | Per ogni strato: spessore, **modulo elastico E**, coefficiente **αK** |
| Traffico di progetto | Serve per f_adm |

!!! note "Costante di sottofondo K"
    Il metodo di Westergaard richiede il **modulo di reazione K** del sottofondo (in *Caratteristiche sottofondo*) e i coefficienti **αK** dei singoli strati (in *Stratigrafia*).

## Risultati

Nella scheda **Risultati** trovi la deflessione ammissibile, quella calcolata, il fattore di sicurezza e la condizione di verifica.

!!! tip "Quando usarlo"
    Usa Westergaard per le **pavimentazioni rigide** (lastre in calcestruzzo); per le flessibili sono più indicati AASHTO 1993 (empirico) o Ivanov (deflessione).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20RPD%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rpd/docs/it/westergaard.md).*
