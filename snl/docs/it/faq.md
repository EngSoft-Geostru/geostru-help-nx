# Domande frequenti

**Il calcolo consuma crediti?**
No. Il calcolo, i risultati e i disegni a video sono gratuiti; consumano crediti la relazione Word, la tavola DXF e i messaggi all'assistente. Vedi [Crediti](crediti.md).

**Dove inserisco le fasi di scavo?**
Da nessuna parte: SNL NX ne crea una per chiodo, in ordine di profondità. La fase scava fino a metà fra un chiodo e il successivo, l'ultima fino al piede. Vedi [Cenni teorici](teoria.md#fasi-di-scavo).

**Perché i chiodi nel calcolo sono in un ordine diverso dal mio elenco?**
Il calcolo li considera sempre in ordine di profondità. L'elenco del passo Chiodi resta come l'hai scritto; **Ordina per profondità** lo riordina.

**I diametri vanno in millimetri?**
No, in metri: una barra da 32 mm si scrive 0,032. Se un valore non è plausibile, il passo Chiodi lo segnala.

**Perché la verifica a rottura di un chiodo è uguale in tutte le fasi?**
La forza nel chiodo si calcola una volta, sulla parete finita; in ogni fase cambia la lunghezza efficace, quindi cambia lo sfilamento ma non la rottura.

**Ho scelto Rankine ma il calcolo usa Coulomb.**
Con kh > 0 la spinta si calcola sempre con Coulomb / Mononobe-Okabe, qualunque sia la scelta.

**Come scelgo kh e kv?**
Nel passo Progetto: calcola i parametri del sito e applica la proposta kh = βm·amax/g, kv = ±0,5·kh, oppure scrivili a mano. La scelta resta tua; il segno di kv può cambiare l'esito.

**Il coefficiente A del carico non cambia con la categoria.**
È voluto: la categoria descrive il carico, il coefficiente A si scrive a mano per ogni carico.

**Perché lo scorrimento non è verificato con la falda alta?**
La spinta dell'acqua sul lato interno del blocco e la sottospinta alla base riducono molto il margine, e il paramento è considerato impermeabile. Controlla quota della falda, Bl e parametri del terreno di fondazione.

**SNL NX verifica la stabilità globale?**
No. Per le superfici che passano dietro o sotto i chiodi serve un programma di stabilità dei pendii, come GeoStru Slope. Vedi [Validazione e limiti](validazione.md).

**E la sezione del rivestimento?**
SNL NX ne dà pressione, taglio e momento; la verifica della sezione in calcestruzzo armato e della testa del chiodo si fa a parte.

**Perché il risultato è «non aggiornato»?**
Hai cambiato un dato che entra nel calcolo (quote, terreno, carichi, chiodi, coefficienti, kh, kv). Premi di nuovo **Calcola**. Cambiare dati generali, studio o sito non rende il risultato superato.

**Dopo l'importazione di un .snl i risultati non coincidono con quelli del file.**
I risultati salvati non si importano: si ricalcolano. Alcune differenze vengono dalle correzioni del metodo. Leggi il rapporto e [Validazione e limiti](validazione.md).

**Ho perso il progetto.**
Il progetto resta in sessione per 30 minuti di inattività. Salvalo spesso in un `.snlnx` o su GeoDropbox.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/snl/docs/it/faq.md).*
