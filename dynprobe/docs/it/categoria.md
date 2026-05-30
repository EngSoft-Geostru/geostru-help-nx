# Categoria di sottosuolo

## A cosa serve

La categoria di sottosuolo determina l'amplificazione sismica attesa per il sito e condiziona il valore del parametro **S** (coefficiente di amplificazione stratigrafica) negli spettri di risposta NTC 2018.

Dynamic Probing NX calcola automaticamente la categoria a partire dalle velocità V_s degli strati, derivate dalle correlazioni N_SPT → Vs.

## Normative supportate

| Normativa | Parametro di riferimento | Note |
|---|---|---|
| **NTC 2018** (D.M. 17/01/2018) | V_s,30 | Metodo principale per edifici e opere |
| **NTC 2008** (D.M. 14/01/2008) | V_s,30 | Compatibilità con progetti pregressi |
| **Eurocodice 8** (EN 1998-1) | V_s,30 | Riferimento europeo |

## Come si calcola V_s,30

V_s,30 è la velocità media delle onde di taglio nei primi 30 m di profondità, pesata per gli spessori degli strati. Per profondità del sondaggio minore di 30 m, l'app utilizza un substrato sismico di default (roccia) per i metri mancanti — questo valore è configurabile nella tab **Cat. suolo**.

## Come si legge il risultato

Nel tab **Cat. suolo** dell'Editor trovi:

- **V_s,eq**: velocità equivalente calcolata (m/s)
- **Categoria**: lettera A / B / C / D / E (NTC 2018) con descrizione testuale
- **Tabella strati**: contributo di ogni strato al calcolo V_s,30

Il calcolo si aggiorna automaticamente ogni volta che modifichi la stratigrafia o le velocità V_s degli strati.

!!! info "Vs da prove in laboratorio"
    Se disponi di misure dirette di V_s (MASW, down-hole, cross-hole), puoi sovrascrivere il valore V_s di ogni strato nella colonna dedicata della tabella — il calcolo V_s,30 usa i valori inseriti manualmente al posto di quelli stimati dalle correlazioni.

## Categorie NTC 2018

| Categoria | Descrizione |
|---|---|
| **A** | Ammassi rocciosi affioranti o terreni molto rigidi (V_s,30 > 800 m/s) |
| **B** | Depositi di sabbie, ghiaie compatte o argille rigide (360 < V_s,30 ≤ 800 m/s) |
| **C** | Depositi di sabbie, ghiaie mediamente compatte o argille di media consistenza (180 < V_s,30 ≤ 360 m/s) |
| **D** | Depositi di terreni granulari sciolti o terreni coesivi molli (V_s,30 ≤ 180 m/s) |
| **E** | Profili con strati superficiali alluvionali con V_s < 360 m/s e spessore compreso tra certi limiti su substrato di categoria A o B |
