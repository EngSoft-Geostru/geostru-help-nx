# Domande frequenti

## Generali

??? question "Quale meccanismo di rottura analizza RockPlane?"
    Solo **rottura planare**: un cuneo bidimensionale che scivola lungo una singola discontinuità persistente con daylighting (α < β). Per rottura **a cuneo poliedrale** (due discontinuità che si intersecano) o **toppling** (ribaltamento) servono software dedicati. Per **failure circolare** in roccia degradata serve un metodo a conci (es. Bishop, Janbu).

??? question "Posso usarlo per fronti di scavo in roccia?"
    Sì, la formulazione è identica. L'unica differenza nella verifica è il coefficiente γ<sub>R</sub>: per fronti di scavo NTC §6.8 prescrive γ<sub>R</sub> = 1.20 (anziché 1.10 dei pendii naturali). Imposta l'approccio "Caratteristico" con FS<sub>req</sub> = 1.20.

??? question "C'è una versione desktop?"
    Sì, esiste **RockPlane desktop** (legacy GeoStru). Questa è la versione web NX, accessibile da `nx.geostru.ai/rockplane/` con qualsiasi browser moderno, senza installazione.

??? question "I file sono compatibili con la versione desktop?"
    Il formato `.rockplane` NX è **JSON**, diverso dal formato binario della versione desktop. Non c'è oggi compatibilità diretta. Per importare un caso dalla desktop, usa lo stesso input nei due software.

## Geometria

??? question "Cosa significa α < β?"
    È la condizione di *daylighting*: il piano di rottura deve emergere sul fronte del versante, non rimanere nascosto sotto. Se α ≥ β il cuneo non è cinematicamente ammissibile per rottura planare.

??? question "Come scelgo B (profondità blocco)?"
    Se hai un cuneo lateralmente delimitato da due discontinuità subverticali (es. larghezza 5 m), usa B = 5 m. Se il fronte è esteso, usa B = 1 m e ragiona "a corsia" (forze in kN/m). Il calcolo lavora sempre per metro internamente; B serve a scalare i risultati a forze totali.

??? question "Quando attivare la tension crack?"
    Quando si osserva sul rilievo una **fessura subverticale persistente** alle spalle del cuneo (tipico in roccia stratificata o blocchi isolati). T è la distanza dal ciglio (B), θ è l'inclinazione della fessura (90° = verticale, la prassi più conservativa).

## Materiale

??? question "Quali valori di c e φ usare?"
    Sulle discontinuità reali la coesione è quasi sempre **bassa o nulla**. φ va dal "basic friction angle" della roccia matrice (giunto liscio sigillato) fino a 50° con asperità di alto ordine non infrante. Vedi tabella in [Materiale →](materiale.md).

??? question "γ del materiale o γ del blocco?"
    γ del **blocco** (cuneo come unità). Se il blocco è integro, è lo stesso della roccia matrice. Se è alterato/fratturato, è leggermente inferiore. Per calcari/graniti integri tipicamente 25-28 kN/m³.

## Acqua

??? question "Differenza tra Hw e Zw?"
    - **Hw** = acqua **esterna** al versante (lago, ristagno al piede). Genera spinta sul fronte.
    - **Zw** = acqua **interna** alla frattura. Genera sottospinta U sul piano di rottura (effetto principale destabilizzante).
    
    Sono concettualmente diverse. Quando il versante è "pervio" (toggle), le due sono idraulicamente connesse e RockPlane usa Hw come livello di Zw.

??? question "Quale distribuzione di pressione scegliere?"
    Caso più conservativo: **"max al piede"** (eq. 20 manuale teorico). Indicato quando il drenaggio è in sommità ma l'acqua si accumula al piede.
    
    "Max a metà altezza" suggerisce un drenaggio bilanciato (raro nella pratica). "Max alla base della tension crack" è specifico per casi con TC riempita d'acqua e drenaggio non efficiente.

??? question "Cosa succede se non imposto la distribuzione (Assente)?"
    Anche con Zw > 0, U resta nullo. È utile per simulare casi "secchi" mantenendo Zw inserito per scopi documentali.

## Sisma

??? question "Come calcolo k_h da NTC?"
    k_h = β<sub>s</sub> · a<sub>max</sub> / g dove β<sub>s</sub> è tabellato in NTC Tab. 7.11.I (~0.18-0.32) e a<sub>max</sub> = a<sub>g</sub> · S<sub>T</sub> · S<sub>S</sub> per il sito. Per ora va calcolato esternamente; un wizard è in roadmap.

??? question "Devo considerare anche k_v?"
    NTC ammette k_v = ±0.5·k_h. RockPlane permette di impostarlo (campo Ω = ±90°), ma nella prassi italiana spesso si trascura perché l'effetto è marginale rispetto al k_h.

## Interventi

??? question "Chiodo passivo o tirante attivo: come scegliere?"
    - **Tirante attivo**: applicato con precarico, attivo da subito, controlla deformazioni. Più costoso, richiede testata e tesatura. Indicato quando serve garantire una FS elevata senza tolleranza di spostamento.
    - **Chiodo passivo**: cementato senza precarico, lavora solo quando il cuneo prova a muoversi. Più economico. Indicato per consolidamenti diffusi con spostamenti accettabili.

??? question "Perché il chiodo passivo mostra il taglio (V_max)?"
    Per NTC §6.7 e prassi (Clouterre 1993, FHWA), il chiodo passivo che attraversa il piano di rottura subisce simultaneamente trazione T e taglio V. RockPlane applica l'interazione N-V con criterio lineare T/T<sub>max</sub> + V/V<sub>max</sub> ≤ 1. Per i tiranti attivi (precaricati) il taglio non è rilevante: la barra lavora puramente in trazione.

??? question "Perché aumentando il numero di prove pull-out aumenta R_d?"
    Tab. 6.6.III di NTC §6.6: con più prove di pull-out preventive il coefficiente ξ scende (1.40 → 1.10 da 0 a ≥4 prove). R<sub>k</sub> = R<sub>min</sub>/ξ → con ξ minore, R<sub>k</sub> maggiore → R<sub>d</sub> maggiore. È un beneficio normativo per aver verificato sperimentalmente la capacità.

??? question "Il numero verticali geognostiche conta per i tiranti?"
    **No**, per i tiranti contano le **prove di pull-out preventive** (Tab. 6.6.III), non le verticali geognostiche (che entrano in Tab. 6.4.IV per i pali). Il campo nell'UI si chiama esplicitamente "N. prove pull-out".

## Reti

??? question "Differenza R1 corticale vs R2 caging?"
    - **R1**: pressione normale q sul fronte. Aumenta N → aumenta attrito (effetto indiretto). Per distacchi superficiali sottili.
    - **R2**: capacità di taglio τ sul piano. Somma direttamente a τ resistente. Per blocchi spessi che vogliono scivolare.

??? question "RockPlane verifica il punzonamento della rete?"
    No. La verifica strutturale del singolo nodo (R_punz) e della trazione globale del pannello (R_tr) è **delegata al fornitore** della rete (datasheet certificato). RockPlane usa la capacità dichiarata come azione nel calcolo planare. Vedi [reti →](reti.md).

## Verifica normativa

??? question "Quale approccio usare in Italia?"
    **NTC 2018 (A2+M2+R2)**. È prescritta da NTC §6.8.2 per stabilità di pendii naturali.

??? question "Quando usare EC7 DA1.C1 (γ_G=1.35)?"
    Per **dimensionamento strutturale** delle armature (chiodi/tiranti). DA1.C1 amplifica le azioni → critico per la verifica dell'acciaio. DA1.C2 invece riduce i materiali → critico per la geotecnica. Per copertura totale fai entrambe.

??? question "Perché con c=0 la verifica NTC dà FS = FS_TA / 1.25?"
    Caso puro attrito: FS = tan φ / tan α. NTC riduce tan φ di 1.25 → FS riduce di 1.25 esatto. Risultato analitico noto, utile come **test di consistenza** del software.

## α critico

??? question "Quando usare la ricerca α critico?"
    Quando l'orientazione esatta del giunto persistente non è conosciuta con precisione. La ricerca trova il **caso peggiore** all'interno del dominio cinematico. Utile per dimensionamenti robusti.

??? question "Perché α_crit dipende da c?"
    Con c=0 il minimo è al bordo (α → β). Con c>0 il termine di coesione cresce con α (perché W cala più rapidamente di L), spostando il minimo all'interno. Vedi [α critico →](alfa-critico.md).

## Export / formati

??? question "La relazione Word è personalizzabile?"
    Il template è hardcoded nel software (genera tutto proceduralmente da DocumentFormat.OpenXml). Per personalizzazioni grafiche (logo, header, footer) modifica il `.docx` generato in Word, salvando una nuova versione. In futuro è prevista la possibilità di caricare un template `.dotx`.

??? question "Il DXF è leggibile da AutoCAD 2010?"
    Sì, versione **AC1027** (compatibile dal 2013). Per versioni più vecchie, apri in AutoCAD 2013+ e salva come DXF 2010 o DWG legacy.

??? question "Come condivido il progetto con un collega?"
    Salva il `.rockplane` (JSON UTF-8 ~10-100 KB) e invialo via email. Il collega lo apre con **File → Apri da file…**. Se hai inserito una foto del sito è inclusa nel JSON.

## Problemi e troubleshooting

??? question "FS sempre 1.213, non cambia mai modificando i parametri"
    Sei in caso "puro attrito" (c=0, no acqua, no sisma). FS = tan φ/tan α: dipende solo da φ e α. Cambia uno dei due o aggiungi coesione.

??? question "Il bottone Misura non risponde"
    Verifica che ci sia un cuneo disegnato (FS calcolato almeno una volta). Lo strumento Misura funziona solo dopo il primo render del SVG. Premi il bottone, poi tieni il mouse premuto su un punto e trascina su un altro.

??? question "I chip dei γ restano tutti 1.00 anche cambiando normativa"
    Forza un refresh con **Ctrl+F5**. Se persiste, controlla che il selettore Normativa abbia effettivamente cambiato valore (testo del dropdown visibile).

??? question "Verifica non soddisfatta con FS = 0.998"
    Sei al limite del criterio normativo (FS<sub>req</sub> = 1.00). Aggiungi un piccolo intervento (un chiodo in più, o aumenta il passo della rete) per superare la soglia.

## Crediti e licenza

??? question "Chi sviluppa RockPlane NX?"
    **GeoStru S.r.l.** — software house specializzata in geotecnica, geologia e ingegneria sismica. Sito: [www.geostru.ai](https://www.geostru.ai).

??? question "Come segnalo un bug?"
    Email: [info@geostru.ai](mailto:info@geostru.ai?subject=Bug%20RockPlane%20NX) con descrizione del problema, screenshot e (se possibile) il file `.rockplane` che lo riproduce.

??? question "Posso usarlo per uso commerciale?"
    Sì, RockPlane NX è destinato a uso professionale di geologi e ingegneri progettisti. Il modello a credito permette di pagare solo per i calcoli effettivi.
