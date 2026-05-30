# Capacitate portantă fundații

## Fundații superficiale

Dynamic Probing NX calculează **presiunea admisibilă** pentru fundații superficiale pe terenuri granulare și coezive conform metodelor de referință din literatura geotehnică. Rezultatele sunt exprimate în kPa.

### Metode disponibile

| Metodă | Tip de teren | Note |
|---|---|---|
| **Terzaghi-Peck** | Nisipuri, pietrișuri | Clasică din N_SPT, include corectarea tasării |
| **Meyerhof** | Nisipuri, pietrișuri | Ține cont de forma și adâncimea fundației |
| **Bazaraa** | Nisipuri, pietrișuri | Alternativă conservativă la Meyerhof |
| **Peck-Hanson-Thornburn** | Nisipuri, pietrișuri | Cu limita de tasare admisibilă |
| **Meigh-Hobbs** | Argile | Din N_SPT pentru terenuri coezive |
| **De Beer-Martens** | Nisipuri | Metodă europeană |

### Date de intrare necesare

În fila **Capacitate portantă** setează:

- **Lățimea fundației B** (m)
- **Adâncimea de pozare D** (m față de cota terenului)
- **Tasarea admisibilă** (mm) — în mod tipic 25 mm pentru fundații continue, 25–50 mm pentru fundații izolate
- **Stratul de calcul**: metoda folosește N_SPT al stratului în care este amplasată fundația

### Citirea rezultatului

Tabelul arată presiunea admisibilă q_adm pentru fiecare metodă. Raportul prezintă toate metodele comparativ — alege-o pe cea mai adecvată contextului stratigrafic.

!!! warning "Fundații pe argile"
    Pentru fundații pe argile, calculul se bazează pe Cu derivat din corelația N_SPT → Cu. Completează cu încercări de laborator (triaxial, consolidare) pentru proiectele definitive.

## Fundații adânci — pilot înfipt (Meyerhof)

Pentru piloții înfipți, aplicația implementează metoda **Meyerhof** care estimează separat:

- **Q_p**: capacitatea portantă pe vârf (contribuția stratului de sub vârful pilotului)
- **Q_l**: capacitatea portantă laterală (contribuția straturilor traversate de pilot)
- **Q_tot = Q_p + Q_l − W_p**: capacitatea portantă totală după deducerea greutății proprii a pilotului

### Date de intrare necesare

- **Diametrul pilotului** D (m)
- **Lungimea pilotului** L (m)
- **Tipul pilotului**: metoda Meyerhof distinge între piloți înfipți în nisip și în argilă

Calculul folosește valorile N_SPT ale straturilor conform distribuției de adâncime definite în stratigrafie. Capacitatea portantă totală este raportată în kN.

!!! info "Coeficient de siguranță"
    Capacitatea portantă admisibilă se obține împărțind capacitatea portantă ultimă la coeficientul de siguranță global. Dynamic Probing NX raportează capacitatea portantă ultimă — aplicarea coeficientului de siguranță este de competența proiectantului conform normativului aplicabil.
