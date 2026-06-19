# Domande frequenti

Le risposte rapide ai dubbi più comuni su Rock Mechanics NX: quale classificazione scegliere, come stimare i parametri mancanti e come produrre la relazione.

### Quale classificazione devo scegliere?

Dipende dal problema. Per una **caratterizzazione generale** o per opere in **sotterraneo** parti dall'indice Q di [Barton](barton.md) o dall'indice N di [Singh & Goel](singh-goel.md). Per la stabilità dei **versanti** usa lo SMR di [Romana](rmr-romana.md); se il versante è in **roccia tenera** (RMR < 40) ricorri allo SRMR di [Robertson](robertson.md). Per gli **ammassi carbonatici** è tarato l'indice n di [Jašarević](jasarevic.md). Nulla vieta di calcolarne più d'una sullo stesso rilievo e confrontare le classi.

### Che differenza c'è tra l'indice Q e l'RMR?

Sono due sistemi diversi. L'**RMR** di Bieniawski è una somma di punteggi su scala 0–100 (vedi [RMR](rmr-romana.md)); l'**indice Q** di [Barton](barton.md) è un prodotto/rapporto di sei parametri di giunto e varia su scala logaritmica, tipicamente da $0{,}001$ a $1000$. Misurano la stessa qualità con grandezze diverse e sono legati da correlazioni empiriche; la più usata è $RMR = 9 \ln Q + 44$.

### Come stimo l'RQD se non ho carote di sondaggio?

Dal rilievo delle discontinuità. Con la relazione di **Palmström** lo ricavi dal *volumetric joint count*: $RQD = 115 - 3{,}3\,J_v$. In alternativa, con la formula di **Priest e Hudson** dal numero medio di giunti per metro lineare $\lambda$. Entrambe sono descritte in [RQD](classificazioni.md#rqd-rock-quality-designation).

### Posso importare il rilievo da GMS o eGeo Compass?

Sì. Rock Mechanics NX legge i dati di rilievo geostrutturale provenienti da **GMS** e da **eGeo Compass**, così non devi reinserire le giaciture a mano. Formati supportati e modalità di import sono descritti in [Formati file](formati.md).

### Qual è la differenza tra scivolamento planare e a cuneo?

Lo **scivolamento planare** è il movimento di un blocco lungo una *singola* discontinuità che emerge sul fronte: è una verifica all'equilibrio limite in 2D (vedi [Scivolamento planare](scivolamento-planare.md)). Lo **scivolamento a cuneo** riguarda invece un cuneo tetraedrico delimitato da *due* discontinuità che si intersecano, e si analizza in 3D lungo la loro linea d'intersezione (vedi [Sliding 3D](sliding-3d.md)).

### Quando uso Rock Mechanics e quando RockPlane?

Usa **Rock Mechanics** per la *classificazione geomeccanica* dell'ammasso, la derivazione dei parametri caratteristici e le verifiche di base dei cinematismi (scivolamento planare e a cuneo). Passa a **[RockPlane](https://help.nx.geostru.ai/rockplane/it/)** quando devi *progettare gli interventi* (chiodi, tiranti, reti) su una rottura planare con fessura di trazione e due giunti, con verifica secondo NTC/Eurocodici.

### Come ottengo coesione, angolo d'attrito e modulo dell'ammasso?

Sono i **parametri caratteristici** che l'app deriva automaticamente dalle classificazioni. Una volta calcolato l'indice di qualità (RMR, Q o GSI), Rock Mechanics applica le correlazioni note per restituire coesione $c$, angolo d'attrito $\varphi$ e modulo di deformazione $E$ dell'ammasso, pronti da riportare nelle verifiche di stabilità.

### Come esporto la relazione?

Dalla funzione di esportazione: l'app genera la **relazione di calcolo** con i dati di rilievo, gli indici, le classi e i parametri caratteristici, insieme agli elaborati grafici. Procedura, formati e personalizzazioni sono descritti in [Esportazione e report](export.md).

### Dove trovo le figure e il disegno CAD citati nel manuale?

Nella pagina [Risorse](risorse.md): puoi scaricare le figure dei cinematismi in PDF, il disegno dello scivolamento planare in DWG e il manuale storico della versione desktop.

### Come segnalo un errore o un bug?

Scrivi a [info@geostru.ai](mailto:info@geostru.ai?subject=Bug%20Rock%20Mechanics%20NX) descrivendo il problema e, se possibile, allegando uno screenshot e il file di progetto che lo riproduce.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
