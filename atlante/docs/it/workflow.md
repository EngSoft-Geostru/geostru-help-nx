# Flusso di lavoro completo

La sequenza di un fascicolo reale, con tutte le opzioni.

## Il sito

**Punto.** Latitudine e longitudine WGS84, in gradi decimali (virgola o punto). Devono cadere in
Italia. La ricerca per indirizzo passa dal server (Nominatim) e propone una posizione
*indicativa*: sposta sempre il segnaposto sul sito.

**Raggio.** L'intorno, in metri, usato dalle fonti che ragionano per distanza (eventi sismici:
il raggio del catalogo è fisso a 30 km, il tuo raggio compare nelle tavole come cerchio
tratteggiato). Da 500 a 30 000 m.

**Perimetro (facoltativo).** Disegno a clic o import da file; le fonti che sanno interrogare
un'area lo usano al posto del punto. Dettagli in [Perimetro del sito](perimetro.md).

## Il profilo

Stesse fonti, pesate in modo diverso. Ogni fonte del catalogo dichiara a quali profili serve; il
profilo scelto decide cosa viene interrogato e quali app NX vengono proposte alla fine. Vedi
[Profili della relazione](profili.md).

## L'incarico

Titolo, committente e descrizione dell'intervento non cambiano le interrogazioni, ma entrano nel
Word (capitolo «Oggetto e limiti dell'incarico») e nel prompt dell'assistente. Se non descrivi
l'intervento, il Word lo dichiara: geometria, quote e fasi dell'opera vanno indicati, perché da
essi dipende il volume significativo da caratterizzare.

## La corsa

Il fascicolo entra in coda e un lavoratore in background interroga le fonti: prima i **limiti
amministrativi** ISPRA, che danno Comune, Provincia, Regione e codice ISTAT (IdroGEO vuole
l'ISTAT), poi tutto il resto in parallelo con un tetto, perché gli enti non gradiscono le
raffiche. Ogni fonte ha un tempo massimo; se non risponde, l'evidenza è «non disponibile» e il
fascicolo si completa lo stesso.

Limiti per account: **20 fascicoli al giorno**, **3 in lavorazione** contemporaneamente. I
fascicoli si conservano **12 mesi**.

## Le evidenze

Per ogni fonte vedi nome, ente e licenza, l'esito, una riga di sintesi, la durata, il link
all'**originale** (l'interrogazione esatta, riproducibile) e, aprendo **Dettaglio**, i record
restituiti. Le tavole sono immagini cliccabili.

| Esito | Significato |
|---|---|
| **trovata** | la fonte ha restituito uno o più elementi al punto (o nel perimetro) |
| **nulla al punto** | la fonte ha risposto e non risulta nulla: è un risultato, non una prova di assenza |
| **non disponibile** | il servizio non ha risposto entro il tempo massimo; il dato resta da acquisire |

## Il testo dell'assistente

**Genera il testo** manda all'assistente le sole evidenze numerate — mai le tavole, mai i campi
tecnici — e riceve sintesi, una sezione per tema e l'elenco «da verificare». Ogni frase che
afferma un dato cita [n]; una sezione senza riferimenti viene scartata, un riferimento inesistente
tolto. Il testo si rigenera a richiesta, mai da solo. Dettagli e quota in
[Testo dell'assistente e Word](relazione.md).

## Le tue indagini

Un PDF alla volta: l'assistente propone gli elementi letti (con pagina e citazione), tu accetti
quelli che ti servono e diventano evidenze «documento fornito». Vedi [Le tue indagini](indagini.md).

## Il Word

Indice, premessa e metodo, oggetto e limiti, sintesi, ubicazione, un capitolo per tema con tavole
e tabelle, verifiche da completare, conclusioni (tue), le app NX, le fonti con i portali. Vedi
[Testo dell'assistente e Word](relazione.md).

## GeoDropbox e i tuoi fascicoli

Il pulsante **GeoDropbox** salva nel progetto scelto il Word e il file `.atlante` (fascicolo con
le tavole dentro), e da lì un `.atlante` si reimporta come nuovo fascicolo. **I miei fascicoli**
elenca i tuoi con stato, rinomina, rilancio (nuova corsa sulle stesse fonti) ed eliminazione.

## Prosegui con le app NX

A fascicolo pronto, le schede in testa alla pagina aprono le app NX pertinenti al profilo con
`lat`, `lon` e Comune già passati: Parametri Sismici, Loadcap, MP, Slope, LiquiTer, RSL III,
Stratigrapher, Dynamic Probing, Maps, Hydrogeo. **Copia coordinate** mette lat, lon negli appunti.
