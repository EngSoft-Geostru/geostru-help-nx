# Esportazione

RockPlane NX produce due output finali del progetto:

## Relazione di calcolo (Word .docx)

Menu **File → Salva** oppure **Esporta → Word**, oppure shortcut: clicca direttamente sulla voce nel menu dropdown.

### Contenuto

La relazione `.docx` generata è completa e autonoma:

1. **Copertina** — titolo, sottotitolo, data, descrizione del progetto, sito, tecnico
2. **§1 Premessa e quadro normativo**
   - NTC 2018 §6.8 — tabella coefficienti A2/M2/R2
   - NTC 2018 §6.6 — tiranti, ξ Tab. 6.6.III
   - NTC 2018 §6.7 — chiodi Variante A SoilNail
   - Eurocodice 7 — DA1/DA2/DA3
   - Sisma NTC §3.2 / §7.11.3
3. **§2 Modello teorico** — geometria caso A, equazioni equilibrio (26-30), interventi
4. **§3 Dati di input**
   - Progetto (descrizione, sito, data)
   - Geometria (H, β, α, ψ, B, eventuale TC)
   - Materiale (γ, c, φ)
   - Approccio di verifica con coefficienti applicati
   - Acque, sisma, forza esterna
   - Interventi posizionati
5. **§4 Geometria risolta** — L, M, Q, A, W, coordinate B/C
6. **§5 Resistenze di progetto · chiodi e tiranti** (se presenti tipologie con CalcolaCapacitaNTC):
   - Breakdown R_acciaio · R_aderenza · R_estrazione · V_max
   - Catena R_min → R_k → R_d con ξ e γ<sub>Ra,t</sub>
   - **Verifiche stile NTC §6.6**: R.2/R.3/R.4/R.5 con rapporto R/E e ✓/✗
7. **§6 Forze sul piano di rottura** — ΣF<sub>x</sub>, ΣF<sub>y</sub>, U, V, N, S, τ
8. **§7 Esito della verifica** — FS con confronto FS<sub>req</sub>
9. **§8 Avvisi**
10. **Annex A · Validazione del codice** — 12 test benchmark con valori attesi, esito 97/97
11. **Bibliografia**

### Formato

- Tabelle con bordi soft, header con sfondo soft blu
- Testo principale Inter, monospace Consolas per i numeri
- Page break tra sezioni principali
- ~12-15 pagine per un progetto medio (con interventi)

### Nome file

`RockPlane-<slug-descrizione>-AAAAMMGG-HHMM.docx`

dove `slug-descrizione` è la descrizione del progetto in slug (lowercase, no spazi).

## Sezione 2D (DXF)

Menu **Esporta → DXF**, oppure dal menu File.

### Contenuto

File DXF AutoCAD-compatibile con la **sezione bidimensionale** del cuneo:

- Contorno del cuneo (OBC o OBCD)
- Piano sommitale (β=ψ se ψ≠0)
- Fessura di trazione (se attiva)
- Hatching diagonal del cuneo
- Chiodi/tiranti posizionati (linea + bulbo)
- Reti (overlay schematico sul fronte)
- Vettori delle forze (W, S, U, V) al baricentro
- Quote dimensionali (H, L, M, angoli α, β, ψ)
- Etichette dei punti O, B, C, D, G

### Layer DXF

Il file DXF è organizzato in **layer** per facilità di editing:

- `0` — default
- `cuneo` — contorno e hatching
- `piani` — fronte + bench + failure plane
- `tc` — tension crack
- `chiodi` — chiodi e tiranti
- `reti` — overlay reti
- `forze` — vettori forze
- `quote` — quote dimensionali
- `testo` — etichette

Importa il file in AutoCAD, Civil3D, Bricscad, ZWCAD o qualsiasi altro CAD compatibile DXF.

### Sistema di riferimento

Il DXF usa lo stesso math frame di RockPlane:
- Origine = piede del versante O
- X verso monte (destra in default mirror=false)
- Y verticale
- Unità = **metri** ([m])

## Salva progetto (`.rockplane`)

Menu **File → Salva su file…**

Il file `.rockplane` è un **JSON** umano-leggibile contenente tutto lo stato del progetto:

- Anagrafica e localizzazione
- Geometria, materiale, acque, sisma, forza esterna
- Catalogo tipologie chiodi/tiranti + reti
- Interventi posizionati
- Approccio normativo
- Immagine del sito (base64 inline)

[Dettagli formato →](formati.md)

## Apri progetto

Menu **File → Apri da file…**. Carica un `.rockplane` precedentemente salvato. Se il progetto corrente ha modifiche non salvate, compare un prompt di conferma.

## Nuovo progetto

Menu **File → Nuovo progetto**. Resetta tutti i campi ai default. Se ci sono modifiche non salvate, conferma prima.

## Modifiche non salvate — badge

Quando ci sono modifiche non ancora salvate, in alto a destra (accanto al menu File) compare un **badge ambra** "● non salvato" che pulsa. Salva su file per resettarlo.

Se chiudi la tab del browser con modifiche non salvate, il browser ti chiede conferma (prompt nativo).

## Esempio nome file

Progetto "Versante SS-18 km 42" salvato il 14 maggio 2026 alle 14:30:

- Relazione: `RockPlane-versante-ss-18-km-42-20260514-1430.docx`
- DXF: `RockPlane-versante-ss-18-km-42-20260514-1430.dxf`
- Progetto: `Versante SS-18 km 42.rockplane`
