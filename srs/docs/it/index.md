---
title: SRS NX — Manuale
---

# SRS NX

**SRS NX** calcola e verifica la **chiodatura corticale dei versanti** (soil
nailing) con **rete di facciata**, secondo **NTC 2018 / Eurocodici**. Stabilizza
pendii in terreno o roccia con chiodi/barre passive cementate e una rete di
rivestimento, dimensionando gli ancoraggi fino a raggiungere il coefficiente di
sicurezza di progetto. È l'app web della suite **GeoStru NX**.

[**Apri l'app**](https://nx.geostru.ai/srs/){ .md-button .md-button--primary }

![Interfaccia di SRS NX](img/srs-interfaccia.png)

## A chi serve

A chi progetta interventi di stabilizzazione superficiale di pendii in terra o
roccia — scarpate stradali e ferroviarie, fronti di scavo, versanti soggetti a
franamenti superficiali — con chiodatura e rete metallica di facciata.

## Cosa calcola

- **Coefficiente di sicurezza pre-intervento FS₀**, a partire dalla geometria
  del pendio e dai parametri geotecnici della coltre.
- La **forza di trazione** che i chiodi devono fornire per portare il
  coefficiente di sicurezza dal valore pre-intervento FS₀ al valore di
  progetto **FS_des** che imposti tu.
- Le **sei verifiche di resistenza** (R.2–R.7) di barra, malta, bulbo e rete,
  con il relativo coefficiente di sicurezza.
- Il **numero di ancoraggi e i metri di perforazione** necessari ogni 100 m² di
  rete, e una stima del costo dell'intervento.
- La **relazione di calcolo** in Word e PDF.

## Come funziona, in breve

Descrivi il pendio (inclinazione, spessore della coltre, parametri
geotecnici) e il substrato (terreno o roccia). Scegli un chiodo dal catalogo o
inserisci i parametri manualmente, imposta l'interasse della maglia di posa e
la rete di facciata. SRS calcola FS₀, ti chiede il coefficiente di sicurezza
di progetto FS_des e dimensiona di conseguenza la trazione richiesta
all'ancoraggio. Premi **Calcola** e leggi l'esito delle sei verifiche.

## Il manuale

| Capitolo | Contenuto |
|---|---|
| [Guida rapida](quickstart.md) | Dall'apertura al primo calcolo in cinque minuti |
| [Interfaccia e flusso di lavoro](workflow.md) | Toolbar, sidebar, tab e sequenza input → calcolo → verifiche |
| [Pendio e substrato](pendio.md) | Coltre, terreno/roccia, parametri geotecnici |
| [Azione sismica](sismica.md) | Coefficiente sismico orizzontale K_h |
| [Chiodi e ancoraggi](chiodi.md) | Catalogo GEWI/TITAN, parametri manuali, geometria |
| [Rete di facciata](rete.md) | Maglia, filo, resistenze a trazione e punzonamento |
| [Verifiche](verifiche.md) | R.2–R.7, FS₀/FS_des/ΔFS, ancoraggi per 100 m² |
| [Assistente AI](assistente-ai.md) | Imposta il progetto da una descrizione, coefficiente sismico da località |
| [Relazione ed esportazioni](relazione.md) | Word/DOC/PDF, salvataggio progetto, GeoDropbox |
| [Progetti di esempio](esempi.md) | File .srs pronti all'uso (terreno, roccia) |
| [Domande frequenti](faq.md) | FAQ |

---

## Su SRS NX

Parte della suite **GeoStru NX** — applicazioni web professionali per
geologia, geotecnica e idrologia.

[Apri l'app SRS NX](https://nx.geostru.ai/srs/) · [Tutti i prodotti NX](https://help.nx.geostru.ai/) · [Sito GeoStru](https://www.geostru.ai/)

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20SRS%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/it/index.md).*
