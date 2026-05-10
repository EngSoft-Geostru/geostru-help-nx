# GeoStru NX — Manuali utente (web apps)

Questo repo contiene i **sorgenti** dei manuali delle nuove applicazioni web della
suite **GeoStru NX**. Ogni cartella prodotto è un sito MkDocs Material indipendente.

Sito pubblicato su **https://help.nx.geostru.ai/&lt;prodotto&gt;/**.

> Per i manuali della **versione desktop** legacy → repo `geostru-help` (pubblicato
> su `help.geostru.eu`).

## Prodotti

| Prodotto | Cartella | URL pubblicato | App live |
|---|---|---|---|
| **GMS NX** — rilievo geomeccanico | [`gms/`](gms/) | https://help.nx.geostru.ai/gms/ | https://nx.geostru.ai/gms/ |
| LiquiTer NX — liquefazione | _coming soon_ | — | https://nx.geostru.ai/liquiter/ |
| Computo NX — computo metrico | _coming soon_ | — | https://nx.geostru.ai/computo/ |
| Trispace NX — CAD/web | _coming soon_ | — | https://nx.geostru.ai/trispace/ |
| Hydrogeo NX — idrogeologia | _coming soon_ | — | https://nx.geostru.ai/hydrogeo/ |
| Runoff Lab NX — pluviometria | _coming soon_ | — | https://nx.geostru.ai/runofflab/ |
| GeoSection NX — sezioni | _coming soon_ | — | https://nx.geostru.ai/geosection/ |
| Stratigrapher NX — colonne | _coming soon_ | — | https://nx.geostru.ai/stratigrapher/ |

## Per iniziare un nuovo manuale prodotto

```bash
# 1. Copia il template
cp -r _template-nx <nuovo-prodotto>

# 2. Modifica mkdocs.yml: site_name, site_url, plugin
cd <nuovo-prodotto>
# … edita …

# 3. Anteprima locale
pip install mkdocs-material mkdocs-static-i18n
mkdocs serve   # http://127.0.0.1:8000

# 4. Aggiungi i contenuti in docs/it/, docs/en/, docs/es/, docs/ro/
```

Vedi [`STANDARD.md`](STANDARD.md) per le convenzioni di stile, struttura pagine,
slug, screenshot, link cross-prodotto. **Da rispettare per coerenza in tutta la suite NX.**

## Struttura monorepo

```
geostru-help-nx/
├── README.md                 ← questo file
├── CONTRIBUTING.md           ← come contribuire (anche per non-developer)
├── STANDARD.md               ← convenzioni stile + struttura pagine NX
├── _template-nx/             ← template per nuovi prodotti
│   ├── mkdocs.yml
│   └── docs/{it,en,es,ro}/
├── .github/workflows/
│   └── deploy.yml            ← build + deploy → GitHub Pages → help.nx.geostru.ai
├── gms/                      ← manuale GMS NX
│   ├── mkdocs.yml
│   └── docs/{it,en,es,ro}/
├── liquiter/                 ← manuale LiquiTer NX (in arrivo)
└── …
```

## Contribuzione

Vedi [`CONTRIBUTING.md`](CONTRIBUTING.md). In sintesi: edit dei `.md` via
GitHub web (icona ✏️), Pull Request, dopo il merge la modifica è online in
pochi minuti.

## Licenza

© GeoStru Software — contenuti dei manuali tutti i diritti riservati.
