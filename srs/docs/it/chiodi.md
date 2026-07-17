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

### Schema della maglia di posa

In pianta gli ancoraggi sono disposti su una maglia di interassi
**i_x** (orizzontale) e **i_y** (lungo il pendio), a **quinconce** (rombo,
sinistra) o a **maglia rettangolare** (destra):

<figure markdown="span">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 300" font-family="sans-serif" font-size="13" role="img" aria-label="Disposizione in pianta"><polygon points="195.0,60.0 245.0,160.0 195.0,260.0 145.0,160.0" fill="#b9c4d6" stroke="#43403a" stroke-width="1" fill-opacity="0.55"/><circle cx="95.0" cy="60.0" r="7" fill="#43403a"/><circle cx="195.0" cy="60.0" r="7" fill="#43403a"/><circle cx="295.0" cy="60.0" r="7" fill="#43403a"/><circle cx="145.0" cy="160.0" r="7" fill="#43403a"/><circle cx="245.0" cy="160.0" r="7" fill="#43403a"/><circle cx="95.0" cy="260.0" r="7" fill="#43403a"/><circle cx="195.0" cy="260.0" r="7" fill="#43403a"/><circle cx="295.0" cy="260.0" r="7" fill="#43403a"/><line x1="145.0" y1="36.0" x2="95.0" y2="36.0" stroke="#8a5a00" stroke-width="1.1"/><polygon points="95.0,36.0 101.4,33.1 101.4,38.9" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><line x1="145.0" y1="36.0" x2="195.0" y2="36.0" stroke="#8a5a00" stroke-width="1.1"/><polygon points="195.0,36.0 188.6,38.9 188.6,33.1" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><text x="145.0" y="30.0" fill="#8a5a00" text-anchor="middle" font-size="12" font-weight="600" transform="rotate(0.0 145.0 36.0)">i<tspan font-size="9" dy="2">x</tspan></text><line x1="67.0" y1="110.0" x2="67.0" y2="60.0" stroke="#8a5a00" stroke-width="1.1"/><polygon points="67.0,60.0 69.9,66.4 64.1,66.4" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><line x1="67.0" y1="110.0" x2="67.0" y2="160.0" stroke="#8a5a00" stroke-width="1.1"/><polygon points="67.0,160.0 64.1,153.6 69.9,153.6" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><text x="67.0" y="104.0" fill="#8a5a00" text-anchor="middle" font-size="12" font-weight="600" transform="rotate(90.0 67.0 110.0)">i<tspan font-size="9" dy="2">y</tspan></text><polygon points="455.0,110.0 555.0,110.0 555.0,210.0 455.0,210.0" fill="#b9c4d6" stroke="#43403a" stroke-width="1" fill-opacity="0.55"/><circle cx="405.0" cy="60.0" r="7" fill="#43403a"/><circle cx="505.0" cy="60.0" r="7" fill="#43403a"/><circle cx="605.0" cy="60.0" r="7" fill="#43403a"/><circle cx="405.0" cy="160.0" r="7" fill="#43403a"/><circle cx="505.0" cy="160.0" r="7" fill="#43403a"/><circle cx="605.0" cy="160.0" r="7" fill="#43403a"/><circle cx="405.0" cy="260.0" r="7" fill="#43403a"/><circle cx="505.0" cy="260.0" r="7" fill="#43403a"/><circle cx="605.0" cy="260.0" r="7" fill="#43403a"/><line x1="455.0" y1="36.0" x2="405.0" y2="36.0" stroke="#8a5a00" stroke-width="1.1"/><polygon points="405.0,36.0 411.4,33.1 411.4,38.9" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><line x1="455.0" y1="36.0" x2="505.0" y2="36.0" stroke="#8a5a00" stroke-width="1.1"/><polygon points="505.0,36.0 498.6,38.9 498.6,33.1" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><text x="455.0" y="30.0" fill="#8a5a00" text-anchor="middle" font-size="12" font-weight="600" transform="rotate(0.0 455.0 36.0)">i<tspan font-size="9" dy="2">x</tspan></text><line x1="377.0" y1="110.0" x2="377.0" y2="60.0" stroke="#8a5a00" stroke-width="1.1"/><polygon points="377.0,60.0 379.9,66.4 374.1,66.4" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><line x1="377.0" y1="110.0" x2="377.0" y2="160.0" stroke="#8a5a00" stroke-width="1.1"/><polygon points="377.0,160.0 374.1,153.6 379.9,153.6" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><text x="377.0" y="104.0" fill="#8a5a00" text-anchor="middle" font-size="12" font-weight="600" transform="rotate(90.0 377.0 110.0)">i<tspan font-size="9" dy="2">y</tspan></text></svg>
<figcaption>Disposizione delle barre in pianta: quinconce e maglia rettangolare.</figcaption>
</figure>

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
