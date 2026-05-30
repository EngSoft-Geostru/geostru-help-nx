# Strumenti — DPL · DPM · DPH · DPSH · SPT in foro

## Prove dinamiche continue

Nella prova dinamica continua il maglio cade ripetutamente e si conta il numero di colpi necessari a far avanzare la punta di un passo fisso (tipicamente 10 o 20 cm). La sequenza colpi/profondità è la materia prima di tutta l'elaborazione.

Dynamic Probing NX supporta i quattro tipi normati dalla **UNI EN ISO 22476-2**:

| Sigla | Tipo | Energia per colpo |
|---|---|---|
| **DPL** | Leggero | bassa |
| **DPM** | Medio | media |
| **DPH** | Pesante | alta |
| **DPSH** | Super pesante | molto alta |

Ogni tipo ha massa del maglio, altezza di caduta e diametro della punta definiti dalla norma. Nella libreria strumenti dell'app trovi i modelli più diffusi sul mercato già tabulati — puoi anche aggiungere uno strumento personalizzato con i tuoi dati di taratura.

### Il coefficiente di correlazione β

Il coefficiente β converte il numero di colpi della prova dinamica (N_DPM, N_DPSH…) nell'equivalente N_SPT. Il valore dipende dallo strumento e viene determinato con prove comparative in sito. Ogni strumento in catalogo ha un β di default; puoi sovrascriverlo con il valore della tua taratura specifica.

## Prove SPT in foro

La prova SPT (Standard Penetration Test, **UNI EN ISO 22476-3**) si esegue all'interno di un foro di sondaggio. Si battono 45 cm in tre tratti da 15 cm:

- **N1**: primo tratto (assestamento) — non entra nel conteggio
- **N2** + **N3**: secondo e terzo tratto → **N_SPT = N2 + N3**

Inserisci una prova SPT in foro dal Dashboard con il bottone **+ Prova in foro**. Definisci le quote di inizio delle singole battitura (es. 1,0 m — 2,5 m — 4,0 m) e per ciascuna inserisci N1, N2, N3. L'app calcola automaticamente N_SPT e costruisce il profilo.

### Stratigrafia delle prove in foro

Per le prove SPT in foro la stratigrafia si inserisce manualmente nella sezione **Stratigrafia interpretata**, strato per strato, esattamente come per le prove continue. N_SPT medio per strato viene calcolato dalle battitura che cadono nel range di profondità dello strato.

## Libreria strumenti

Vai in **Strumenti** dalla barra di navigazione per accedere alla libreria. Puoi:

- Visualizzare i parametri di ogni strumento (massa, altezza caduta, diametro punta, angolo punta, passo, β)
- Aggiungere uno strumento personalizzato
- Modificare il β di un modello esistente per il tuo specifico datalogger

Gli strumenti sono salvati nel file di progetto `.dprobe` — il file è autonomo e portabile anche su un altro PC senza perdere i dati di taratura.
