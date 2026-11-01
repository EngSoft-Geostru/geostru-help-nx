# File, progetti del desktop e GeoDropbox

## Salvare

Il progetto vive in sessione sul server e **sparisce dopo 30 minuti di inattività o a un riavvio**. Salvalo dal menu **File**
con **Salva** o **Salva con nome**: ottieni un file `.maswnx` con dati, picking, strati, soluzioni e tracce.
Oltre i 30 MB le tracce restano riferimenti e il salvataggio lo dice.

## Aprire

**Apri** accetta `.maswnx` e `.mswx`.

Il `.mswx` è il formato di Easy-MASW desktop: tracce, spettro, picking, inversione e categoria arrivano nell'app. Nel desktop
ritaglio e filtro modificano i campioni, quindi i campioni del `.mswx` sono già elaborati: si importano così come sono e il
ritaglio riparte da zero, come avvisa l'app.

Il vecchio `.msw` binario non si apre: salvalo come `.mswx` dal desktop.

## GeoDropbox

Dal pulsante **GeoDropbox** salvi il `.maswnx` in un tuo progetto e apri da lì un `.maswnx` o un `.mswx`.

## Limiti

File fino a 64 MB per volta. Più tracce, campioni o celle di mappa di quanti il server possa elaborare vengono rifiutati con
un messaggio.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MASW%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/it/file.md).*
