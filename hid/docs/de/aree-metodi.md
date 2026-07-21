# Flächen und Berechnungsverfahren

## Einzugsflächen

Jede Zeile der Tabelle ist eine hinsichtlich Nutzung und Durchlässigkeit
homogene Fläche. Erforderlich sind Beschreibung, Typ, Fläche in m² und
Abflussbeiwert φ nach der Maßnahme.

![Definition der Flächen](img/02-aree-metodi.png)

Der Flächentyp (undurchlässig, teildurchlässig, durchlässig) ist eine
beschreibende Kennzeichnung, die die Größenordnung von φ nahelegt; in die
Berechnung geht stets der von Ihnen eingetragene Wert ein.

HID berechnet den **flächengewichteten Abflussbeiwert**:

$$\varphi_{pond} = \frac{\sum \varphi_i \cdot S_i}{\sum S_i}$$

und die **befestigte Vergleichsfläche** $S_{pond} = S_{tot} \cdot \varphi_{pond}$,
also die äquivalente undurchlässige Fläche.

## Die Bemessungsverfahren

HID unterscheidet die **universellen** Verfahren, die überall gültig sind, von
den **zuständigkeitsgebundenen**, die nur dort existieren, wo das Regelwerk sie
vorschreibt.

### Mindestanforderungen

Vom Regelwerk in Abhängigkeit vom Kritikalitätsbereich vorgegebenes spezifisches
Volumen je Hektar. In Lombardia gilt 800, 500 oder 400 m³/ha je nach Bereich A, B
oder C und Regelwerksversion. Wo das Regelwerk keine Vorgabe macht, geben Sie das
Mindestvolumen selbst vor.

### Regenspende-Verfahren

Bilanziert das zufließende mit dem bei konstantem Abfluss abgeleiteten Volumen
und sucht die Dauer, die den Rückhalteraum maximiert. Es ist das am weitesten
verbreitete Verfahren für überschlägige Nachweise.

!!! note "Dauern unter einer Stunde"
    Wenn die maßgebende Dauer unter eine Stunde sinkt, verwendet HID
    vorschriftsgemäß den Exponenten n₁ der Kurve. Die Dauer wird nicht auf eine
    Stunde aufgerundet: Das würde das Volumen unterschätzen — ein Fehler, den wir
    bei der Validierung der App gegenüber der Vorgängerversion korrigiert haben.

### Fließzeitverfahren

Führt die Fließzeit des Einzugsgebiets ein und berücksichtigt damit die Form der
Abflussganglinie. Es liefert maßgebende Dauer und Volumen.

### Direktverfahren

Vergleicht die spezifischen Rückhaltevolumina vor und nach der Maßnahme über das
Verhältnis der Abflussbeiwerte. In Emilia-Romagna und Marche schreibt das
Regelwerk eine Variante mit festen Beiwerten vor, die HID als eigenes Verfahren
ausweist: **Regionales Direktverfahren**, nur in diesen Regionen sichtbar.

### Detailliertes Verfahren

Dies ist die vollständige Simulation: Bemessungsregenganglinie,
Niederschlagsverluste, Hochwasserganglinie und schrittweise Retention des
Rückhalteraums. Es ist das aufwendigste und zugleich am besten belegbare
Verfahren.

## Wie das Volumen gewählt wird

HID berechnet alle ausgewählten Verfahren und übernimmt als zulässiges Volumen
das **Maximum** der Ergebnisse. Das vom Regelwerk vorgeschlagene Verfahren ist
unter den Kontrollkästchen angegeben, schränkt aber nicht ein, welche Verfahren
Sie berechnen können.

---

*Haben Sie auf dieser Seite einen Fehler gefunden? [Melden Sie ihn uns](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
