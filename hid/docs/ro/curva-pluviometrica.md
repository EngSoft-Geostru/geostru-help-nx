# Curbă intensitate-durată-frecvență

Curba leagă înălțimea de ploaie de durata evenimentului pentru o perioadă de
revenire dată. Este intrarea fiecărei metode de dimensionare.

![Curbă intensitate-durată-frecvență](img/03-curva-pluviometrica.png)

## Curba cu doi parametri

Forma clasică:

$$h(t) = a \cdot t^{n}$$

cu `h` în mm și `t` în ore. Introdu `a` (coeficient pluviometric orar) și `n`
(coeficient de scară). Parametrul **n₁** guvernează duratele sub o oră, unde
curba are altă pantă; valoarea uzuală este 0,5.

!!! example "Exemplu"
    Cu a = 46,49 și n = 0,364, ploaia de 3 ore are 46,49 × 3^0,364 = 69,35 mm;
    cea de 24 de ore are 147,83 mm.

## Curba GEV

Distribuția generalizată a valorilor extreme deduce coeficientul `a` din
coeficientul orar `a₁` și din factorul de creștere legat de perioada de revenire:

$$a = a_1 \cdot K_T$$

Introdu parametrii α (alfa), k (kappa) și ε (epsilon) și perioada de revenire.
HID calculează K_T și îl afișează alături de curbă.

!!! warning "Lombardia"
    Regulamentul regional impune curba GEV. Parametrii se obțin de la serviciul
    regional de referință. Cu curba cu doi parametri HID blochează calculul.

## Tabel și grafic

După calcul, tabelul prezintă înălțimile pentru cele 28 de durate standard: 0,
0,25, 0,50, 0,75, 1 oră, apoi din oră în oră până la 24. Graficul de dedesubt
afișează aceeași serie.

!!! note "Rotunjiri"
    Valorile sunt calculate în dublă precizie și rotunjite doar pentru afișare.
    Mici diferențe la ultima cifră față de alte programe depind de sensul
    rotunjirii, nu de calcul.

---

*Ai găsit o eroare în această pagină? [Semnalează-ne-o](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
