# Domande frequenti

Altre domande sull'interpretazione dei risultati sono in [Risultati → Domande frequenti](risultati.md#domande-frequenti).

**Quanto costa usare GeoTheis NX?**
Dati, calcolo, risultati, grafici, disegni a video, mappa e anteprima della relazione sono gratuiti. Costano crediti NX la relazione
Word (10 crediti), il DXF del pozzo (10) e ogni messaggio all'assistente (3). Un'operazione fallita non si paga, e rigenerare lo
stesso documento con gli stessi dati non si ripaga. Vedi [Relazione e crediti](relazione.md#crediti).

**Devo premere un pulsante per calcolare?**
No. I risultati si aggiornano da soli a ogni modifica dei dati o delle scelte, nella scheda [Risultati](risultati.md).

**Perché i miei risultati sono diversi da quelli del programma desktop?**
Il desktop aveva alcuni errori di formula (per esempio la T di Cooper-Jacob era 24 volte più piccola su CELICO, e la curva tipo di
Theis era spostata), corretti nel desktop il 15/11/2026. GeoTheis NX usa le formule di letteratura e ricalcola tutto: i risultati
salvati nel `.wtax` non si importano. Ogni differenza è spiegata in [Validazione](validazione.md#differenze-dal-programma-desktop).

**Posso aprire i miei progetti `.wtax`?**
Sì, con **File → Apri…**. Si importano pozzo, quote, stratigrafia, piezometri, gradini, letture di pompaggio e di risalita e le scelte
fatte nel desktop. Controlla le note che compaiono dopo l'apertura, in particolare tipo di falda e tempi della risalita. Le coordinate
del desktop sono locali: se ti servono mappa e pozzi vicini, posiziona il pozzo nella scheda [Pozzo](pozzo.md). Dettagli in
[File](file.md#progetti-del-programma-desktop-wtax).

**Ho chiuso il browser e il progetto non c'è più.**
Il progetto resta in sessione per 30 minuti di inattività. Riapri il file `.geotheisnx` che hai salvato, o il progetto su GeoDropbox.
Salva spesso con **Salva** (Ctrl+S).

**Ho solo la prova a portata costante sul pozzo, senza piezometri. Che cosa ottengo?**
T da Cooper-Jacob e dalla risalita, indicativa; S no, perché dal pozzo di emungimento non è affidabile. La portata concedibile proposta
è quella della prova. Per S e il raggio d'azione servono le letture in almeno un piezometro.

**Non ho fatto la prova a gradini ma conosco la portata critica.**
Indica Q~c~, s~c~ e il raggio d'azione presunto nel riquadro *Portata critica nota* della scheda [Prova](prove.md): il programma
calcola i pozzi singoli, che danno T e K indicativi, e propone 0,9·Q~c~ come portata concedibile, dichiarando che Q~c~ è indicata da te.
Se c'è anche un gradino valido, vale la prova a gradini.

**Perché Hantush non compare?**
Hantush si calcola solo se il tipo di falda è semiconfinato (scheda Pozzo) e ci sono letture di pompaggio in un piezometro. Se il
fitting trova r/B trascurabile, la drenanza non si vede nei dati e i valori coincidono con Theis.

**Perché la falda libera dà un avviso con Theis e Cooper-Jacob?**
Quei metodi presuppongono la falda confinata. Il programma calcola comunque, ma senza correzione dello spessore saturo: i valori sono
buoni finché l'abbassamento è piccolo rispetto a H~1~. Vedi [Cenni teorici](teoria.md#validita-dei-risultati).

**I tempi della risalita contano dall'inizio o dall'arresto?**
Dall'arresto della pompa (t′). Indica l'istante d'arresto nella scheda Prova; se manca, il programma assume l'ultima lettura di
pompaggio. Se incolli ore dell'orologio, indica l'ora dell'arresto.

**Che cosa vuol dire «da verificare» su alcuni metodi dei pozzi incompleti?**
Che la formula, presa dal programma desktop, non è ancora stata verificata sul testo di riferimento (Muskat, Girinski, «L/b − L/2r» e
i tipi B e C di Chiesa). Il programma la calcola e la relazione lo dichiara: usala solo come confronto.

**L'assistente può decidere i valori di progetto al posto mio?**
No. Ti mostra l'effetto delle scelte e le applica solo se glielo chiedi esplicitamente; i numeri li calcola il motore. La scelta dei
valori di progetto e della portata da richiedere resta tua. Vedi [Assistente](assistente.md).

**La relazione dice «nessuna perforazione censita entro 500 m». È sufficiente per l'istanza?**
No. L'archivio ISPRA raccoglie solo le perforazioni comunicate ai sensi della L. 464/84 ed è incompleto: i pozzi preesistenti vanno
verificati sul posto e presso gli uffici competenti.

**In che lingua esce la relazione?**
Nella lingua dell'interfaccia, italiano o inglese. Nel documento inglese i testi scritti dal motore (nomi dei metodi, motivazioni,
avvisi) restano in italiano, e la copertina lo dice.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/it/faq.md).*
