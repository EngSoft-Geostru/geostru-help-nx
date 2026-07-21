# Formaty plików

## Projekt `.hid`

HID zapisuje projekt w pliku `.hid`, który jest formatem JSON czytelnym w
dowolnym edytorze tekstu.

```json
{
  "schemaVersion": 2,
  "name": "Esempio 9.4 — Procedura dettagliata",
  "general": { "country": "IT", "region": "", "regulationVersion": "rr-2017" },
  "surfaces": [ { "description": "Area impermeabile", "areaM2": 4000, "runoffPost": 0.95 } ],
  "rainfall": { "kind": "twoParameters", "a": 35.04, "n": 0.421 }
}
```

Pole `schemaVersion` zabezpiecza przed otwarciem plików utworzonych w nowszych
wersjach aplikacji: jeśli numer jest wyższy niż obsługiwany, HID odrzuca plik,
zamiast odczytać go błędnie.

!!! note "Uwaga"
    Dane wejściowe wymagane przez przepisy przechowywane są w słowniku
    `jurisdictionInputs`. Dzięki temu dodanie obsługi nowego kraju nie zmienia
    formatu pliku: już zapisane projekty pozostają czytelne.

## Zapis i otwieranie

- **Zapisz** pobiera plik `.hid` na Twój komputer.
- **Otwórz** wczytuje istniejący plik `.hid`.
- **GeoDropbox** zapisuje i ponownie otwiera projekt w przestrzeni chmurowej
  GeoStru, dostępnej z tego samego paska narzędzi.

## Operat obliczeniowy

Z menu **Operat** wybierz format:

| Format | Rozszerzenie | Uwagi |
|---|---|---|
| Word | `.docx` | Zawsze dostępny |
| PDF | `.pdf` | Wymaga konwertera po stronie serwera |
| Word 97 | `.doc` | Wymaga konwertera po stronie serwera |

Jeśli PDF i Word 97 nie pojawiają się w menu, konwerter nie jest dostępny na tym
serwerze: użyj formatu Word.

Operat zawiera odniesienia normatywne, dane ogólne, powierzchnie zlewni, krzywą
IDF, parametry hydrologiczne, hietogram, wymiarowanie, system odpływu,
sprawdzenia końcowe i hydrogram, wraz z osadzonymi wykresami.

!!! tip "Wskazówka"
    Operat powstaje w języku wybranym na pasku narzędzi. Zmień język przed jego
    wygenerowaniem, jeśli przekazujesz go zagranicznemu organowi.

---

*Znalazłeś błąd na tej stronie? [Zgłoś go nam](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
