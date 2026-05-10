# GeoStru NX — Standard manuali

Convenzioni di stile e struttura **comuni a tutti i manuali NX** per coerenza
nella suite. Da rispettare quando si crea o modifica un manuale prodotto.

## Struttura cartella prodotto

Ogni prodotto è una cartella indipendente con:

```
<prodotto>/
├── mkdocs.yml             ← config MkDocs (theme, plugin, nav)
└── docs/
    ├── it/                ← lingua principale (obbligatoria)
    │   ├── index.md         (home prodotto)
    │   ├── quickstart.md    (5 minuti per iniziare)
    │   ├── workflow.md      (sequenza completa input → calcolo → export)
    │   ├── glossario.md     (definizioni termini chiave del dominio)
    │   ├── formati.md       (file supportati: import/export)
    │   ├── faq.md
    │   ├── tutorials/       (cartella di tutorial passo-passo)
    │   ├── img/             (screenshot, max 1200×800, kebab-case)
    │   └── … capitoli specifici al prodotto
    ├── en/                ← traduzione inglese (consigliata)
    ├── es/                ← traduzione spagnola (opzionale)
    └── ro/                ← traduzione rumena (opzionale)
```

**Regola**: l'italiano è sorgente di verità. Le altre lingue si aggiornano *dopo*
il consolidamento del contenuto IT.

## Slug standard delle pagine

Ogni manuale prodotto deve avere almeno questi file (anche brevi):

| Slug | Scopo |
|---|---|
| `index.md` | Home prodotto: cos'è l'app, a chi serve, in quanti minuti si fa il primo rilievo. Fa da landing dal modal `?` dell'app e da SEO. |
| `quickstart.md` | Tutorial guidato 5 minuti, dal "vado su nx.geostru.ai" al "vedo i risultati". Screenshot e bullet, niente teoria. |
| `workflow.md` | Sequenza completa di un progetto reale, con tutte le opzioni avanzate. |
| `glossario.md` | Definizioni dei termini specifici del dominio (es. *cono d'attrito*, *Markland*, *α₉₅*). |
| `formati.md` | File supportati: import (.gms, .pol, .csv, .ply, ecc.) + export (Word, DXF, CSV). |
| `faq.md` | Domande frequenti raccolte da assistenza/feedback utenti. |

Capitoli specifici al prodotto **dopo questi**, con slug semantici (es.
`stereonet.md`, `markland.md`, `compass.md`, `ai-import.md`).

## Convenzioni di stile

### Tipografia e voce

- **Tu**, non *lei* (linguaggio diretto, professionale ma cordiale)
- Frasi brevi, paragrafi di 3-5 righe max
- Niente *"semplicemente"*, *"basta"*, *"facilmente"* (frasi vuote che il lettore frustrato odia)
- Termini tecnici sempre col loro nome italiano + sigla in parentesi: *"angolo di attrito (φ)"*, *"dip direction (β)"*
- Screenshot **dopo** il testo che spiega cosa cercare, non prima

### Heading

- `# H1` — solo per il titolo della pagina (uno per pagina)
- `## H2` — sezioni principali
- `### H3` — sottosezioni
- Mai oltre H4

### Codice

```markdown
File `.gms` (sorgente progetto):
```json
{
  "Versione": "2026.1",
  "Giunti": [...]
}
```
```

Il fenced code-block ha sempre il **language hint** (`json`, `csv`, `yaml`, `bash`, `text`).

### Admonition (callout Material)

Usali parsimoniosamente. Solo per:

```markdown
!!! note "Nota"
    Informazione importante che il lettore potrebbe perdere.

!!! warning "Attenzione"
    Comportamento che può portare a errori.

!!! tip "Suggerimento"
    Trucco non ovvio.

!!! example "Esempio"
    Caso d'uso concreto, sempre con dati reali.
```

Non usare `!!! info` (ridondante con `note`), né `!!! danger` (drammatico, lascia per la sicurezza).

### Tabelle

Usa Markdown tables per dati comparativi. Niente HTML inline a meno che la tabella richieda colspan/rowspan complesse.

### Link

- **Interni** al manuale: relativi (`[stereonet](stereonet.md)`)
- **Cross-prodotto** NX: URL completo (`[LiquiTer](https://help.nx.geostru.ai/liquiter/it/)`)
- **Esterni** (sito GeoStru, riferimenti tecnici): URL completo + `target="_blank"` solo se necessario

### Screenshot

- PNG ottimizzato, max 1200×800 px, **< 200 kB** (usa TinyPNG/Squoosh)
- Nome file in kebab-case: `stereonet-equiareale-polare.png`
- `alt` text **sempre presente** e descrittivo (per accessibilità + SEO)
- UI in italiano (lingua sorgente). Le altre lingue useranno screenshot localizzati separati.

## Footer ogni pagina

Aggiungi alla fine di ogni capitolo:

```markdown
---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GMS%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/gms/docs/it/index.md).*
```

(Il path dell'edit link va aggiornato per ogni pagina — il theme Material lo
fa automaticamente con `edit_uri` in `mkdocs.yml`.)

## Link bidirezionali app ↔ manuale

**Dal modal `?` dell'app NX** ci deve essere un bottone CTA prominente verso
il manuale esterno. Vedi sezione successiva ("Template del modal info NX").

**Dalla home del manuale** un pulsante prominente:

```markdown
[**Apri l'app**](https://nx.geostru.ai/<slug>/){ .md-button .md-button--primary }
```

## Template del modal info NX

Tutti i prodotti NX (GMS, LiquiTer, RSL III, Computo, Trispace, Hydrogeo,
Runoff Lab, GeoSection, Stratigrapher, Maps, Loadcap, Tiranti, Converter)
devono usare lo **stesso modal info** per consistenza UX. Il modal ha 4 tab:
*Versione · Help · Risorse · Feedback*. Il tab Help in cima ha sempre il
pulsante CTA al manuale esterno.

### Posizione del pulsante `?`

Il pulsante che apre il modal **deve stare in navbar top-level**, sempre visibile.
**NON dentro il dropdown utente** (avatar / "Account" / "Le mie applicazioni").
Questo perché:

- Aiuto deve essere a 1 click, non a 3 (dropdown → menu → voce)
- Convenzione industry (Google Docs, Notion, GitHub, Slack, Stripe — tutti hanno
  `?` top-level)
- Onboarding dei primi 5 minuti: l'utente nuovo deve trovare la guida senza
  esplorare menu
- Su mobile/tablet il dropdown utente è scomodo

Posizione canonica: subito a sinistra del language picker, accanto alla
campanella delle notifiche.

In aggiunta al `?` top-level, **mantenere anche** una voce "Aiuto" dentro il
dropdown utente (belt & suspenders — utenti che cercano lì la trovano comunque).
La voce nel dropdown deve aprire lo stesso modal: `data-bs-target="#nxHelpModal"`.

### File template

Il markup canonico è in `_template-nx/_NxHelpModal.cshtml`. Per applicarlo a
un prodotto:

1. Copia `_template-nx/_NxHelpModal.cshtml` come
   `<NomeApp>/Pages/Shared/_NxHelpModal.cshtml` e personalizza i 5 segnaposti
   `[CAMBIA-…]` (slug, nome prodotto, descrizione, link rapidi, riferimenti).
2. Nel `_Layout.cshtml` dell'app, sostituisci il vecchio modal info con:
   ```cshtml
   <partial name="_NxHelpModal" />
   ```
3. Aggiungi/sposta il pulsante `?` in navbar top-level (vedi sopra) con
   `data-bs-toggle="modal" data-bs-target="#nxHelpModal"`.
4. Se esiste una voce "Aiuto" nel dropdown utente, lasciala ma sostituisci
   l'`onclick`/`href` con `data-bs-target="#nxHelpModal"`.
5. Verifica che la variabile `lang` sia definita nel layout (di solito già c'è).

Una volta inserito, il modal:
- Apre il manuale esterno a `https://help.nx.geostru.ai/<slug>/<lang>/`
- Mantiene Versione/Risorse/Feedback specifici del prodotto
- È identico in tutti i prodotti per UX coerente

**Dalla home del manuale** un pulsante prominente:

```markdown
[**Apri l'app GMS NX**](https://nx.geostru.ai/gms/){ .md-button .md-button--primary }
```

## Configurazione MkDocs (template)

Il template `_template-nx/mkdocs.yml` è già configurato per:

- Theme **Material** con palette navy GeoStru
- Plugin `mkdocs-static-i18n` per il switcher lingue (no path `/it/`, `/en/`, ma URL puliti `/?lang=en`)
- Plugin `search` multi-lingua
- `pymdownx.arithmatex` + MathJax per formule
- `pymdownx.details` + `pymdownx.superfences` per admonition annidate
- `attr_list` + `md_in_html` per HTML inline pulito
- `toc.permalink` (icona ¶ accanto agli heading)

Quando crei un nuovo prodotto, copia il template e modifica solo:

- `site_name`
- `site_url`
- `repo_name` / `repo_url`
- `nav` (l'elenco dei capitoli)

Tutto il resto rimane uguale per coerenza.

## Versioning

Il versioning del manuale è **continuo** (no major.minor): la modifica viene
deployata appena mergiata. Se serve mantenere snapshot per release passate,
usa branch dedicati (`v2026.1`, ecc.) — al momento non è necessario.

Le **release notes** dell'app vivono nel manuale stesso, in
`docs/<lang>/release-notes.md`.

## Glossario condiviso (futuro)

Quando i prodotti NX cresceranno, valuteremo di estrarre il **glossario condiviso**
dei termini geotecnici/geomeccanici in un sub-modulo separato (`_shared/glossario/`)
incluso da ogni prodotto via `mkdocs-monorepo-plugin`. Per ora ogni prodotto ha
il suo `glossario.md` indipendente.
