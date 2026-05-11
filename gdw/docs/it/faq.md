# FAQ

## Generale

??? question "Cosa fa GDW NX?"
    GDW NX dimensiona e verifica muri di sostegno in gabbioni secondo NTC 2018.
    Spinta multistrato (Coulomb/Mononobe-Okabe), verifiche esterne, verifiche
    interne fila per fila, stabilità globale Bishop. Output: Word, file
    `.gabbioni`, disegni.

??? question "Per chi è pensato?"
    Ingegneri geotecnici, studi di consulenza, tecnici di cantiere che
    progettano o verificano muri a gravità in gabbioni per regimazione
    idraulica, protezione versanti, sostegno stradale, ecc.

??? question "Funziona offline?"
    No — è un'applicazione web in cloud. Serve connessione internet.
    Il browser cache offre autosave nel `localStorage`, ma il calcolo è
    server-side.

??? question "Posso usarla su tablet?"
    Sì in lettura/visualizzazione. Per l'editing intensivo (compilazione di
    molti campi) consigliato un PC con tastiera.

## Calcolo

??? question "Perché il mio FS scorrimento è basso?"
    Tipicamente per: (1) base muro stretta, (2) sismica attiva, (3) terreno
    di fondazione povero, (4) interfaccia "fondazione c.a." (δ=2/3 φ). Rimedi:
    aumentare base, inclinare la fondazione β (vedi [Fondazione](fondazione.md)),
    battere il muro α, ancorare con palificata.

??? question "Il FS ribaltamento peggiora con α > 0, perché?"
    Probabilmente la versione di GDW che stai usando ha una correzione direzionale
    incompleta. Nella versione attuale, FS_rib migliora con α perché la spinta
    viene proiettata su (δ+α) e Sy stabilizzante cresce sensibilmente.
    Se vedi un calo, verifica di essere sulla build più recente.

??? question "Cos'è Ψ₂ e perché GDW non lo applica automaticamente?"
    Ψ₂ è il coefficiente di combinazione quasi-permanente (NTC tab. 2.5.I)
    che riduce i sovraccarichi variabili Q in combinazione sismica. GDW non
    lo applica automaticamente perché dipende dalla destinazione d'uso
    dell'opera (abitazioni 0.3, uffici 0.3, commerciale 0.6, neve a<1000m 0.0).
    L'utente deve inserire Q già ridotto. Un alert in UI lo ricorda quando
    attivi la sismica.

??? question "Cosa cambia tra rete elettrosaldata e doppia torsione nel calcolo?"
    Sostanzialmente:
    
    - **DT**: φ_g fissato a 45°, coesione apparente c_g > 0 (entra nelle
      verifiche di scorrimento interne), verifica σ_max ≤ σ_adm Maccaferri
      Gawac al posto del punzonamento.
    - **ES**: φ_g calcolato da formula 25·γ−10° (~26÷32°), c_g = 0, verifica
      classica punzonamento del filo singolo.
    
    [Dettagli completi →](rete.md)

??? question "Posso usare reti non Maccaferri?"
    Per la DT: scegli "Personalizzato" o inserisci a mano i parametri da
    scheda tecnica del produttore. Per la ES: i parametri vengono già inseriti
    a mano (non c'è catalogo).

## Geometria

??? question "Quando usare 'Allineamento a sinistra' vs 'a destra'?"
    - **A destra** (default): paramento monte verticale, gradoni a valle. Il
      più comune per muri di regimazione idraulica o stradali. Calcolo con
      spinta dal terreno (Coulomb completo).
    - **A sinistra**: paramento valle verticale, gradoni a monte → richiede
      un **riempimento a tergo** tra muro e terreno spingente. Il riempimento
      conta come peso stabilizzante; spinta con δ=φ (contatto diretto
      riempimento-gabbione).

??? question "Qual è il range raccomandato per α (inclinazione muro)?"
    5÷10° per muri 3÷5 m è la pratica standard Maccaferri. Sotto 5°
    l'effetto è trascurabile. Sopra 12° serve cautela: la base di scavo
    deve essere effettivamente inclinata e i gabbioni devono essere posati
    con cura per non risultare sghembi.

??? question "Posso inclinare solo la fondazione senza il muro?"
    Sì. β (Fondazione → Inclinazione) e α (Geometria → Inclinazione muro)
    sono parametri **indipendenti**. La fondazione inclinata aiuta soprattutto
    lo scorrimento esterno; il muro inclinato aiuta il ribaltamento + la
    direzione della spinta.

??? question "La fondazione c'è sempre?"
    No, se imposti **AltezzaFondazione = 0** la fondazione non viene disegnata
    né considerata. La prima fila di gabbioni poggia direttamente sul
    terreno di fondazione. In quel caso le verifiche interne fila 0 usano
    φ_fond e c_fond del terreno (non φ_g del gabbione).

## Bishop

??? question "GDW trova il cerchio critico automaticamente?"
    **No**. GDW calcola un solo cerchio alla volta. Per la ricerca del
    cerchio critico devi modificare manualmente i 3 punti (valle, monte,
    base) e rilanciare. Strumenti dedicati come GeoStru Slope/GSA fanno
    la ricerca automatica.

??? question "Errore 'La superficie di scorrimento attraversa il muro'"
    Il cerchio che hai definito attraversa muro o fondazione anziché
    passare sotto. Sposta il **punto base** più in profondità (Y più
    negativo), o il punto valle più a sinistra, o il punto monte più a
    destra. Per fondazione inclinata, il cerchio deve passare sotto la
    quota più profonda (lato monte = `wallBaseY - h_m`).

## File e salvataggio

??? question "Dove vengono salvati i miei progetti?"
    - **Sessione browser**: autosave in `localStorage` ogni 1.5 s (recupero
      automatico al crash/chiusura imprevista).
    - **File `.gabbioni`**: scarica sul tuo PC con File → Salva. Lo apri
      quando vuoi con File → Apri.
    - **Server GeoStru**: GDW NON memorizza i tuoi progetti sui server
      (privacy). Sono solo sul tuo browser/PC.

??? question "Ho perso il progetto chiudendo il browser, posso recuperarlo?"
    Sì, se ti riesci ad arrivare alla stessa pagina entro **7 giorni**:
    appare un banner giallo "Bozza non salvata trovata — Ripristina /
    Scarta". Clicca Ripristina. Dopo 7 giorni lo snapshot scade.

??? question "Il `.gabbioni` di un anno fa si apre ancora?"
    Sì, il formato è backward-compatible. Le versioni 1÷4 si caricano e i
    campi nuovi (es. InclinazioneMuro, CoesioneGabbione) assumono i default.

## Supporto

??? question "Ho un bug o un suggerimento, dove segnalo?"
    Apri il modale `?` in alto a destra → tab **Feedback** → email a
    info@geostru.ai. Includi: versione di GDW (visibile nel tab Versione),
    file `.gabbioni` del progetto, screenshot del problema.

??? question "Documentazione teorica completa dove la trovo?"
    Nel modale `?` → tab **Help** → "Guida teorica" (apre `/docs/guida.html`
    in nuova tab). Contiene formule estese, riferimenti normativi e abachi.

??? question "Esiste una versione desktop / app native?"
    Non per ora. GDW NX è solo web. Esiste una versione storica desktop
    GeoStru "GabbioniWall" su PC Windows, ma non viene più aggiornata.

---

*Domanda non trovata? [Scrivici](mailto:info@geostru.ai?subject=Help%20GDW%20NX%20-%20FAQ).*
