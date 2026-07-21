# HID NX — Invarianță hidraulică

HID dimensionează sistemele de atenuare pentru **invarianța hidraulică și
hidrologică**: verifică faptul că o intervenție de transformare a terenului nu
mărește debitul evacuat în receptor față de situația anterioară.

Aplicația compară în paralel metodele de calcul pe care le selectezi și adoptă ca
volum de retenție **maximul rezultatelor**, astfel încât verificarea rămâne
valabilă indiferent de metoda cerută de autoritatea care instrumentează dosarul.

[**Deschide aplicația**](https://nx.geostru.ai/hid/){ .md-button .md-button--primary }

![Interfața HID NX, secțiunea Date generale](img/01-dati-generali.png)

## Cui se adresează

Celor care proiectează lucrări de atenuare a apelor meteorice: ingineri
hidrotehnicieni, geologi și proiectanți care trebuie să anexeze un memoriu de
invarianță hidraulică la o autorizație de construire, la un plan urbanistic sau la
o autorizație de evacuare.

## Ce calculează

| Domeniu | Conținut |
|---|---|
| Ploi | Curbă intensitate-durată-frecvență (IDF) GEV sau cu doi parametri |
| Hietograme | Chicago, uniformă, Sifalda, triunghiulară |
| Pierderi hidrologice | Coeficient de scurgere, Horton, SCS-CN |
| Hidrografe | Metoda timpului de concentrare și Nash |
| Dimensionare | Cerințe minime, metoda ploilor, metoda directă, metoda timpului de concentrare, procedură detaliată |
| Evacuare | Opt organe, de la orificii înecate la puțuri absorbante |
| Verificări | Înălțime utilă, volum util, timp de golire |

## Reglementări

HID aplică **profiluri de reglementare** alese în funcție de țară și regiune.
Profilul stabilește ce metode sunt admise, ce date sunt necesare și dacă debitul
maxim admis și volumul minim sunt impuse de reglementare sau le alegi tu.

- **Lombardia** — R.R. 7/2017, completarea 2019, R.R. 3/2025: curbă GEV
  obligatorie, SCS-CN exclus, criticitatea și debitul maxim admis deduse din
  localitate.
- **Emilia-Romagna și Marche** — metoda directă regională cu n = 0,48.
- **Orice altă țară sau regiune** — profil generic: metode combinabile liber,
  debit maxim admis și volum minim alese de tine.

!!! note "În afara Italiei"
    Acolo unde nu există un nomenclator al localităților, regiunea și
    coordonatele se introduc manual. Nu este o eroare: este modul prevăzut de
    lucru în țările care încă nu sunt acoperite de un profil dedicat.

## De unde să începi

- [Ghid rapid](quickstart.md) — prima dimensionare în cinci minute
- [Flux de lucru complet](workflow.md) — un proiect real de la început până la memoriu
- [Glosar](glossario.md) — termenii domeniului, cu simbolurile folosite în aplicație

---

*Ai găsit o eroare în această pagină? [Semnalează-ne-o](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
