# Micropali

Nei **Dati generali** scegli la **Tipologia** **Micropalo**: la card **Palo** prende il
titolo **Micropalo** e mostra i campi del bulbo, del sistema e del metodo. Il calcolo usa la
routine dedicata ai micropali del programma desktop MP, non quella dei pali trivellati.

## Geometria e sistema

| Campo | Significato |
|---|---|
| **Diametro di perforazione D** | diametro del fusto sopra il bulbo |
| **Diametro del bulbo** | bulbo iniettato, maggiore o uguale al diametro di perforazione |
| **Lunghezza del bulbo** | misurata dalla punta; 0 = tutto il tratto interrato |
| **Lunghezza L**, **Sporgenza fuori terra** | come per il palo |
| **Tipo di iniezione** | **IGU** (iniezione globale unica) o **IRS** (iniezione ripetuta e selettiva) |
| **Sistema** | **Tubifix** (iniezioni ripetute ad alta pressione) o **Radice** (getto o iniezione a bassa pressione) |
| **Portata laterale** | **Mayer modificato** o **Bustamante & Doix** |
| **Pressione limite** | di Menard o d'iniezione, in kN/m² |
| **Coefficiente di spinta (Radice)** | K~0~ = 1 − sin φ, K~a~ oppure K~p~ |

In cima alla card scegli l'armatura: **Armatura con barre** oppure **Tubolare (tubo in
acciaio)**.

## Come si calcola la portata

La **resistenza laterale** è calcolata sul **solo bulbo**, integrando la tensione
tangenziale a passi di 10 cm lungo la sua lunghezza.

- **Mayer modificato**: τ = σ~h~·tan φ + α·c. Per il sistema **Tubifix**
  σ~h~ = γ·z·tan²(45° + φ/2), con la pressione limite come tetto se l'hai assegnata. Per il
  sistema **Radice** σ~h~ = K·γ·z, con K scelto fra K~0~, K~a~ e K~p~.
- **Bustamante & Doix**: τ dipende dalla pressione limite p~lim~. Nei terreni attritivi
  τ = p~lim~/10; in quelli coesivi vale una correlazione lineare in p~lim~, diversa per
  iniezione **IRS** e **IGU**. Se la pressione limite è 0 il programma assume 300 kN/m².

La **resistenza di punta** è calcolata sul **diametro del bulbo**, con N~q~ e N~c~ del
metodo scelto e la tensione litostatica alla punta. Il **peso** somma la malta del fusto, la
malta del bulbo e l'armatura per metro. Il carico limite orizzontale di **Broms** lavora sul
bulbo, con γ, φ e c medi pesati sugli spessori degli strati.

L'adesione α e la coesione c (o c~u~ negli strati non drenati) sono quelle della
[stratigrafia](stratigrafia.md).

![Card Micropalo: diametro di perforazione, bulbo, tipo di iniezione, sistema Tubifix e metodo di Mayer modificato](img/16-micropalo.png)

## Il tubolare

Con **Tubolare** la card **Materiali e armatura** mostra il blocco **Tubolare**:

- **Diametro di serie** e **Spessore di serie** propongono la serie dimensionale
  **UNI EN 10220**. La scelta scrive **Diametro esterno del tubo**, **Spessore del tubo** e
  **Peso dell'armatura**, che restano modificabili per un tubo fuori serie.
- Il **Peso dell'armatura**, in kN/m, viene dalla geometria del tubo (0,02466·t·(D − t)
  kg/m) e si somma al peso della malta.
- **Acciaio del tubolare** sceglie il grado dall'archivio degli acciai per tubi: gradi
  S235…S460 delle UNI EN 10210/10219, tubi meccanici EN 10297-1, tubi API 5CT e API 5L.
  La resistenza di calcolo è f~yd~ = f~yk~/1,05. L'archivio si modifica come gli altri
  [materiali](materiali.md).
- **Copriferro** è lo spessore di malta fra tubo e perforazione.

### M~y~ della sezione mista

In Broms serve il momento ultimo della sezione, M~y~. Se lo lasci a 0, per il tubolare il
programma calcola il **momento di plasticizzazione della sezione mista tubo + malta** a
sforzo normale nullo: acciaio del tubolare a f~yd~, malta compressa a f~cd~ della classe di
calcestruzzo scelta. Se il solutore non converge usa il momento plastico del solo tubo,
W~pl~·f~yd~, e lo segnala fra i messaggi.

!!! note "Il momento misto può essere più basso di quello del solo tubo"
    Nell'esempio DPHS1 la sezione mista dà 39,68 kNm contro 42,70 kNm del solo tubo. Con la
    malta compressa l'asse neutro sale e l'acciaio compresso diminuisce più di quanto la
    malta compensi. È il valore del programma desktop, riprodotto e dichiarato.

Se assegni M~y~ a mano, prevale il tuo valore. Nel modello FEM l'inerzia è quella
equivalente tubo + malta, omogeneizzata con E~s~/E~c~, a meno che tu non assegni J.

## Cosa non è disponibile

- La **verifica SLU nodo per nodo della sezione mista** tubo + malta: la scheda **Sezioni e
  armature** mostra l'avviso «Verifica della sezione tubolare non disponibile». Il FEM viene
  eseguito comunque.
- **Reticoli di micropali** e **micropali inclinati**.
- Il **carico critico d'instabilità** del micropalo.
- Il cedimento con il metodo iperbolico di Fleming: il cedimento è quello di
  [Poulos e Davis](cedimenti.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MP%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mp/docs/it/micropali.md).*
