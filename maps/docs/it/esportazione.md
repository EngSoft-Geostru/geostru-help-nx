# Esportazione e coordinate

## Sistemi di riferimento

La mappa lavora in **coordinate geografiche WGS84** (latitudine e longitudine in
gradi decimali). Le esportazioni **NEZ** e **DXF** proiettano in **UTM**.

!!! note "Zona UTM"
    La zona e l'emisfero derivano dalla posizione dei punti. Se il rilievo è a
    cavallo di due zone, verifica il risultato: le coordinate proiettate hanno
    senso solo dentro la propria zona.

## I formati

| Formato | Che cosa contiene | Quando usarlo |
|---|---|---|
| **TXT** | testo semplice, un punto per riga | scambio rapido, ispezione a occhio |
| **CSV** | separato da carattere (predefinito `;`) | foglio di calcolo, database |
| **LLE** | latitudine, longitudine, quota | GPS e strumenti che lavorano in geografiche |
| **NEZ** | nord, est, quota (UTM) | topografia e CAD in cartesiane |
| **DXF** | entità CAD reali (punti e polilinee) | disegno tecnico |
| **GMT** | formato GMT | cartografia scientifica |
| **Profilo Sezione** | progressiva e quota dei campioni | sezioni in relazione |

!!! tip "Il DXF non è un'immagine"
    L'esportazione DXF scrive punti e polilinee come **entità vere**: si possono
    modificare, agganciare con gli snap e referenziare come qualunque altro
    disegno.

## Come si esporta

Scegli il **Formato** nella barra laterale e premi **Esporta**. Il file viene
prodotto e scaricato.

!!! info "Costo e garanzie"
    Ogni esportazione consuma **10 crediti**, qualunque sia il formato.
    Se l'esportazione fallisce **non viene addebitato nulla**: i crediti sono
    prenotati prima e confermati solo a file prodotto. Ripetere la stessa
    esportazione, con gli stessi dati e lo stesso formato, entro pochi minuti non
    la fa pagare due volte.

## Salvare e riaprire il progetto

Esportare non è salvare. Per conservare il lavoro:

- **File › Salva** scarica lo stato della mappa in un file `.gmap`.
- **File › Apri** lo ricarica.
- **GeoDropbox** conserva il progetto nel cloud GeoStru: lo riapri da qualunque
  postazione.

Il file `.gmap` contiene la vista, i punti, i tracciati, le aree e i nodi mesh —
tutto ciò che serve a ritrovare il rilievo come l'avevi lasciato.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Maps%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/maps/docs/it/esportazione.md).*
