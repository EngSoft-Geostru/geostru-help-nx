# Domande frequenti

**Il calcolo consuma crediti?**
No. Il calcolo a video, i diagrammi, gli inviluppi e le verifiche sono gratuiti. Word, DXF, CAD Tools e assistente consumano crediti. Vedi [Crediti](crediti.md).

**Perché devo definire le combinazioni prima delle fasi?**
Perché ogni combinazione deve seguire la stessa storia costruttiva. L'ambito sceglie le fasi da verificare senza creare coefficienti diversi dentro ogni fase.

**Posso cambiare stratigrafia da una fase all'altra?**
No. SPW NX usa una sola stratigrafia per tutto il progetto. Le variazioni presenti in un file desktop vengono segnalate nel rapporto di importazione.

**Posso usare sezioni diverse lungo la paratia?**
No. Il progetto ha una sola tipologia per tutta l'altezza. Un file desktop a tronconi richiede la scelta di riferimento indicata dal rapporto.

**Ho definito un tirante ma nel disegno non è attivo. Perché?**
La definizione nel passo Elementi non lo installa. Aggiungi l'evento **Installa tirante** nella fase corretta.

**Che differenza c'è fra precarico e coefficiente di combinazione?**
Il precarico è una forza del tirante o del suo evento di tesatura. Il coefficiente di combinazione appartiene alla matrice e deriva dalla regola della combinazione.

**Perché con il LEM non vedo la deformata?**
Il LEM studia l'equilibrio limite e non calcola gli spostamenti. Per spostamenti e verifica SLE usa il FEM.

**Perché una combinazione non compare negli inviluppi?**
Può essere disattivata oppure non completata. Controlla l'esito e gli avvisi nel passo Calcolo.

**Che cosa significa «Non calcolata»?**
La verifica non ha un esito. Non significa «verificata». Controlla dati, tipo di combinazione e limiti indicati nella pagina.

**Perché i risultati sono diventati non aggiornati?**
Hai cambiato uno o più ingressi dopo il calcolo. Ripeti il calcolo prima di usare risultati, relazione o export dei risultati.

**Perché i risultati importati non sono uguali al desktop?**
I risultati salvati non vengono importati. Il nuovo modello gestisce in modo diverso storia delle fasi, combinazioni, sisma e alcuni dati. Leggi il rapporto e [Validazione](validazione.md).

**Il pulsante Scarica Word è disattivato.**
Manca un calcolo completo e aggiornato. Il messaggio sopra i pulsanti lo dice. Calcola di nuovo e torna al passo. L'**Anteprima gratuita** resta disponibile.

**Ho premuto Computo NX ma non è successo niente.**
Il browser può bloccare la nuova scheda. Consenti le finestre a comparsa per il sito e riprova. Se il servizio non risponde, compare un messaggio e non si consuma nulla.

**Dove trovo le formule dei metodi?**
Il manuale descrive ipotesi, uso e limiti senza riportare le equazioni del motore. Per la teoria usa la [bibliografia pubblica](metodi.md#bibliografia-essenziale).

**L'assistente può completare i dati che mancano?**
No, non inventa parametri o quote. Può scrivere i dati che gli fornisci e segnalare quelli mancanti.

**Il progetto è sparito dopo una pausa.**
La sessione scade dopo 30 minuti di inattività. Riapri il `.spwnx` salvato oppure il progetto da GeoDropbox.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/spw/docs/it/faq.md).*
