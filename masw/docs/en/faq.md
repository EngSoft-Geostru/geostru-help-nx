# FAQ

## My project has disappeared

The project lives in a session and expires after 30 minutes of inactivity or on a restart. Save the `.maswnx` often.

## Can I open desktop projects?

Yes, `.mswx` files. Binary `.msw` files must first be saved as `.mswx` from the desktop.

## Why is f max refused?

It must stay below the Nyquist frequency, 1/(2·dt), which the app shows next to **Calcola**.

## Two inversions give different results. Is it an error?

No: the search starts from random values. Compare the solutions: if very different profiles have a similar misfit, the data cannot
tell them apart.

## The category differs from the desktop

On projects with layers reaching 30 m you may get C where the desktop gave E: it is a declared correction, see
[Validation](validazione.md). Also check the chosen solution.

## The report is not generated

Data changed after the inversion: run it again.

## Was I charged twice for the inversion?

An identical run on identical data is not charged again. A run after changing data, iterations or layers is a new run.

## How deep can I go?

About λ/2 of the longest wavelength reliably read: a short spread or a light source will not reach 30 m.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MASW%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/en/faq.md).*
