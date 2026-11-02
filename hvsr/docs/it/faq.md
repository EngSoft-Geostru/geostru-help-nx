# Domande frequenti

## Il mio progetto è sparito

Il progetto vive in sessione e scade dopo 30 minuti di inattività o a un riavvio. Salva spesso il `.hvsrnx` con **File → Salva**.

## Non ho un file per provare

Scegli **File → Apri l'esempio**: è una registrazione di 20 minuti con un modello già fatto. Il [Tutorial](tutorial.md) la usa passo per passo.

## Posso aprire i progetti del desktop?

Sì, i `.hvsrx`. I `.ehv` vanno prima salvati come `.hvsrx` dal desktop.

## Il mio strumento non è fra i formati

Esporta dal software dello strumento in SAF o in testo. Il formato SEG-2 si legge direttamente.

## f~0~ è diversa da quella del mio vecchio progetto

Le curve salvate nei progetti di anni fa non coincidono con quelle che il desktop di oggi ricalcola dagli stessi dati. Inoltre HVSR NX media sempre sulle finestre incluse. Sui
criteri e sui parametri vedi [Validazione](validazione.md).

## Il filtro tiene più finestre del desktop

È voluto: il filtro del desktop aveva un difetto e cancellava finestre buone. Rileggi comunque f~0~ dopo il filtro.

## f~0~ è uguale a f min

Il massimo è sul bordo della banda: non è un picco. Allarga la banda o restringila attorno al picco che ti interessa.

## La curva è affidabile ma il picco non è chiaro

Sono due giudizi diversi: la misura è buona e il picco è basso o largo. Può indicare un basso contrasto: f~0~ va riportata con questa riserva.

## La Ricerca dà un modello diverso a ogni corsa

Dipende dal modello di partenza e dal seme. Attiva **Seme fisso** per ripetere la stessa corsa. Se modelli diversi hanno misfit simile, i dati non bastano a distinguerli.

## Posso ricavare la categoria dalla sola H/V?

No, non in modo affidabile: la curva dipende dal rapporto fra V~s~ e H. Fissa almeno uno strato con un dato indipendente.

## La categoria è diversa dal desktop

Il calcolo di V~s,eq~ è stato corretto: vedi [Validazione](validazione.md).

## Posso combinare HVSR e MASW?

L'inversione congiunta non è ancora in HVSR NX. Per ora usa il risultato di [MASW NX](https://help.nx.geostru.ai/masw/) per fissare gli strati.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20HVSR%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hvsr/docs/it/faq.md).*
