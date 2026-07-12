---
title: Carichi e combinazioni
---

# Carichi e combinazioni

La card **Carichi di progetto** raccoglie le combinazioni di azioni agenti sulla
fondazione. Ogni riga è una combinazione, già combinata (SLU o SLE), con i suoi
coefficienti parziali.

## Le azioni

Per ogni combinazione inserisci, al **piano di posa**:

| Simbolo | Unità | Azione |
|---|---|---|
| **q** | kN/m² | Pressione normale di progetto (se assegnata, sostituisce N) |
| **N** | kN | Sforzo normale verticale |
| **M_x**, **M_y** | kN·m | Momenti attorno agli assi x e y |
| **H_x**, **H_y** | kN | Tagli (azioni orizzontali) lungo x e y |

Se assegni **q**, la fondazione è caricata con una pressione uniforme; se assegni
**N** (con eventuali momenti), la pressione al contatto viene ricavata da N e
dall'eccentricità.

### Convenzione dei segni

L'icona **bussola** nell'intestazione della card apre lo schema della
**convenzione di segno delle sollecitazioni**: N verticale verso il basso, H_x e
H_y i tagli lungo gli assi, M_x e M_y i momenti attorno agli assi x e y.

## Approcci di progetto

Il menu **Approccio** precompila i coefficienti parziali secondo la normativa.
Cambiando approccio, i coefficienti si aggiornano automaticamente; se li modifichi
a mano, la combinazione diventa *Personalizzata*.

| Approccio | Uso tipico | γ_R,v (R) |
|---|---|---|
| **A1+M1+R1** | NTC — Approccio 2 | 1,0 |
| **A2+M2+R2** | NTC — Approccio 1, comb. 2 | 1,8 |
| **A1+M1+R3** | NTC — capacità portante GEO (R3) | 2,3 |
| **A2+M2+R3** | NTC — variante R3 | 2,3 |
| **DA1-C1 / DA1-C2 / DA2 / DA3** | Eurocodice 7 — Design Approach | secondo EC7 |
| **Sisma** | Combinazione sismica | 2,3 |
| **SLE** | Stato limite di esercizio → **cedimenti** | 1,0 |
| **Personalizzato** | Coefficienti liberi | — |

!!! note "SLU per il carico limite, SLE per i cedimenti"
    Le combinazioni **SLU/GEO** vengono usate per la capacità portante; le
    combinazioni **SLE** (di servizio) per i cedimenti. Un progetto completo ha
    almeno una combinazione di ciascun tipo.

## Coefficienti parziali

Ogni combinazione porta con sé i coefficienti parziali applicati:

- sui **parametri** (M): γ su tan φ′, su c′ e su c_u;
- sui **pesi** (A): γ sul peso in fondazione e sul peso di copertura;
- sulle **resistenze** (R): γ_R,v sulla capacità portante verticale e γ_R,o su
  quella orizzontale (scorrimento).

La resistenza di progetto è `R_d = q_lim / γ_R,v`.

## Import da CSV

Puoi importare le combinazioni da un file **CSV**:

- il pulsante di **modello CSV** scarica un file di esempio, con la convenzione
  dei segni riportata nei commenti di intestazione;
- il pulsante **CSV** importa un file (delimitatore `;` o `,`, decimali `.` o
  `,`), con colonne `descrizione ; approccio ; q ; N ; Mx ; My ; Hx ; Hy`.

Approcci ammessi nel CSV: `A1M1R1 A2M2R2 A1M1R3 A2M2R3 EC_DA1C1 EC_DA1C2 EC_DA2
EC_DA3 SISMA SLE`.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/it/carichi.md).*
