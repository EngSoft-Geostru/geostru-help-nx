# Carichi

Il peso proprio del muro e del terreno il programma lo calcola da solo. Nel passo 5 aggiungi i **carichi distribuiti sul terrapieno** e le
**forze concentrate**. In un progetto nuovo i due elenchi sono vuoti: **+ Carico** e **+ Forza** aggiungono una riga, il cestino la toglie.

## Carichi distribuiti sul terrapieno

| Campo | Unità | Note |
|---|---|---|
| Descrizione | | testo libero |
| Tipo | | Uniforme, Striscia, Trapezoidale |
| Categoria | | Non assegnata, Generici, Permanenti strutturali, Permanenti non strutturali, Folla, Traffico, Ferroviari, Edifici |
| Ascissa iniziale, Ascissa finale | m | misurate dalla testa del muro verso monte |
| Intensità iniziale, Intensità finale | kPa | uguali per il carico uniforme |
| Profondità | m | |

Il carico entra nella spinta come **sovraccarico uniforme equivalente**, come nel desktop: la parte di carico che cade entro una distanza
dalla testa del muro pari all'altezza del muro più la suola di monte è spalmata su tutta quella lunghezza. Con carichi lontani o concentrati in una striscia stretta
la spinta è quindi approssimata (vedi [Validazione e limiti](validazione.md)).

La **categoria** decide come pesa il carico sulla fondazione: un carico **permanente** (strutturale o non strutturale) che sta sopra la
suola di monte conta come peso stabilizzante con un coefficiente non maggiore di 1; un carico **variabile** (tutte le altre categorie) non
conta come peso stabilizzante, ma solo come spinta.

!!! note "Nota"
    Il programma desktop pesava il sovraccarico sulla suola con il coefficiente sfavorevole della combinazione, cioè lo faceva più
    stabilizzante proprio quando doveva essere più gravoso. MDC NX lo corregge.

Il coefficiente con cui ogni carico entra in una combinazione sta nella combinazione (1,5 nelle combinazioni A1 generate dalla normativa, 1
nelle sismiche): vedi [Combinazioni e verifiche](verifiche.md).

## Forze concentrate

Forze e momenti **per metro di muro**, applicati in un punto del sistema del muro (x dal bordo di valle della fondazione, y dal piano di
posa).

| Campo | Unità | Verso positivo |
|---|---|---|
| Ascissa x, Quota y | m | |
| Forza orizzontale F~x~ | kN/m | verso valle (a sinistra nel disegno) |
| Forza verticale F~y~ | kN/m | verso il basso |
| Momento M~z~ | kN·m/m | ribaltante, cioè nel verso che fa ruotare il muro verso valle (antiorario nel disegno) |

È la stessa convenzione delle risultanti nella relazione (F~x~ > 0 verso valle, F~y~ > 0 verso il basso, M > 0 ribaltante). Servono per
azioni che arrivano da altre strutture: un parapetto, una barriera, la reazione di una soletta. I carichi applicati alla **mensola di valle**
si scrivono qui, con il punto sulla mensola: il programma li usa per progettarne l'armatura.

## Tiranti

I tiranti non sono carichi da scrivere qui: si descrivono nel passo [Pali e tiranti](pali-tiranti.md) e il programma ne ricava la forza.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MDC%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mdc/docs/it/carichi.md).*
