# Files, desktop projects and GeoDropbox

## The `.rsl3anx` file

The project lives in a session on the server and expires after 30 minutes of inactivity: save it. **File → Save** (Ctrl+S) overwrites the open
file, **Save as** creates a new one. The file is JSON and contains only the input data: the results are recomputed when you open it.

## Desktop program projects

**File → Open** also accepts the `.rs3` and `.rs3a` projects of RSL III A desktop. The app reads spectrum, parameters, categories, T~min~ and
T~max~ and **recomputes** everything according to the text of the Ordinance. If the file was saved with different settings (η other than 1, limit
state other than SLV, vertical spectrum), a warning tells you. The results saved in the file are not used: they may be outdated, and the
desktop read condition 1 in a different way (see [Validation and limits](validazione.md)).

## GeoDropbox

The **GeoDropbox** button saves the project into a GeoDropbox project, or opens a `.rsl3anx` (or a `.rs3`) saved there.

## Example

**File → Example** loads San Severino Marche, microzone 13, with the parameters of the GeoStru PS report.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20RSL%20III%20A%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rsl3a/docs/en/file.md).*
