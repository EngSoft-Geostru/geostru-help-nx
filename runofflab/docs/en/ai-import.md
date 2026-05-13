# AI Import — loading rainfall series from PDF/Excel

Historical annual series are commonly found in:

- **PDFs of regional annuals** (dozens of pages, scanned or textual tables);
- **Excel files** downloaded from hydro-meteorological portals;
- **non-standard CSV** with Italian headers, mixed separators.

Entering this data manually is slow and error-prone. Runoff Lab NX
integrates an **AI-assisted importer** that automatically recognises the
file schema and fills the station.

## How it works

1. *File → Import → From file with AI…* → the modal opens.
2. Drag-drop the file (PDF or Excel) or paste text directly.
3. The AI extracts:
   - **station metadata** (name, code, municipality, region, lat/lon, observation period);
   - **annual maxima** by duration (60′, 3h, 6h, 12h, 24h).
4. **Preview** panel: compare extracted values against the file, edit as needed.
5. Hit *Confirm* → everything enters the study.

## Supported formats

| Format | Notes |
|--------|-------|
| Textual PDF | Regional annuals, table extracts. |
| Scanned PDF | Automatic OCR, quality dependent on scan. |
| Excel `.xlsx` | One row = one year; columns = durations. Order-independent. |
| CSV / TSV / TXT | Separators `,`, `;`, `\t` or spaces. |
| Free text (copy-paste) | Useful for excerpts from older annuals. |

## Ready samples

In the Info modal → **Resources** you'll find two example files to download:

- `ai-rainfall-sample-cosenza.xlsx` — realistic Excel format (Calabria annual).
- `ai-rainfall-sample-cosenza.pdf` — PDF extract from a regional annual.

Open the AI Import modal and drop one of them in to see the procedure live.

## What the AI does under the hood

Extraction runs on our backend with a multimodal model (Gemini 1.5 Pro)
trained to recognise Italian rainfall tables:

- identifies **Italian headers** (e.g. "Massimi annuali di pioggia di durata 1h, 3h…");
- distinguishes **valid values** from footnotes, placeholders (`---`, `n/d`);
- recognises **metadata** even when it's mid-page text;
- normalises decimal separators and numbers.

Only the uploaded file is sent to the backend; **it is not stored or
indexed**. Cost: a few NX credits per operation (visible on the wallet
chip before launch).

## When verification matters

The AI has good accuracy but isn't infallible. Cases requiring inspection:

- **Multi-station tables**: the AI tries to identify the requested station,
  but on unstructured PDFs it may confuse rows.
- **Ambiguous decimals**: `34,8` (Italian) vs `34.8` (English) — the AI
  decides from context; check a few values.
- **Series with gaps**: some series mark gaps with `---`; verify they
  were skipped correctly.

Always confirm the preview before accepting.

## Manual alternative

If you prefer, you can:

- copy the annual-maxima column from Excel;
- paste directly into the single-duration box.

The simple parser accepts `.` and `,` as decimal separator, one value per line.
