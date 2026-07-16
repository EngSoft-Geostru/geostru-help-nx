---
title: Progetti di esempio
---

# Progetti di esempio

SRS NX include due progetti di esempio pronti all'uso, uno per substrato in
**terreno** e uno in **roccia**. In entrambi il pendio è instabile allo stato
attuale (FS₀ = 0,5) e l'intervento lo porta a un coefficiente di sicurezza di
progetto FS_des = 1,3: rappresentano quindi un caso reale in cui la
chiodatura è necessaria, non solo un caso limite.

| Esempio | Substrato | Contenuto |
|---|---|---|
| **Esempio terreno** | Terreno (ad_soil = 0,3 MPa) | Pendio a 35°, coltre 1,6 m, chiodo GEWI Ø25, malta R_ck 30 |
| **Esempio roccia** | Roccia (ad_rock = 1,0 MPa) | Stessa geometria di pendio e stesso chiodo, substrato roccioso |

## Come usarli

1. Vai su **File → Apri** nella toolbar.
2. Scarica (o seleziona, se già presente sul disco) il file `.srs`
   dell'esempio che ti interessa.
3. La form si compila automaticamente.
4. Premi **Calcola** per rieseguire il calcolo e confrontare i risultati.

!!! tip "Confronta terreno e roccia"
    I due esempi condividono la stessa geometria di pendio, lo stesso chiodo
    e lo stesso interasse: cambia solo il substrato. Sono un buon punto di
    partenza per capire quanto la tensione di aderenza substrato-malta (I.8
    o I.10) influenzi la verifica R.5 di sfilamento del bulbo.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20SRS%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/it/esempi.md).*
