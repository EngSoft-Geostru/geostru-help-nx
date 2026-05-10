# Quickstart — il tuo primo computo in 5 minuti

In 5 minuti vedi Computo NX al lavoro su un PDF di preventivo realistico.

## 1. Apri l'app

Vai su [`nx.geostru.ai/computo/`](https://nx.geostru.ai/computo/).

## 2. Carica una risorsa di esempio

Click sull'icona **`?`** in alto a destra → si apre il modal *Computo NX*.

Sezione **"Da trascinare nella chat AI"**: scegli **Preventivo PDF (CAL25)**
e clicca per scaricarlo.

Una volta scaricato, **trascinalo dentro la chat AI** in basso (o usa il
pulsante 📎 *Allega*).

## 3. L'AI estrae le voci

L'AI (Claude integrato):

1. Legge il PDF (testo + tabelle + immagini se presenti)
2. Identifica le **voci di preventivo** con descrizione + quantità + unità
3. Mappa ogni voce al **prezzario regionale CAL25**: trova la voce
   corrispondente per codice o descrizione
4. Restituisce una **tabella strutturata** con:
   - Codice voce CAL25
   - Descrizione
   - U.M. (unità di misura)
   - Quantità rilevata dal PDF
   - Prezzo unitario CAL25
   - Importo

Nei casi di ambiguità (descrizione PDF non chiara), l'AI propone più match e
ti chiede conferma.

## 4. Rivedi e correggi

Sulla **destra** vedi la **tabella del computo** popolata. Click su una riga
per editare:

- Quantità (se l'AI l'ha letta male dal PDF)
- Descrizione (se vuoi personalizzare per il committente)
- Voce di prezzario (se preferisci un'altra voce dal catalogo)

In basso vedi **Totale** e **Subtotali per categoria**.

## 5. Esporta

Toolbar **File → Esporta**:

- **PDF** — computo metrico impaginato (tabella + totali + intestazione)
- **Excel** — `.xlsx` editabile per personalizzazioni
- **XPWE** — formato standard di interscambio (importabile in altri software
  di computo)
- **CSV** — per analisi semplici

---

## Prossimi passi

- [**Workflow completo**](workflow.md) — un progetto reale dall'inizio alla fine
- [**FAQ**](faq.md) — domande sulle import AI

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20Computo%20NX%20-%20Quickstart).*
