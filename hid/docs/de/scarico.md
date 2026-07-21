# Ableitungssystem

Das Drosselorgan bestimmt den aus dem Rückhalteraum austretenden Abfluss und
damit die Retention. HID implementiert acht davon.

![Ableitungssystem](img/06-calcoli-verifiche.png)

## Die verfügbaren Organe

| Organ | Parameter | Gesetzmäßigkeit |
|---|---|---|
| Konstanter Abfluss | Q<sub>u,lim</sub> | Q konstant, unabhängig vom Wasserstand |
| Thomson-Überfall | Winkel θ | Q ∝ tan(θ/2) · h<sup>5/2</sup> |
| Bazin-Überfall | Breite | Q ∝ L · h<sup>3/2</sup> |
| Crump-Überfall | Breite | Q ∝ L · h<sup>3/2</sup> |
| Kreisförmiger Grundablass | Fläche A | Q = 0,6 · A · √(2gh) |
| Schütz | Öffnung, Breite | Q = 0,6 · a · L · √(2gh) |
| Konstante Infiltration | K, Gradient | Q ∝ K · i · Fläche |
| Sickerschacht | Anzahl, Durchmesser, Länge | Funktion des Wasserstands und der Sickerfläche |

## Wie der Drosselabfluss gewählt wird

Hier werden die meisten Fehler gemacht, daher folgt HID einer eindeutigen
Reihenfolge:

1. **Wenn das Regelwerk ihn vorgibt**, gilt dieser Wert. In Lombardia wird er aus
   Fläche, Abflussbeiwert und Kritikalitätsbereich abgeleitet.
2. **Andernfalls wählen Sie ihn selbst.** Das Feld „konstanter austretender
   Abfluss" ist jedoch nur für eine Ableitung mit konstantem Abfluss sinnvoll:
   Für einen Grundablass, einen Überfall oder ein Schütz gilt der **Abfluss des
   Organs beim Bemessungswasserstand**.

!!! warning "Achtung"
    Punkt 2 ist der Grund, weshalb sich das erforderliche Volumen beim Wechsel
    des Ableitungstyps erheblich ändern kann: Der maßgebende Abfluss ist nicht
    mehr der von Ihnen im Feld eingetragene, sondern jener, den das Organ
    tatsächlich ableitet.

## Bemessungswasserstand

Bei den vom Wasserstand abhängigen Organen ist der von Ihnen eingegebene Wert H
die maximale nutzbare Einstauhöhe. Der zugehörige Abfluss wird unter dem Block
als **Abfluss beim Bemessungswasserstand** angezeigt.

---

*Haben Sie auf dieser Seite einen Fehler gefunden? [Melden Sie ihn uns](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
