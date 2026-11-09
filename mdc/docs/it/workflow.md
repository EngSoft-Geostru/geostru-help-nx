# Flusso di lavoro

Un progetto reale, dall'inizio alla relazione. I passi sono nell'ordine in cui li trovi a sinistra; puoi tornare indietro in qualunque
momento. Ogni campo si salva quando lo lasci e il calcolo riparte da solo: le verifiche a destra sono sempre quelle dei dati a video.

## 1. Dati generali e tipologia

Nel passo [Dati generali e sito](progetto.md) scrivi descrizione, committente, cantiere e progettista, scegli il sito sulla carta e premi
**Salva**. Nel passo [Tipologia](progetto.md#tipologia) crea il muro con la **procedura guidata** (tipologia e altezza), poi scegli la
fondazione (diretta, con dente, su pali) e le parti facoltative. La tipologia decide quali campi vedi: il dente compare solo con la
fondazione «Con dente», i pali solo con una fondazione su pali.

Se parti da un progetto del desktop, aprilo con **File → Apri…** (`.mdcx`): vedi [File, progetti del desktop e GeoDropbox](file.md).

## 2. Descrivi il muro e il terreno

- [Geometria](geometria.md): le misure dell'elevazione e delle suole, le inclinazioni, dente, mensole e magrone. Le quote si correggono
  anche con un clic sul loro valore nella sezione.
- [Terreni e falda](terreno.md): strati dall'alto in basso, quota della falda, profilo del terreno a monte e a valle, riempimenti.
- [Carichi](carichi.md): carichi distribuiti sul terrapieno e forze concentrate.
- [Pali e tiranti](pali-tiranti.md): pali (con la fondazione su pali) e tiranti.
- [Materiali](materiali.md): classi di calcestruzzo e acciaio, coefficienti parziali, copriferri, condizioni ambientali.

## 3. Normativa e sisma

Nel passo [Normativa e sisma](sisma.md) scegli la normativa geotecnica e strutturale e le opzioni di calcolo (regime e metodo di spinta,
spinta passiva, carico limite). I parametri sismici arrivano dalle coordinate del sito con **Calcola dal sito**; **k_h e k_v dai parametri
del sito (SLV)** li porta nel muro, e da lì nelle combinazioni sismiche generate.

## 4. Combinazioni e verifiche

Il passo [Combinazioni](verifiche.md#le-combinazioni) mostra le combinazioni generate dalla normativa, in sola lettura. **Personalizza** le
copia nel progetto e le rende modificabili; **Torna alla normativa** le rigenera. Il passo [Verifiche](verifiche.md) riporta, per ogni
combinazione, i fattori di sicurezza, i coefficienti parziali e il riepilogo **verifica × combinazione**. Un clic su una riga mostra quella
combinazione nella sezione al centro (spinte, pressioni, sollecitazioni).

!!! tip "Suggerimento"
    Se una verifica globale non passa, la leva cambia con la verifica: per lo **scorrimento** allunga la base o passa alla fondazione con
    dente; per il **ribaltamento** allunga la suola di monte, che porta più terreno stabilizzante; per il **carico limite** allarga la base o
    riduci l'eccentricità.

## 5. Armature

Il passo [Armature](armature.md) mostra i ferri progettati sull'inviluppo delle combinazioni strutturali e la distinta; sotto ci sono i dati
di progetto delle armature (diametri, numero minimo e massimo di barre, ripartitori).

## 6. Relazione e disegni

Nel passo [Relazione](relazione.md) l'anteprima è gratuita. **Genera Word** e **Scarica la sezione (DXF)** consumano crediti; un'operazione
fallita non si paga e rigenerare lo stesso documento con gli stessi dati non si ripaga.

## 7. Salva

Il progetto vive sul server finché lavori: salvalo con **File → Salva** (`.mdcnx`) o in **GeoDropbox**. Un progetto non salvato si perde
alla scadenza della sessione.

## Che cosa è gratuito

| Azione | Costo |
|---|---|
| Modellazione, calcolo con tutte le verifiche, disegni e diagrammi a video, anteprima della relazione | gratuiti |
| Relazione Word | crediti NX |
| Sezione in DXF | crediti NX |
| Messaggio all'assistente | crediti NX |

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MDC%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mdc/docs/it/workflow.md).*
