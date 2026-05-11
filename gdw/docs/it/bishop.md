# Stabilità globale (Bishop semplificato)

La **stabilità globale** verifica che il complesso muro + terreno NON
collassi lungo una superficie di scorrimento circolare passante sotto la
fondazione. È un controllo essenziale per muri su versanti o terreni di
scarsa qualità.

## Metodo

GDW usa il **metodo di Bishop semplificato** (1955) per superfici circolari:

$$
FS = \frac{\sum \frac{c' \cdot b + (W \cdot (1 - k_v) - u \cdot b) \cdot \tan\varphi'}{m_\alpha(FS)}}{\sum [W \cdot (1 - k_v) \cdot \sin\alpha + k_h \cdot W \cdot (Y_c - Y_{cg})/R]}
$$

con:

$$
m_\alpha(FS) = \cos\alpha + \sin\alpha \cdot \frac{\tan\varphi'}{FS}
$$

dove:

- W = peso del concio (terreno + muro se il concio attraversa il muro + sovraccarico)
- b = larghezza orizzontale del concio
- α = angolo della base del concio
- u = pressione neutra alla base del concio (= γ_w · h_w se sotto falda)
- φ', c' = parametri ridotti del terreno (γ_M sismico applicato)
- R = raggio del cerchio
- Y_c = quota del centro del cerchio, Y_cg = quota baricentro del concio

L'equazione è **implicita in FS** (FS appare a destra in m_α). GDW risolve
iterativamente fino a convergenza (tipicamente 5÷10 iterazioni).

## Geometria del cerchio

Il cerchio di scorrimento è definito da **3 punti**:

- **Punto uscita a valle**: dove la superficie emerge dal terreno (lato valle del muro)
- **Punto ingresso a monte**: dove entra (lato monte, oltre il muro)
- **Punto base**: punto interno al cerchio, sotto il muro (forza il centro a stare sopra)

GDW costruisce il cerchio (centro + raggio) dai 3 punti tramite formula
analitica `FindCircle` (passaggio per 3 punti).

## Controllo automatico vs manuale

I 3 punti sono modificabili nella sezione **Stabilità globale**:

- Lasciandoli vuoti / `auto` → GDW sceglie posizioni geometricamente ragionevoli vicino alla fondazione
- Modificandoli a mano → puoi esplorare cerchi alternativi (più profondi, più ampi, ecc.)

!!! warning "Singolo cerchio, non ricerca automatica del critico"
    GDW calcola **un solo cerchio** alla volta, NON esegue la ricerca del
    cerchio critico (FS minimo) tramite ottimizzazione. Per esplorare diverse
    superfici di scorrimento e individuare quella critica, modifica
    manualmente i 3 punti del cerchio e ricalcola.
    
    Per analisi parametriche complete, esporta in GeoStru Slope o GSA.

## Validazione automatica

Prima del calcolo Bishop, GDW verifica che il cerchio:

1. Passi **SOTTO la fondazione** (faccia inferiore inclinata se β > 0). La quota limite varia linearmente da `FondBottomYValle` (lato sx) a `FondBottomYMonte` (lato dx).
2. Non attraversi il muro o la fondazione in nessun punto.

Se viola questi vincoli, GDW restituisce un errore esplicito:

> *"La superficie di scorrimento attraversa il muro o la fondazione a X=X.XXm.
> I punti di vincolo del cerchio devono essere posizionati in modo che la
> superficie passi SOTTO la base."*

## Inversione automatica valle/monte

Se inserisci il punto valle con X > X del punto monte, GDW li scambia
automaticamente per coerenza geometrica e mostra un messaggio informativo:

> *"I punti valle/monte sono stati scambiati per coerenza geometrica (valle a
> sinistra, monte a destra)."*

## Conci

Il cerchio viene discretizzato in **N conci** (default 30, range 4÷200). Più
conci = maggiore accuratezza, più lento il calcolo. 30 è un buon trade-off
per la maggior parte dei casi.

Per ogni concio GDW calcola:

- W (peso): terreno × γ + muro × γ_G + sovraccarico × q + peso falda
- u (pressione neutra): γ_w · profondità sotto falda
- α (angolo base): dalla geometria del cerchio
- Phi, c effettivi (dello strato che attraversa la base del concio)

I conci che attraversano il muro hanno W = W_terreno + W_muro_parziale.

## Coefficienti

Per la stabilità globale (NTC tab. 6.5.I):

- **A2** (parametri ridotti): γ_Mφ = γ_Mc = **1.25** (statico) o **1.0** (sismico)
- **R2**: γ_R = **1.1** (statico) o **1.2** (sismico)

Verifica: **FS_Bishop ≥ γ_R2** (cioè 1.1 statico, 1.2 sismico).

## Visualizzazione

Sezione **Stabilità globale** in fondo alla pagina dei risultati:

- Disegno della sezione (terreno + muro + foundazione + cerchio)
- Conci colorati (giallo = terreno, rosso semitrasparente = parte muro)
- Centro O e raggio R indicati
- FS calcolato, log dettagliato dei conci, badge ✓/✗

## Pannello debug

Il `BishopDebugLog` (visibile in modalità DebugCalcolo abilitata) mostra:

- I 3 punti del cerchio, centro, raggio
- Per ogni concio: x, larghezza, base Y, alpha, W, u, contributi al numeratore/denominatore
- Iterazioni e FS finale

Utile per validare numericamente in casi controversi.

## Vedi anche

- [Fondazione](fondazione.md) — validazione cerchio sotto fondazione inclinata
- [Coefficienti NTC](coefficienti.md) — A2·M2·R2 per stabilità globale
- [Sisma](sisma.md) — k_h, k_v entrano nel calcolo Bishop
