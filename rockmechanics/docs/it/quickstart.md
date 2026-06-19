# Guida rapida (5 minuti)

L'obiettivo: dal rilievo di poche discontinuità alla **prima classificazione geomeccanica** con i parametri caratteristici dell'ammasso. Niente teoria — quella è nelle pagine dei singoli metodi.

## 1. Apri l'app

Vai su [nx.geostru.ai/rockmechanics](https://nx.geostru.ai/rockmechanics/) e crea un **Nuovo file** dal menu File. Compila i **Dati generali** (descrizione del sito, località, data, operatore).

## 2. Inserisci il rilievo dei giunti

Per ogni **famiglia di discontinuità** rilevata in sito indica almeno:

- **giacitura**: immersione (dip direction) e inclinazione (dip);
- **spaziatura** media $s$;
- **persistenza, apertura, rugosità, alterazione, riempimento**;
- **condizioni idrauliche** (asciutto → forti venute).

Indica anche l'**orientamento del fronte** (immersione e inclinazione) del versante o dello scavo: serve al fattore di correzione per l'orientamento e allo Slope Mass Rating.

!!! tip "Da dove arrivano i dati"
    Il rilievo si esegue con bussola e clinometro secondo le raccomandazioni ISRM. Se usi **eGeo Compass** o **GMS (GeoMechanical Survey)**, le famiglie di giunti e le giaciture si importano già pronte (vedi [Formati file](formati.md)).

## 3. Definisci resistenza e fratturazione

- **$S_u$** — resistenza a compressione uniassiale della roccia intatta: inseriscila da prova Point Load, da sclerometro o con la stima ISRM (vedi [parametri comuni](classificazioni.md#resistenza-a-compressione-uniassiale-su)).
- **RQD** — da carote di sondaggio, oppure stimato dal numero di giunti per metro cubo $J_v$.

## 4. Scegli la classificazione

Apri la scheda **Classificazioni** e seleziona il metodo adatto al tuo caso:

| Se ti serve… | Usa |
|---|---|
| Caratterizzazione generale o opera in sotterraneo | [Barton (Q)](barton.md) |
| Stabilità di un **versante** | [Romana (SMR)](rmr-romana.md) o [Robertson (SRMR)](robertson.md) |
| Gallerie | [Singh & Goel (N)](singh-goel.md) |
| Ammasso carbonatico | [Jašarević (n)](jasarevic.md) |

L'app calcola subito l'**indice** (Q, RMR, SMR, N…), la **classe** e la **qualità** dell'ammasso.

## 5. Leggi i parametri caratteristici

Nella stessa scheda trovi i parametri derivati, pronti per il calcolo:

- coesione $c$,
- angolo d'attrito $\varphi$,
- modulo di deformazione $E$,
- (per RMR) il **GSI**.

## 6. (Opzionale) Verifica la stabilità

Se hai un cinematismo riconosciuto, passa a [Scivolamento planare](scivolamento-planare.md) o [Sliding 3D](sliding-3d.md): inserisci geometria del fronte, acqua, sisma ed eventuali forze esterne e leggi il coefficiente di sicurezza.

## 7. Esporta

Genera la **relazione di calcolo** con tabelle e grafici dalla scheda Report (vedi [Esportazione](export.md)).

---

➡️ Prosegui con il [workflow completo](workflow.md) per il dettaglio di ogni fase.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
