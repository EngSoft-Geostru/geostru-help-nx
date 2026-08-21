# MRE NX — Terre rinforzate

**MRE NX** verifica e progetta opere di sostegno in **terra rinforzata** con geosintetici:
verifiche esterne (ribaltamento, scorrimento, capacità portante), verifiche interne sui
rinforzi (sfilamento e rottura), stabilità globale con Bishop e verifiche interne con
superfici **tieback** e **compound**. Il motore di calcolo deriva da GSRD, il software
GeoStru di riferimento per le terre rinforzate.

![Interfaccia di MRE NX: i parametri a sinistra, l'anteprima della sezione a destra](img/01-parametri.png)

## Cosa fa

- **Combinazioni automatiche NTC 2018**: statica A1+M1+R3 e, con sisma attivo, la
  combinazione sismica con coefficienti unitari e resistenze di tab. 7.11.III.
- **Progetto o Verifica**: lunghezze di ancoraggio dedotte livello per livello, oppure
  imposte e verificate.
- **Sezione 2D e modello 3D** sempre aggiornati mentre inserisci i dati, con risvolto
  in facciata (wrap-around) e texture a griglia dei geosintetici.
- **Archivio rinforzi** con catalogo, archivio personale e import da scheda tecnica PDF (AI).
- **Stabilità globale** A2+M2+R2 e superfici interne tieback/compound con animazione.
- **Relazione di calcolo** narrativa con figure e grafici, esportabile in DOCX/PDF.

## Da dove iniziare

1. [Guida rapida](quickstart.md) — dal nuovo progetto al primo calcolo in 5 minuti.
2. [Normativa e combinazioni](combinazioni.md) — come vengono applicati i coefficienti.
3. [Verifiche](verifiche.md) — come leggere i risultati per combinazione.

!!! tip "Assistente AI"
    Il pulsante **Assistente** apre la chat integrata: sa leggere il progetto corrente,
    spiegare i risultati e aprire un ticket di supporto.

![Il pannello dell'assistente AI affiancato al progetto](img/15-assistente.png)

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MRE%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mre/docs/it/index.md).*
