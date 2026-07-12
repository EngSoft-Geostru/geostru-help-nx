---
title: Capacità portante
---

# Capacità portante

Il carico limite **q_lim** è la pressione che porta a rottura il terreno di
fondazione. Loadcap NX lo calcola con più metodi in parallelo, per ogni
combinazione SLU, e ne confronta gli esiti.

## L'equazione trinomia

Tutti i metodi partono dalla forma classica del carico limite:

`q_lim = c·N_c·s_c·d_c·i_c + q·N_q·s_q·d_q·i_q + ½·γ·B·N_γ·s_γ·d_γ·i_γ`

dove:

- **N_c, N_q, N_γ** — fattori di capacità portante, funzione di φ′;
- **s** — fattori di **forma** (dipendono da B/L);
- **d** — fattori di **profondità** (dipendono da D/B);
- **i** — fattori di **inclinazione** del carico;
- **q = γ·H_F** — sovraccarico al piano di posa (vedi
  [altezza di incastro](geometria.md#altezza-di-incastro-h_f));
- **c** — coesione (c′ in drenata, c_u in non drenata).

## I metodi

| Metodo | Anno | Note |
|---|---|---|
| **Terzaghi** | 1955 | Formulazione storica, fondazioni non troppo profonde |
| **Meyerhof** | 1963 | Fattori di forma, profondità e inclinazione generali |
| **Hansen** | 1970 | Estende Meyerhof (base e terreno inclinati) |
| **Vesic** | 1975 | Fattori N_γ ampiamente adottati; include il punzonamento |
| **Brinch-Hansen** | — | Formulazione EC7/EC8 |
| **Meyerhof-Hanna** | 1978 | Terreni a **due strati** (strato debole su resistente o viceversa) |
| **Richards** | 1993 | Capacità portante in **condizioni sismiche** |

Attiva i metodi da confrontare nella card **Metodi di calcolo**. Il **risultato
che governa** è quello con la **resistenza di progetto minima** tra tutti i metodi
e tutte le combinazioni.

!!! tip "Perché più metodi"
    Metodi diversi adottano fattori N_γ e correzioni differenti: confrontarli dà
    una misura della dispersione del risultato. Meyerhof-Hanna, in particolare, è
    indispensabile quando uno strato debole sovrasta uno strato resistente.

## Eccentricità e area efficace

In presenza di momento, il carico è eccentrico. L'eccentricità è `e = M / N`.
Loadcap adotta il criterio dell'**area efficace** di Meyerhof, riducendo le
dimensioni: `B′ = B − 2·e_B`, `L′ = L − 2·e_L`.

!!! warning "Ribaltamento"
    Se l'eccentricità supera `B/6` la reazione si parzializza; oltre `B/2` la
    fondazione **ribalta** e Loadcap lo segnala. Grandi eccentricità riducono
    fortemente l'area efficace e quindi la capacità portante.

## Verifica e fattore di sicurezza

Per ogni metodo e combinazione:

- **Resistenza di progetto**: `R_d = q_lim / γ_R,v`;
- **Tensione di esercizio** al piano di posa `E_d`;
- **Fattore di sicurezza**: `FS = q_lim / E_d`.

La combinazione è **verificata** quando la resistenza di progetto è maggiore della
sollecitazione (equivalente a `FS ≥ γ_R,v`).

## Verifica a scorrimento

Verifica aggiuntiva contro lo scorrimento della fondazione sotto l'azione
orizzontale. Si attiva quando esiste un taglio (H_x o H_y). La resistenza di
progetto è:

`R_d = (N·tan δ + a·A′ + E_pd) / γ_R,o`

con **δ** angolo di attrito terreno-fondazione, **a** adesione
terreno-fondazione, **A′** area efficace ed **E_pd** spinta passiva laterale. La
sollecitazione è `V_d = √(H_x² + H_y²)`; la verifica è soddisfatta quando
`FS = R_d·γ_R,o / V_d ≥ γ_R,o`.

Nella card **Verifica a scorrimento** (sopra la Falda) imposti:

- **Adesione terreno-fondazione a** [kN/m²];
- **Angolo di attrito terreno-fondazione δ** [°];
- **Frazione spinta passiva** [%].

!!! note "Valori a zero = derivazione automatica"
    Lasciando **adesione e δ a 0**, Loadcap li deriva dallo strato sotto il piano
    di posa (a = coesione dello strato, δ = φ′). Una **frazione spinta passiva a
    0** esclude la spinta passiva laterale (attiva solo per trave rovescia e
    plinto). In analisi non drenata δ è posto a 0.

## Verifica a punzonamento

Per fondazioni su terreni poco rigidi, Loadcap esegue la verifica a
**punzonamento** secondo Vesic, confrontando l'indice di rigidezza I_r con il suo
valore critico I_crit. Se I_r < I_crit si ha rottura per punzonamento, segnalata
nei risultati.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/it/carico-limite.md).*
