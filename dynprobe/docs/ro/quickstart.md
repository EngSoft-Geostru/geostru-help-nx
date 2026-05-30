# Ghid rapid — primul proiect în 5 minute

Obiectiv: încărcarea unui fișier de exemplu, citirea stratigrafiei și a corelațiilor principale, exportul raportului.

## 1. Deschide aplicația și creează un proiect nou

Mergi la [nx.geostru.ai/dynprobe](https://nx.geostru.ai/dynprobe/). Fă clic pe **Fișier nou** din meniul Fișier.  
Dă un nume proiectului (ex. "Sit strada Roma") și fă clic pe **Creează**.

Ca alternativă, folosește un **fișier de exemplu** din ecranul de start — vei vedea imediat toate secțiunile deja completate.

## 2. Adaugă o încercare

În **Dashboard** fă clic pe **+ Încercare continuă** (sau **+ Încercare în foraj** pentru SPT). Introdu:

- **Siglă**: codul de identificare al încercării (ex. `DP-1`)
- **Instrument**: selectează din catalog (DPM, DPSH, DPH, DPL…). Instrumentul definește masa berbecului, înălțimea de cădere și pasul de avansare — toți parametrii energetici sunt deja tabulați intern.
- **Coordonate**: introdu lat/lon pentru a poziționa încercarea pe hartă (opțional, dar util pentru exportul planului de situație).

## 3. Introdu înregistrările

Mergi în fila **Înregistrări**. Ai trei moduri:

- **Manual**: tastează numărul de lovituri rând cu rând.
- **Importă CSV**: lipește sau încarcă un fișier de la datalogger — sistemul recunoaște automat adâncimea și loviturile.
- **Importă .dypx**: încarcă direct un fișier exportat din GeoStru Dynamic Probing desktop.

Graficul N/adâncime se actualizează în timp real.

## 4. Interpretează stratigrafie

Mergi în fila **Stratigrafie interpretată**. Aplicația propune un prim strat pe întreaga adâncime.

- Fă clic pe **+ Adaugă strat** pentru a subdiviza profilul.
- Pentru fiecare strat setează adâncimea inferioară, **tipul de teren** (coeziv / necoeziv / mixt) și **greutatea volumică** γ.
- Metoda de agregare N_SPT pe strat se alege în antetul coloanei (implicit: medie). Vezi [Stratigrafie →](stratigrafia.md) pentru cele 7 metode disponibile.

!!! tip "Culori și insigne"
    Insigna **Σ straturi / încercare** din partea de jos arată dacă suma adâncimilor straturilor coincide cu adâncimea încercării (bifă verde = coerent, triunghi galben = abatere de verificat).

## 5. Citește corelațiile

Fila **Corelații geotehnice**: pentru fiecare strat apare un tabel cu parametrii estimați (Cu, φ, Mo, Ey, Vs, γ, Dr …) calculați din formulele de referință din literatura geotehnică. Vezi [Corelații →](correlazioni.md).

!!! note
    Corelațiile sunt estimări empirice. Folosește-le ca punct de plecare — completează întotdeauna cu date de laborator când sunt disponibile.

## 6. Verifică categoria de teren

Fila **Cat. teren**: aplicația calculează viteza echivalentă V_s,30 și atribuie automat categoria NTC 2018. Vezi [Categorie →](categoria.md).

## 7. Exportă raportul

Meniu **Fișier → Salvează** pentru a descărca fișierul `.dprobe`. Meniu **Exportă → Raport Word** pentru raportul complet.

În 5 minute ai obținut:

- ✅ o încercare cu înregistrări
- ✅ o stratigrafie interpretată
- ✅ parametrii geotehnici pentru fiecare strat
- ✅ categoria de teren
- ✅ fișierul de proiect descărcat
