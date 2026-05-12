# Glossario

Definizioni dei termini chiave usati in GDW.

## Geometria

**α (alfa) — Inclinazione muro**
Angolo del muro rispetto alla verticale (0÷15°). > 0 = top spostato verso
monte (muro battuto). Influenza la formula di Coulomb (β nel codice) e
ruota il muro come corpo rigido per il disegno.

**β (beta) — Inclinazione fondazione**
Angolo della **faccia inferiore** della fondazione rispetto all'orizzontale
(0÷15°). > 0 = faccia inferiore inclinata verso monte (spessore monte
maggiore). Migliora resistenza allo scorrimento.

**β_terreno o ε — Inclinazione terrapieno**
Angolo del terreno a monte del muro rispetto all'orizzontale (positivo verso
l'alto = pendio salente da monte verso l'alto).

**B_muro**
Larghezza del muro alla base = blocchi[0] × base_gabbione.

**B_fond**
Larghezza della fondazione. ≥ B_muro. L'esubero è centrato.

**h_v, h_m**
Spessore della fondazione lato valle (sinistra) e monte (destra).
h_m = h_v + B_fond · tan(β).

**Fila / file (di gabbioni)**
Riga orizzontale di gabbioni. Numerate dal basso (I, II, III in numeri
romani sui disegni).

**Allineamento**
Disposizione delle file: "A destra" (paramento monte verticale), "A sinistra"
(paramento valle verticale, gradoni verso monte → riempimento a tergo),
"Centrato", "Personalizzato".

**Shift / spostamento per fila**
Spostamento orizzontale di una fila rispetto al riferimento. > 0 = verso
valle, < 0 = verso monte.

## Calcolo spinta

**K_a — Coefficiente di spinta attiva (Coulomb / Mononobe-Okabe)**
Coefficiente adimensionale che esprime quanta spinta orizzontale il terreno
trasmette al muro: S = ½ · γ · K_a · H².

**δ (delta) — Angolo di attrito muro-terreno**
Tipicamente 2/3 φ (gabbione-cls) o φ (gabbione-riempimento contatto pieno).

**θ (theta) — Angolo sismico equivalente**
θ = atan(k_h / (1 − k_v)). Entra nella formula di Mononobe-Okabe.

**S_x, S_y**
Componenti orizzontale e verticale della spinta totale. Proiettate sull'angolo
δ+α se inclinazione muro > 0.

**S_falda / S_w**
Spinta idrostatica orizzontale = ½ · γ_w · h_w².

**S_q**
Spinta indotta dal sovraccarico distribuito sul terrapieno.

## Verifiche

**FS — Fattore di sicurezza**
Rapporto tra resistenza e azione sollecitante, con coefficiente parziale γ_R
al denominatore. Verifica soddisfatta se FS ≥ 1.

**FS_rib — Ribaltamento**
M_s / (γ_R · M_r). γ_R_rib = 1.0 statico, 1.2 sismico.

**FS_scorr — Scorrimento (base inclinata)**
R / (γ_R · F_drive). γ_R_scorr = 1.1.

**FS_qlim — Capacità portante**
q_lim / (γ_R · σ_eff). γ_R = 2.3.

**FS_Bishop — Stabilità globale**
Risultato iterativo del metodo di Bishop. Soglia γ_R2 = 1.1 statico, 1.2
sismico.

**γ_R — Coefficiente parziale di resistenza**
Riduce la resistenza calcolata per ottenere la resistenza di progetto.

**N_⊥ — Forza normale al piano inclinato**
N_⊥ = F_y · cos β + F_x · sin β. Comprime la base inclinata della fondazione.

**F_drive**
Componente della risultante parallela al piano inclinato che tende a far
scorrere il muro verso valle. F_drive = F_x · cos β − F_y · sin β.

## Materiali (rete e gabbioni)

**DT — Doppia torsione**
Rete metallica esagonale a doppia torsione. Flessibile, intessuta. Conferisce
al gabbione una coesione apparente c_g.

**ES — Elettrosaldata**
Rete metallica a maglia ortogonale con fili saldati ai nodi. Rigida. Verifica
classica trazione + punzonamento del singolo filo.

**γ_G — Peso specifico del gabbione**
Peso del gabbione riempito di pietrame per unità di volume.
Tipico: 14÷18 kN/m³.

**φ_g — Angolo attrito gabbione-gabbione**
Per **DT**: 45° (valore di letteratura). Per **ES**: 25·γ−10° (formula
gabbioni elettrosaldati). Range tipico 26÷45°.

**c_g — Coesione apparente del gabbione**
Resistenza alla trazione/taglio data dalla rete intessuta. Solo DT. Tipico
2÷5 kPa.

**P_u — Peso unitario rete**
Peso della rete per unità di superficie sviluppata. Tipico 1.3÷2.2 kg/m².

**σ_adm — Tensione ammissibile al giunto**
Tensione normale massima che il giunto fra due file di gabbioni può
sopportare prima dello snervamento della rete. Solo per rete DT.
Input editabile dall'utente, oppure default empirico σ_adm[kPa] =
(50·γ_G[tf/m³] − 30)·9.81.

## Coefficienti parziali NTC 2018

**A1 / A2 — Combinazione azioni**
A1 (statico): G1_fav = 1.0, G1_sfav = 1.3, G2 = 1.5, Q = 1.5
A2 (sismico): tutti i coefficienti = 1.0 (sismica già amplificata da PGA)

**M1 / M2 — Combinazione parametri**
M1 (statico): γ_Mφ = γ_Mc = 1.0
M2 (sismico): γ_Mφ = γ_Mc = 1.25

**R3 — Combinazione resistenze**
γ_R3_qlim = 2.3, γ_R3_scorr = 1.1, γ_R3_pass = 1.4, γ_R_rib = 1.0 (statico) o 1.2 (sismico)

**Ψ₂ — Coefficiente di combinazione quasi-permanente**
Riduce il sovraccarico variabile Q in combinazione sismica (NTC tab. 2.5.I).

## Stabilità globale

**Bishop semplificato**
Metodo iterativo di equilibrio limite su superficie circolare divisa in conci.
Formula iterativa: FS = Σ(...)/Σ(W·sin α + k_h·W·braccio).

**Conci**
Suddivisione del cerchio in N parti uguali per il calcolo Bishop. 30 default
in GDW.

**FindCircle**
Costruzione analitica del cerchio passante per 3 punti dati (geometria
elementare). Usato per costruire la superficie di scorrimento dai 3 input
utente.
