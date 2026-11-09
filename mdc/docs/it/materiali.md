# Materiali

Il passo 7 ha un riquadro per i **materiali del muro**, uno per i **materiali dei pali** (solo con la fondazione su pali), uno per
**coefficienti e copriferri** e, per il muro a gravità, uno per il **muro a gravità**. Resistenze e moduli sono in **MPa**, i pesi in
**kN/m³**, i copriferri in **metri**.

## Calcestruzzo e acciaio

**Classe** sceglie dall'archivio e compila le proprietà; i valori restano modificabili.

| Materiale | Classi | Campi |
|---|---|---|
| Calcestruzzo | C20/25, C25/30, C28/35, C30/37, C32/40, C35/45, C40/50, C45/55, C50/60 | Resistenza cubica R~ck~, Resistenza cilindrica f~ck~, Modulo elastico E~c~, Resistenza di calcolo f~cd~, Resistenza a trazione media f~ctm~, Resistenza a trazione di calcolo f~ctd~ (MPa); Peso dell'unità di volume (kN/m³) |
| Acciaio | B450C, B450A | Snervamento f~yk~, Snervamento di calcolo f~yd~, Modulo elastico E~s~ (MPa); Deformazione ultima ε~uk~ |

Le proprietà dell'archivio seguono le NTC 2018 (f~cd~ = 0,85·f~ck~/1,5, f~ctd~ = 0,7·f~ctm~/1,5). Un progetto aperto dal desktop porta
le classi del suo archivio («dal file»). Muro e pali possono avere materiali diversi.

## Coefficienti e copriferri

| Campo | Unità | Note |
|---|---|---|
| Peso del muro | kN/m³ | usato quando la classe del calcestruzzo non dà il peso |
| γ~c~ del calcestruzzo | | 1,5 di norma |
| γ~s~ dell'acciaio | | 1,15 di norma |
| Condizioni ambientali | | Ordinarie, Aggressive, Molto aggressive |
| Copriferri: Elevazione, Fondazione, Dente, Ferri di ripresa | m | entrano nell'altezza utile delle sezioni e nell'apertura delle fessure |

Le condizioni ambientali (NTC 2018 §4.1.2.2.4) decidono i limiti di apertura delle fessure nelle combinazioni di esercizio.

## Muro a gravità

| Campo | Unità |
|---|---|
| Resistenza a compressione di calcolo | MPa |
| Resistenza a trazione di calcolo | MPa |
| Peso dell'unità di volume | kN/m³ |
| Diametro dei ferri di ripresa | mm |

Le tensioni nel corpo del muro si confrontano con queste resistenze: vedi [Sezioni, armature e distinta](armature.md#muro-a-gravita).

## Armature di progetto

Diametri e numero di barre con cui il programma progetta i ferri stanno nel passo [Armature](armature.md#armature-di-progetto).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MDC%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mdc/docs/it/materiali.md).*
