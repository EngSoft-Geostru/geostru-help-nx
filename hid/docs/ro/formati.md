# Formate de fișier

## Proiect `.hid`

HID salvează proiectul într-un fișier `.hid`, care este JSON lizibil cu orice
editor de text.

```json
{
  "schemaVersion": 2,
  "name": "Esempio 9.4 — Procedura dettagliata",
  "general": { "country": "IT", "region": "", "regulationVersion": "rr-2017" },
  "surfaces": [ { "description": "Area impermeabile", "areaM2": 4000, "runoffPost": 0.95 } ],
  "rainfall": { "kind": "twoParameters", "a": 35.04, "n": 0.421 }
}
```

Câmpul `schemaVersion` protejează împotriva deschiderii fișierelor produse de
versiuni mai recente ale aplicației: dacă numărul este mai mare decât cel
suportat, HID refuză fișierul în loc să îl citească greșit.

!!! note "Notă"
    Datele de intrare cerute de reglementare se află într-un dicționar
    `jurisdictionInputs`. Astfel, adăugarea suportului pentru o țară nouă nu
    modifică formatul fișierului: proiectele deja salvate rămân lizibile.

## Salvare și deschidere

- **Salvează** descarcă fișierul `.hid` pe calculatorul tău.
- **Deschide** încarcă un fișier `.hid` existent.
- **GeoDropbox** salvează și redeschide proiectul din spațiul cloud GeoStru,
  accesibil din aceeași bară de instrumente.

## Memoriu de calcul

Din meniul **Memoriu** alege formatul:

| Format | Extensie | Note |
|---|---|---|
| Word | `.docx` | Întotdeauna disponibil |
| PDF | `.pdf` | Necesită convertorul de pe server |
| Word 97 | `.doc` | Necesită convertorul de pe server |

Dacă PDF și Word 97 nu apar în meniu, convertorul nu este disponibil pe acel
server: folosește formatul Word.

Memoriul conține referințele normative, datele generale, suprafețele de
colectare, curba IDF, parametrii hidrologici, hietograma, dimensionarea, sistemul
de evacuare, verificările finale și hidrograful, cu graficele incorporate.

!!! tip "Recomandare"
    Memoriul este generat în limba selectată în bara de instrumente. Schimbă
    limba înainte de a-l genera, dacă îl predai unei autorități străine.

---

*Ai găsit o eroare în această pagină? [Semnalează-ne-o](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
