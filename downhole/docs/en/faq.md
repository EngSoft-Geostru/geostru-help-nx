# FAQ

## Traces and formats

**Which trace files can I upload?**
SEG-2 (`.sg2`, `.seg2`, `.dat`) and text files with the traces in columns (`.txt`, `.csv`).
Each file up to 20 MB. See [Traces and time picking](tracce.md#uploading-the-files).

**My format is not among them. What do I do?**
Downhole NX does not read SEG-Y or the proprietary formats of acquisition instruments. Two
ways out: export the traces from the instrument software to SEG-2 or text, or read the times
elsewhere and enter them in the [Measurements](misure.md) tab. Processing starts from the
times: traces are not required.

**A SEG-2 file is rejected with “Unsupported SEG-2 data format”.**
The app reads SEG-2 samples as 16- and 32-bit integers and as 32- and 64-bit floating point.
The 20-bit floating-point encoding is not read: export the file in another encoding.

**The P-shot and S-shot files have a different number of channels.**
The app warns you and does not merge them: channels are read by number. Check **P-wave
channel** and **Channels per geophone**, or export the files again with the same number of
channels.

**I have a large survey. Are there limits?**
A project holds up to 600 files, 400 depth rows and 64 channels. Files are uploaded in
batches: if the server rejects an upload because it is too large, upload fewer files at a
time. In the `.dhnx` file traces fit up to 30 MB in all; beyond that the file carries the
references, and the traces are uploaded again on reopening. Always keep the original files.
See [Files](file.md#traces-in-the-file).

**I uploaded the files but the plot is empty.**
The depths are missing. Type those of the first two rows in the **Depths and files** card:
the others take the step.

**The depths assigned to the files are wrong.**
Grouping follows the order of the names. Check **S-wave shots** (1 or 2), correct the cells
by hand, or press **Group again** after changing the options.

**Can I trust the proposed times?**
As you would a first reading made by someone else: all of them must be looked at again on
the traces. On the sample survey the proposal on P waves is within about half a millisecond
of the manual pick; on S waves within a few milliseconds, with the largest deviations at the
shallowest depths. Start with the times marked “?”, but look at the others too. See
[Proposing the times](tracce.md#proposing-the-times).

**Why are so many S times doubtful?**
Because the shear wave arrives inside the tail of the P waves and its first arrival is less
sharp. The app marks a time as doubtful when it deviates from the trend of the neighbouring
depths, when it does not increase with depth or when the signal is weak: on S waves that
happens often. “Doubtful” does not mean wrong, it means to be looked at.

**How do I remove the “?” from a time I have checked?**
Pick it yourself: switch on **Tp** or **Ts** and click on the trace, even at the same point.

**Does having times or seismic layers proposed use credits?**
No, with the buttons in the tab it is free. If you ask the assistant, you pay for the
message.

## Measurements and calculation

**I only have S waves (or only P waves). Can I process the test?**
Yes. Leave at zero the times of the wave you do not have: zero means “not measured”. The
columns of that wave show “--”; with S waves alone you get V~s~, G and V~s,eq~, while ν,
E~d~, E and E~v~ also need V~p~.

**A time is missing at one depth.**
Leave it at zero. The two intervals touching that receiver stay “--” for that wave; in the
direct method the times at the layer bases are interpolated on the measured receivers.

**What does “--” mean?**
“Cannot be computed”, not zero: a time is missing, the corrected time does not increase
between two receivers, or V~p~ and V~s~ do not give a Poisson's ratio between 0 and 0.5.

**Where is the “Calculate” button?**
There is none. Processing updates at every change and is free.

**I move the seismic layers but V~s,eq~ does not change. Is that a bug?**
No. In the direct method the sum of the travel times through the layers is the corrected
S-wave time at depth H, wherever the bases are. In the interval method V~s,eq~ is computed
on the measurement intervals. It changes only if the test is shorter than H: there the last
layer is extended, and its velocity depends on the base just above it. See
[Processing](elaborazione.md#equivalent-velocity-vseq).

**Are the proposed seismic layers the stratigraphy of the site?**
No. They are the subdivision that best follows the corrected times, with bases on the
measurement depths. Use them as a starting point and move them where the borehole log and
your reading of the travel-time curve require. See
[Proposing the seismic layers](elaborazione.md#proposing-the-seismic-layers).

**I set 40 m as the final depth and the label still says “Vs,30”.**
With a final depth of 30 m or more the label is **Vs,30**, but the value is the one between
the two depths written in the note below the number. For V~s,30~ leave 0 and 30.

**The test stops at 20 m. Can I get V~s,30~?**
The app extends the last layer to 30 m and says so on screen and in the report. It is an
assumption: it is for you to judge whether the velocity of the last layer can be extended.

**Does the program tell me the subsoil category?**
No. V~s,eq~ is a number; the category takes the depth of the bedrock and is left to the
designer.

**Can I use the moduli for settlements?**
Not directly: they are dynamic, small-strain moduli.

**Is the unit weight measured or estimated?**
With the switch on it is estimated from a correlation with V~s~ and depth. If you have
measured values, switch it off and type γ in the table. See
[Measurements](misure.md#unit-weight-automatic-or-assigned).

## Desktop version

**I open the same desktop project and the numbers are different. Why?**
Downhole NX fixes some calculation defects of the desktop program. The differences are in
precise places: velocity of the last layer, γ and moduli of the direct method, V~s,eq~ of
the interval method and of tests shorter than H. Corrected times and values per interval
match. The full table, with reason and effect, is in
[Validation and differences from the desktop version](validazione.md#differences-from-the-desktop-program).

**Can I save to `.dwhx` to reopen in the desktop program?**
No. Downhole NX opens desktop files but saves only to `.dhnx`.

**After opening a `.dwhx` the traces are not there.**
The desktop project does not contain them. Upload the SEG-2 files again in the Traces tab.

## Session, files and credits

**I left the app open and now it says “The session has expired”.**
After 30 minutes of inactivity the project is no longer in memory. Nothing was written or
charged: reopen your `.dhnx`. Save often. See [Files](file.md#the-session).

**“The project was modified in the meantime”.**
The assistant or another browser tab changed the project. Reload the page: what you had on
screen was not saved.

**What uses credits?**
**Generate Word**, **Export DXF** and each message to the assistant. Everything else is
free.

**Was I charged for a failed operation?**
No. Credits are charged only when the operation succeeds.

**In which language is the report? Can I have it as a PDF?**
In the interface language: switch it before generating. The format is Word; you get the PDF
from your word processor.

**Does it work on a tablet or with Safari?**
The app is tested with Chromium-based desktop browsers and windows at least 900 px wide.
Touch dragging and Safari have not been tested.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Downhole%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/downhole/docs/en/faq.md).*
