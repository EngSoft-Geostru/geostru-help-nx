# Sovraccarichi e spinta aggiuntiva

I sovraccarichi sono carichi distribuiti sul terrapieno a monte del muro che
incrementano la spinta attiva. La spinta aggiuntiva è una forza esterna
applicata direttamente al muro.

## Tipi di sovraccarico

GDW gestisce **due tipi** di sovraccarico distribuito (entrambi simultanei se
necessario):

### G — Sovraccarico permanente

Carichi che agiscono in modo continuo nel tempo. Esempi:

- Peso di una pavimentazione stradale
- Banchina o cordolo a tergo del muro
- Manufatti permanenti sul terrapieno

Unità: **kN/m²** (pressione distribuita).

### Q — Sovraccarico accidentale

Carichi variabili nel tempo. Esempi:

- Carico veicolare su una strada a tergo
- Carico di una folla
- Carico di una macchina operatrice

Unità: **kN/m²** (pressione distribuita).

## Posizione del sovraccarico

Per ogni sovraccarico (G e Q) imposti:

- **Ascissa iniziale**: distanza dall'angolo top-monte del muro
- **Ascissa finale**: distanza finale del carico

Esempio: G = 10 kN/m² da 2 m a 8 m → c'è una pavimentazione larga 6 m, distante
2 m dal bordo del muro.

I vertici noti del profilo (ascissa = 0 alla sommità muro, ascissa = L₁ a fine
monte 1, ascissa = L₁+L₂ a fine monte 2) appaiono come placeholder nel preview
sovraccarichi.

## Calcolo della spinta da sovraccarico

Il sovraccarico totale q (kN/m²) viene calcolato come:

$$
q_{tot} = G \cdot \gamma_{G2} + Q \cdot \gamma_Q
$$

dove γ_G2 e γ_Q sono i coefficienti parziali NTC (vedi [Coefficienti](coefficienti.md)).

La spinta indotta dal sovraccarico sulla parete del muro (altezza H) è:

$$
S_q = K_a \cdot q_{tot} \cdot H \cdot \chi
$$

dove χ = sin(α) / sin(α+i) è il fattore di riduzione per pendenza terrapieno
i (formula di Caquot-Kerisel per sovraccarichi finiti).

Il punto di applicazione di S_q è ad altezza:

$$
y_q = \frac{\gamma H^2 + 3 q H}{3 \gamma H + 6 q}
$$

(spinta combinata terreno + sovraccarico, baricentro pesato).

## Spinta aggiuntiva S

Forza **orizzontale** (kN) applicata direttamente al muro, indipendente dal
terrapieno. Esempi d'uso:

- Tiro di un cavo elettrico
- Carico orizzontale da macchinari ancorati al muro
- Spinta da paratie a tergo trasmessa puntualmente

Il punto di applicazione è la **mezzeria del muro in altezza** (H/2 dal piede).
S entra direttamente nell'equilibrio orizzontale per scorrimento e ribaltamento,
senza moltiplicazione per K_a.

## Combinazione sismica

In combinazione sismica (NTC 2018 § 7.11.6), il sovraccarico variabile Q deve
essere ridotto dal coefficiente Ψ₂ (quasi-permanente) della Tab. 2.5.I. GDW
**NON applica automaticamente** Ψ₂ — l'utente deve inserire il valore già
ridotto.

Quando attiva la normativa sismica appare un alert giallo che ricorda:

!!! warning "Attenzione — Combinazione sismica"
    Per i sovraccarichi variabili (Q) accidentali deve essere applicato il
    coefficiente Ψ₂ (quasi-permanente) della Tab. 2.5.I NTC 2018 prima
    dell'inserimento. Esempi: abitazioni Ψ₂=0.3, uffici Ψ₂=0.3, ambienti
    commerciali Ψ₂=0.6, neve (a≤1000m) Ψ₂=0.0.

## Vedi anche

- [Coefficienti NTC 2018](coefficienti.md) — γ_G, γ_Q, Ψ₂
- [Sisma](sisma.md) — combinazione sismica
- [Geotecnica](geotecnica.md) — profilo terrapieno (ε, L)
