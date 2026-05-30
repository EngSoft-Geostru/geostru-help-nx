# Formate fișiere

## .dprobe — formatul nativ NX

Fișierul `.dprobe` este formatul de proiect al Dynamic Probing NX. Este un fișier **JSON** în clar, lizibil cu orice editor de text. Conține:

- Metadate ale proiectului (nume, sit, beneficiar, coordonate)
- Lista încercărilor cu toate înregistrările
- Biblioteca de instrumente înglobată în fișier
- Stratigrafie interpretată (straturi, adâncimi, tip, γ)
- Setări corelații (autori preferați)
- Rezultate calculate (corelații, categoria de teren, capacitate portantă, estimare parametri)

Fișierul este **autonom și portabil**: copiază-l pe alt PC, deschide-l în Dynamic Probing NX — totul funcționează fără configurare suplimentară.

## .dypx — formatul desktop GeoStru (import)

Fișierul `.dypx` este formatul de export text al GeoStru Dynamic Probing desktop. Dynamic Probing NX îl poate importa din ecranul de start cu **Importă .dypx…**. La import sunt citite:

- Toate încercările cu înregistrările de lovituri
- Datele instrumentului (tip, β dacă este prezent)
- Coordonatele încercărilor (dacă sunt salvate în fișierul desktop)

Stratigrafie și corelațiile nu sunt importate din desktop — trebuie reintroduse în NX.

## CSV datalogger

Mulți dataloggeri pentru încercări dinamice exportă datele în format CSV sau TXT. Dynamic Probing NX recunoaște automat formatul dacă coloanele sunt structurate astfel:

```
adâncime, lovituri
0.10, 8
0.20, 9
0.30, 11
...
```

Coloanele pot fi separate prin virgulă, punct și virgulă sau tab. Dacă fișierul are un antet cu coordonatele sitului (lat, lon, cotă), acestea sunt citite automat.

Pentru a importa: în fila **Înregistrări** din editor, fă clic pe **Importă înregistrări din fișier…** și selectează CSV-ul. Ca alternativă, lipește conținutul direct în câmpul text al modalului.

## AGS4 (.ags)

Dynamic Probing NX exportă în format AGS4 (v4.2) dar nu importă din AGS4. Vezi [Export →](export.md).
