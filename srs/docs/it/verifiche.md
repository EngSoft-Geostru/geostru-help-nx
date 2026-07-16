---
title: Verifiche
---

# Verifiche

Dopo **Calcola**, la tab **Verifiche** riepiloga i coefficienti di sicurezza e
l'esito delle sei verifiche di resistenza dell'ancoraggio. Questa pagina
spiega cosa confronta ciascuna e come interpretarle.

![Esito delle verifiche](img/srs-verifiche.png)

## Coefficienti di sicurezza

- **FS₀** — coefficiente di sicurezza del pendio **prima** dell'intervento
  (calcolato al passo 1 della card Parametri di Progetto).
- **FS_des** — coefficiente di sicurezza **di progetto**, quello che hai
  scelto come obiettivo.
- **R.1 ΔFS** — l'incremento ottenuto: `ΔFS = FS_des − FS₀`.

A partire da FS_des, SRS ricava la **forza di trazione A** che ogni ancoraggio
deve fornire per portare il pendio da FS₀ a FS_des, tenendo conto
dell'inclinazione dell'ancoraggio β rispetto al pendio. Questa forza,
moltiplicata per il coefficiente γ_Q1 di normativa, è la sollecitazione di
progetto **E_d** (trazione) e **T_d** (taglio) usata in tutte le verifiche
seguenti.

## Le sei verifiche (R.2–R.7)

| Codice | Verifica | Confronto |
|---|---|---|
| **R.2** | Trazione barra | R_f > E_d |
| **R.3** | Taglio barra | T_f > T_d |
| **R.4** | Sfilamento barra/malta | R_bm > E_d |
| **R.5** | Sfilamento del bulbo | R_bulb > E_d |
| **R.6** | Punzonamento della rete | R_punz,des > E_d |
| **R.7** | Trazione della rete | R_tr,des > T_d / i_x |

Ogni verifica è **soddisfatta** quando la resistenza supera la sollecitazione
e mostra il proprio coefficiente di sicurezza `FS = resistenza / sollecitazione`.

### R.2 — Trazione barra

Confronta la resistenza massima a trazione della barra **R_f** (dal diametro
φ_b, dalla tensione di snervamento f_yk e dal coefficiente γ_s) con la
sollecitazione di trazione di progetto **E_d**. Se non è soddisfatta: aumenta
il diametro della barra o usa un acciaio con f_yk superiore.

### R.3 — Taglio barra

Confronta la resistenza a taglio della barra **T_f** (ricavata da R_f con il
criterio di von Mises, `T_f = R_f / √3`) con la sollecitazione di taglio di
progetto **T_d**. Se non è soddisfatta: aumenta il diametro barra, la
spaziatura (i_x, i_y) o usa un acciaio con f_yk superiore.

### R.4 — Sfilamento barra/malta

Confronta l'aderenza massima tra barra e malta **R_bm** (dalla resistenza
tangenziale di progetto della malta f_bd e dalla lunghezza L_a) con **E_d**.
Se non è soddisfatta: aumenta la lunghezza dell'ancoraggio, il diametro di
perforazione o la resistenza della malta (R_ck).

### R.5 — Sfilamento del bulbo

Confronta la resistenza allo sfilamento del bulbo dal substrato **R_bulb**
(dalla lunghezza collaborante del bulbo L_b, dalla tensione di aderenza
substrato-malta τ_sub, dal diametro di perforazione e dai coefficienti
riduttivi ξ_a4 e γ_Rap) con **E_d**. Se non è soddisfatta: aumenta la
lunghezza dell'ancoraggio, il diametro di perforazione o il numero di
profili di indagine geognostica (riduce ξ_a4).

### R.6 — Punzonamento della rete

Confronta la resistenza a punzonamento di progetto della rete
**R_punz,des** con **E_d**. Se non è soddisfatta: scegli una rete con
resistenza a punzonamento superiore.

### R.7 — Trazione della rete

Confronta la resistenza a trazione di progetto della rete **R_tr,des** con la
sollecitazione di taglio ripartita sull'interasse orizzontale, **T_d / i_x**.
Se non è soddisfatta: scegli una rete con resistenza a trazione superiore o
riduci l'interasse i_x.

!!! tip "Un suggerimento per ogni verifica non soddisfatta"
    Quando una verifica fallisce, la card mostra automaticamente un
    suggerimento su quale parametro modificare — sono gli stessi indicati
    sopra.

## Ancoraggi per 100 m²

- **R.8 Numero** — quanti ancoraggi servono ogni 100 m² di rete:
  `N_tot = round(100 / (i_x · i_y))`.
- **R.9 Lunghezza totale perforazioni** — i metri di perforazione
  corrispondenti: `L_tot = N_tot · L_a`.

Sono i due numeri da riportare in un computo metrico di massima
dell'intervento.

## Costo stimato

Se hai compilato i **Parametri Costo** (perforazione €/m, acciaio €/kg, malta
€/m³, rete €/m²) nella sezione Dati Professionista e Progetto, la tab
Verifiche mostra anche una stima del **costo totale per 100 m²** di rete,
somma del costo di perforazione, dell'acciaio della barra, della malta di
iniezione e della rete.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20SRS%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/it/verifiche.md).*
