---
title: AI assistant
---

# AI assistant

Loadcap NX integrates a context-aware **AI assistant**: it always knows the open
project (type, geometry, stratigraphy, combinations and results) and helps you in
three ways. Open it from the **AI assistant** button in the top bar.

## 1. Fill from a document

Instead of typing the stratigraphy and parameters by hand, **attach a document to
the chat** and ask to import it: the assistant extracts the data and fills the
form.

**Accepted formats**: geological or geotechnical report (`.pdf`, `.txt`), tables
(`.csv`, `.tsv`, `.xlsx`, `.xls`), penetration-test files (`.edp`, `.dprobe`),
projects (`.json`).

1. Attach the file (paperclip icon) and type *"fill the form from this document"*.
2. The assistant extracts what it finds — even just the **stratigraphy**, if the
   document has no foundation geometry.
3. The form updates and the assistant summarises in one line what it filled in.
4. **Always review** the imported values before computing.

For **raw penetration data** (blow count, resistance) the assistant builds a
**draft** stratigraphy (segmentation by refusal trend, φ′ from Peck's correlation,
typical γ and c′), stating it as a draft to verify.

!!! warning "Save before importing"
    Import **overwrites** the open project. If you have unsaved changes, Loadcap
    flags them with a **dot on the File button** and asks for confirmation. Use
    **File → Save** to keep the current work.

!!! tip "From test data"
    For a rigorous stratigraphy from in-situ tests, prefer the export from
    **Dynamic Probing NX** over the draft from raw data.

## 2. Geotechnical review

An automatic consistency check of the project, **read-only**: the review does not
change anything, it only produces a report. Start it from the **Geotechnical
review** action in the assistant menu, or type *"check the parameters"*. The
assistant examines:

- **parameter plausibility** by soil type (φ′, c′, c_u, γ, E consistent with
  N_SPT);
- **analysis consistency** drained/undrained, water table, embedment height;
- **geometry and loads** (D/B, presence of ULS and SLS combinations, consistency
  with the sign convention);
- **results** (governing method, adequacy of FS, order of magnitude of the
  settlements).

The report is a **checklist** with OK / attention / problem markers and an overall
verdict, referred to the real numbers of the project.

## 3. Technical chat

Beyond the two functions above, the assistant answers questions about the project:
it explains why a method governs, compares the approaches, interprets bearing
capacity and settlements with an **engineer's opinion**, and can **open a support
ticket** when needed.

The assistant **does not run the calculation** (that is the **Compute** button,
which consumes credits) and does not invent numbers: it cites the project's values
or states that a datum is missing.

!!! note "Designer's responsibility"
    The AI assistant is a support tool: always verify the imported data and the
    review report. Responsibility for the calculation remains with the designer.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/en/assistente-ai.md).*
