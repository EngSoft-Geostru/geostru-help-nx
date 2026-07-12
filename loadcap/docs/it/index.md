---
title: Loadcap NX — Manuale
---

# Loadcap NX

**Loadcap NX** calcola la **capacità portante** (carico limite) e i **cedimenti**
delle fondazioni superficiali, e redige la **relazione geotecnica** professionale
secondo NTC 2018 / Eurocodici. È l'app web della suite **GeoStru NX**, porting del
desktop Loadcap.

[**Apri l'app**](https://nx.geostru.ai/loadcap/){ .md-button .md-button--primary }

---

## Cosa calcola

- **Carico limite** di trave rovescia, plinto, platea e fondazione circolare con i
  metodi di **Terzaghi** (1955), **Meyerhof** (1963), **Hansen** (1970), **Vesic**
  (1975), **Brinch-Hansen** (EC7/EC8), **Meyerhof-Hanna** (1978, terreni a due
  strati) e **Richards** (1993, condizioni sismiche).
- **Combinazioni di carico** con coefficienti parziali NTC 2018 (A1/A2 · M1/M2 ·
  R1/R2/R3) ed Eurocodice 7 (DA1/DA2/DA3), più SLE e sisma.
- **Verifiche aggiuntive**: scorrimento sul piano di posa e punzonamento.
- **Cedimenti**: elastici (Timoshenko-Goodier), edometrici (logaritmico e
  monodimensionale), **Schmertmann**, **Burland & Burbidge**, con il **decorso nel
  tempo** dalla teoria della consolidazione.
- **Stato tensionale**: bulbo delle tensioni, mappa dei colori, pressioni di
  contatto e modello 3D.
- **Azione sismica NTC** con pericolosità completa (spettro, categorie di
  sottosuolo e topografiche) e riduzione dei fattori di capacità portante.

## Il manuale

| Capitolo | Contenuto |
|---|---|
| [Guida rapida](quickstart.md) | Dall'apertura al primo calcolo in cinque minuti |
| [Fondazione e geometria](geometria.md) | Tipologie, B/L/H/D, altezza di incastro, pendio |
| [Stratigrafia e falda](stratigrafia.md) | Parametri per strato, falda, incolla/importa |
| [Carichi e combinazioni](carichi.md) | Approcci di progetto, coefficienti parziali, convenzione dei segni |
| [Azione sismica](sismica.md) | Pericolosità NTC, effetti su terreno e struttura |
| [Capacità portante](carico-limite.md) | Metodi, fattori Nc/Nq/Nγ, verifiche a scorrimento e punzonamento |
| [Cedimenti](cedimenti.md) | Elastici, edometrici, Schmertmann, Burland, decorso nel tempo |
| [Stato tensionale e 3D](stato-tensionale.md) | Bulbo, mappa, pressioni di contatto, modello 3D |
| [Assistente AI](assistente-ai.md) | Compila da documento e revisione geotecnica |
| [Relazione ed esportazioni](relazione.md) | Relazione geotecnica, Word/PDF, GeoDropbox |
| [Progetti di esempio](esempi.md) | File di validazione pronti all'uso |
| [Domande frequenti](faq.md) | FAQ |

---

## Su Loadcap NX

Parte della suite **GeoStru NX** — applicazioni web professionali per geologia,
geotecnica e idrologia.

[Apri l'app Loadcap NX](https://nx.geostru.ai/loadcap/) · [Tutti i prodotti NX](https://help.nx.geostru.ai/) · [Sito GeoStru](https://www.geostru.ai/)

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/it/index.md).*
