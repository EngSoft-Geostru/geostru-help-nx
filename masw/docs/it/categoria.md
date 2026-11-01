# Categoria del suolo

La scheda lavora sulla soluzione scelta nell'[Inversione](inversione.md).

## Vs,eq e categoria

Scegli **NTC 2018** o **NTC 2008** e indica la **Profondità piano di posa**, misurata dal piano campagna.

- **NTC 2018**: V~s,eq~ = H / Σ(h~i~/V~s,i~). H è la profondità del substrato con V~s~ ≥ 800 m/s; se non c'è entro 30 m, H = 30.
- **NTC 2008**: V~s,30~ sui 30 m sotto il piano di posa. **Probabile suolo di tipo E** segnala la condizione che il dato
  di velocità da solo non può stabilire.

![Categoria e tabella delle categorie](img/06-categoria.png)

Se il valore cade esattamente su un bordo (100, 360 o 800 m/s), o il piano di posa è nel substrato oltre i 30 m, la tabella
di norma non assegna una categoria e l'app lo dice a parole invece di sceglierne una.

## Parametri per strato

Per ogni strato: G~0~, E~d~, K, E e ν. Sono **moduli dinamici a piccole deformazioni**: non vanno usati direttamente nel
calcolo dei cedimenti.

**NSPT** (Ohta e Goto) e **Q~c~** (Jamiolkowski) sono correlazioni empiriche invertite da V~s~: scegli composizione, fattore di età
e tipo di terreno. Oltre 100 colpi o 5000 kPa l'app scrive N/D. Il semispazio non ha queste stime.

## Funzione di trasferimento

Il grafico mostra la risposta 1D del profilo, con smorzamento dell'1 %, e la frequenza del massimo. Con lo smorzamento così
basso i picchi sono molto alti: è un'indicazione delle frequenze di risonanza, non un'amplificazione di progetto.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MASW%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/it/categoria.md).*
