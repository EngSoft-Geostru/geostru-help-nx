# HID NX — Invarianza idraulica

HID dimensiona i sistemi di laminazione per l'**invarianza idraulica e
idrologica**: verifica che un intervento di trasformazione del suolo non aumenti
la portata scaricata nel ricettore rispetto alla condizione precedente.

L'applicazione confronta in parallelo i metodi di calcolo che selezioni e adotta
come volume di invaso il **massimo dei risultati**, così la verifica resta valida
qualunque sia il metodo richiesto da chi istruisce la pratica.

[**Apri l'app**](https://nx.geostru.ai/hid/){ .md-button .md-button--primary }

![Interfaccia di HID NX, sezione Dati generali](img/01-dati-generali.png)

## A chi serve

A chi progetta opere di laminazione delle acque meteoriche: ingegneri idraulici,
geologi e progettisti che devono allegare una relazione di invarianza idraulica a
un permesso di costruire, a un piano attuativo o a un'autorizzazione allo scarico.

## Cosa calcola

| Ambito | Contenuto |
|---|---|
| Piogge | Curva di probabilità pluviometrica GEV o a due parametri |
| Ietogrammi | Chicago, uniforme, Sifalda, triangolare |
| Depurazione | Coefficiente di deflusso, Horton, SCS-CN |
| Idrogrammi | Corrivazione e Nash |
| Dimensionamento | Requisiti minimi, sole piogge, metodo diretto, corrivazione, procedura dettagliata |
| Scarico | Otto organi, dalle luci a battente ai pozzi disperdenti |
| Verifiche | Altezza utile, volume utile, tempo di svuotamento |

## Normativa

HID applica **profili normativi** scelti in base a paese e regione. Il profilo
determina quali metodi sono ammessi, quali dati servono, e se la portata limite e
il volume minimo sono imposti dalla normativa o li scegli tu.

- **Lombardia** — R.R. 7/2017, integrazione 2019, R.R. 3/2025: curva GEV
  obbligatoria, SCS-CN escluso, criticità e portata limite ricavate dal comune.
- **Emilia-Romagna e Marche** — metodo diretto regionale con n = 0,48.
- **Ogni altro paese o regione** — profilo generico: metodi liberamente
  combinabili, portata limite e volume minimo scelti da te.

!!! note "Fuori dall'Italia"
    Dove non esiste un'anagrafica dei comuni, regione e coordinate si inseriscono
    a mano. Non è un errore: è il modo previsto di lavorare nei paesi non ancora
    coperti da un profilo dedicato.

## Da dove iniziare

- [Guida rapida](quickstart.md) — il primo dimensionamento in cinque minuti
- [Workflow completo](workflow.md) — un progetto reale dall'inizio alla relazione
- [Glossario](glossario.md) — i termini del dominio, con i simboli usati nell'app

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
