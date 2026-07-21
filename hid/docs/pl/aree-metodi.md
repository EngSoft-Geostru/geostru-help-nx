# Powierzchnie i metody obliczeniowe

## Powierzchnie zlewni

Każdy wiersz tabeli to powierzchnia jednorodna pod względem użytkowania i
przepuszczalności. Potrzebne są opis, typ, wielkość w m² oraz współczynnik spływu
φ po inwestycji.

![Definicja powierzchni](img/02-aree-metodi.png)

Typ powierzchni (nieprzepuszczalna, półprzepuszczalna, przepuszczalna) jest
etykietą opisową sugerującą rząd wielkości φ; do obliczeń wchodzi zawsze wartość,
którą wpiszesz samodzielnie.

HID oblicza **ważony współczynnik spływu**:

$$\varphi_{pond} = \frac{\sum \varphi_i \cdot S_i}{\sum S_i}$$

oraz **zastępczą powierzchnię nieprzepuszczalną** $S_{pond} = S_{tot} \cdot \varphi_{pond}$,
czyli równoważną powierzchnię nieprzepuszczalną.

## Metody wymiarowania

HID rozróżnia metody **uniwersalne**, ważne wszędzie, oraz metody
**regulacyjne**, istniejące tylko tam, gdzie przepisy je nakazują.

### Wymagania minimalne

Jednostkowa objętość na hektar narzucona przez przepisy w zależności od strefy
krytyczności. W Lombardii wynosi 800, 500 lub 400 m³/ha zależnie od strefy A, B
lub C oraz od wersji rozporządzenia. Tam, gdzie przepisy tego nie określają,
objętość minimalną narzucasz sam.

### Metoda opadów

Bilansuje objętość dopływającą z objętością odprowadzaną przy stałym natężeniu,
poszukując czasu trwania maksymalizującego retencję. To metoda najczęściej
stosowana w obliczeniach uproszczonych.

!!! note "Czasy trwania krótsze niż godzina"
    Gdy krytyczny czas trwania spada poniżej godziny, HID stosuje wykładnik n₁
    krzywej, zgodnie z założeniami. Nie zaokrągla czasu trwania do jednej godziny:
    takie działanie zaniża objętość i jest błędem, który skorygowaliśmy, walidując
    aplikację względem wersji poprzedniej.

### Metoda czasu koncentracji

Wprowadza czas koncentracji zlewni, a więc uwzględnia kształt hydrogramu. Zwraca
krytyczny czas trwania i objętość.

### Metoda bezpośrednia

Porównuje jednostkowe objętości retencyjne przed i po inwestycji poprzez stosunek
współczynników spływu. W Emilia-Romagna i Marche przepisy nakazują wariant o
stałych współczynnikach, który HID udostępnia jako osobną metodę, **Regionalną
metodę bezpośrednią**, widoczną tylko w tych regionach.

### Procedura szczegółowa

To pełna symulacja: hietogram projektowy, straty opadu, hydrogram wezbrania i
retencja zbiornika krok po kroku. To metoda najbardziej pracochłonna i najlepiej
uzasadniona.

## Jak wybierana jest objętość

HID oblicza wszystkie wybrane metody i przyjmuje jako objętość dopuszczalną
**maksimum** z wyników. Metoda proponowana przez przepisy jest wskazana pod
polami wyboru, ale nie ogranicza tego, które metody możesz obliczyć.

---

*Znalazłeś błąd na tej stronie? [Zgłoś go nam](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
