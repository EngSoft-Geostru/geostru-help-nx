# Quickstart — il tuo primo sondaggio in 5 minuti

## 1. Apri l'app

Vai su [`nx.geostru.ai/stratigrapher/`](https://nx.geostru.ai/stratigrapher/).

## 2. Scegli un template

Nel modal info (`?` in alto a destra) sezione **"Modelli di esempio"**:

- **Sondaggio standard** — colonna stratigrafica generica
- **DPSH** — penetrometro dinamico super-pesante
- **CPT/CPTU** — penetrometro statico (con misura U se CPTU)
- **Piezometro** — letture progressive del livello freatico
- **Inclinometro** — letture in profondità di Δx, Δy

Click sul template → si carica un esempio pronto.

## 3. Modifica la stratigrafia

Pannello centrale: tabella **Strati**. Per ogni strato:

| Campo | Significato |
|---|---|
| Top / Base | profondità in metri da p.c. |
| Litologia | testo descrittivo (auto-completion) |
| Simbolo | simbolo grafico (ISO/UNI) |
| Colore | auto da litologia, override |
| Note | parametri ISRM, prove, granulometria |

## 4. Aggiungi prove in sito

A destra, **pannello prove**:

- **SPT** — colpi/30cm a profondità → grafico N-SPT vs z
- **DPSH** — colpi/10cm
- **CPT** — qc, fs in continuo (drag&drop file CPT del produttore)
- **Vane Test** — Su per profondità
- **Pressiometro** — moduli E, p_l per profondità

## 5. Allega foto carote

Trascina le **foto delle cassette di carote** nell'apposita area. Stratigrapher
le associa alla profondità delle carote.

## 6. Esporta

Toolbar **Esporta**:

- **PDF** — log di sondaggio impaginato
- **`.borehole`** (JSON GeoStru) — per import in GeoSection NX, Liquefaction NX, ecc.

---

## Prossimi passi

- [**Workflow completo**](workflow.md)
- [**FAQ**](faq.md)

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20Stratigrapher%20NX%20-%20Quickstart).*
