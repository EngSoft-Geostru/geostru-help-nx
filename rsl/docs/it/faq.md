# FAQ — domande frequenti

## Generali

### RSL III è gratuito?

RSL III è incluso nella **suite GeoStru NX** con piano *freemium*. Per
dettagli aggiornati visita [`geostru.eu`](https://www.geostru.eu/) o scrivi
a `info@geostru.eu`.

### Devo installare qualcosa?

**No**. RSL III è una **web app** che si apre da
[`nx.geostru.ai/rsl/`](https://nx.geostru.ai/rsl/) in qualsiasi browser
moderno.

### Cosa significa "lineare equivalente"?

È un metodo di analisi di risposta sismica locale che approssima il
comportamento non lineare del terreno con iterazioni successive di
analisi **lineari**. Vedi [metodo.md](metodo.md) per i dettagli.

---

## Stratigrafia

### Da dove prendo le velocità Vs?

Misurazione diretta con prove sismiche:

- **MASW** (Multichannel Analysis of Surface Waves) — la più diffusa, da
  superficie con geofoni allineati
- **ReMi** (Refraction Microtremor) — da rumore sismico ambientale
- **Cross-hole** / **Down-hole** — sondaggi accoppiati o singoli con
  sismografo (più precisi)
- **HVSR** (sismica passiva microtremor, Nakamura 1989) — solo per stimare
  la frequenza fondamentale del sito, non Vs(z) puntuale
- **Cone Penetration Test sismico** (SCPT) — Vs continuo lungo CPTU

Se non hai misure dirette, **non** stimare Vs da letteratura o da N-SPT —
è troppo impreciso per RSL.

### Quanto deve essere profonda la stratigrafia?

Fino alla **bedrock di riferimento sismico** (Vs ≥ 800 m/s).

In Italia tipicamente:

- Pianura padana / sedimentarie costiere: 50-300 m
- Bacini intermontani (Umbria, Marche, Abruzzo): 30-100 m
- Aree montane / falesia: 5-30 m

Se non raggiungi Vs > 800 m/s con i sondaggi, estrapola con Vs costante o
crescente lineare fino a una profondità di ipotesi (DOC: scrivilo nella
relazione tecnica).

### Posso usare gli SPT al posto di Vs?

**No, non direttamente**. SPT misura la resistenza alla penetrazione, non la
velocità delle onde di taglio. Esistono correlazioni empiriche
(Ohta-Goto 1978, Ohsaki-Iwasaki 1973, Pitilakis 1999) ma sono **molto
incerte** (errore tipico 30-50%).

Per la liquefazione SPT è perfetto (vedi [LiquiTer](https://nx.geostru.ai/liquiter/)).
Per RSL serve sismica diretta.

### Come scelgo la curva di degradazione?

Dipende dal terreno:

- **Sabbie** → Seed-Idriss (1970), Darendeli (2001)
- **Argille** → Vucetic-Dobry (1991), in funzione dell'IP
- **Ghiaie** → curve specifiche (limited library, raramente disponibili)
- **Riempimenti antropici** → curve di sabbia con ξ_min maggiorato
- **Terreni marini molli** → Vucetic-Dobry per IP medio + γ_min più piccolo

In dubbio, prova 2 curve diverse (es. Seed-Idriss + Darendeli) e confronta
i risultati. Se i fattori FA/FH cambiano poco (< 10%), la scelta non è
critica.

---

## Accelerogramma di input

### Quanti accelerogrammi servono?

Per studi conformi NTC 2018 / ICMS 2008-2018: **almeno 7 accelerogrammi**
spectro-compatibili (paragrafo 7.3.5 NTC). RSL III in modalità multi-input
li elabora tutti e produce lo spettro **medio**.

Per studi di sensibilità o didattici: 1-3 accelerogrammi sono sufficienti.

### Dove trovo accelerogrammi reali?

- **PEER NGA-West** (USA, ma anche eventi europei): [ngawest2.berkeley.edu](https://ngawest2.berkeley.edu/)
- **ITACA** (italiano, INGV): [itaca.mi.ingv.it](http://itaca.mi.ingv.it/)
- **ESM** (European Strong-Motion Database): [esm.mi.ingv.it](https://esm-db.eu/)
- **REXEL** (software Iervolino): suite per la selezione spectro-compatibile

### Come faccio lo "spectral matching" / scaling?

RSL III **non** fa scaling automatico. Devi pre-processare gli accelerogrammi
con software dedicato:

- **REXEL** (Iervolino-Galasso, gratuito)
- **SeismoMatch** (commerciale)
- **EzFrisk** (commerciale)

Quindi importi gli accelerogrammi già "matchati" in RSL III.

### Outcrop o within?

Vedi [dati-input.md#outcrop-vs-within](dati-input.md#outcrop-vs-within). Per
registrazioni di archivio (PEER, ITACA): **outcrop** è l'opzione giusta nel
99% dei casi.

---

## Calcolo

### Quante iterazioni servono?

Tipicamente **4-8** per accelerogrammi standard. Se il calcolo richiede >15
iterazioni e non converge, di solito significa:

- Terreno con γ_max > 1% (regime fortemente non lineare → metodo EQL non
  affidabile, usa SRA non lineare)
- Curva di degradazione anomala
- Discretizzazione troppo fine (riduci f_max)

### Cosa fare se il calcolo non converge?

1. Aumenta tolleranza al 1% (default 0.5%)
2. Aumenta max iterazioni a 50
3. Verifica che il γ_max calcolato sia < 1% in tutti gli strati
4. Se γ_max > 1% in qualche strato → il sito è in regime non lineare
   significativo, RSL III non è lo strumento giusto

### γ_eff = 0.65 · γ_max — perché 65%?

È un valore empirico tarato da Idriss (1968) su test sperimentali. Vale
come "deformazione media equivalente" durante la storia ciclica. Per
storie sismiche con un pulsazione dominante può essere 0.5-0.55, per
storie con coda lunga 0.7-0.85. RSL III usa 0.65 di default; puoi
modificarlo in **Avanzate**.

---

## Output

### FA, FH, FT — quale uso per il mio progetto?

Vedi [icms.md](icms.md) per la tabella completa.

In sintesi:

- **Edifici bassi** (1-3 piani): FA
- **Edifici medi** (4-7 piani): FH
- **Edifici alti** (10+ piani): direttamente lo spettro RSL (FT è solo un
  riassuntivo)

### Lo spettro RSL è sotto quello NTC, va bene?

Sì, può succedere. Significa che il tuo sito amplifica **meno** rispetto a
quanto previsto dallo spettro NTC standard per la categoria di suolo
assunta. Conseguenza: **puoi progettare in modo meno conservativo** ma
solo se la tua analisi RSL è ben supportata da:

- Vs misurato (non stimato)
- 7+ accelerogrammi spectro-compatibili
- Conformità ICMS 2008/2018

In caso contrario, usa lo spettro NTC standard.

### Cedimenti post-sismici?

RSL III **non** calcola cedimenti post-sismici da liquefazione. Se il tuo
sito ha strati liquefacibili, dopo aver fatto l'analisi RSL usa
[**LiquiTer NX**](https://nx.geostru.ai/liquiter/) per la liquefazione +
cedimenti.

---

## Manca la mia domanda

[Scrivici](mailto:info@geostru.ai?subject=Help%20RSL%20III%20-%20FAQ) e la
aggiungiamo qui.
