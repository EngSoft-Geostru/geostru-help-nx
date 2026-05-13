# AI Import — caricare serie pluviometriche da PDF/Excel

Le serie storiche annuali si trovano spesso in:

- **PDF degli annuari regionali** (decine di pagine, tabelle scansionate o testuali);
- **Excel** scaricati da portali idro-meteorologici;
- **file CSV** non standard, con intestazioni in italiano, separatori vari.

Inserire questi dati a mano è lungo e soggetto a errori di trascrizione.
Runoff Lab NX integra un **importer assistito da intelligenza artificiale**
che riconosce automaticamente lo schema del file e popola la stazione.

## Come funziona

1. *File → Importa → Da file con AI…* → si apre il modale.
2. Trascina il file (PDF o Excel) oppure incolla testo direttamente.
3. L'AI estrae:
   - **anagrafica della stazione** (nome, codice, comune, regione, lat/lon, periodo osservazione);
   - **valori massimi annui** per durata (60′, 3h, 6h, 12h, 24h).
4. Pannello di **anteprima**: confronta i valori estratti con quelli del file,
   correggi se serve.
5. Premi *Conferma* → tutto entra nello studio.

## Formati riconosciuti

| Formato | Note |
|---------|------|
| PDF testuale | Annuari regionali, estratti tabellari. |
| PDF scansionato | OCR automatico, qualità funzione della scansione. |
| Excel `.xlsx` | Una riga = un anno; colonne = durate. Anche se ordinate diversamente. |
| CSV / TSV / TXT | Separatori `,`, `;`, `\t` o spazi. |
| Testo libero (copia-incolla) | Utile per estratti di annuari più vecchi. |

## Esempi pronti

Nel modale Info → **Risorse** trovi due file di esempio scaricabili:

- `ai-rainfall-sample-cosenza.xlsx` — formato Excel realistico (annuario Calabria).
- `ai-rainfall-sample-cosenza.pdf` — estratto PDF annuario regionale.

Apri il modale AI Import e trascina uno dei due per vedere la procedura in azione.

## Cosa fa l'AI dietro le quinte

L'estrazione gira sul nostro backend con un modello multimodale (Gemini
1.5 Pro) addestrato a riconoscere tabelle pluviometriche italiane:

- identifica **header in italiano** (es. "Massimi annuali di pioggia di durata 1h, 3h…");
- distingue **valori validi** da note a piè di pagina, segnaposto (`---`, `n/d`);
- riconosce **anagrafiche** anche quando sono testo a metà pagina;
- normalizza separatori decimali e numero.

Solo il file caricato viene inviato al backend; **non vengono salvati né
indicizzati**. Costo: l'operazione consuma alcuni crediti NX (visibile nel
chip in alto a destra prima del lancio).

## Quando la verifica conta

L'AI ha buona precisione ma non è infallibile. Casi che richiedono controllo:

- **Tabelle multi-stazione**: l'AI prova a identificare la stazione richiesta,
  ma su PDF non strutturati può confondere righe.
- **Decimali ambigui**: `34,8` italiano vs `34.8` inglese — l'AI sceglie in
  base al contesto ma controlla almeno qualche valore.
- **Periodi spezzati**: alcune serie hanno buchi indicati con `---`; verifica
  che siano stati saltati correttamente.

Conferma sempre l'anteprima prima di accettare.

## Alternativa manuale

Se preferisci, puoi:

- copiare la colonna dei massimi annui da Excel;
- incollare direttamente nella casella della singola durata.

Il parser semplice supporta `.` e `,` come separatore decimale, uno per riga.
