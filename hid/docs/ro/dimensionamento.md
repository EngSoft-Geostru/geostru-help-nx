# Dimensionarea bazinului de retenție

## Hietograma de proiect

Hietograma distribuie în timp înălțimea de ploaie dată de curbă.

| Tip | Când se folosește |
|---|---|
| **Chicago** | Cea mai răspândită: vârful se poziționează cu coeficientul r |
| **Uniformă** | Intensitate constantă pe toată durata |
| **Sifalda** | Trei tronsoane, formă trapezoidală |
| **Triunghiulară** | Creștere și descreștere liniare |

Pentru Chicago, **coeficientul de poziție r** indică unde cade vârful: 0,4
înseamnă la 40 % din durată.

![Hietogramă și pierderi hidrologice](img/05-depurazione-piogge.png)

## Pierderi hidrologice

Transformă ploaia brută în ploaie netă, adică cea care devine scurgere.

- **Procentual** — înmulțește cu coeficientul de scurgere φ al suprafeței. Este
  modelul cel mai simplu și cel mai folosit.
- **Horton** — infiltrație descrescătoare în timp, în funcție de clasa de sol.
- **SCS-CN** — metoda curve number, cu condiția de umiditate antecedentă AMC I,
  II sau III.

!!! warning "Lombardia"
    Metoda SCS-CN nu este admisă de regulamentul regional.

## Hidrograf

Transformă ploaia netă în debit:

- **Timp de concentrare** — folosește timpul de concentrare al suprafeței.
- **Nash** — cascadă de n rezervoare liniare cu constanta K, pentru bazine mai
  complexe.

## Atenuare

Bazinul de retenție este rutat pas cu pas prin rezolvarea bilanțului de masă
între debitul intrat, debitul ieșit prin organul de evacuare și volumul
acumulat. Maximul volumului este rezultatul procedurii detaliate.

![Calcule și verificări](img/06-calcoli-verifiche.png)

## Verificările finale

| Verificare | Condiție |
|---|---|
| Înălțime utilă | H de proiect ≥ înălțimea necesară |
| Volum util | V de proiect ≥ volumul admisibil |
| Timp de golire | T ≤ timpul admis (de regulă 48 h) |

Timpul de golire este calculat doar pentru evacuările la debit constant și pentru
infiltrația constantă: pentru celelalte organe debitul depinde de sarcina
hidraulică și variază în timpul golirii.

---

*Ai găsit o eroare în această pagină? [Semnalează-ne-o](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
