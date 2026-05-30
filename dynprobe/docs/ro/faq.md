# Întrebări frecvente

## General

??? question "Care este diferența dintre Dynamic Probing NX și Dynamic Probing desktop?"
    GeoStru Dynamic Probing desktop este versiunea istorică pentru Windows. Dynamic Probing NX este versiunea web, accesibilă din orice browser fără instalare. Funcționalitățile principale sunt echivalente; NX adaugă suport multi-încercare (gestionarea unui întreg sit cu N încercări), harta interactivă, exportul AGS4 și integrarea cu GeoSection NX. Datele desktop se importă în NX prin formatul `.dypx`.

??? question "Datele sunt salvate pe server?"
    Nu — Dynamic Probing NX este **local-first**: datele proiectului se află în browserul tău (localStorage) și sunt salvate pe PC-ul tău numai când exporți fișierul `.dprobe`. Niciun dat de proiect nu este trimis pe serverele GeoStru.

??? question "Pot să îl folosesc offline?"
    Pentru încărcarea inițială a aplicației este necesară o conexiune. Odată încărcată, aplicația funcționează și offline pentru introducerea datelor și calcule (cu excepția generării raportului Word, care necesită conexiune).

??? question "Există o versiune mobilă?"
    Aplicația este proiectată pentru desktop/tabletă. Pe smartphone navigarea funcționează, dar introducerea înregistrărilor pe ecrane foarte mici este incomodă.

## Instrumente și înregistrări

??? question "Cum adaug un instrument care nu este în catalog?"
    Mergi la **Instrumente** din bara de navigare → **+ Adaugă instrument**. Introdu: nume, tip (DPL/DPM/DPH/DPSH), masa berbecului (kg), înălțimea de cădere (m), diametrul vârfului (mm), unghiul vârfului (°), pasul de avansare (m) și coeficientul β. Instrumentul este salvat în fișierul de proiect.

??? question "CSV-ul meu nu este recunoscut corect. Cum îl formatez?"
    Asigură-te că primele două coloane sunt adâncimea (m) și loviturile (număr întreg), separate prin virgulă, punct și virgulă sau tab. Elimină rândurile de antet care nu urmează acest format sau inserează-le ca comentarii cu `#` la începutul rândului. Dacă coordonatele sunt în antet, folosește formatul: `# lat=41.9028 lon=12.4964 cota=120`.

??? question "Pot exclude înregistrări din calcul?"
    Da — în fila Înregistrări, fiecare rând are o casetă de selectare pentru a-l exclude. Înregistrările excluse nu intră în agregarea N_SPT pe strat nici în corelații. Util pentru eliminarea valorilor anomale (refuz anticipat, pierdere de noroi).

## Stratigrafie

??? question "Cum aleg metoda de agregare N_SPT?"
    Depinde de obiectiv. Pentru o estimare medie conservativă folosește **Medie − 1σ**. Pentru valoarea caracteristică EC7 folosește **RNC** (distribuție normală) sau **RC** (log-normală). Dacă ai puține înregistrări pe strat (< 4), preferă Media simplă sau Minimul. Vezi [Stratigrafie →](stratigrafia.md) pentru descrierea completă a celor 7 metode.

??? question "Insigna Σ straturi este galbenă — ce înseamnă?"
    Suma adâncimilor inferioare ale straturilor nu coincide cu adâncimea încercării. Verifică că ultimul strat ajunge exact la adâncimea de final al încercării (ex. dacă încercarea este de 12,00 m, limita inferioară a ultimului strat trebuie să fie 12,00 m).

## Corelații

??? question "De ce unele valori de corelație apar ca —?"
    Pentru unele combinații tip teren / autor, parametrul nu este definit. De exemplu, Dr (densitate relativă) este definit numai pentru terenuri necoezive: în straturile coezive celula afișează —. Analogic, Cu (coeziunea nedrenată) este definit numai pentru coezive.

??? question "Pot introduce valorile de laborator în locul corelațiilor?"
    Momentan aplicația folosește corelațiile din N_SPT ca sursă primară. Pentru calculul capacității portante poți introduce direct Cu sau φ în câmpurile stratului din stratigrafie — acele valori le înlocuiesc pe cele corelate.

## Export și raport

??? question "Raportul Word este modificabil?"
    Da — este un fișier `.docx` standard deschis în Word, LibreOffice sau Google Docs. Poți personaliza antetul, adăuga logo-ul biroului tău și modifica textul descriptiv. Tabelele numerice sunt date statice (nu formule Excel).

??? question "Pot exporta în PDF?"
    Nu direct din aplicație. Deschide `.docx`-ul generat în Word și folosește **Fișier → Imprimare → Salvează ca PDF**.

??? question "AGS4: ce grupuri sunt exportate?"
    Sunt incluse grupurile: TRAN (date de transmitere), PROJ (proiect), LOCA (poziția încercărilor), GEOL (stratigrafie), DPRG (parametri încercare dinamică), DPRB (înregistrări de lovituri). Corelațiile și capacitatea portantă nu sunt exportate — aceste rezultate prelucrate nu fac parte din standardul AGS4 pentru încercări dinamice.
