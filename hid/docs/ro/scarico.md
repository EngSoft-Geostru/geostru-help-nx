# Sistem de evacuare

Organul de evacuare determină debitul ieșit din bazinul de retenție și, prin
urmare, atenuarea. HID implementează opt astfel de organe.

![Sistem de evacuare](img/06-calcoli-verifiche.png)

## Organele disponibile

| Organ | Parametri | Lege |
|---|---|---|
| Debit constant | Q<sub>u,lim</sub> | Q constant, independent de sarcina hidraulică |
| Deversor Thomson | unghi θ | Q ∝ tan(θ/2) · h<sup>5/2</sup> |
| Deversor Bazin | lățime | Q ∝ L · h<sup>3/2</sup> |
| Deversor Crump | lățime | Q ∝ L · h<sup>3/2</sup> |
| Orificiu înecat circular | arie A | Q = 0,6 · A · √(2gh) |
| Stavilă | deschidere, lățime | Q = 0,6 · a · L · √(2gh) |
| Infiltrație constantă | K, gradient | Q ∝ K · i · suprafață |
| Puț absorbant | număr, diametru, lungime | funcție de sarcina hidraulică și de suprafața de infiltrare |

## Cum este ales debitul maxim admis la evacuare

Este punctul în care se greșește cel mai des, de aceea HID urmează o ordine
unică:

1. **Dacă reglementarea îl impune**, se aplică acela. În Lombardia se deduce din
   arie, coeficientul de scurgere și zona de criticitate.
2. **Altfel îl alegi tu.** Însă câmpul „debit constant evacuat" are sens doar
   pentru o evacuare la debit constant: pentru un orificiu înecat, un deversor
   sau o stavilă se aplică **debitul organului la sarcina hidraulică de
   proiect**.

!!! warning "Atenție"
    Punctul 2 este motivul pentru care, schimbând tipul de evacuare, volumul
    necesar se poate modifica considerabil: debitul de referință nu mai este cel
    pe care l-ai scris în câmp, ci cel pe care organul îl evacuează efectiv.

## Sarcina hidraulică de proiect

Pentru organele care depind de sarcina hidraulică, valoarea H pe care o introduci
este sarcina hidraulică utilă maximă. Debitul corespunzător este afișat sub bloc
ca **debit la sarcina hidraulică de proiect**.

---

*Ai găsit o eroare în această pagină? [Semnalează-ne-o](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
