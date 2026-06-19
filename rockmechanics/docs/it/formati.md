# Formati file

Rock Mechanics NX lavora su un unico **file di progetto** e dialoga con gli strumenti di rilievo a monte e con la documentazione di calcolo a valle. Questa pagina riassume cosa puoi importare e cosa puoi esportare.

## Il file di progetto

Il file di progetto salva l'intero stato del lavoro: il **rilievo geostrutturale** (famiglie di discontinuità con i parametri ISRM, $S_u$ e RQD), le **classificazioni** adottate con i relativi parametri caratteristici e le **verifiche di stabilità** impostate.

È un file di progetto GeoStru NX in formato testuale (struttura JSON), pensato per essere riaperto in qualsiasi momento per riprendere o aggiornare le elaborazioni: puoi salvare un rilievo, tornarci in un secondo momento per aggiungere una classificazione o rivedere una verifica, e rigenerare la relazione senza reinserire i dati.

!!! tip "Un solo file per l'intero studio"
    Conserva il file di progetto insieme agli elaborati di campagna: contiene già rilievo, classificazioni e verifiche, quindi è sufficiente per ricostruire l'intero percorso di calcolo.

## Import del rilievo

Il rilievo geostrutturale non deve essere reinserito a mano. Rock Mechanics NX si interfaccia con due strumenti GeoStru dedicati all'acquisizione e all'elaborazione del rilievo:

- **eGeo Compass** — acquisizione delle giaciture direttamente in campo (immersione e inclinazione delle discontinuità), con lo smartphone usato come bussola-clinometro digitale.
- **GMS (GeoMechanical Survey)** — elaborazione del rilievo geomeccanico: famiglie di giunti, parametri ISRM e organizzazione dei dati di stazione.

Le famiglie di discontinuità e le giaciture rilevate con questi strumenti si importano nell'app senza reinserimento manuale, pronte per la classificazione e le verifiche. Per il quadro completo del flusso di lavoro vedi [Workflow completo](workflow.md).

## Export

A valle del calcolo, Rock Mechanics NX produce la documentazione dello studio:

- la **relazione di calcolo** geomeccanica in formato **Word**, con i dati del rilievo, le classificazioni adottate, i parametri caratteristici e le verifiche di stabilità;
- gli **elaborati grafici** del rilievo e delle verifiche (proiezioni e diagrammi del rilievo, schemi delle verifiche).

I dettagli sul contenuto e sulla generazione sono in [Esportazione e report](export.md).

## Cosa puoi importare / esportare

| Direzione   | Contenuto                                  | Sorgente / destinazione           |
|-------------|--------------------------------------------|-----------------------------------|
| Importa     | Giaciture e famiglie di discontinuità      | **eGeo Compass**                  |
| Importa     | Rilievo geomeccanico (parametri ISRM)      | **GMS (GeoMechanical Survey)**    |
| Apri        | Rilievo, classificazioni e verifiche       | File di progetto GeoStru NX       |
| Salva       | Stato completo del progetto                | File di progetto GeoStru NX       |
| Esporta     | Relazione di calcolo geomeccanica          | Documento **Word**                |
| Esporta     | Elaborati grafici (rilievo e verifiche)    | Immagini / diagrammi              |

## Risorse correlate

Figure di esempio, file di campagna e materiale di riferimento sono raccolti nella pagina [Risorse e file di esempio](risorse.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
