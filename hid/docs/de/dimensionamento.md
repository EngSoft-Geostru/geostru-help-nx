# Bemessung des Rückhalteraums

## Bemessungsregenganglinie

Die Regenganglinie verteilt die aus der Kurve gewonnene Niederschlagshöhe über
die Zeit.

| Typ | Anwendung |
|---|---|
| **Chicago** | Am weitesten verbreitet: Spitze über den Beiwert r positionierbar |
| **Gleichförmig** | Konstante Intensität über die gesamte Dauer |
| **Sifalda** | Drei Abschnitte, trapezförmiger Verlauf |
| **Dreieckig** | Linearer Anstieg und Abfall |

Beim Chicago-Ansatz gibt der **Lagebeiwert r** an, wo die Spitze liegt: 0,4
bedeutet bei 40 % der Dauer.

![Regenganglinie und Niederschlagsverluste](img/05-depurazione-piogge.png)

## Niederschlagsverluste

Wandeln den Gesamtniederschlag in den effektiven Niederschlag um, also jenen
Anteil, der zu Abfluss wird.

- **Prozentsatz** — Multiplikation mit dem Abflussbeiwert φ der Fläche. Das ist
  das einfachste und am häufigsten verwendete Modell.
- **Horton** — mit der Zeit abnehmende Infiltration je nach Bodenklasse.
- **SCS-CN** — Curve-Number-Verfahren, mit vorausgegangener Feuchtebedingung
  AMC I, II oder III.

!!! warning "Lombardia"
    Das Verfahren SCS-CN ist nach dem regionalen Regelwerk nicht zulässig.

## Abflussganglinie

Wandelt den effektiven Niederschlag in Abfluss um:

- **Fließzeitverfahren** — verwendet die Fließzeit der Fläche.
- **Nash** — Kaskade aus n linearen Speichern mit der Konstanten K, für stärker
  gegliederte Einzugsgebiete.

## Retention

Der Rückhalteraum wird schrittweise durchgerechnet, indem die Massenbilanz
zwischen Zufluss, Abfluss aus dem Drosselorgan und gespeichertem Volumen gelöst
wird. Das Maximum des Volumens ist das Ergebnis des detaillierten Verfahrens.

![Berechnungen und Nachweise](img/06-calcoli-verifiche.png)

## Die abschließenden Nachweise

| Nachweis | Bedingung |
|---|---|
| Nutzhöhe | H der Planung ≥ erforderliche Höhe |
| Nutzvolumen | V der Planung ≥ zulässiges Volumen |
| Entleerungszeit | T ≤ zulässige Zeit (in der Regel 48 h) |

Die Entleerungszeit wird nur für Ableitungen mit konstantem Abfluss und für
konstante Infiltration berechnet: Bei den übrigen Organen hängt der Abfluss vom
Wasserstand ab und ändert sich während der Entleerung.

---

*Haben Sie auf dieser Seite einen Fehler gefunden? [Melden Sie ihn uns](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
