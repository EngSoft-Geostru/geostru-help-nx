# Workflow completo

Sequenza di un progetto reale, dal rilievo in sito alla relazione. Le opzioni di dettaglio sono nelle pagine dei singoli capitoli.

## 1. Il rilievo geostrutturale (ISRM)

Rock Mechanics NX rappresenta ed elabora il **rilievo geostrutturale di discontinuità** eseguito in sito con il metodo della **bussola e del clinometro**, secondo le raccomandazioni ISRM *"Suggested Methods for the Quantitative Description of Discontinuities in Rock Masses"* (1978).

Per ogni famiglia di discontinuità si descrivono i parametri ISRM:

| Parametro | Descrizione | Dove pesa |
|---|---|---|
| **Giacitura** | immersione (dip direction) e inclinazione (dip) | orientamento `A6`, SMR, stabilità |
| **Spaziatura** $s$ | distanza media fra discontinuità adiacenti | `A3`, RQD da $J_v$ |
| **Persistenza** | continuità del giunto sul fronte | `A4` (v1) |
| **Apertura** | distanza fra le pareti | `A4` (v2), $J_a$ |
| **Rugosità** | a piccola e media scala | `A4` (v3), $J_r$, JRC |
| **Alterazione** delle pareti | grado di degradazione | `A4` (v4), $J_a$ |
| **Riempimento** | natura e spessore del materiale | `A4` (v5), $J_a$ |
| **Condizioni idrauliche** | da asciutto a forti venute | `A5`, $J_w$ |

!!! tip "Acquisizione digitale del rilievo"
    Il rilievo può essere acquisito in campo con **eGeo Compass** o elaborato con **GMS (GeoMechanical Survey)**, che si interfaccia con l'app. Le famiglie di giunti e le giaciture si importano così senza reinserimento manuale.

## 2. Resistenza della roccia intatta e RQD

- **$S_u$** (resistenza a compressione uniassiale): da Point Load Test, sclerometro o stima ISRM.
- **RQD**: da carote di sondaggio o stimato dal volumetric joint count $J_v$ / dal numero di giunti per metro.

Definizioni ed equazioni complete in [Panoramica e parametri comuni](classificazioni.md).

## 3. Classificazione geomeccanica

Si sceglie il metodo (o più di uno) in funzione dell'opera e della litologia. Tutti i metodi attingono allo stesso rilievo:

- **Sotterraneo / generale** → [Barton (Q)](barton.md), [Singh & Goel (N)](singh-goel.md)
- **Gallerie e fondazioni** → [Bieniawski (RMR)](rmr-romana.md)
- **Versanti** → [Romana (SMR)](rmr-romana.md), [Robertson (SRMR)](robertson.md)
- **Ammassi carbonatici** → [Jašarević (n)](jasarevic.md)
- **RMR continuo semplificato** → [Sen](sen.md)

L'output di ogni classificazione è: indice numerico → **classe** (I–V o I–IX) → **qualità** dell'ammasso → **parametri caratteristici** ($c$, $\varphi$, $E$, GSI).

!!! note "Più classificazioni a confronto"
    È buona pratica calcolare l'ammasso con più metodi e confrontarne i parametri caratteristici: le correlazioni empiriche sono tarate su contesti diversi, e la dispersione dei risultati è essa stessa un'informazione sull'affidabilità.

## 4. Verifica di stabilità

Quando il rilievo individua un cinematismo cinematicamente possibile:

- **[Scivolamento planare](scivolamento-planare.md)** — una discontinuità con immersione prossima (± 20°) a quella del fronte e inclinazione minore. Si considerano frattura di trazione, acqua nei giunti, sisma e forze esterne.
- **[Sliding 3D](sliding-3d.md)** — due famiglie che si intersecano formando un cuneo tetraedrico; scorrimento lungo la linea di intersezione o su un singolo piano.

Per lo scivolamento lungo **due giunti** in chiave di progetto dell'intervento (chiodi, tiranti, reti) si rimanda alla scheda tecnica di [RockPlane NX](https://help.nx.geostru.ai/rockplane/it/).

## 5. Utility

- **[Forza d'impatto di un masso](utility.md#forza-dimpatto-di-un-masso)** su struttura muraria o in calcestruzzo (Paronuzzi, 1989).
- **[Previsione del crollo per evento sismico](utility.md#previsione-del-crollo-per-evento-sismico)** (Harp & Noble, 1993), con classificazione di suscettibilità derivata da Q.

## 6. Esportazione

Si genera la **relazione di calcolo** con i dati del rilievo, le classificazioni e le verifiche, più gli elaborati grafici. Vedi [Esportazione e report](export.md) e [Formati file](formati.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
