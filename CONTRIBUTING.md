# Come contribuire ai manuali GeoStru NX

Questo repo contiene i **sorgenti markdown** dei manuali web NX. Il sito su
`help.nx.geostru.ai` viene generato **automaticamente** quando una modifica
viene approvata e mergiata in `main`. Niente FTP, niente upload manuali.

## Per chi non ha familiarità con Git

1. Accedi a `https://github.com/EngSoft-Geostru/geostru-help-nx` con il tuo
   account (chiedi l'invito a chi gestisce l'organization).
2. Apri la cartella del prodotto, es. `gms/docs/it/`.
3. Apri il file `.md` che vuoi modificare (oppure click su **"Add file"** → **"Create new file"**).
4. Click sull'icona **matita ✏️** in alto a destra → modifica il testo nel form web.
5. In fondo, **"Commit changes"** → seleziona *"Create a new branch for this commit and start a pull request"*, dai un titolo breve, conferma.
6. Si apre una **Pull Request**: aspetta che la CI mostri ✅ e che un reviewer la approvi. Dopo il merge, in pochi minuti la modifica è online su `help.nx.geostru.ai/<prodotto>/`.

Niente da installare.

## Per chi usa Git

```bash
git clone https://github.com/EngSoft-Geostru/geostru-help-nx.git
cd geostru-help-nx
git checkout -b fix/<breve-descrizione>

# Anteprima locale del prodotto su cui lavori
cd gms   # (o liquiter, trispace, …)
pip install mkdocs-material mkdocs-static-i18n
mkdocs serve    # apri http://127.0.0.1:8000

# … edita .md in docs/<lingua>/ …

git add -A
git commit -m "gms: descrizione modifica"
git push origin fix/<breve-descrizione>
```

Poi apri una Pull Request su GitHub.

## Regole di editing

### Slug e link

- **Non rinominare i file `.md` esistenti** se non strettamente necessario:
  i link interni di altri capitoli e i bookmark esterni si rompono.
- Se rinomini, aggiorna tutti i link che li referenziano e aggiungi un
  redirect nel file `mkdocs.yml` (sezione `redirects`).

### Struttura pagina

Vedi [`STANDARD.md`](STANDARD.md) per slug standard (`index`, `quickstart`,
`workflow`, `glossario`, `formati`, `faq`) e convenzioni di stile.

### Lingua di lavoro

L'**italiano** (`docs/it/`) è la lingua principale. EN/ES/RO sono traduzioni:
le aggiorniamo *dopo* aver consolidato il contenuto IT, non in parallelo.

Se cambi una pagina IT, **lascia un TODO** sulle altre lingue invece di
provare a tradurre tu (a meno che tu non sia madrelingua):

```markdown
<!-- TODO it→en: aggiornare questa pagina, modificata il 2026-05-12 -->
```

### Screenshot

- Cartella `docs/<lingua>/img/`
- Formato preferito: PNG ottimizzato, max 1200×800 px, < 200 kB
- Nome file in kebab-case: `stereonet-2d-equiareale.png` non `Screenshot 1.png`
- Sempre con `alt` text descrittivo: `![Stereonet 2D Schmidt-Lambert](img/stereonet-equiareale.png)`

### Admonition (callout)

Usa quelli di Material per blocchi di rilievo:

```markdown
!!! note "Nota"
    Testo informativo.

!!! warning "Attenzione"
    Avviso importante.

!!! tip "Suggerimento"
    Suggerimento pratico.

!!! example "Esempio"
    Caso d'uso concreto.
```

### Riferimenti cross-prodotto

Per linkare un altro manuale NX, usa l'URL pubblicato:

```markdown
Vedi anche [LiquiTer NX — analisi della liquefazione](https://help.nx.geostru.ai/liquiter/it/).
```

Non linkare mai a path relativi tra prodotti diversi (sono siti MkDocs separati).

## Cosa NON committare

- Cartella `site/` (output di `mkdocs build`) — è in `.gitignore`
- File `.DS_Store`, `Thumbs.db`
- Credenziali, chiavi API, percorsi locali

## Domande

Apri una **Issue** sul repo o scrivi a `info@geostru.ai`.
