# Import — formati accettati e workflow

GeoSection NX accetta diversi formati per i due input principali — il **profilo
topografico** e i **sondaggi**. Quasi tutti possono essere importati anche tramite
il chat AI quando il file non rispetta il formato standard.

## Profilo topografico

### CSV

Una coppia `X,Z` per riga (X distanza in m, Z quota in m s.l.m.):

```
0,120
10,118.5
30,115
60,109.2
100,103
```

Separatori ammessi: virgola, punto-e-virgola, tab, spazio. Decimale `.` o `,`.
Apri *Importa profilo → Tab CSV*, incolla, conferma.

### Immagine raster (BMP / PNG / JPG)

Carica una scansione di sezione cartacea (es. PRG, PAI, vecchi piani regolatori).
Sezione **Tab Img** del modal Importa profilo:

1. Carica l'immagine.
2. Imposta i 4 punti di calibrazione (origine + 3 punti noti X/Z) cliccando sulla
   griglia che compare.
3. L'immagine viene **georeferenziata** e diventa il fondo della sezione; la
   polilinea del profilo va poi tracciata a mano sulla griglia o estratta tramite
   AI vision.

### DXF (LWPOLYLINE)

Apri *Importa profilo → Tab DXF*, carica il `.dxf`. GeoSection cerca polilinee
leggere (LWPOLYLINE) nel layer `PROFILO` o nel primo layer disponibile, le
ordina per X crescente e le importa come linea topografica. Se il file ha più
polilinee, l'app chiede di scegliere.

## Sondaggi

### AGS4

[AGS4](https://www.ags.org.uk/) è lo standard internazionale per scambio dati
geotecnici. *File → Importa sondaggi → AGS4* legge i gruppi `LOCA` (anagrafica),
`GEOL` (stratigrafia), `WSTK` (acqua) e popola sondaggi + livello falda.

### CSV / TSV

Per file da fogli di calcolo. Schema atteso:

```
hole_id,x,y,quota,depth_top,depth_bot,layer,description
SD1,1024.5,3850.2,118,0,1.5,terreno_vegetale,Vegetale
SD1,1024.5,3850.2,118,1.5,4.2,argilla,Argilla limosa
SD1,1024.5,3850.2,118,4.2,8.0,sabbia,Sabbia ghiaiosa
SD2,1090.1,3855.4,115,0,2.0,argilla,Argilla
```

- `hole_id`: identificativo del sondaggio (stringa).
- `x, y`: coordinate piane (qualsiasi sistema di riferimento, basta sia coerente con la traccia).
- `quota`: quota assoluta della testa del sondaggio (m s.l.m.).
- `depth_top, depth_bot`: profondità dello strato dal piano campagna (m).
- `layer`: codice/sigla strato (usato per accorpare colori in legenda).
- `description`: descrizione testuale dello strato.

Separatori per CSV: `,`, `;`, tab. Per TSV: tab. Decimale `.` o `,`.

### AI Import (formati liberi)

Quando il file ha headers in italiano, decimali con virgola, righe vuote,
colonne aggiuntive, o è una scansione PDF di un sondaggio storico — usa
**Importa con AI**:

1. Modal *File → Importa con AI*.
2. Trascina file o incolla testo (anche da Excel).
3. L'AI riconosce automaticamente schema, separatori, lingua, scarta righe note.
4. Anteprima dei valori estratti — modificabile prima di confermare.

Costa qualche credito NX per chiamata; visibile nel chip wallet prima della conferma.

## Esempi pronti

Nel modale **Info → Risorse** trovi sample preconfezionati per ciascun formato:
- 2 esempi profilo (DXF + immagine raster);
- 3 esempi sondaggi (AGS4 + CSV + TSV);
- 6 esempi AI per testare il chat (formati "messy" reali).
