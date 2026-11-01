# Domande frequenti

## Il mio progetto è sparito

Il progetto vive in sessione e scade dopo 30 minuti di inattività o a un riavvio. Salva spesso il `.maswnx`.

## Posso aprire i progetti del desktop?

Sì, i `.mswx`. I `.msw` binari vanno prima salvati come `.mswx` dal desktop.

## Perché f max viene rifiutata?

Deve restare sotto la frequenza di Nyquist, 1/(2·dt), che l'app mostra accanto a **Calcola**.

## Due inversioni danno risultati diversi. È un errore?

No: la ricerca parte da valori casuali. Confronta le soluzioni: se profili molto diversi hanno misfit simile, i dati non bastano a
distinguerli.

## La categoria è diversa dal desktop

Su progetti con strati che arrivano a 30 m può uscire C dove il desktop dava E: è una correzione dichiarata, vedi
[Validazione](validazione.md). Controlla anche la soluzione scelta.

## La relazione non si genera

I dati sono cambiati dopo l'inversione: rifai la corsa.

## L'inversione mi è costata due volte?

Una corsa identica su dati identici non si paga di nuovo. Una corsa dopo aver cambiato dati, cicli o strati è una corsa nuova.

## Quanto in profondità arrivo?

Circa λ/2 della lunghezza d'onda più lunga letta con affidabilità: uno stendimento corto o una sorgente leggera non arrivano a 30 m.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MASW%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/it/faq.md).*
