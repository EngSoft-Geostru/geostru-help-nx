# Domande frequenti

**MP NX calcola i gruppi di pali?**
No. Calcola il palo singolo e il micropalo singolo: niente efficienza della palificata né
effetto di gruppo sui cedimenti. L'elenco completo di ciò che non copre è nella
[home](index.md).

**Devo amplificare i carichi o lo fa il programma?**
Li amplifichi tu. I carichi sono **valori di progetto**: MP NX non applica γ~F~ alle azioni.
Il nome della combinazione è un'etichetta. Vedi
[Carichi, combinazioni e normativa](combinazioni.md).

**In che verso è positiva F~x~?**
Da destra a sinistra. F~y~ è positiva verso il basso e M è positivo orario: è la convenzione
del programma desktop MP. Lo schema delle azioni sopra la testa del palo, nell'anteprima, ti
mostra il verso prima di calcolare.

**Perché la scheda Cedimenti dice «Nessun cedimento calcolato»?**
La combinazione scelta nelle **Opzioni cedimenti** non ha carico verticale. Assegna F~y~ in
quella combinazione, scegline un'altra, oppure scrivi il **Carico** Q. Vedi
[Cedimenti](cedimenti.md).

**Perché il momento resistente è più basso di quello degli abachi?**
Con **NTC 2018 (sismica non dissipativa)** M~u~ è il momento di **primo snervamento**, più
basso di quello a rottura: è voluto. Per il confronto con gli abachi scegli **NTC (a
rottura)**. Vedi [Sezioni e armature](armature.md).

**Le schede Analisi FEM e Sezioni e armature sono vuote.**
L'analisi FEM non è attiva. Spunta **Esegui l'analisi FEM e il progetto della sezione con
Calcola** nella card **Armatura e analisi FEM** e ricalcola. Se era attiva, leggi i messaggi
in fondo alla scheda **Carico limite**: il FEM può non essere riuscito, e in quel caso il
suo credito non è stato addebitato.

**Manca H~max~ di Broms.**
M~y~ vale 0 e l'analisi FEM è spenta, quindi il programma non ha un momento ultimo da usare.
Scrivi M~y~ nella card **Materiali e armatura** oppure attiva il FEM.

**Ho scritto c~u~ ma il risultato non cambia.**
Controlla di aver spuntato **Condizione non drenata** nelle proprietà dello strato. Senza
la casella lo strato è calcolato in condizione drenata con φ e c′. Vedi
[Stratigrafie e falda](stratigrafia.md).

**Il calcolo si ferma con un messaggio sulla falda.**
Due cause: la profondità della falda coincide con una quota di strato, oppure a uno strato
sotto falda manca il peso saturo γ~sat~.

**I miei risultati differiscono dell'1–2 % da quelli del programma desktop.**
Quasi sempre è l'archivio dei materiali: peso di volume e modulo elastico del calcestruzzo
sono diversi fra l'archivio SI e quello tecnico del desktop. Metti nell'archivio del
progetto i valori che vuoi confrontare. Vedi [Validazione del codice](validazione.md).

**Cambiare le regole della gabbia costa crediti?**
No. Barra commerciale, sovrapposizione, ripresa, spirale e cerchiature ridisegnano la gabbia
dal risultato già calcolato, senza ricalcolo e senza addebito.

**Ho pagato un'operazione che non è andata a buon fine?**
No. I crediti sono addebitati solo a operazione riuscita: calcolo senza errori, file
prodotto, risposta dell'assistente arrivata.

**Dove sono i progetti di esempio?**
Nel pulsante **?**, scheda **Risorse**: si scaricano come file `.mpnx` e si aprono con
**File → Apri**. Vedi [Progetti di esempio](esempi.md).

**Il progetto resta salvato se chiudo il browser?**
L'app conserva lo stato nella sessione mentre lavori, ma il progetto vero è il file
`.mpnx`. Salvalo con **File → Salva** o su **GeoDropbox** prima di chiudere.

**In quali lingue è disponibile?**
Interfaccia e relazione sono in italiano e in inglese. Cambi lingua dal selettore in alto a
destra.

**La vista 3D non compare.**
Serve WebGL. Se il browser non lo supporta o lo ha disattivato, l'app lo segnala al posto
della vista.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MP%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mp/docs/it/faq.md).*
