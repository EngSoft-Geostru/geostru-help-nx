# Files, desktop projects and GeoDropbox

## Saving

The project lives in a server session and **disappears after 30 minutes of inactivity or on a restart**. Save it from the
**File** menu with **Salva (Save)** or **Salva con nome (Save as)**: you get a `.maswnx` file with data, picks, layers, solutions and
traces. Above 30 MB traces stay as references, and saving says so.

## Opening

**Apri (Open)** accepts `.maswnx` and `.mswx`.

`.mswx` is the Easy-MASW desktop format: traces, spectrum, picks, inversion and category come into the app. On the desktop,
cropping and filtering change the samples, so samples in a `.mswx` are already processed: they are imported as they are and
the crop restarts from zero, as the app warns.

The old binary `.msw` cannot be opened: save it as `.mswx` from the desktop.

## GeoDropbox

With the **GeoDropbox** button you save the `.maswnx` to one of your projects and open a `.maswnx` or `.mswx` from there.

## Limits

Files up to 64 MB at a time. More traces, samples or map cells than the server can process are refused with a message.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MASW%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/en/file.md).*
