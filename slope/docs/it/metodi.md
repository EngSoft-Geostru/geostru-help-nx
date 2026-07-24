---
title: Metodi di calcolo (LEM) — Slope NX
---

# Metodi di calcolo (LEM)

Slope NX usa il **metodo dell'equilibrio limite** (Limit Equilibrium Method): la massa potenzialmente instabile è divisa in **conci** verticali e si cerca il **fattore di sicurezza** (FS) come rapporto tra la resistenza al taglio disponibile e quella mobilitata lungo la superficie di scorrimento.

$$ FS = \frac{\tau_{f}}{\tau} = \frac{c' + (\sigma - u)\tan\varphi'}{\tau_{mob}} $$

## I cinque metodi

| Metodo | Equilibrio | Forze tra conci | Superfici |
|---|---|---|---|
| **Fellenius** (ordinario) | Momenti | Trascurate | Circolari |
| **Bishop semplificato** | Momenti | Solo orizzontali | Circolari |
| **Janbu** | Forze | Solo orizzontali | Qualsiasi |
| **Spencer** | Forze + momenti | Inclinazione costante | Qualsiasi |
| **Morgenstern-Price** (GLE) | Forze + momenti | Funzione f(x) | Qualsiasi |

- **Fellenius** è il più conservativo (trascura le forze tra conci): utile come stima rapida e di riferimento normativo.
- **Bishop semplificato** è lo standard per le superfici **circolari**: preciso e stabile, valido quando la base non assume il braccio = R.
- **Janbu, Spencer, Morgenstern-Price** soddisfano più equazioni di equilibrio e valgono anche per superfici **generiche** (non circolari). Bishop e Fellenius sono ammessi solo per i cerchi.

!!! note "Condizione di analisi"
    In **drenata** (tensioni efficaci) la resistenza usa c′ e φ′ e alla base si sottrae la pressione neutra u. In **non drenata** (tensioni totali) la resistenza è c<sub>u</sub> con φ = 0 e **non** si sottrae u (c<sub>u</sub> la incorpora già). Se scegli non drenata assicurati che i materiali abbiano c<sub>u</sub> > 0.

## Forma della superficie

- **Circolari** — la ricerca esamina i cerchi con centro nei nodi della **maglia dei centri**; per ogni centro si provano più raggi. **Auto-posiziona maglia** colloca la maglia sopra la zona critica del pendio.
- **Generica** — superficie di forma qualsiasi definita per **punti**, oppure trovata da una **ricerca globale** (algoritmo evolutivo) che esplora tutto il dominio.

## Superfici ammissibili

Una superficie è scartata se non è cinematicamente valida: se **emerge sopra il profilo** (dividerebbe la massa in due), se **attraversa un'opera di sostegno** o se scende **sotto il bedrock**. Se la ricerca non trova nulla, il riquadro azionabile ne spiega il motivo.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Slope%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/slope/docs/it/metodi.md).*
