# GeoDropbox

Il fascicolo è una relazione su un luogo preciso, con un nome e delle coordinate. Su GeoDropbox
diventa un **progetto** con lo stesso nome, il **pin sul sito** e i file dentro — e dall'elenco
dei fascicoli vedi subito quali sono collegati a un progetto e lo apri con un clic.

## Inviare un fascicolo

A fascicolo pronto, nell'intestazione accanto a *Scarica Word* trovi **Invia a GeoDropbox**
(nell'elenco *I miei fascicoli* è la nuvola con il «+»).

- Se non hai progetti vicino al sito, il progetto viene **creato** con il nome dell'incarico
  (o «Comune — Relazione geologica» se l'incarico è vuoto), il pin sulle coordinate, comune,
  provincia, regione e indirizzo compilati, il profilo come categoria e i tag `atlante` + profilo.
- Se hai già progetti **entro 500 m** dal sito — lo stesso cantiere, magari aperto da un'altra
  app — ti vengono proposti con la distanza: puoi entrare in uno di quelli o aprirne uno nuovo.
- Fatto l'invio, la riga di esito porta il link **Apri il progetto**; il pulsante diventa
  **Aggiorna su GeoDropbox** e ricarica i file nello stesso progetto, senza crearne un altro.

Nell'elenco dei fascicoli la colonna **GeoDropbox** mostra la nuvola verde **Apri** sui fascicoli
collegati (in tooltip nome del progetto e data d'invio).

## Cosa arriva nel progetto

| Dove | File | A cosa serve |
|---|---|---|
| radice | **PDF** | la relazione da leggere: ha l'anteprima in GeoDropbox ed è quello che l'AI di GeoDropbox analizza |
| radice | **DOCX** | la stessa relazione da modificare in Word |
| cartella **Atlante NX** | **`.atlante`** | il fascicolo completo (evidenze, tavole, testo, indagini), per riaprirlo in Atlante |
| cartella **Atlante NX** | `LEGGIMI - Atlante NX.txt` | spiega il file `.atlante` a chi apre la cartella senza conoscere Atlante |

Il PDF si scarica anche da Atlante (*Scarica PDF*, accanto a *Scarica Word*).

## Riaprire un fascicolo da GeoDropbox

Il file `.atlante` serve a una cosa sola: **riaprire il fascicolo in Atlante** — da un altro
computer, o da un **altro account** dello studio con cui il progetto GeoDropbox è condiviso.
Chi ha solo PDF e Word ha il documento finito; chi ha il `.atlante` ha il fascicolo vivo.

1. In Atlante premi **GeoDropbox** in alto a destra, poi **Apri**.
2. Scegli il progetto e, nella cartella *Atlante NX*, il file `.atlante`.
3. Il fascicolo viene importato come **nuovo fascicolo** nel tuo elenco, con evidenze e tavole:
   puoi rilanciare le fonti, generare il testo, aggiungere le tue indagini, scaricare Word e PDF.

!!! warning "Non rinominare e non modificare il `.atlante`"
    È un formato di Atlante NX, non un documento. Per leggere usa il PDF, per modificare il Word.
    Dopo un *Aggiorna su GeoDropbox* nella cartella c'è un nuovo `.atlante` con la data nel nome:
    vale l'ultimo.

!!! note "Le indagini PDF"
    Le tue indagini caricate (i PDF analizzati dall'assistente) restano in Atlante: il
    `.atlante` porta le proposte accettate come evidenze, non i PDF originali.

## Accesso a GeoDropbox

Lo stesso account GeoStru apre Atlante e GeoDropbox: ogni account ha il piano **Free**
(5 progetti, 1 GB) senza abbonamento. Da geodropbox.ai, «Accedi con Geostru» entra con
l'account con cui usi Atlante.
