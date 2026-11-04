# FAQ

**Why is the outcome different from the one of the desktop program?**
The desktop read condition 1 as a percentage of points above the code spectrum; the Ordinance says «exceeds pointwise by more than 30 %». NX
follows the text. See [Validation and limits](validazione.md).

**Can I use a return period other than 475 years?**
No: the Ordinance prescribes the comparison at 475 years. Nominal life and use class of the structure are for information only.

**My file does not import.**
Check that it has two numeric columns (period and acceleration) and increasing periods. The message tells you at which line it stops. Headers
are skipped automatically.

**The spectrum starts at 0.02 s.**
Appendix 1 requires Se(0.01 s): without that value the regularisation cannot be done.

**What does «Comparison not applicable» mean?**
That 2·T~max~ exceeds 1.1 s: according to note 1 of the Ordinance the comparison is not made.

**The parameters service does not respond.**
Import a GeoStru PS report or enter the SLV row by hand (T~R~ = 475 years).

**How much does it cost?**
Everything is free except the Word report and the messages to the assistant. A failed operation is not charged.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20RSL%20III%20A%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rsl3a/docs/en/faq.md).*
