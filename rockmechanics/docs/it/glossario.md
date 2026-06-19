# Glossario

Definizioni sintetiche dei termini, degli indici e dei simboli usati nel rilievo geostrutturale, nelle classificazioni geomeccaniche e nella relazione di calcolo di Rock Mechanics NX. Dove utile, ogni voce rimanda al capitolo che la approfondisce.

## Rilievo e discontinuità

**Immersione (dip direction)** — direzione, misurata in gradi rispetto al Nord (0–360°), verso cui un piano di discontinuità immerge, cioè la direzione di massima pendenza proiettata sull'orizzontale.

**Inclinazione (dip)** — angolo (0–90°) fra il piano di discontinuità e l'orizzontale, misurato lungo la linea di massima pendenza. Insieme all'immersione definisce la *giacitura* del piano.

**Discontinuità** — qualsiasi superficie di separazione meccanica nell'ammasso (giunto, frattura, faglia, piano di strato, scistosità) lungo cui la resistenza a trazione è praticamente nulla. È l'elemento che governa il comportamento dell'ammasso roccioso.

**Famiglia di giunti** — insieme di discontinuità con giacitura simile, originate dallo stesso evento tettonico. Il numero di famiglie presenti determina il parametro $J_n$ nella classificazione di [Barton](barton.md).

**Persistenza** — estensione areale di una discontinuità nel suo piano, misurata come lunghezza di traccia. Esprime quanto la frattura è continua: alta persistenza significa superfici di scorrimento potenzialmente passanti.

**Apertura** — distanza, misurata ortogonalmente, fra le due pareti di una discontinuità nel tratto in cui non sono a contatto. Influenza permeabilità, riempimento e resistenza al taglio.

**Rugosità** — irregolarità della superficie di una discontinuità a piccola e media scala. Aumenta l'angolo d'attrito di picco; si quantifica con il **JRC** (*Joint Roughness Coefficient*, 0–20) per il criterio di Barton-Bandis, o con i descrittori che fissano $J_r$.

**Alterazione** — grado di degrado per agenti chimico-fisici delle pareti della discontinuità e della roccia matrice. Riduce la resistenza ed entra in $J_a$ e nei punteggi RMR.

**Riempimento** — materiale (argilla, limo, sabbia, calcite, ecc.) interposto fra le pareti di una discontinuità. Natura e spessore del riempimento controllano la resistenza al taglio del giunto.

**Spaziatura** — distanza media $s$ fra discontinuità adiacenti della stessa famiglia, misurata ortogonalmente ai piani. Determina la dimensione dei blocchi e il parametro `A3` di RMR (vedi [Classificazioni](classificazioni.md#spaziatura-delle-discontinuita)).

**$J_v$ (volumetric joint count)** — numero totale di giunti per metro cubo di ammasso, sommato su tutte le famiglie. È la base per stimare l'RQD quando mancano le carote di sondaggio.

## Indici di classificazione

**RQD (Rock Quality Designation)** — grado di fratturazione dell'ammasso, espresso come percentuale di carota recuperata in spezzoni $\geq 100$ mm. In assenza di sondaggi si stima da $J_v$ (Palmström) o da $\lambda$ (Priest-Hudson). Vedi [RQD](classificazioni.md#rqd-rock-quality-designation).

**Indice Q (Barton)** — indice della *Norwegian Geotechnical Institute classification* per opere in sotterraneo e caratterizzazione generale: $Q = \frac{RQD}{J_n} \cdot \frac{J_r}{J_a} \cdot \frac{J_w}{SRF}$. Vedi [Barton](barton.md).

**RMR (Rock Mass Rating)** — indice di Bieniawski (0–100) ottenuto sommando punteggi parziali (resistenza, RQD, spaziatura, condizioni dei giunti, acqua) e correggendo per l'orientamento. È il riferimento da cui derivano molte altre classificazioni. Vedi [Bieniawski & Romana](rmr-romana.md).

**SMR (Slope Mass Rating)** — adattamento dell'RMR ai versanti, di Romana: a RMR si applicano fattori che pesano l'orientamento relativo fronte/giunto e il metodo di scavo. Vedi [Bieniawski & Romana](rmr-romana.md).

**SRMR (Slope Rock Mass Rating)** — scala di Robertson dedicata ai versanti in roccia tenera (RMR < 40), dove l'RMR classico perde di affidabilità. Vedi [Robertson](robertson.md).

**Indice n (Jašarević)** — indice della classificazione di Jašarević & Kovačević per gli ammassi carbonatici, correlato empiricamente all'RMR. Vedi [Jašarević](jasarevic.md).

**Indice N / Rock Mass Number** — *Rock Mass Number* di Singh & Goel: coincide con l'indice Q calcolato ponendo $SRF = 1$, cioè depurato dall'effetto dello stato tensionale. Vedi [Singh & Goel](singh-goel.md).

**RCR (Rock Condition Rating)** — RMR privato del punteggio della resistenza a compressione e della correzione per orientamento; usato come grandezza intermedia nelle correlazioni fra RMR e Q.

**GSI (Geological Strength Index)** — indice di Hoek che descrive la qualità dell'ammasso dalla struttura e dalle condizioni delle discontinuità; è il parametro d'ingresso del criterio di rottura Hoek-Brown per derivare i parametri di resistenza.

## Parametri di resistenza

**$S_u$ — resistenza a compressione uniassiale** — resistenza a compressione monoassiale della roccia *intatta* (matrice). Si determina da Point Load, sclerometro o stima ISRM e alimenta il parametro `A1` di tutti i metodi derivati da RMR (vedi [Classificazioni](classificazioni.md#resistenza-a-compressione-uniassiale-su)).

**$I_s$ — indice di carico puntuale (point load)** — indice ricavato dalla prova Point Load Test, correlato a $S_u$ dalla $S_u = K \cdot I_s$ con $K$ funzione di $I_s$.

**$\sigma_c$** — tensione di compressione; nel contesto dell'ammasso indica la resistenza a compressione di riferimento (roccia intatta o ammasso, secondo il criterio adottato).

**Coesione $c$** — componente della resistenza al taglio indipendente dalla tensione normale, nel criterio di Mohr-Coulomb $\tau = c + \sigma_n \tan\varphi$. Sulle discontinuità reali è spesso bassa o nulla.

**Angolo d'attrito $\varphi$** — componente attritiva della resistenza al taglio: $\tan\varphi$ moltiplica la tensione normale efficace $\sigma_n$ nel criterio di Mohr-Coulomb.

**Modulo di deformazione $E$** — modulo che lega tensione e deformazione dell'ammasso roccioso; si stima dalle classificazioni (correlazioni con RMR, Q o GSI) ed è un parametro caratteristico dell'output.

**SRF (Stress Reduction Factor)** — fattore di riduzione tensionale dell'indice Q, che tiene conto dello stato di sforzo in roccia massiva, del disturbo tettonico e di condizioni spingenti o rigonfianti (vedi [Barton](barton.md#srf)).

**$J_n$ (Joint Set Number)** — parametro di Barton legato al numero di famiglie di giunti: cresce all'aumentare delle famiglie e quindi della disgregazione dell'ammasso (vedi [Classificazioni](classificazioni.md#jn)).

**$J_r$ (Joint Roughness Number)** — parametro di Barton funzione della rugosità e dell'ondulazione della famiglia di giunti più sfavorevole (vedi [Classificazioni](classificazioni.md#jr)).

**$J_a$ (Joint Alteration Number)** — parametro di Barton funzione dell'alterazione delle pareti e della natura/spessore del riempimento della discontinuità (vedi [Classificazioni](classificazioni.md#ja)).

**$J_w$ (Joint Water Number)** — parametro di Barton funzione delle condizioni idrauliche (afflusso e pressione dell'acqua nelle discontinuità) (vedi [Classificazioni](classificazioni.md#jw)).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
