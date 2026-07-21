# HID NX — Hydraulische Invarianz

HID bemisst Retentionssysteme für die **hydraulische und hydrologische
Invarianz**: Es weist nach, dass ein Eingriff in die Flächennutzung den in den
Vorfluter abgeleiteten Abfluss gegenüber dem vorherigen Zustand nicht erhöht.

Die Anwendung vergleicht parallel die von Ihnen ausgewählten Berechnungsverfahren
und übernimmt als Rückhaltevolumen das **Maximum der Ergebnisse**. So bleibt der
Nachweis gültig, unabhängig davon, welches Verfahren die genehmigende Stelle
verlangt.

[**App öffnen**](https://nx.geostru.ai/hid/){ .md-button .md-button--primary }

![Oberfläche von HID NX, Bereich Allgemeine Daten](img/01-dati-generali.png)

## Für wen

Für alle, die Anlagen zur Retention von Niederschlagswasser planen:
Wasserbauingenieure, Geologen und Planer, die einer Baugenehmigung, einem
Bebauungsplan oder einer Einleitungserlaubnis einen Nachweis der hydraulischen
Invarianz beilegen müssen.

## Berechnungsumfang

| Bereich | Inhalt |
|---|---|
| Niederschlag | Regenhöhenlinie GEV oder mit zwei Parametern |
| Regenganglinien | Chicago, gleichförmig, Sifalda, dreieckig |
| Niederschlagsverluste | Abflussbeiwert, Horton, SCS-CN |
| Abflussganglinien | Fließzeitverfahren und Nash |
| Bemessung | Mindestanforderungen, Regenspende-Verfahren, Direktverfahren, Fließzeitverfahren, detailliertes Verfahren |
| Ableitung | Acht Drosselorgane, vom Grundablass bis zum Sickerschacht |
| Nachweise | Nutzhöhe, Nutzvolumen, Entleerungszeit |

## Regelwerk

HID wendet **Regelwerksprofile** an, die nach Land und Region ausgewählt werden.
Das Profil bestimmt, welche Verfahren zulässig sind, welche Daten benötigt werden
und ob Drosselabfluss und Mindestvolumen vom Regelwerk vorgegeben sind oder von
Ihnen gewählt werden.

- **Lombardia** — R.R. 7/2017, Ergänzung 2019, R.R. 3/2025: GEV-Kurve
  verpflichtend, SCS-CN ausgeschlossen, Kritikalität und Drosselabfluss aus der
  Gemeinde abgeleitet.
- **Emilia-Romagna und Marche** — regionales Direktverfahren mit n = 0,48.
- **Jedes andere Land oder jede andere Region** — generisches Profil: Verfahren
  frei kombinierbar, Drosselabfluss und Mindestvolumen von Ihnen gewählt.

!!! note "Außerhalb Italiens"
    Wo kein Gemeindeverzeichnis vorliegt, werden Region und Koordinaten manuell
    eingegeben. Das ist kein Fehler, sondern die vorgesehene Arbeitsweise in
    Ländern, die noch nicht von einem eigenen Profil abgedeckt sind.

## Einstieg

- [Kurzanleitung](quickstart.md) — die erste Bemessung in fünf Minuten
- [Vollständiger Arbeitsablauf](workflow.md) — ein reales Projekt vom Beginn bis zum Bericht
- [Glossar](glossario.md) — die Fachbegriffe mit den in der App verwendeten Formelzeichen

---

*Haben Sie auf dieser Seite einen Fehler gefunden? [Melden Sie ihn uns](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
