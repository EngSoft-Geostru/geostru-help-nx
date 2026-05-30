# Instrumente — DPL · DPM · DPH · DPSH · SPT în foraj

## Încercări dinamice continue

În încercarea dinamică continuă berbecul cade în mod repetat și se numără numărul de lovituri necesare pentru a avansa vârful cu un pas fix (de obicei 10 sau 20 cm). Secvența lovituri/adâncime este materia primă a întregii prelucrări.

Dynamic Probing NX suportă cele patru tipuri normalizate prin **UNI EN ISO 22476-2**:

| Siglă | Tip | Energie per lovitură |
|---|---|---|
| **DPL** | Ușor | scăzută |
| **DPM** | Mediu | medie |
| **DPH** | Greu | ridicată |
| **DPSH** | Super greu | foarte ridicată |

Fiecare tip are masa berbecului, înălțimea de cădere și diametrul vârfului definite de normă. În biblioteca de instrumente a aplicației găsești modelele cele mai răspândite pe piață deja tabulate — poți adăuga și un instrument personalizat cu datele tale de calibrare.

### Coeficientul de corelație β

Coeficientul β convertește numărul de lovituri al încercării dinamice (N_DPM, N_DPSH…) în echivalentul N_SPT. Valoarea depinde de instrument și se determină prin încercări comparative in situ. Fiecare instrument din catalog are un β implicit; îl poți suprascrie cu valoarea calibrării tale specifice.

## Încercări SPT în foraj

Încercarea SPT (Standard Penetration Test, **UNI EN ISO 22476-3**) se execută în interiorul unui foraj. Se bat 45 cm în trei tronsoane de câte 15 cm:

- **N1**: primul tronson (aşezare) — nu intră în calcul
- **N2** + **N3**: al doilea și al treilea tronson → **N_SPT = N2 + N3**

Adaugă o încercare SPT în foraj din Dashboard cu butonul **+ Încercare în foraj**. Definește cotele de start ale fiecărei batere (ex. 1,0 m — 2,5 m — 4,0 m) și pentru fiecare introdu N1, N2, N3. Aplicația calculează automat N_SPT și construiește profilul.

### Stratigrafie pentru încercările în foraj

Pentru încercările SPT în foraj, stratigrafie se introduce manual în secțiunea **Stratigrafie interpretată**, strat cu strat, exact ca pentru încercările continue. N_SPT mediu pe strat se calculează din baterile care se încadrează în intervalul de adâncime al stratului.

## Biblioteca de instrumente

Mergi la **Instrumente** din bara de navigare pentru a accesa biblioteca. Poți:

- Vizualiza parametrii fiecărui instrument (masă, înălțime cădere, diametru vârf, unghi vârf, pas, β)
- Adăuga un instrument personalizat
- Modifica β al unui model existent pentru dataloggerul tău specific

Instrumentele sunt salvate în fișierul de proiect `.dprobe` — fișierul este autonom și portabil pe alt PC fără a pierde datele de calibrare.
