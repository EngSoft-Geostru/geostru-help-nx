# Curva di probabilità pluviometrica

La curva lega l'altezza di pioggia alla durata dell'evento per un dato tempo di
ritorno. È l'ingresso di ogni metodo di dimensionamento.

![Curva di probabilità pluviometrica](img/03-curva-pluviometrica.png)

## Curva a due parametri

La forma classica:

$$h(t) = a \cdot t^{n}$$

con `h` in mm e `t` in ore. Inserisci `a` (coefficiente pluviometrico orario) e
`n` (coefficiente di scala). Il parametro **n₁** governa le durate inferiori
all'ora, dove la curva ha pendenza diversa; il valore consueto è 0,5.

!!! example "Esempio"
    Con a = 46,49 e n = 0,364 la pioggia di 3 ore vale
    46,49 × 3^0,364 = 69,35 mm; quella di 24 ore vale 147,83 mm.

## Curva GEV

La distribuzione generalizzata dei valori estremi ricava il coefficiente `a` dal
coefficiente orario `a₁` e dal fattore di crescita legato al tempo di ritorno:

$$a = a_1 \cdot K_T$$

Inserisci i parametri α (alfa), k (kappa) ed ε (epsilon) e il tempo di ritorno.
HID calcola K_T e lo mostra accanto alla curva.

!!! warning "Lombardia"
    Il regolamento regionale impone la curva GEV. I parametri si ricavano dal
    servizio regionale di riferimento. Con la curva a due parametri HID blocca il
    calcolo.

## Tabella e grafico

Dopo il calcolo la tabella riporta le altezze alle 28 durate standard: 0, 0,25,
0,50, 0,75, 1 ora, poi ogni ora fino a 24. Il grafico sotto mostra la stessa
serie.

!!! note "Arrotondamenti"
    I valori sono calcolati in doppia precisione e arrotondati solo per la
    visualizzazione. Piccole differenze sull'ultima cifra rispetto ad altri
    software dipendono dal verso di arrotondamento, non dal calcolo.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
