---
title: Metodo empirico AASHTO 1993
---

# Metodo empirico AASHTO 1993

Il metodo empirico è quello proposto dall'*AASHTO Guide for Design of Pavement Structures* (1993), basato sui risultati sperimentali dell'AASHO Road Test. Misura l'adeguatezza della pavimentazione in termini di **numero di assi standard da 82 kN (8,2 t)** che la struttura può sopportare, mantenendo la funzionalità richiesta, per la vita utile di progetto.

## Principio di verifica

La verifica confronta due grandezze:

- **N₈.₂,Calc** — gli assi standard che *transitano* effettivamente sulla corsia di progetto nella vita utile (vedi [Traffico di progetto](traffico.md));
- **N₈.₂,Lim** — gli assi standard che la pavimentazione è in grado di *sopportare*.

Il **fattore di sicurezza** è:

`FS = N₈.₂,Lim / N₈.₂,Calc`

La sovrastruttura è **verificata** quando `FS > 1`.

## Structural Number (SN)

Lo **Structural Number** rappresenta la capacità strutturale del pacchetto. È la somma dei contributi degli strati:

`SN = Σ aᵢ · mᵢ · Dᵢ`

dove, per ciascuno strato *i*:

- **Dᵢ** — spessore, in pollici (inch);
- **aᵢ** — coefficiente strutturale (dipende dal materiale);
- **mᵢ** — coefficiente di drenaggio (adimensionale; vale 1 per i conglomerati bituminosi).

!!! note "Unità"
    In RPD lo Structural Number è mostrato in **inch** (con l'equivalente in cm accanto). Gli spessori degli strati si inseriscono invece in **cm**.

## L'equazione AASHTO

Il numero di assi ammissibili N₈.₂,Lim si ottiene da:

`log₁₀(N₈.₂,Lim) = Z_R·S₀ + 9,36·log₁₀(SN+1) − 0,20 + [log₁₀(ΔPSI / 2,7)] / [0,40 + 1094/(SN+1)^5,19] + 2,32·log₁₀(M_R) − 8,07`

con:

- **Z_R** — deviata normale standard legata all'affidabilità R (vedi tabella sotto);
- **S₀** — deviazione standard (errore su traffico e prestazioni): 0,40–0,50;
- **ΔPSI = PSI,in − PSI,fin** — perdita di servizio ammessa;
- **M_R** — modulo resiliente del sottofondo, in psi.

### Affidabilità R e coefficiente Z_R

L'affidabilità R è la probabilità che la pavimentazione raggiunga la vita utile prevista. A ogni R corrisponde un valore di Z_R (**negativo per R > 50%**):

| R (%) | Z_R |
|---|---|
| 50 | 0,000 |
| 90 | −1,282 |
| 95 | −1,645 |
| 99 | −2,327 |

Per valori intermedi RPD interpola linearmente.

!!! note "Perché Z_R è negativo?"
    Non è un errore: Z_R è la deviata della coda inferiore della normale. Più alza l'affidabilità, più diventa negativo, e nel termine `Z_R·S₀` questo rende il progetto più cauto (SN richiesto maggiore). Con R = 90% → Z_R = −1,282.

### Modulo resiliente dal CBR

Puoi inserire direttamente **M_R** oppure ricavarlo dal **CBR** del sottofondo. In RPD scegli il parametro in *Caratteristiche sottofondo*; la conversione CBR → M_R è gestita dal software.

## Dati richiesti in RPD

| Sezione | Dato |
|---|---|
| Dati generali | Vita utile, affidabilità R, PSI iniziale e finale |
| Traffico di progetto | TGM, tasso di crescita, % commerciali, % corsia, deviazione standard S₀ |
| Caratteristiche sottofondo | CBR **o** Modulo resiliente |
| Stratigrafia | Per ogni strato: spessore, coefficiente strutturale a, coefficiente di drenaggio m |

## Risultati

Nella scheda **Risultati** trovi il fattore di sicurezza, lo Structural Number, gli **assi ammissibili** (N₈.₂,Lim), il coefficiente di equivalenza, Z_R, ΔPSI e M_R. Se la verifica non è soddisfatta, la card **Come rientrare in verifica** propone gli spessori (o il TBR della geogriglia) necessari — vedi [Guida rapida](quickstart.md).

!!! tip "Approfondimento teorico"
    Il documento completo del metodo è scaricabile dall'app (menu **?** → *Risorse* → "Metodo empirico"), oppure consulta l'[AASHTO Guide for Design of Pavement Structures](https://habib00ugm.files.wordpress.com/2010/05/aashto1993.pdf). In Italia il riferimento pratico è il **Catalogo Italiano delle Pavimentazioni Stradali (CNR, BU 168/95)**.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20RPD%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rpd/docs/it/aashto.md).*
