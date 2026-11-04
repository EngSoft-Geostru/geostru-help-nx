# Validazione e limiti

Il documento di validazione completo (NTC 2018 §10.2) accompagna il codice: campo d'impiego, basi teoriche, casi di prova risolti e scarti
dal programma desktop. Si chiama validazione, non certificazione: nessun ente terzo è coinvolto.

## Campo d'impiego e limiti

- Territori e interventi a cui si applica l'Ordinanza 55/2018; zone per cui lo studio MS3 fornisce uno spettro.
- Confronto sempre con lo spettro orizzontale, η = 1, T~R~ = 475 anni.
- La categoria topografica usa S~T~ di cresta, senza la riduzione con la quota del sito.
- T~min~ e T~max~ sono un dato del progettista.

## Casi di prova

- **Casi a mano** ai bordi delle soglie: rapporto esattamente 1,30 (non supera) e 1,31 (supera); aree +20 % (non supera) e +21 % (supera);
  2·T~max~ = 1,10 s (si confronta) e 1,12 s (non effettuabile).
- **Parità con il desktop** su 42 casi prodotti con il programma desktop: stessi conteggi, stessi esiti, regolarizzazione entro 1e-5, nella
  modalità che riproduce il desktop (usata solo nelle prove).
- **Esempio San Severino** (microzona 13, cat. C, T1, T~min~ 0,1 s, T~max~ 0,5 s): rapporto massimo 1,498, aree −17,2 %, esito approfondimenti.

## Differenze dal programma desktop

L'app segue il testo dell'Ordinanza dove il desktop (prima della correzione del 03/11/2026) se ne discostava:

| Desktop | NX |
|---|---|
| condizione 1 come quota dei punti sopra la norma, soglia 30 % | supero puntuale: rapporto massimo > 1,30 |
| tre esiti, con «RSL» automatico; video e relazione potevano differire | due esiti dal testo, uguali ovunque |
| area con un triangolo in più dall'origine, e −1 con T~min~ e 2·T~max~ nello stesso tratto | integrali esatti |
| 2·T~max~ > 1,1 s non gestito | confronto non effettuabile |
| stato limite, η e spettro verticale liberi | T~R~ 475, η = 1, orizzontale |
| a~max~ dalla Sa del secondo punto | da Se(0,01 s) |
| SV letta dal file | SV ricavata da SA |

Per questo, sullo stesso spettro, l'esito di NX può essere diverso da quello del desktop: nell'esempio San Severino il desktop scriveva
«approccio semplificato», NX «servono approfondimenti».

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20RSL%20III%20A%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rsl3a/docs/it/validazione.md).*
