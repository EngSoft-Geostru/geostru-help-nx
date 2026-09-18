# Materiali

La card **Materiali e armatura** raccoglie tre cose: i materiali del palo, l'armatura della
sezione e i parametri per l'analisi laterale (M~y~ e J assegnato).

## Scegliere i materiali

- **Classe di calcestruzzo**: sotto la tendina compaiono i valori della classe scelta. Dal
  calcestruzzo vengono il peso del palo W, il modulo elastico E~c~ usato dal FEM e da
  Poulos e Davis, e f~cd~ per la verifica della sezione.
- **Acciaio**: l'acciaio delle barre, per il palo e per il micropalo armato con barre.
- **Acciaio del tubolare**: compare al posto dell'acciaio delle barre quando il micropalo è
  tubolare. Vedi [Micropali](micropali.md).

## L'archivio del progetto

Apri **Archivio materiali (NTC / EC)** per vedere e modificare le tabelle. L'archivio è
**del progetto**: parte da quello del programma desktop MP, viaggia nel file `.mpnx` e non
tocca gli altri progetti. Un file salvato senza archivio prende quello di partenza.

Nelle tabelle puoi:

- modificare qualunque valore, riga per riga;
- aggiungere righe con **Aggiungi calcestruzzo**, **Aggiungi acciaio** e, per i tubolari,
  **Aggiungi acciaio per tubi**;
- eliminare una riga con il cestino a fine riga.

Passa il mouse sulle intestazioni per leggere la descrizione di ogni colonna.

| Tabella | Colonne |
|---|---|
| Calcestruzzi | R~ck~, E~c~, f~ck~, f~cd~, f~ctd~, f~ctm~, ν, α~T~, γ |
| Acciai | E~s~, f~yk~, f~yd~, f~tk~, f~td~, ε~uk~, ε~ud~, β~1~β~2~ iniziale e finale |
| Acciai per tubi | norma di prodotto, E~s~, f~yk~, f~tk~ |

Quando cambi **R~ck~** il programma ricalcola f~ck~, f~cd~, f~ctm~, f~ctd~ ed E~c~ secondo
NTC 2018 § 11.2.10; i valori ricalcolati restano modificabili. Da **f~yk~** ricalcola
f~yd~ e f~td~. Per gli acciai dei tubi f~yd~ = f~yk~/1,05 non è una colonna: si ricava
sempre.

![Card Materiali e armatura: classe di calcestruzzo e acciaio, archivio dei materiali da aprire, armatura della sezione circolare, M_y e J assegnato](img/03-materiali.png)

!!! warning "Il peso di volume del calcestruzzo cambia il carico limite"
    Nell'archivio di partenza il peso di volume γ vale 25, 26, 27 e 28 kN/m³ per le quattro
    classi di calcestruzzo. Entra nel peso W del palo, che si sottrae al carico limite. Se
    confronti i risultati con un altro calcolo, controlla prima γ ed E~c~: sono la causa
    più frequente di scarti dell'1–2 %.

## Armatura della sezione circolare

Per il palo e per il micropalo armato con barre scrivi:

- **Barre longitudinali (min.)**: il numero di partenza. Il semiprogetto può aumentarle nodo
  per nodo;
- **Diametro barre** e **Diametro staffe**, in mm;
- **Copriferro**, in m. Il suggerimento a video ricorda i 5 cm consigliati per i pali di
  fondazione; il programma accetta anche valori minori.

Questi dati servono alla verifica SLU e al disegno della gabbia: vedi
[Sezioni e armature](armature.md).

## Parametri per l'analisi laterale del palo

- **M~y~**: momento ultimo della sezione per la verifica orizzontale di Broms. Con 0 e
  l'analisi FEM attiva il programma lo calcola dalla sezione armata; con 0 e il FEM spento
  non c'è verifica orizzontale. I dettagli sono in [Carico limite](carico-limite.md).
- **J assegnato**: momento d'inerzia usato dal FEM, in m⁴. Con 0 è calcolato dalla sezione
  circolare. Serve per sezioni non circolari o per riprodurre un caso di letteratura.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MP%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mp/docs/it/materiali.md).*
