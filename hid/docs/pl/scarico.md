# System odpływu

Urządzenie odpływowe określa natężenie odpływu ze zbiornika, a więc i retencję.
HID implementuje ich osiem.

![System odpływu](img/06-calcoli-verifiche.png)

## Dostępne urządzenia

| Urządzenie | Parametry | Zależność |
|---|---|---|
| Stałe natężenie odpływu | Q<sub>u,lim</sub> | Q stałe, niezależne od wysokości napełnienia |
| Przelew Thomsona | kąt θ | Q ∝ tan(θ/2) · h<sup>5/2</sup> |
| Przelew Bazina | szerokość | Q ∝ L · h<sup>3/2</sup> |
| Przelew Crumpa | szerokość | Q ∝ L · h<sup>3/2</sup> |
| Kołowy otwór zatopiony | pole A | Q = 0,6 · A · √(2gh) |
| Zasuwa | otwarcie, szerokość | Q = 0,6 · a · L · √(2gh) |
| Stała infiltracja | K, gradient | Q ∝ K · i · powierzchnia |
| Studnia chłonna | liczba, średnica, długość | funkcja wysokości napełnienia i powierzchni chłonnej |

## Jak wybierane jest dopuszczalne natężenie odpływu

To miejsce, w którym najczęściej popełnia się błąd, dlatego HID stosuje jedną
kolejność:

1. **Jeśli narzucają je przepisy**, obowiązuje ta wartość. W Lombardii wynika ona
   z powierzchni, współczynnika spływu i strefy krytyczności.
2. **W przeciwnym razie wybierasz je sam.** Pole „stałe natężenie odpływu" ma
   jednak sens tylko dla odpływu o stałym natężeniu: dla otworu zatopionego,
   przelewu lub zasuwy obowiązuje **natężenie urządzenia przy projektowej
   wysokości napełnienia**.

!!! warning "Uwaga"
    Punkt 2 jest powodem, dla którego przy zmianie typu odpływu wymagana objętość
    może się znacznie zmienić: natężenie odniesienia nie jest już tym, które
    wpisałeś w pole, lecz tym, które urządzenie rzeczywiście odprowadza.

## Projektowa wysokość napełnienia

Dla urządzeń zależnych od wysokości napełnienia wprowadzana wartość H jest
maksymalną użyteczną wysokością napełnienia. Odpowiadające jej natężenie jest
pokazywane pod blokiem jako **natężenie przy projektowej wysokości napełnienia**.

---

*Znalazłeś błąd na tej stronie? [Zgłoś go nam](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
