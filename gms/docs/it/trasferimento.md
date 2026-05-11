# Trasferimento dal tablet al PC

Hai rilevato giaciture in campo con [GMS Compass](compass.md) sul tablet
o smartphone. Per portarle dentro GMS NX sul PC dello studio hai
3 opzioni: **codice di trasferimento**, **file `.gms`**, o **anteprima
diretta**.

## A. Codice di trasferimento (consigliato)

È la modalità più rapida e *senza-cavi*: 8 caratteri da digitare.

### Sul tablet (Compass)

1. A fine rilievo, in alto a destra di Compass premi **"Trasferisci al PC"**.
2. Compass impacchetta tutte le misure (giaciture + linea di scansione
   + note) in un JSON e lo invia al server GeoStru.
3. Il server risponde con un **codice di 8 caratteri** del tipo `K7M9-A2BX`
   (alfanumerico, alfabeto Crockford-safe — niente confusione tra `0`/`O`
   o `1`/`l`/`I`).
4. Il codice resta valido **30 giorni** dal momento dell'emissione.

### Sul PC (GMS NX)

1. Apri `nx.geostru.ai/gms/`.
2. **File → Importa da → Codice trasferimento**.
3. Digita il codice (con o senza il trattino: `K7M9A2BX` ≡ `K7M9-A2BX`).
4. Le giaciture entrano nella tabella *Discontinuità* + i parametri della
   linea di scansione vanno in *Dati progetto*.

!!! tip "Codice riusabile"
    Lo stesso codice può essere "scaricato" più volte entro la TTL di
    30 giorni — utile se devi importare lo stesso rilievo su più PC
    (per esempio: laptop di campo + PC fisso dello studio).

!!! warning "Niente account = niente sicurezza"
    L'endpoint del codice di trasferimento è **pubblico** per non
    obbligare gli operatori di campo a gestire credenziali. Chiunque
    conosca il codice può scaricare i dati. Non usarlo per dati
    sensibili (rilievi su siti riservati, perizie giudiziali, …).
    In quei casi preferisci il file `.gms` trasferito a mano via USB
    o cloud privato.

## B. File `.gms`

Modalità classica, funziona offline, niente di sensibile passa per i
nostri server.

### Sul tablet (Compass)

1. Premi **"Esporta .gms"** in alto.
2. Il browser scarica un file `Rilievo_AAAAMMGG_HHMM.gms` nella
   cartella *Download* del dispositivo.
3. Trasferiscilo al PC come preferisci: cavo USB, AirDrop, email,
   cloud (Drive / Dropbox / OneDrive), …

### Sul PC (GMS NX)

**File → Apri…** → seleziona il `.gms` → entra come progetto pieno
(giaciture + pendio + famiglie + metadati).

## C. Anteprima diretta nel browser

Se sei seduto davanti al PC con il tablet a fianco e vuoi solo
*controllare* il rilievo prima di trasferirlo:

1. Sul tablet, in Compass, premi **"Anteprima"**.
2. Si apre una vista riepilogativa con: numero misure, statistica
   sintetica (β medio, α medio per famiglia se già taggate), elenco
   giaciture.
3. Da lì puoi correggere/eliminare misure prima di generare il codice
   o salvare il `.gms`.

L'anteprima **non trasferisce nulla** — è solo per controllo qualità
sul tablet.

---

## Errori frequenti

| Sintomo | Causa probabile | Cosa fare |
|---|---|---|
| "Codice non valido" | Codice scaduto (>30 giorni) o digitato male | Rigenera dal tablet o ricontrolla |
| "Codice valido ma 0 giaciture" | Hai trasferito una sessione vuota | Sul tablet, controlla che la lista non sia vuota |
| `.gms` non si apre | File corrotto durante il trasferimento | Riesporta dal tablet |
| Sul tablet, "Trasferisci" è grigio | Sessione vuota o nessuna connessione | Aggiungi almeno 1 misura, controlla rete |
| Codice ricevuto ma "errore di rete" sul PC | Firewall aziendale che blocca `nx.geostru.ai` | Usa file `.gms` come ripiego |

## Architettura tecnica (per i curiosi)

- **Endpoint**: `POST /api/transfer/upload` riceve il payload JSON e
  ritorna il codice. `GET /api/transfer/{code}` lo restituisce.
- **Storage**: file system del server con cleanup automatico TTL
- **Alfabeto del codice**: `0123456789ABCDEFGHJKMNPQRSTVWXYZ` (32 simboli,
  Crockford), 8 caratteri = 32⁸ ≈ **10¹² combinazioni** (collisioni
  improbabili anche con migliaia di codici contemporanei).
- **Autenticazione**: nessuna. La sicurezza è demandata alla brevità
  della finestra (30 giorni) e all'imprevedibilità del codice (non
  enumerabile in tempi ragionevoli).

---

## Vedi anche

- [GMS Compass](compass.md) — la sorgente delle misure
- [Workflow completo](workflow.md) — il trasferimento nel ciclo intero
- [Formati file](formati.md) — dettaglio del formato `.gms`

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20GMS%20NX%20-%20Trasferimento).*
