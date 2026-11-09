# Domande frequenti

**Posso aprire i miei progetti di MDC desktop?**
Sì, i file `.mdcx` si aprono con **File → Apri…** o da GeoDropbox. Gli ingressi si importano e i risultati si ricalcolano. Vedi
[File, progetti del desktop e GeoDropbox](file.md).

**Perché i fattori di sicurezza sono diversi da quelli del desktop?**
Dove il desktop sbagliava MDC NX corregge: con la falda (sottospinta), con la spinta passiva, con il sisma. L'elenco è in
[Validazione e limiti](validazione.md).

**Quali norme posso usare?**
La prima consegna calcola con NTC 2018, NTC 2008 ed Eurocodici. Le altre norme del desktop si leggono dai file e restano nel progetto, con un
avviso; il loro calcolo è in arrivo.

**Posso modificare le combinazioni?**
Le combinazioni generate dalla norma sono in sola lettura; **Personalizza**, nel passo Combinazioni, le copia nel progetto e le rende
modificabili. **Torna alla normativa** le rigenera.

**Le combinazioni sismiche hanno k~h~ = 0: perché?**
I coefficienti del muro non sono ancora stati scritti. Nel passo Normativa e sisma premi **Calcola dal sito** e poi **k_h e k_v dai
parametri del sito (SLV)**, oppure scrivili a mano. Se i parametri del sito ci sono già, il calcolo usa comunque k~h~ e k~v~ del sito
per le combinazioni sismiche rimaste a zero, e lo dice negli avvisi. Vedi [Normativa e sisma](sisma.md).

**Il muro non verifica a scorrimento: che cosa faccio?**
Allunga la base, scegli la fondazione con dente o inclina il piano di posa. Considera la spinta passiva a valle solo se il terreno davanti
al muro resterà al suo posto per tutta la vita dell'opera. Vedi [Combinazioni e verifiche](verifiche.md).

**Come si mettono i carichi della mensola di valle?**
Come forze concentrate nel passo [Carichi](carichi.md), con il punto di applicazione sulla mensola.

**Posso modificare a mano i ferri?**
Non ancora: le armature si progettano sempre sull'inviluppo, entro i limiti del riquadro «Armature di progetto». La modifica manuale è in
arrivo.

**Gabbioni, contrafforti, stabilità globale?**
Non ancora: arrivano con la seconda consegna. Nel frattempo la stabilità globale va verificata a parte con un programma di stabilità dei
pendii, come dice anche la relazione.

**Da dove vengono i parametri sismici?**
Dalle coordinate del sito, con il servizio GeoStru Parametri Sismici. Vedi [Normativa e sisma](sisma.md).

**Che cosa costa?**
Modellazione, calcolo e verifiche sono gratuiti; relazione Word, DXF della sezione e messaggi all'assistente consumano crediti. Un'operazione
fallita non si paga, e rigenerare lo stesso documento con gli stessi dati non si ripaga.

**Il progetto si salva da solo?**
No: il progetto vive sul server mentre lavori e scade dopo un periodo di inattività. Salvalo in `.mdcnx` o in GeoDropbox.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MDC%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mdc/docs/it/faq.md).*
