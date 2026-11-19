# Validazione e limiti

La validazione documenta campi d'impiego, basi teoriche, casi di prova e scarti noti. Aiuta il progettista a valutare l'affidabilità del codice come richiesto dal punto 10.2 delle NTC 2018.

Non è una certificazione. Non sostituisce il controllo del modello, dei dati e dei risultati da parte di chi firma il progetto.

Il riferimento generale è la pagina [Validazione del codice di calcolo](https://geostru.ai/en/validation/). Il documento tecnico di SPW NX accompagna il motore indicato nel blocco «Codice di calcolo» della relazione.

## Riferimenti usati

La verifica usa due famiglie di riferimento:

- **letteratura pubblica**, per metodi, ipotesi e casi risolti;
- **programma desktop**, per controllare il porting dove i due modelli coincidono.

La bibliografia dei metodi è in [Metodi](metodi.md#bibliografia-essenziale). Un confronto con il desktop non sostituisce un riferimento indipendente.

## I livelli di confronto

| Livello | In parole semplici | Cosa dimostra |
|---|---|---|
| L0 | Il lettore del desktop viene confrontato con i risultati già noti dello stesso programma | che il porting di riferimento è letto e riprodotto correttamente |
| L1 | SPW NX e desktop lavorano su un caso a una fase con lo stesso modello | che il calcolo coincide dove il confronto diretto è possibile |
| L2 | Un progetto a più fasi viene confrontato con un riferimento indipendente | che la sequenza costruttiva è corretta rispetto a una fonte esterna |
| L3 | SPW NX e desktop vengono confrontati su un progetto a più fasi con modelli diversi | quali differenze nascono dal nuovo modello, senza pretendere coincidenza |

Il confronto L1 usa casi in cui geometria, combinazioni e storia sono compatibili. Il confronto L3 misura e spiega gli scarti. Non li considera automaticamente errori né li nasconde.

Per i casi a più fasi resta necessario ampliare i riferimenti indipendenti L2. Un risultato vicino al desktop non basta a dimostrare la validità del nuovo modello.

## Differenze che richiedono attenzione

Nei progetti a più fasi le differenze possono venire da:

- supporti installati sulla paratia già deformata;
- applicazione dei coefficienti alle azioni o ai loro effetti secondo la combinazione;
- azione sismica limitata alle combinazioni e alle fasi previste;
- verifiche idrauliche senza diagrammi strutturali;
- dati del desktop non rappresentabili nel modello a paratia e stratigrafia uniche.

Il rapporto di importazione e il documento di validazione aiutano a distinguere una differenza voluta da un dato da controllare.

## Campo d'impiego

SPW NX riguarda paratie di pali in c.a., micropali e diaframmi, con supporti e carichi, analizzate per fasi. Il FEM fornisce spostamenti, azioni interne, pressioni e forze nei supporti. Le verifiche coprono gli ambiti indicati nel passo Verifiche e armature.

Il LEM fornisce sollecitazioni, infissione e forze nei supporti, senza spostamenti. La tabella dei coefficienti normativi è segnalata come da confermare.

## Limiti principali

- La risposta dipende dalla qualità dei parametri del terreno e dal modulo di reazione scelto.
- Le ipotesi sulle spinte devono essere coerenti con geometria, attrito terra-parete e spostamenti.
- Il regime di filtrazione usa il modello disponibile; il reticolo di flusso del desktop non viene importato.
- L'instabilità dei puntoni non è verificata.
- Stabilità globale, carico limite verticale e verifiche SLE delle sezioni non sono disponibili.
- Una combinazione non completata non entra negli inviluppi.
- Una voce «Non calcolata» non è una verifica soddisfatta.
- Dopo una modifica agli ingressi, i risultati precedenti non sono aggiornati.

## Responsabilità del progettista

Prima di usare i risultati:

1. controlla il rapporto di importazione;
2. conferma la tabella dei coefficienti e leggi ogni eccezione;
3. verifica convergenza e avvisi del calcolo;
4. controlla la condizione governante e le azioni concomitanti;
5. completa con altri strumenti le verifiche non coperte;
6. conserva con la relazione la versione del motore e l'impronta dei dati.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/spw/docs/it/validazione.md).*
