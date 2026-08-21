# FAQ

**Are the reinforcement elevations measured from the top or from the bottom?**
From the **crest**: z = 0 at the top, level 1 is the highest one. The actions therefore
grow with z, going down.

**Why don't the factors in the card change when I switch the seismic action on?**
That card is the **static** combination; the seismic one is generated separately with its
own factors (the read-only "Seismic" column). See [Combinations](combinazioni.md).

**Why can't the last reinforcement fall exactly at the base?**
At z = H the Rankine length is zero: change the spacing or the height slightly.

**Does the facing inclination enter the checks?**
No: as in the GSRD desktop program, α defines the shape of the section; the thrust is
evaluated on the equivalent vertical wall (conservative with battered facings). The
tieback/compound surfaces cover the reinforced-soil behaviour.

**What does "design envelope" mean in the Reinforcements tab?**
Per level: the combination with the lowest FS and the largest total length across the
combinations — the length to build.

**The figures don't show up in the report.**
They are captured from the page: run the calculation and open the 2D section / 3D /
Stability tabs before generating the document.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MRE%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mre/docs/en/faq.md).*
