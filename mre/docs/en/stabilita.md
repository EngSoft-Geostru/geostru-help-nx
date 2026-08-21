# Global, tieback and compound stability

## Global stability (Bishop)

Check with **simplified Bishop** on a circular surface, **A2+M2+R2** approach: reduced
parameters (γ~tanφ′~ = γ~c′~ = 1.25) and threshold **FS ≥ γ~R2~** (1.1 static · 1.2
seismic). The circle is automatic (it passes below the structure) or can be constrained
with the three downhill/uphill/base points; the reinforcements crossing the surface
contribute with the lesser of R~d~ and the pullout of the portion anchored beyond the circle.

![Result of global stability and of the internal tieback and compound checks](img/12-stabilita.png)

## Internal checks: tieback and compound

When the facing is battered the structure behaves as reinforced soil: besides global
stability, the program analyses a **fan of circles exiting on the facing** at the
reinforcement levels:

- **Tieback** — surface entirely inside the reinforced volume (entry on the crest);
- **Compound** — exit on the facing but entry beyond the block (it also cuts the retained
  soil).

For each family the program reports the **minimum FS** with the γ~R2~ comparison, the
reinforcements crossed and the critical circle, drawn dashed (purple for tieback, blue for
compound). The **Animate internal checks** button replays the fan of circles that were
tried; press it again to go back to the static drawing.

![Global critical circle in red, tieback in purple and compound in blue](img/13-stabilita-disegno.png)

!!! tip
    With a 90° facing the structure behaves as a wall and the external checks usually
    govern; as α decreases (85° and below) the internal checks become significant.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MRE%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mre/docs/en/stabilita.md).*
