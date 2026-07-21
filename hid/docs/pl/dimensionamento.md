# Wymiarowanie zbiornika retencyjnego

## Hietogram projektowy

Hietogram rozkłada w czasie wysokość opadu wynikającą z krzywej.

| Typ | Kiedy stosować |
|---|---|
| **Chicago** | Najczęściej stosowany: położenie szczytu ustalane współczynnikiem r |
| **Równomierny** | Stałe natężenie przez cały czas trwania |
| **Sifalda** | Trzy odcinki, kształt trapezowy |
| **Trójkątny** | Liniowy wzrost i opadanie |

Dla hietogramu Chicago **współczynnik położenia r** wskazuje, gdzie wypada
szczyt: 0,4 oznacza 40 % czasu trwania.

![Hietogram i straty opadu](img/05-depurazione-piogge.png)

## Straty opadu

Przekształcają opad całkowity w opad efektywny, czyli w tę część, która staje się
spływem.

- **Procentowy** — mnoży przez współczynnik spływu φ powierzchni. To model
  najprostszy i najczęściej używany.
- **Horton** — infiltracja malejąca w czasie zależnie od klasy gruntu.
- **SCS-CN** — metoda curve number, z uprzednim stanem wilgotności AMC I, II lub
  III.

!!! warning "Lombardia"
    Metoda SCS-CN nie jest dopuszczona przez rozporządzenie regionalne.

## Hydrogram

Przekształca opad efektywny w natężenie przepływu:

- **Metoda czasu koncentracji** — wykorzystuje czas koncentracji powierzchni.
- **Nash** — kaskada n zbiorników liniowych o stałej K, dla zlewni bardziej
  złożonych.

## Retencja

Przepływ przez zbiornik jest prowadzony krok po kroku poprzez rozwiązanie bilansu
masy między natężeniem dopływu, natężeniem odpływu z urządzenia odpływowego i
objętością zgromadzoną. Maksimum objętości jest wynikiem procedury szczegółowej.

![Obliczenia i sprawdzenia](img/06-calcoli-verifiche.png)

## Sprawdzenia końcowe

| Sprawdzenie | Warunek |
|---|---|
| Wysokość użyteczna | H projektowa ≥ wysokość wymagana |
| Objętość użyteczna | V projektowa ≥ objętość dopuszczalna |
| Czas opróżniania | T ≤ czas dopuszczalny (zwykle 48 h) |

Czas opróżniania jest obliczany wyłącznie dla odpływów o stałym natężeniu oraz
dla stałej infiltracji: dla pozostałych urządzeń natężenie zależy od wysokości
napełnienia i zmienia się w trakcie opróżniania.

---

*Znalazłeś błąd na tej stronie? [Zgłoś go nam](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
