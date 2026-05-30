# Export și raport

## Raport Word (.docx)

Raportul Word este raportul de calcul complet, gata de atașat la documentația de proiect. Se generează din meniul **Exportă → Raport**.

Documentul include:

- Antet cu datele sitului (nume, beneficiar, coordonate, dată)
- Fișa instrumentului: tip, parametri tehnici, β utilizat
- Profilul înregistrărilor de lovituri N/adâncime (grafic)
- Tabelul stratigrafiei: straturi, adâncimi, tip teren, N_SPT pe strat
- Tabelul corelațiilor geotehnice pentru fiecare strat (autori selectați)
- Categoria de teren: V_s,eq, categoria atribuită, tabelul straturilor
- Capacitatea portantă a fundațiilor (dacă este calculată): tabel comparativ metode
- Valorile caracteristice EC7 / NTC §6.2.2 (dacă sunt calculate)

## AGS4 (.ags)

Formatul **AGS4** este standardul deschis pentru schimbul de date geotehnice (AGS Data Format v4.2). Exportă-l din **Exportă → AGS4** pentru a partaja datele de încercare cu alte programe sau cu beneficiarul.

Grupurile incluse în exportul AGS4: TRAN, PROJ, LOCA, GEOL, DPRG (parametri încercare dinamică), DPRB (înregistrări).

## GeoSection (.geosection)

Exportă încercările cu stratigrafie interpretată spre **GeoSection NX** pentru a construi secțiunea geologică. Din **Exportă → GeoSection**: selectează încercările de inclus (cele cu coordonate), fă clic pe **Exportă**. Fișierul `.geosection` se deschide direct în aplicația GeoSection.

## Plan de situație (imagine PNG)

Dacă încercările au coordonate atribuite, din **Exportă → Plan de situație (imagine)** se obține o imagine PNG a planului de situație cu poziția încercărilor, cotele și distanțele dintre încercări. Disponibil numai cu cel puțin 2 încercări georeferențiate.

## KMZ (Google Earth)

Meniul **Exportă → KMZ** generează un fișier vizualizabil în Google Earth cu poziția tuturor încercărilor georeferențiate din proiect.

## Fișier de proiect (.dprobe)

Fișierul `.dprobe` este formatul nativ al Dynamic Probing NX — un JSON lizibil care conține toate informațiile proiectului (încercări, instrumente, stratigrafie, corelații, date de sit). Se salvează din **Fișier → Salvează** și se redeschide din Pagina principală cu **Deschide fișier…**.

!!! tip "Compatibilitate desktop"
    Poți importa un fișier `.dypx` (formatul text al GeoStru Dynamic Probing desktop) din Pagina principală a Dynamic Probing NX. Fișierul NX `.dprobe` nu poate fi deschis cu versiunea desktop.
