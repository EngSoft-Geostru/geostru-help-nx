# Categoria de teren

## La ce servește

Categoria de teren determină amplificarea seismică așteptată pentru sit și condiționează valoarea parametrului **S** (coeficientul de amplificare stratigrafică) din spectrele de răspuns NTC 2018.

Dynamic Probing NX calculează automat categoria pe baza vitezelor V_s ale straturilor, derivate din corelațiile N_SPT → Vs.

## Normative suportate

| Normativă | Parametru de referință | Note |
|---|---|---|
| **NTC 2018** (D.M. 17/01/2018) | V_s,30 | Metodă principală pentru clădiri și lucrări |
| **NTC 2008** (D.M. 14/01/2008) | V_s,30 | Compatibilitate cu proiecte anterioare |
| **Eurocodul 8** (EN 1998-1) | V_s,30 | Referință europeană |

## Cum se calculează V_s,30

V_s,30 este viteza medie a undelor de forfecare în primii 30 m de adâncime, ponderată cu grosimile straturilor. Pentru adâncimi de foraj mai mici de 30 m, aplicația folosește un substrat seismic implicit (rocă) pentru metrii lipsă — această valoare este configurabilă în fila **Cat. teren**.

## Cum se citește rezultatul

În fila **Cat. teren** din Editor găsești:

- **V_s,eq**: viteza echivalentă calculată (m/s)
- **Categorie**: litera A / B / C / D / E (NTC 2018) cu descriere textuală
- **Tabelul straturilor**: contribuția fiecărui strat la calculul V_s,30

Calculul se actualizează automat de fiecare dată când modifici stratigrafie sau vitezele V_s ale straturilor.

!!! info "Vs din măsurători de laborator"
    Dacă dispui de măsurători directe de V_s (MASW, down-hole, cross-hole), poți suprascrie valoarea V_s a fiecărui strat în coloana dedicată din tabel — calculul V_s,30 folosește valorile introduse manual în locul celor estimate din corelații.

## Categorii NTC 2018

| Categorie | Descriere |
|---|---|
| **A** | Mase stâncoase aflorante sau terenuri foarte rigide (V_s,30 > 800 m/s) |
| **B** | Depozite de nisipuri, pietrișuri compacte sau argile rigide (360 < V_s,30 ≤ 800 m/s) |
| **C** | Depozite de nisipuri, pietrișuri mediu compacte sau argile de consistență medie (180 < V_s,30 ≤ 360 m/s) |
| **D** | Depozite de terenuri granulare afânate sau terenuri coezive moi (V_s,30 ≤ 180 m/s) |
| **E** | Profile cu straturi superficiale aluvionare cu V_s < 360 m/s și grosime cuprinsă între anumite limite pe substrat de categorie A sau B |
