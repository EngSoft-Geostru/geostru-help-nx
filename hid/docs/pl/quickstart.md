# Szybki start

Pięć minut od uruchomienia aplikacji do sprawdzonej objętości retencyjnej.
Wykorzystamy przykład wczytany fabrycznie z podręcznika, aby widoczne liczby były
porównywalne.

## 1. Otwórz aplikację i wczytaj przykład

Wejdź na [nx.geostru.ai/hid](https://nx.geostru.ai/hid/). Po uruchomieniu
załadowany jest już **przykład 9.4 — Procedura szczegółowa**: trzy powierzchnie o
łącznej wielkości 10 000 m².

![Pasek narzędzi HID](img/00-toolbar.png)

Wszystkie polecenia znajdują się na górnym pasku: **Nowy**, **Otwórz**,
**Zapisz**, **Operat**, a po prawej przycisk **Oblicz**.

## 2. Sprawdź powierzchnie

Otwórz sekcję **2. Powierzchnie i metody**. Każdy wiersz to jedna powierzchnia z
własną wielkością i własnym współczynnikiem spływu φ.

![Definicja powierzchni i wybór metod](img/02-aree-metodi.png)

Kolorowy pasek podaje wartości zagregowane: powierzchnię całkowitą, φ ważony,
zastępczą powierzchnię nieprzepuszczalną i dopuszczalne natężenie odpływu. Poniżej
wybierasz metody do porównania.

!!! tip "Wskazówka"
    Pozostaw aktywnych kilka metod. HID obliczy je wszystkie i przyjmie maksimum:
    to warunek najbardziej bezpieczny i pozwala uniknąć powtarzania pracy, gdy
    organ prowadzący postępowanie zażąda innej metody.

## 3. Zweryfikuj krzywą opadu

Sekcja **3. Krzywa IDF**. Przy krzywej dwuparametrowej wprowadzasz `a` i `n`;
przy GEV wprowadzasz parametry rozkładu oraz okres powtarzalności.

![Krzywa natężenie-czas trwania-częstość (IDF)](img/03-curva-pluviometrica.png)

## 4. Oblicz

Naciśnij **Oblicz** w prawym górnym rogu. Przejdź do sekcji **6. Obliczenia i
sprawdzenia**.

![Wyniki wymiarowania](img/06-calcoli-verifiche.png)

Każda metoda ma własną kartę z obliczoną objętością. Pasek poniżej podaje
przyjętą **objętość dopuszczalną**, odpowiadającą jej wysokość oraz czas
opróżniania.

Dla przykładu 9.4 powinieneś odczytać: metoda bezpośrednia 234,89 m³, metoda
czasu koncentracji 169,51 m³, procedura szczegółowa 175,74 m³, metoda opadów
175,58 m³. Przyjęta objętość wynosi **234,89 m³**.

## 5. Wygeneruj operat

Otwórz menu **Operat** na pasku i wybierz format: Word, PDF lub Word 97.
Dokument powstaje w języku wybranym w aplikacji.

---

*Znalazłeś błąd na tej stronie? [Zgłoś go nam](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
