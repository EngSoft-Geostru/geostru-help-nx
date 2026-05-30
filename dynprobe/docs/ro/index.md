# Dynamic Probing NX

> Prelucrarea **încercărilor de penetrare dinamică** (DPL · DPM · DPH · DPSH) și **SPT în foraj** — stratigrafie automată, corelații geotehnice, categoria de teren NTC 2018, capacitate portantă a fundațiilor superficiale și adânci, valori caracteristice EC7 / NTC §6.2.2.

[**Deschide aplicația**](https://nx.geostru.ai/dynprobe/){ .md-button .md-button--primary }
[Ghid rapid (5 minute)](quickstart.md){ .md-button }

---

## Rezumat

- **Ce face**: citește înregistrările de teren ale unei încercări dinamice continue sau ale unei serii de încercări SPT în foraj, returnează stratigrafiei interpretate cu parametrii geotehnici caracteristici și verificările de capacitate portantă, toate conforme cu normele în vigoare (NTC 2018, NTC 2008, EC8, Eurocodul 7).
- **Pentru cine**: geologi și ingineri geotehnici care trebuie să prelucreze foraje dinamice, să clasifice profilul stratigrafic și să producă raportul de calcul.
- **În câte minute**: 5 (cazul cu fișierul .dypx de exemplu) → 30 (cazul real complet cu stratigrafie, corelații și capacitate portantă).

## Flux de lucru tipic

1. Deschide aplicația: `nx.geostru.ai/dynprobe/`
2. Creează un fișier nou sau importă un `.dypx` din GeoStru desktop sau un CSV de la datalogger.
3. Mergi la **Date generale** și completează informațiile despre sit (nume, coordonate, instrument, beneficiar).
4. Introdu (sau verifică) **înregistrările de lovituri** în fila Înregistrări: aplicația le afișează imediat în graficul N/adâncime.
5. Treci la **Stratigrafie interpretată**: definește numărul de straturi, limitele și tipul de teren (coeziv / necoeziv). Aplicația calculează N_SPT mediu pe strat cu metoda aleasă.
6. Consultă **Corelațiile geotehnice** — pentru fiecare strat, un tabel cu parametrii derivați (Cu, φ, Mo, Ey, Vs, γ …).
7. Verifică **Categoria de teren** conform NTC 2018 / NTC 2008 / EC8.
8. Dacă este necesar, calculează **Capacitatea portantă** a unei fundații superficiale sau adânci (pilot înfipt Meyerhof).
9. Citește **Valorile caracteristice** EC7 / NTC §6.2.2 în fila dedicată.
10. Exportă **raportul Word** (Raport) sau fișierul de proiect `.dprobe`.

## Capitolele manualului

| Capitol | Conținut |
|---|---|
| [Ghid rapid](quickstart.md) | De la încărcarea fișierului la primul rezultat în 5 minute |
| [Instrumente](strumenti.md) | DPL, DPM, DPH, DPSH, SPT în foraj — cum se introduc și parametrii relevanți |
| [Stratigrafie interpretată](stratigrafia.md) | Cum se definesc straturile, cele 7 metode de agregare N_SPT |
| [Corelații geotehnice](correlazioni.md) | Parametri derivați pentru terenuri coezive și necoezive, autori de referință |
| [Categoria de teren](categoria.md) | NTC 2018, NTC 2008, EC8 — date de intrare, logică de calcul, citirea rezultatului |
| [Capacitate portantă fundații](portanze.md) | Fundații superficiale (6 metode) și adânci (Meyerhof pilot înfipt) |
| [Valori caracteristice](caratter.md) | EC7 §2.4.5.2 / NTC §6.2.2 — normală, lognormală, Student-t |
| [Export și raport](export.md) | Raport Word, AGS4, GeoSection, plan de situație, KMZ |
| [Formate fișiere](formati.md) | `.dprobe` (JSON NX) · `.dypx` (desktop) · CSV datalogger |
| [Resurse și exemple](risorse.md) | Fișiere de exemplu descărcabile |
| [Întrebări frecvente](faq.md) | Întrebări frecvente |
