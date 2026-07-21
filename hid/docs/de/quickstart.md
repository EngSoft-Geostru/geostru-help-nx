# Kurzanleitung

Fünf Minuten vom Öffnen der App bis zum nachgewiesenen Rückhaltevolumen. Wir
verwenden das vorgeladene Beispiel des Handbuchs, damit die angezeigten Zahlen
vergleichbar sind.

## 1. App öffnen und Beispiel laden

Rufen Sie [nx.geostru.ai/hid](https://nx.geostru.ai/hid/) auf. Beim Start ist
bereits das **Beispiel 9.4 — Detailliertes Verfahren** geladen: drei Flächen mit
insgesamt 10.000 m².

![Werkzeugleiste von HID](img/00-toolbar.png)

Alle Befehle befinden sich in der oberen Leiste: **Neu**, **Öffnen**,
**Speichern**, **Bericht** und rechts die Schaltfläche **Berechnen**.

## 2. Flächen prüfen

Öffnen Sie den Bereich **2. Flächen und Verfahren**. Jede Zeile ist eine Fläche
mit ihrer Größe und ihrem Abflussbeiwert φ.

![Definition der Flächen und Auswahl der Verfahren](img/02-aree-metodi.png)

Das farbige Band zeigt die aggregierten Werte: Gesamtfläche, flächengewichtetes
φ, befestigte Vergleichsfläche und Drosselabfluss. Darunter wählen Sie die zu
vergleichenden Verfahren.

!!! tip "Hinweis"
    Lassen Sie mehrere Verfahren aktiv. HID berechnet alle und übernimmt das
    Maximum: Das ist die konservativste Bedingung und erspart Ihnen die
    Wiederholung der Arbeit, falls die genehmigende Stelle ein anderes Verfahren
    verlangt.

## 3. Regenhöhenlinie prüfen

Bereich **3. Regenhöhenlinie**. Bei der Kurve mit zwei Parametern geben Sie `a`
und `n` ein; bei der GEV die Parameter der Verteilung und das Wiederkehrintervall.

![Regenhöhenlinie](img/03-curva-pluviometrica.png)

## 4. Berechnen

Drücken Sie oben rechts **Berechnen**. Wechseln Sie in den Bereich
**6. Berechnungen und Nachweise**.

![Ergebnisse der Bemessung](img/06-calcoli-verifiche.png)

Jedes Verfahren hat eine eigene Karte mit dem berechneten Volumen. Das Band
darunter zeigt das übernommene **zulässige Volumen**, die zugehörige Höhe und die
Entleerungszeit.

Für das Beispiel 9.4 müssen Sie ablesen: Direktverfahren 234,89 m³,
Fließzeitverfahren 169,51 m³, detailliertes Verfahren 175,74 m³,
Regenspende-Verfahren 175,58 m³. Das übernommene Volumen beträgt **234,89 m³**.

## 5. Bericht erzeugen

Öffnen Sie in der Leiste das Menü **Bericht** und wählen Sie das Format: Word,
PDF oder Word 97. Das Dokument wird in der in der App ausgewählten Sprache
erzeugt.

---

*Haben Sie auf dieser Seite einen Fehler gefunden? [Melden Sie ihn uns](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
