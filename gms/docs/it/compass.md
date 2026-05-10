# GMS Compass — bussola digitale per tablet

**GMS Compass** è l'app web companion di GMS NX che trasforma uno smartphone
o tablet in una **bussola di geologo digitale**: appoggi il dispositivo
sul piano, premi un pulsante, e la coppia immersione/inclinazione (β/α)
viene letta direttamente dai sensori (accelerometro + magnetometro).

## Requisiti

- **Smartphone o tablet** con accelerometro e magnetometro (la stragrande
  maggioranza dei dispositivi consumer).
- **Browser moderno con accesso ai sensori**: Chrome / Edge / Safari iOS
  recenti. Firefox Android ha alcune limitazioni note (vedi sotto).
- **HTTPS obbligatorio** — i sensori non sono accessibili da contesti `http://`.
  L'URL ufficiale è `https://nx.geostru.ai/gms/compass`.
- **Permesso esplicito ai sensori** — al primo accesso, iOS chiede
  l'autorizzazione: tocca *Consenti*.

!!! warning "iOS richiede HTTPS *e* gesto utente"
    Su iPhone/iPad la richiesta del permesso ai sensori parte solo dopo
    un *tap* (non al caricamento della pagina). Compass mostra un
    pulsante **"Attiva sensori"** che innesca la richiesta.

## Apertura

Da GMS NX (PC o tablet):

1. Toolbar in alto → pulsante **"Compass 📐"**
2. Si apre la pagina `https://nx.geostru.ai/gms/compass`
3. Tocca **"Attiva sensori"** (solo prima volta)

Da tablet, in autonomia: digita `nx.geostru.ai/gms/compass` nel browser.

## Procedura di misura

Compass è in **modalità landscape** (orizzontale) ed è ottimizzata per
essere **appoggiata sul piano** da rilevare:

1. **Trova un punto rappresentativo** della superficie del giunto.
   Evita zone curve, distorte o coperte di detrito.
2. **Appoggia il dispositivo schermo in alto, faccia posteriore in
   contatto col piano**. Tienilo fermo per ~1 secondo.
3. Quando i numeri si **stabilizzano** (β e α a sinistra dello schermo
   smettono di oscillare), premi il **pulsante centrale "+"**.
4. La giacitura viene salvata nella **lista a destra** con un
   progressivo (`#1`, `#2`, …).
5. **Stacca il dispositivo**, sposta sul prossimo piano, ripeti.

!!! tip "Misura stabile = misura buona"
    Compass mostra in tempo reale il valore β/α aggiornato. Se i
    numeri *ballano* di ±5° o più, il dispositivo non è ben appoggiato
    o c'è interferenza magnetica (cavi, ferro, pacchetti elettronici).
    Spostati di mezzo metro e riprova.

### Modificare o eliminare una misura

Nella lista a destra, ogni riga ha:

- **`✎`** — modifica i valori (per esempio se vuoi correggere a mano)
- **`✕`** — elimina la misura

### Annotare la distanza progressiva

Se stai rilevando lungo una **linea di scansione**, prima della misura
digita il **valore di distanza** (m) nel campo dedicato in alto. Compass
lo salverà insieme alla giacitura. È quello che poi GMS userà per
geolocalizzare il punto sulla mappa.

### Note testuali

In coda a ogni misura puoi aggiungere una **nota** (rugosità apparente,
indizi di scivolamento, presenza d'acqua, …). Non sostituisce i
parametri ISRM completi ma è utilissima per ricordarsi *cosa hai
guardato*.

## Calibrazione del magnetometro

Il magnetometro deriva nel tempo (specialmente vicino a oggetti
metallici). Per **calibrare**:

1. Tieni il dispositivo in mano e fai un **disegno a 8** in aria,
   ruotando attorno ai 3 assi, per 5-10 secondi.
2. Compass mostra in alto a destra un'icona di stato del magnetometro:
   - 🟢 **verde** — ok
   - 🟡 **giallo** — accettabile
   - 🔴 **rosso** — calibra urgentemente

Ricalibra periodicamente (ogni ora di rilievo, o quando ti sposti di
zona) e **sempre** se ti accorgi che β cambia di 20-30° spostando il
dispositivo di pochi metri.

## Trasferimento al PC

A fine sessione, premi in alto a destra **"Trasferisci al PC"**:

1. Compass invia tutte le misure raccolte al server GeoStru
2. Riceve in cambio un **codice di 8 caratteri** (es. `K7M9-A2BX`)
3. Il codice resta valido **30 giorni**

Apri GMS NX sul PC e da **File → Importa da → Codice trasferimento**
digita il codice. Le giaciture entrano nella tabella *Discontinuità*
come se le avessi inserite a mano.

Vedi [Trasferimento al PC](trasferimento.md) per il flusso dettagliato.

!!! note "Senza connessione di rete?"
    Se sul cantiere non hai segnale, Compass salva tutto in memoria
    locale del browser (IndexedDB). Quando torni online, il
    trasferimento parte normalmente.

## Salvataggio del progetto Compass

In alternativa al codice di trasferimento, da Compass puoi:

- **Scaricare un `.gms`** — il file viene salvato sul dispositivo
  e poi puoi aprirlo da GMS NX con **File → Apri**
- **Esportare CSV** — formato compatibile con Excel/altri software

## Limitazioni note

- **Firefox Android**: l'accesso al magnetometro è dietro flag
  sperimentale, sconsigliato.
- **Bussola elettronica vs bussola Brunton**: la precisione tipica del
  magnetometro consumer è di **±2-5°** in condizioni buone, peggio
  vicino a strutture metalliche. Per rilievi di alta precisione
  (faglie attive, monitoraggi cinematici) preferisci la bussola da
  geologo.
- **Inclinometro**: l'accelerometro restituisce α con precisione
  ottima (±1°), spesso migliore della bussola analogica.

---

## Vedi anche

- [Cosa si misura](rilievo.md) — guida geologica al rilievo
- [Trasferimento al PC](trasferimento.md) — codice 8-caratteri
- [Workflow completo](workflow.md) — il rilievo Compass nel ciclo intero

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20GMS%20NX%20-%20Compass).*
