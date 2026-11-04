# Flusso di lavoro

Un progetto completo, nell'ordine delle schede. Il calcolo parte a ogni modifica e i risultati sono sempre quelli dei dati a video: non c'è un
pulsante «Calcola», e cambiare scheda non ricalcola nulla.

1. **Sito** — Compila i dati generali (descrizione, committente, cantiere, progettista, geologo, studio di microzonazione, data) e lo studio che
   firma la relazione. Posiziona il sito: la ricerca per indirizzo usa OpenStreetMap e il segnaposto si trascina. Indica vita nominale e classe
   d'uso dell'opera: sono informative, il confronto è sempre a 475 anni. Ottieni i parametri sismici dal servizio, da un report GeoStru PS o a mano.
   → [Sito](sito.md)
2. **Spettro MS3** — Importa il file dello studio con l'anteprima. Controlla gli avvisi (righe scartate, unità sospetta, punto a 0,01 s mancante)
   e la tabella della regolarizzazione. → [Spettro MS3](spettro-ms3.md)
3. **Confronto** — Scegli categoria di sottosuolo e topografica del sito del manufatto e i periodi T~min~ e T~max~ dell'edificio. Leggi il valore
   delle due condizioni, l'esito e gli avvisi. → [Confronto](confronto.md)
4. **Relazione** — Anteprima gratuita, Word a crediti, CSV gratuito. → [Relazione e crediti](relazione.md)
5. **Salva** — Il progetto vive in sessione sul server: salvalo in un file `.rsl3anx` (File → Salva) o su GeoDropbox. → [File e GeoDropbox](file.md)

Puoi anche aprire un progetto del programma desktop (`.rs3`, `.rs3a`): l'app ne legge gli ingressi e ricalcola tutto secondo il testo
dell'Ordinanza.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20RSL%20III%20A%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rsl3a/docs/it/workflow.md).*
