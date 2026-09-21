# GeoDropbox

A dossier is a report on a precise place, with a name and coordinates. On GeoDropbox it becomes
a **project** with the same name, the **pin on the site** and the files inside — and the dossier
list shows at a glance which ones are linked to a project, one click away.

## Sending a dossier

With the dossier ready, next to *Download Word* you find **Send to GeoDropbox** (in *My dossiers*
it is the cloud with the «+»).

- No project near the site: the project is **created** with the assignment's name (or
  «Municipality — Geological report» when the assignment is empty), the pin on the coordinates,
  municipality, province, region and address filled in, the profile as category, tags `atlante`
  + profile.
- Projects already **within 500 m** of the site — the same job, maybe opened from another app —
  are offered with their distance: join one of them or open a new one.
- Once sent, the result line carries **Open the project**; the button becomes **Update on
  GeoDropbox** and uploads the files again to the same project, never a duplicate.

In the dossier list the **GeoDropbox** column shows the green cloud **Open** on linked dossiers
(project name and date in the tooltip).

## What lands in the project

| Where | File | Purpose |
|---|---|---|
| root | **PDF** | the report to read: previewed by GeoDropbox and analysed by its AI |
| root | **DOCX** | the same report, to edit in Word |
| folder **Atlante NX** | **`.atlante`** | the complete dossier (evidence, plates, text, surveys), to reopen it in Atlante |
| folder **Atlante NX** | `README - Atlante NX.txt` | explains the `.atlante` file to whoever opens the folder without knowing Atlante |

The PDF can also be downloaded from Atlante (*Download PDF*, next to *Download Word*).

## Reopening a dossier from GeoDropbox

The `.atlante` file has one purpose: **reopening the dossier in Atlante** — from another
computer, or from **another account** of the office the GeoDropbox project is shared with.
PDF and Word give the finished document; the `.atlante` gives the living dossier.

1. In Atlante press **GeoDropbox** (top right), then **Open**.
2. Pick the project and, in the *Atlante NX* folder, the `.atlante` file.
3. The dossier is imported as a **new dossier** in your list, with evidence and plates: rerun
   the sources, generate the text, add your surveys, download Word and PDF.

!!! warning "Do not rename or edit the `.atlante`"
    It is an Atlante NX format, not a document. Read the PDF, edit the Word. After an *Update on
    GeoDropbox* the folder holds a new `.atlante` with the date in its name: the latest counts.

## Access to GeoDropbox

The same GeoStru account opens Atlante and GeoDropbox: every account has the **Free** plan
(5 projects, 1 GB) with no subscription. On geodropbox.ai, "Sign in with Geostru" logs you in
with the account you use for Atlante.
