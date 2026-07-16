---
title: Chiodi e ancoraggi
---

# Chiodi e ancoraggi

La sezione **Ancoraggi** definisce il chiodo (la barra passiva cementata) e
la sua disposizione sul pendio. Puoi partire da un **catalogo commerciale** o
inserire i parametri **manualmente**.

## Catalogo chiodi

Il campo **Catalogo chiodi** elenca i cataloghi disponibili; selezionandone
uno compare il campo **Tipo chiodo** con l'elenco delle barre di quel
catalogo, ciascuna col proprio diametro. Il catalogo predefinito raccoglie
sistemi di barre e ancoraggi per rete chiodata, nelle due famiglie:

- **GEWI** — barra piena filettata, in acciaio B500B.
- **TITAN** — barra cava autoperforante, con diametro esterno e interno,
  pensata per terreni sciolti o roccia fratturata dove la perforazione
  tradizionale è difficoltosa.

Scegliendo un chiodo dal catalogo, SRS compila automaticamente il **diametro
barra φ_b**, la **tensione di snervamento f_yk** e il **tipo barra**
(riportato poi nella relazione). Puoi comunque correggere manualmente i
valori dopo la selezione.

Selezionando **-- Parametri manuali --** nel campo Catalogo chiodi, tutti i
campi restano modificabili liberamente: usalo per barre non a catalogo o per
verificare una soluzione già definita altrove.

## Parametri della barra e della perforazione

| Simbolo | Parametro | Unità |
|---|---|---|
| — | Tipo barra (descrizione libera, es. B500) | — |
| I.18 φ_b | Diametro barra | mm |
| I.19 f_yk | Tensione di snervamento barra | N/mm² |
| I.17 D_f | Diametro di perforazione | mm |
| I.16 L_a | Lunghezza ancoraggio | m |
| I.15 β | Inclinazione ancoraggio rispetto all'orizzontale | ° |

## Disposizione sul pendio

| Simbolo | Parametro | Unità |
|---|---|---|
| I.13 i_y | Interasse verticale della maglia di posa | m |
| I.14 i_x | Interasse orizzontale della maglia di posa | m |

Interassi più fitti (i_x, i_y più piccoli) aumentano il numero di ancoraggi
per 100 m² ma riducono la trazione richiesta a ciascuno, perché ogni chiodo
trattiene un cuneo di coltre più piccolo (`V = i_x · i_y · S`). Vedi
[Verifiche](verifiche.md#ancoraggi-per-100-m2).

## Malta di iniezione

| Simbolo | Parametro | Unità |
|---|---|---|
| I.20 R_ck (NTC) / f_ck (Eurocodice) | Resistenza a compressione della malta | N/mm² |
| I.21 η₁ | Coefficiente di aderenza | — |
| I.22 N_prof | Numero di profili di indagine geognostica | — |

Con normativa **NTC 2018** inserisci la resistenza cubica **R_ck**; con
**Eurocodice** il campo diventa **f_ck** (resistenza cilindrica, già diretta —
niente conversione 0,83). Il coefficiente **η₁** vale **1,00** per buona
aderenza barra-malta o **0,70** per aderenza non buona (condizioni di getto
meno favorevoli). **N_prof** (da 1 a "≥ 5") è il numero di verticali di
indagine geognostica disponibili nell'area: più sono, più basso è il
coefficiente riduttivo ξ_a4 applicato alla resistenza allo sfilamento del
bulbo (vedi [Verifiche](verifiche.md)).

## Normativa e coefficienti parziali

Il campo **Normativa**, in cima alla sezione **Dati Professionista e
Progetto**, sceglie il set di coefficienti parziali usato in tutte le
verifiche:

| Normativa | γ_s (acciaio) | γ_Rap (ancoraggi) | γ_Q1 statico | γ_Q1 sismico | γ_c (malta) | R_ck→f_ck |
|---|---|---|---|---|---|---|
| **Eurocode 7/8** (EN 1997 + EN 1998, DA1-C2) | 1,15 | 1,10 | 1,5 | 1,0 | 1,5 | 1,0 |
| **NTC 2018** | 1,15 | 1,20 | 1,5 | 1,0 | 1,5 | 0,83 |
| **Utente** | personalizzabile | personalizzabile | personalizzabile | personalizzabile | personalizzabile | personalizzabile |

Selezionando **Utente** compare un pannello con i sei coefficienti, tutti
modificabili: usalo per normative diverse da NTC 2018 ed Eurocodice, o per
studi di sensitività.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20SRS%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/it/chiodi.md).*
