# Formati

## Progetto SNL NX (.snlnx)

È il formato di lavoro. Contiene **solo gli ingressi**: dati generali, studio tecnico, sito e parametri sismici, geometria, strati, falda, carichi, chiodi, coefficienti, kh e kv, e il rapporto d'importazione se il progetto viene da un `.snl`. I risultati non si salvano: si ricalcolano dopo l'apertura, gratuitamente.

- **File → Salva** riscrive il file aperto; se non c'è, chiede dove salvare;
- **File → Salva con nome…** crea un nuovo file `.snlnx`;
- **File → Apri…** apre un `.snlnx` o un `.snl`.

Il nome del file su cui scrive «Salva» compare nella barra.

## File .snl

I progetti `.snl` di SNL si aprono con **File → Apri…** e si convertono nel modello di SNL NX con un rapporto di importazione. SNL NX non scrive file `.snl`. Vedi [Importazione](importazione.md).

## Relazione Word (.docx)

Dal passo **Relazione ed export**, con un calcolo completo e aggiornato. Contiene i dati del progetto, le ipotesi, i risultati per fase e per chiodo, lo scorrimento, i disegni e il blocco **«Codice di calcolo»** richiesto dal §10.2 delle NTC 2018: applicazione, versione, motore di calcolo, validazione e un **codice documento** verificabile su geostru.ai. Consuma 10 crediti.

## Tavola DXF

La sezione della parete in scala, con layer separati per parete, rivestimento, terreno, falda, carichi, chiodi, quote e testi. Il file porta la firma GeoStru nei commenti, ignorati dai programmi CAD. Consuma 10 crediti.

## GeoDropbox

Con il pulsante **GeoDropbox** salvi il progetto `.snlnx` in un progetto GeoDropbox e lo riapri da lì, anche da un altro computer.

## Disegno a video

Il disegno al centro (sezione e viste dei risultati) è gratuito e si aggiorna a ogni modifica. Non serve scaricare nulla per controllare il modello.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/snl/docs/it/formati.md).*
