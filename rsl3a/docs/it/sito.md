# Sito

## Dati generali

Descrizione, committente, cantiere, progettista, geologo, studio di microzonazione da cui viene lo spettro e data finiscono in relazione. Lo
**studio tecnico** (intestazione, indirizzo, contatti, partita IVA) compare in copertina. Premi **Salva** per scriverli nel progetto; cambiando
scheda il modulo si salva da solo.

## Posizione

Scrivi un indirizzo o una località e premi **Cerca**, oppure fai clic sulla carta o trascina il segnaposto: latitudine e longitudine (WGS84) si
aggiornano. Le coordinate servono a **Calcola dal sito**.

## Parametri sismici

L'Ordinanza confronta lo spettro MS3 con lo spettro di norma per **T~R~ = 475 anni**. Per questo:

- **Calcola dal sito** interroga il servizio GeoStru Parametri Sismici con **vita nominale 50 anni e classe II**, qualunque siano vita nominale e
  classe dell'opera: la riga SLV ha così T~R~ = 475 anni;
- **Importa report GeoStru PS** legge il report di testo del programma Parametri Sismici (anche in UTF-16). Se il report è stato fatto con
  un'altra vita nominale o classe, la riga SLV non è a 475 anni e l'app lo dice;
- la tabella si può scrivere **a mano** e applicare con **Applica i valori**. Una riga tutta vuota vuol dire «nessun dato».

La riga **SLV** è quella usata dal confronto ed è evidenziata. Le altre sono informative e finiscono nella relazione.

!!! note "Vita nominale e classe d'uso"
    Sono informative. Classe I: secondo l'Ordinanza l'approccio semplificato è comunque ammesso. Classi III e IV: il confronto si fa comunque con
    lo spettro a 475 anni.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20RSL%20III%20A%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rsl3a/docs/it/sito.md).*
