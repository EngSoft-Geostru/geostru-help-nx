# FAQ — domande frequenti

## Generali

### LiquiTer NX è gratuito?

LiquiTer NX è incluso nella **suite GeoStru NX** con piano *freemium*:

- **Free**: accesso, calcolo completo, export CSV
- **Subscription**: report Word, AI Import, batch multi-sito, supporto prioritario

Per dettagli: [`geostru.ai`](https://www.geostru.ai/) o `info@geostru.ai`.

### Devo installare qualcosa?

**No**. LiquiTer NX è una **web app** che si apre da
[`nx.geostru.ai/liquiter/`](https://nx.geostru.ai/liquiter/) in qualsiasi
browser moderno. Funziona su PC Windows / Mac / Linux.

### I miei dati passano per server GeoStru?

I calcoli avvengono **lato server** (in cloud GCP, criptati). Il progetto
viene salvato sul tuo dispositivo come `.json` quando premi *Salva*. Non
condividiamo i dati con terzi.

Se servono **dati riservati** (perizie giudiziali, siti militari): scrivici
in privato per opzioni di hosting on-premise.

---

## Input

### Dove trovo a_g e Mw del mio sito?

- **a_g** (NTC 2018): da [parametri-sismici.geostru.ai](https://nx.geostru.ai/parametri-sismici/)
  con coordinate + periodo di ritorno (vita nominale × Cu × P_VR)
- **Mw**: dalla magnitudo massima attesa della **zona sismogenetica**
  INGV (DISS database). Per Italia: Calabria/Friuli ~ 7.0, Appennino
  Centrale ~ 6.5, Pianura Padana ~ 5.5–6.5, Sardegna < 5.5.

### Categoria suolo se non ho Vs,30

NTC 2018 ammette stima **da prove geotecniche**:

- Cat. **C**: terreni sabbiosi/ghiaiosi addensati, argille consistenti
- Cat. **D**: terreni granulari sciolti, argille tenere
- Cat. **E**: alluvioni di spessore 5–20 m su substrato di Cat. A

In dubbio, considera **un caso più sfavorevole** o effettua MASW per
misurare Vs,30.

### Quanto cambia il risultato tra Seed e Boulanger?

In sabbie pulite/limose tipiche, la differenza è entro il **10-20%** sul
FSL. Boulanger-Idriss tende a essere **più conservativo** in sabbie
limose. Lancia entrambi e confronta — se entrambi danno IPL > 5, il
sito è critico (concordanza tra metodi rinforza la conclusione).

### Posso usare LiquiTer per terreni argillosi?

**No**, non in modo diretto. La liquefazione vera e propria riguarda
sabbie e sabbie limose sature. Per argille può esistere il fenomeno di
**cyclic softening** (decadimento ciclico della resistenza non drenata),
ma richiede metodi diversi (Boulanger-Idriss 2007 per argille, Bray-
Sancio 2006). LiquiTer attualmente non implementa cyclic softening.

Argille con **>35% di particelle < 5 µm** vengono **escluse**
automaticamente dal calcolo (NTC 2018).

### Posso usare LiquiTer su pendio?

LiquiTer NX assume **terreno orizzontale**. Sui pendii la presenza di una
tensione di taglio statica (K_α correction) modifica il CRR. Per analisi
su pendio servirebbe un metodo dedicato — al momento usiamo solo K_α = 1
(orizzontale), conservativo per pendio non eccessivamente ripido.

---

## Calcolo

### Cosa fa la funzione "Esegui calcolo"?

Per ogni profondità z lungo la stratigrafia:

1. Calcola tensioni σ_v, σ'_v
2. Calcola CSR (Seed-Idriss)
3. Calcola CRR secondo il metodo selezionato
4. Applica MSF e K_σ
5. Calcola FSL = (CRR · MSF · K_σ) / CSR
6. Marca lo strato come liquefacibile se FSL < FSL_limite

Poi integra IPL e cedimenti.

### Vedo FSL = 99 in alcuni strati. Perché?

FSL = 99 (o "non liquefacibile") significa che lo strato:

- È **sopra falda** (terreno non saturo)
- Ha **% argilla > 35%** (escluso da NTC)
- Ha **profondità > 20 m** (escluso da NTC)
- Ha **N-SPT troppo alto** per essere liquefacibile (terreno molto addensato)

Tutti questi sono casi in cui il calcolo è **logicamente bypassato**.

### Il fattore di sicurezza limite default è 1.25, posso cambiarlo?

Sì. Default 1.25 (NTC 2018). Puoi impostare 1.0 (EC8) o 1.5 (analisi
conservativa). Modificalo nel campo *Fattore di sicurezza limite*. Il calcolo
resta identico — cambia solo la **soglia di codifica** (cosa è "rosso" e
cosa è "verde") e il **conteggio dell'IPL**.

---

## Esportazioni

### Il Report Word non si apre

- Verifica di avere Word 2016+, LibreOffice 6+, o Google Docs
- Apri come fallback con LibreOffice (gestisce sempre il `.docx`)
- Se persiste, scrivici a info@geostru.ai col file allegato

### Voglio personalizzare il template Word

Per ora il template è centralizzato. Per un template custom (logo studio,
font), scrivi a `info@geostru.ai`.

---

## Manca la mia domanda

[Scrivici](mailto:info@geostru.ai?subject=Help%20LiquiTer%20NX%20-%20FAQ)
e la aggiungiamo qui.
