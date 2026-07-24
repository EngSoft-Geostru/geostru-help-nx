---
title: Opere di sostegno — Slope NX
---

# Opere di sostegno (muri e gabbioni)

Slope NX modella le opere di sostegno come parte del pendio, sia nel disegno sia nel calcolo. Le aggiungi dal pannello **Input → Opere di sostegno**.

## Muro in c.a. e gabbioni

- **Muro in c.a.**: mensola con fondazione, definito per quote parametriche (altezza, spessori testa/base, mensole valle/monte, spessore fondazione) e peso di volume del calcestruzzo.
- **Gabbioni**: blocchi impilati a gradoni (base × n° file), con il peso di volume del riempimento.

Il muro nasce dal dialogo e si **trascina in posizione** sulla sezione: attiva lo spostamento con l'icona ✥, poi trascina; il comando si disarma da solo dopo lo spostamento. Il verso (lato valle a sinistra o a destra) definisce l'orientamento.

## Effetto nel calcolo

- Il **peso** del muro entra nei conci che ne intersecano il profilo.
- La superficie critica **non attraversa** il muro: è un corpo rigido, le superfici lo aggirano.
- Per la **stabilità globale** conviene estendere il profilo a valle/monte e usare **Auto-posiziona maglia**, che colloca i centri in modo che i cerchi passino sotto la fondazione ed emergano al piede.

## Rinterro dietro il muro

Con l'opzione **raccorda la testa** attiva, il terreno di **rinterro** dietro il muro non è solo grafica: è modellato come **terreno vero** nel calcolo. Il profilo di calcolo si alza nella zona di rinterro (senza contare due volte il calcestruzzo) e il volume aggiunto entra come strato.

Assegna il **materiale del rinterro** con un **doppio-click** sul cuneo tratteggiato dietro il muro: peso e resistenza (c′, φ′) di quel materiale entrano nel calcolo dove la superficie attraversa il rinterro.

!!! tip "Rinterro già a quota"
    Se hai disegnato il profilo topografico **già alla quota finita** (rinterro incluso nella linea di terreno), lascia il raccordo **OFF**: il rinterro è già terreno e non serve il cuneo.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Slope%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/slope/docs/it/muri.md).*
