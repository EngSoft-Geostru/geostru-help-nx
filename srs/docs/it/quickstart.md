---
title: Guida rapida (5 minuti)
---

# Guida rapida (5 minuti)

In cinque minuti passi dall'apertura dell'app alla lettura delle verifiche di
un ancoraggio chiodato. Apri **[nx.geostru.ai/srs](https://nx.geostru.ai/srs/)**
e segui i passi.

!!! tip "Parti da un esempio"
    Il modo più veloce per prendere confidenza è caricare un **progetto di
    esempio**: menu **File → Apri** e seleziona uno dei file `.srs` descritti
    in [Progetti di esempio](esempi.md). La form si compila da sola e puoi
    calcolare subito.

## 1. Pendio

Nella sidebar **PROGETTO**, sezione **Pendio**, inserisci l'inclinazione del
versante **α**, lo spessore della coltre **S**, il peso di volume **γ_col**,
l'angolo d'attrito **φ_col**, la coesione drenata **c'_col** e lo spessore
adimensionalizzato del moto di filtrazione **m** (0 = falda assente, 1 = falda
a piano campagna). Vedi [Pendio e substrato](pendio.md).

## 2. Substrato

In **Substrato** scegli **Terreno** o **Roccia** e imposta la tensione di
aderenza (**ad_soil** o **ad_rock**): un menu a tendina propone valori tipici
per litologia, oppure inseriscila manualmente. Per il terreno aggiungi anche
il coefficiente di modalità di iniezione **α_iniez**. Vedi
[Pendio e substrato](pendio.md#substrato).

## 3. Coefficiente sismico (facoltativo)

Se il sito è sismico, in **Parametri Sismici** imposta il coefficiente
sismico orizzontale **K_h**. Lascialo a 0 per una verifica solo statica. Vedi
[Azione sismica](sismica.md).

## 4. Calcola FS₀

In **Parametri di Progetto**, passo 1, premi **Calcola FS₀**: SRS calcola il
coefficiente di sicurezza del pendio **prima** dell'intervento, a partire solo
dai dati di pendio e substrato inseriti finora.

## 5. Imposta FS_des

Al passo 2 inserisci il coefficiente di sicurezza di progetto **FS_des** che
vuoi raggiungere con l'intervento (deve essere maggiore di FS₀).

## 6. Chiodo, maglia e rete

In **Ancoraggi** scegli un chiodo dal **catalogo** (GEWI o TITAN) o inserisci
i parametri manualmente: diametro barra **φ_b**, tensione di snervamento
**f_yk**, diametro di perforazione **D_f**, lunghezza **L_a**, inclinazione
**β**, interassi **i_x**/**i_y**, resistenza della malta **R_ck** e
coefficiente di aderenza **η₁**. In **Rete** imposta maglia, filo e le
resistenze a trazione e punzonamento. Vedi [Chiodi e ancoraggi](chiodi.md) e
[Rete di facciata](rete.md).

## 7. Calcola

Al passo 3 premi **Avvia** (o il pulsante **Calcola** in alto). Il calcolo
consuma crediti NX.

## 8. Leggi le verifiche

La tab **Verifiche** si apre automaticamente e mostra FS₀, FS_des, l'incremento
**ΔFS** ottenuto e l'esito delle sei verifiche R.2–R.7 (trazione barra, taglio
barra, sfilamento barra/malta, sfilamento del bulbo, punzonamento e trazione
della rete), oltre al numero di ancoraggi necessari ogni 100 m² di rete. Vedi
[Verifiche](verifiche.md).

![Esito delle verifiche](img/srs-verifiche.png)

## 9. Relazione

Dal menu **Relazione** in alto esporti il documento di calcolo in **Word**,
**DOC** o **PDF**; dal menu **File** salvi il progetto (`.srs`). Vedi
[Relazione ed esportazioni](relazione.md).

!!! tip "L'assistente AI"
    Il pulsante **Assistente** in alto imposta un intero progetto da una
    descrizione a parole, recupera il coefficiente sismico per una località e
    spiega i risultati delle verifiche. Vedi [Assistente AI](assistente-ai.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20SRS%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/it/quickstart.md).*
