# Guida rapida (5 minuti)

Usa l'esempio **Parete chiodata d'esempio** del menu File: una parete alta 8 m con paramento inclinato di 25°, terreno a monte inclinato di 10°, tre strati, falda a 2 m dalla testa, un sovraccarico uniforme di 20 kPa e sei chiodi lunghi 5 m.

## 1. Apri l'esempio

Apri [SNL NX](https://nx.geostru.ai/snl/). Nel menu **File** scegli **Esempi → Parete chiodata d'esempio**.

Se il progetto a video ha modifiche che non sono in un file, il programma te lo dice prima di sostituirlo. L'esempio prende il posto del progetto corrente.

## 2. Controlla il modello

Scorri i passi nell'ordine, a sinistra:

1. **Progetto**: normativa e tipo di opera, kh e kv. Nell'esempio il sisma non c'è (kh = kv = 0).
2. **Geometria**: H = 8 m, θ = 25°, ε = 10°.
3. **Terreno**: tre strati dall'alto e la falda a 2 m dalla testa della parete. Accanto al **K di interazione chiodo-terreno** di ogni strato trovi il valore proposto da φ'.
4. **Carichi**: il sovraccarico uniforme e il suo **coefficiente A**.
5. **Chiodi**: l'interasse orizzontale Sh e i sei chiodi, ognuno con profondità, lunghezza, inclinazione, diametri, fy e kn.

Il disegno al centro si aggiorna a ogni modifica: controlla quote, strati, falda, carichi e chiodi. Un passo con dati mancanti o non validi è segnato nell'elenco a sinistra e i messaggi dicono quale campo correggere.

## 3. Calcola

Apri **Calcolo**. Controlla:

- **Teoria della spinta**: Rankine o Coulomb (con kh > 0 si usa sempre Coulomb / Mononobe-Okabe);
- **Superficie di rottura β**: 45° + φ'/2 oppure un valore manuale;
- **Base Bl per lo scorrimento**: Bl = H, manuale o automatica;
- **Combinazione e coefficienti**: ξ, A, M e R caricati dalla normativa scelta nel passo Progetto.

Premi **Calcola**. Il calcolo è gratuito e richiede un istante. Se si ferma, il messaggio sopra il pulsante dice perché e in quale passo intervenire.

## 4. Leggi le verifiche

Il pannello **Verifiche** a destra riassume le quattro famiglie:

- **Stabilità interna (cuneo)**: il fattore di sicurezza minimo fra le fasi e la fase in cui si trova;
- **Rottura dei chiodi** e **Sfilamento dei chiodi**: il minimo fra tutti i chiodi e tutte le fasi, con il chiodo che governa;
- **Scorrimento**: il fattore di sicurezza del blocco chiodato.

Nell'esempio guarda in particolare lo scorrimento: con la falda a 2 m dalla testa, la spinta dell'acqua pesa molto sul blocco. Prova ad abbassare la falda o ad allungare i chiodi e ricalcola: il risultato precedente diventa «non aggiornato» appena cambi un dato.

Nel passo **Risultati** trovi i dettagli per fase e per chiodo, lo scorrimento e i diagrammi del rivestimento. Vedi [Flusso di lavoro](workflow.md#7-risultati).

## 5. Relazione ed export

Con un calcolo aggiornato, apri **Relazione ed export** per scaricare la relazione Word o la tavola DXF della sezione (10 crediti ciascuna). Vedi [Crediti](crediti.md).

## 6. Salva il progetto

Usa **File → Salva con nome…** per scaricare un `.snlnx`. Il file conserva gli ingressi; i risultati si ricalcolano dopo l'apertura. Puoi salvare il progetto anche su **GeoDropbox**. Non lasciare l'unico lavoro nella sessione: scade dopo 30 minuti di inattività.

!!! tip "Chiedi all'assistente"
    Il pulsante **Assistente** apre la chat: puoi chiedergli di calcolare e di spiegarti quale fase o quale chiodo governa. Vedi [Assistente AI](assistente.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/snl/docs/it/quickstart.md).*
