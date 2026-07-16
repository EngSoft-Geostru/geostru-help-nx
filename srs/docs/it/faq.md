---
title: Domande frequenti
---

# Domande frequenti

## Che differenza c'è tra un chiodo e un tirante?

Il **chiodo** (o barra passiva) è un ancoraggio non pretensionato: entra in
tensione solo per effetto della deformazione del terreno, dopo l'iniezione
della malta. Il **tirante** è invece pretensionato con un martinetto subito
dopo l'installazione, per applicare da subito una forza nota. SRS NX calcola
chiodi passivi (soil nailing): la forza di trazione richiesta all'ancoraggio
è quella necessaria a portare il pendio da FS₀ a FS_des, non una precarica
impostata dal progettista.

## Il calcolo dà FS₀ negativo. Cosa significa?

Significa che il pendio è **già instabile allo stato attuale**, prima di
qualunque intervento: la forza di taglio agente supera quella resistente.
Verifica i parametri geotecnici della coltre (in particolare φ_col e c'_col)
e l'inclinazione α: valori realistici per il tuo sito danno quasi sempre un
FS₀ positivo, anche se basso.

## Devo ricalcolare FS₀ ogni volta?

Sì, se cambi un parametro del **pendio** o del **substrato** dopo averlo già
calcolato: FS₀ resta quello del calcolo precedente finché non premi di nuovo
**Calcola FS₀**. Il calcolo completo (**Avvia**/**Calcola**) verifica prima di
tutto che FS₀ sia coerente con i dati correnti.

## R_ck o f_ck: quale inserisco?

Dipende dalla **normativa** scelta. Con **NTC 2018** inserisci la resistenza
cubica a compressione **R_ck**, che SRS converte in resistenza cilindrica
f_ck con il fattore 0,83. Con **Eurocodice** il campo diventa direttamente
**f_ck** (nessuna conversione: EC2 lavora già in resistenza cilindrica). Vedi
[Chiodi e ancoraggi](chiodi.md#malta-di-iniezione).

## Una verifica non è soddisfatta: cosa modifico?

Ogni verifica non soddisfatta mostra un suggerimento specifico nella card dei
risultati. In generale: **R.2/R.3** (barra) si risolvono aumentando il
diametro φ_b o la classe di acciaio; **R.4/R.5** (malta e bulbo) aumentando
la lunghezza L_a, il diametro di perforazione D_f o la resistenza della
malta; **R.6/R.7** (rete) scegliendo una rete con resistenze superiori o
riducendo l'interasse i_x. Vedi il dettaglio in [Verifiche](verifiche.md).

## Il calcolo consuma crediti? E l'assistente AI?

Sì. **Calcola** e l'**esportazione della relazione** consumano crediti NX,
così come ogni messaggio inviato all'**assistente AI**. Non ci sono
operazioni gratuite illimitate: pianifica i calcoli di verifica in base al
tuo saldo crediti.

## L'assistente AI può sostituire il progettista?

No. L'assistente compila la form da una descrizione, recupera il coefficiente
sismico per una località e spiega i risultati, ma non verifica la coerenza
geotecnica del progetto né si assume la responsabilità del calcolo. Rivedi
sempre i valori che imposta prima di calcolare, e i risultati prima di
metterli in relazione. Vedi [Assistente AI](assistente-ai.md).

## Come salvo e riapro un progetto?

Dal menu **File**: **Salva** genera un file **.srs**, **Apri** lo ricarica.
I progetti si possono conservare anche su **GeoDropbox**. Vedi
[Relazione ed esportazioni](relazione.md#salvataggio-del-progetto).

## In quali lingue è disponibile SRS NX?

L'interfaccia dell'app è disponibile in **italiano, inglese, spagnolo,
polacco, francese e rumeno**. Il manuale è pubblicato in italiano (sorgente)
e in inglese.

---

Non hai trovato la risposta? [Scrivici](mailto:info@geostru.ai?subject=Help%20SRS%20NX) — rispondiamo in giornata.

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20SRS%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/it/faq.md).*
