# HID NX — Inwariantność hydrauliczna

HID wymiaruje systemy retencji zapewniające **inwariantność hydrauliczną i
hydrologiczną**: sprawdza, czy przekształcenie terenu nie zwiększa natężenia
odpływu do odbiornika w stosunku do stanu poprzedniego.

Aplikacja porównuje równolegle wybrane przez Ciebie metody obliczeniowe i
przyjmuje jako objętość retencyjną **maksimum z wyników**, dzięki czemu
obliczenie pozostaje ważne niezależnie od metody wymaganej przez organ
prowadzący postępowanie.

[**Otwórz aplikację**](https://nx.geostru.ai/hid/){ .md-button .md-button--primary }

![Interfejs HID NX, sekcja Dane ogólne](img/01-dati-generali.png)

## Dla kogo

Dla projektantów obiektów retencji wód opadowych: inżynierów hydrotechników,
geologów i projektantów, którzy muszą załączyć operat inwariantności
hydraulicznej do pozwolenia na budowę, planu realizacyjnego lub pozwolenia
wodnoprawnego na odprowadzanie wód.

## Co oblicza

| Zakres | Zawartość |
|---|---|
| Opady | Krzywa natężenie-czas trwania-częstość (IDF) GEV lub dwuparametrowa |
| Hietogramy | Chicago, równomierny, Sifalda, trójkątny |
| Straty opadu | Współczynnik spływu, Horton, SCS-CN |
| Hydrogramy | Metoda czasu koncentracji i Nash |
| Wymiarowanie | Wymagania minimalne, metoda opadów, metoda bezpośrednia, metoda czasu koncentracji, procedura szczegółowa |
| Odpływ | Osiem urządzeń, od otworów zatopionych po studnie chłonne |
| Sprawdzenia | Wysokość użyteczna, objętość użyteczna, czas opróżniania |

## Przepisy

HID stosuje **profile regulacyjne** dobierane według kraju i regionu. Profil
określa, które metody są dopuszczalne, jakie dane są potrzebne oraz czy
dopuszczalne natężenie odpływu i objętość minimalna wynikają z przepisów, czy
wybierasz je samodzielnie.

- **Lombardia** — R.R. 7/2017, uzupełnienie z 2019 r., R.R. 3/2025: krzywa GEV
  obowiązkowa, SCS-CN wykluczone, strefa krytyczności i dopuszczalne natężenie
  odpływu wyznaczane na podstawie gminy.
- **Emilia-Romagna i Marche** — regionalna metoda bezpośrednia z n = 0,48.
- **Każdy inny kraj lub region** — profil ogólny: metody dowolnie łączone,
  dopuszczalne natężenie odpływu i objętość minimalna wybierane przez Ciebie.

!!! note "Poza Włochami"
    Tam, gdzie nie istnieje rejestr gmin, region i współrzędne wprowadza się
    ręcznie. To nie jest błąd: taki jest przewidziany sposób pracy w krajach
    nieobjętych jeszcze dedykowanym profilem.

## Od czego zacząć

- [Szybki start](quickstart.md) — pierwsze wymiarowanie w pięć minut
- [Pełny przebieg pracy](workflow.md) — rzeczywisty projekt od początku do operatu
- [Słownik](glossario.md) — terminy dziedzinowe wraz z symbolami używanymi w aplikacji

---

*Znalazłeś błąd na tej stronie? [Zgłoś go nam](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
