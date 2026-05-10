# Glossario

Definizioni dei termini chiave usati in GMS NX e nel rilievo
geomeccanico in generale.

---

### α (alfa) · Inclinazione (dip)

Angolo che il piano della discontinuità forma con l'orizzontale.
Range **0–90°**: 0° = piano orizzontale, 90° = piano verticale.

### α₉₅ (alfa-95)

Semi-apertura del cono di confidenza al 95% del polo medio Fisher di
una famiglia. **Più piccolo = polo medio più preciso**. In pratica:
"con probabilità 95% il polo vero della famiglia sta entro `α₉₅`
gradi dal polo che ho stimato".

### β (beta) · Immersione (dip direction)

Direzione della massima pendenza del piano, misurata in azimut a
partire dal Nord (in senso orario). Range **0–360°**.
Esempio: `β = 90°` significa che il piano "scende" verso Est.

### Banner risultato

L'etichetta colorata in cima alla pagina dei risultati di GMS:

- 🟢 **Versante stabile** — nessun cinematismo critico
- 🟡 **Attenzione: ribaltamenti** — toppling presenti
- 🔴 **Versante a rischio** — planari o cunei instabili

### Ciclografica

La proiezione 2D di un piano sullo stereonet, sotto forma di arco di
cerchio massimo. È il "complemento" del polo: se vuoi visualizzare
*l'orientazione del piano stesso* (non solo della sua normale), guardi
la ciclografica.

### Cilindrico (Cylindrical Best Fit)

Calcolo geometrico che cerca un **asse comune** attorno a cui ruotano
i poli (ipotesi di piegatura cilindrica). Restituisce **β/α dell'asse**
e gli **indici Woodcock K e C** che misurano *cluster vs girdle*.

### Cluster (di poli)

Insieme di poli che si raggruppano in una zona ristretta dello
stereonet. Indica una **famiglia** di discontinuità co-orientate. Il
parametro `k` di Fisher misura quanto è serrato il cluster.

### Cono d'attrito

Cerchio sullo stereonet centrato nel punto verticale, di raggio
proporzionale a `(90° - φ)`. Tutti i poli **al di fuori** del cono
hanno inclinazione `α < φ` ⇒ attrito sufficiente per la stabilità
(in assenza di altri fattori).

### Cuneo

Solido roccioso delimitato da **due famiglie di discontinuità** che si
intersecano. Sullo stereonet la **retta di intersezione** dei due
piani diventa un punto. Se quel punto soddisfa i criteri di Markland,
il cuneo è cinematicamente instabile (`⊗` rosso).

### Daylighting

Condizione per cui un piano "**esce**" dal versante (non è coperto).
In termini quantitativi: `α_giunto < α_pendio`. Senza daylighting, un
piano per quanto inclinato non può scivolare perché trattenuto dal
terreno a valle.

### Discontinuità

Termine generico per qualsiasi superficie di interruzione meccanica
nell'ammasso roccioso: **giunti** (joint), **fratture**, **faglie**,
**piani di stratificazione**, **schistosità**, **scistosità**,
**diaclasi**, **superfici di scivolamento**.

### Famiglia (joint set)

Gruppo di discontinuità con orientazione simile, generate dallo stesso
processo geologico. Sullo stereonet appare come **cluster di poli**.
GMS le identifica con **k-means sferico** o le accetta come **attese**
(centri pre-orientati).

### Fisher (statistica)

Distribuzione di probabilità per **vettori unitari sulla sfera** (=
poli sullo stereonet). Per una famiglia, GMS calcola:

- **vettore medio** (= polo medio Fisher)
- **R̄** (modulo del risultante normalizzato, 0–1)
- **k** (concentrazione, alto = cluster serrato)
- **α₉₅** (cono di confidenza al 95%)

### Giacitura

Coppia (β, α) che definisce l'orientazione di un piano nello spazio
3D. Sinonimo informale di "orientazione del piano".

### Goodman & Bray (1976)

Criterio per il **toppling** (ribaltamento). Un giunto è toppling-
suscettibile se: quadrante opposto al pendio, e
`(90° - α_giunto) + φ < α_pendio`.

### Hoek & Bray (1981)

Riferimento classico per la **stabilità dei pendii rocciosi**, da cui
GMS prende i criteri planari (insieme con Markland 1972).

### Inliers (RANSAC)

In RANSAC, i punti della nuvola 3D che cadono entro la **tolleranza**
dal piano candidato — cioè i punti che "sostengono" il piano. Più
inliers = piano più solido.

### Isodensità (Denness)

Mappa colorata sullo stereonet che mostra la **densità dei poli per
unità di area** (Schmidt-Lambert). Le zone rosse/calde sono dove si
addensano molti poli. Aiuta a identificare visivamente le famiglie
quando il k-means è dubbio.

### Joint set

Vedi **Famiglia**.

### k (Fisher)

Parametro di concentrazione della distribuzione Fisher per una
famiglia. Soglie indicative:

- `k < 5` → cluster molto disperso (probabilmente non è una famiglia
  vera)
- `5 ≤ k ≤ 30` → cluster moderato
- `k > 30` → cluster ben definito

### k-means sferico

Algoritmo di clustering iterativo applicato sulla **sfera unitaria**
(non sul piano). GMS lo usa per identificare automaticamente le
famiglie a partire dalla nuvola di poli.

### Markland (1972)

Test grafico-statistico per la **verifica cinematica** di pendii
rocciosi. Risponde a: "esiste un meccanismo di rottura geometricamente
compatibile?" (planare, toppling, cuneo).

### Pendio

In GMS, il versante su cui si vuole verificare la stabilità.
Caratterizzato da:

- **Dip α_pendio** (inclinazione)
- **Dip direction β_pendio** (direzione di immersione)

### Persistenza

Lunghezza visibile di una discontinuità (m). Uno dei parametri ISRM
classici. In GMS sta nella colonna *Lunghezza* (modalità Dettagli
completi).

### Planare (cinematismo)

Scivolamento di un singolo blocco lungo **un solo piano** di
discontinuità (non un cuneo). Markland lo segnala se: stesso
quadrante del pendio, daylighting, e `α > φ`.

### Polo (di un piano)

Punto in cui la **normale al piano** interseca l'emisfero inferiore
della sfera unitaria. Sullo stereonet è un puntino. Posizione:
distanza dal centro proporzionale a `(90° - α)`, azimut `β + 180°`.

### RANSAC (Random Sample Consensus)

Algoritmo iterativo per estrarre **modelli geometrici** (qui: piani)
da dati rumorosi. Usato in GMS per estrarre piani da nuvole 3D.

### Reticolo stereografico

La griglia di sfondo dello stereonet (meridiani + paralleli). Può
essere **equatoriale** (default matematico) o **polare** (a clessidra).

### Ribaltamento

Vedi **Toppling**.

### Schmidt-Lambert (proiezione)

Proiezione stereografica **equiarea** (conserva le aree). È lo
standard per l'analisi statistica e per le isodensità. Default in GMS.

### Stereonet

Diagramma circolare 2D che rappresenta orientazioni 3D di piani e
linee. Sinonimo di "stereogramma" o "rete stereografica".

### Toppling (ribaltamento)

Cinematismo in cui un blocco roccioso ruota attorno a un'asse alla
sua base (come un libro che cade dalla mensola). Markland lo segnala
con il criterio Goodman & Bray.

### Vettore di Fisher

Vettore risultante (somma vettoriale) di tutti i poli unitari di una
famiglia. La sua **direzione** è il polo medio, il suo **modulo
normalizzato** è `R̄`.

### Vollmer (1990)

Riferimento per l'analisi del fabric con eigenvalues della matrice
di orientazione. GMS lo usa nel **Cylindrical Best Fit**.

### Woodcock K, C (1977)

Indici di forma del cluster sferico:

- `K = ln(λ₁/λ₂) / ln(λ₂/λ₃)` — forma (cluster vs girdle)
- `C = ln(λ₁/λ₃)` — intensità del fabric

Tabella di interpretazione classica nella pagina
[Famiglie](famiglie.md).

### Wulff (proiezione)

Proiezione stereografica **equiangola** (conserva gli angoli).
Tradizionalmente usata per costruzioni geometriche a mano.
Disponibile in GMS come alternativa a Schmidt-Lambert.

### φ (fi) · Angolo d'attrito

Angolo d'attrito interno del materiale roccioso lungo i piani di
discontinuità. Tipicamente **25–35°** per ammassi rocciosi sani,
**15–25°** per giunti con riempimento argilloso. È il **terzo
parametro obbligatorio** del test di Markland.

---

## Vedi anche

- [Cosa si misura](rilievo.md) — i parametri ISRM in dettaglio
- [Stereonet](stereonet.md) — gli elementi grafici sul disco
- [Famiglie](famiglie.md) — k-means e Fisher in pratica
- [Markland](markland.md) — i 3 cinematismi e i criteri

---

*Termine mancante? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GMS%20NX%20-%20Glossario).*
