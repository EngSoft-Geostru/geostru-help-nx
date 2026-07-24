---
title: Domande frequenti — Slope NX
---

# Domande frequenti

## Il calcolo dice "nessuna superficie valida". Perché?

Le cause tipiche, spiegate dal riquadro azionabile che compare:

- **Maglia dei centri fuori posizione** rispetto al pendio → usa **Auto-posiziona maglia**.
- **Analisi non drenata senza c<sub>u</sub>**: se i materiali non hanno coesione non drenata, la resistenza è nulla → passa a **Drenata** o imposta c<sub>u</sub>.
- **Profilo troppo corto**: le superfici emergono oltre l'estremo → **Estendi profilo**.

## Che differenza c'è tra Drenata e Non drenata?

**Drenata** (tensioni efficaci) usa c′ e φ′ e sottrae la pressione neutra alla base: è la condizione di **lungo termine**. **Non drenata** (tensioni totali) usa c<sub>u</sub> con φ = 0 e non sottrae u: è la condizione di **breve termine** nei terreni fini. I nuovi progetti partono in Drenata.

## Quale metodo scelgo?

Per superfici **circolari** parti da **Bishop semplificato**. Per superfici **generiche** (non circolari) usa **Janbu**, **Spencer** o **Morgenstern-Price**. **Fellenius** è il più conservativo, utile come riferimento.

## Perché l'FS deve essere ≥ 1 e non ≥ 1,3?

Dipende dal metodo di verifica. Con i **coefficienti parziali** (NTC/EC agli stati limite) il margine è già in γ<sub>R</sub>, quindi la verifica è soddisfatta per **FS ≥ 1,0**. Con i **parametri caratteristici** (metodo tradizionale) i valori di riferimento sono FS ≈ 1,3÷1,5 (statico) e 1,1÷1,3 (sismico). Vedi **[Normativa](normativa.md)**.

## Come tratta il calcolo il rinterro dietro il muro?

Con il **raccordo** attivo, il rinterro è modellato come **terreno vero**: il suo peso e la sua resistenza entrano nel calcolo, con il materiale che assegni con un doppio-click sul cuneo. Se invece hai disegnato il profilo già alla quota finita, lascia il raccordo OFF. Vedi **[Opere di sostegno](muri.md)**.

## Posso ricostruire un modello da una vecchia relazione?

Sì. Carica il **PDF** della relazione (o una descrizione a parole) nell'assistente **AI**: ricostruisce profilo, strati, falda e opere in un'anteprima da rivedere prima di applicare.

## Il progetto è al sicuro se chiudo il browser?

Slope NX salva una **bozza automatica** nel browser. Per non perdere il lavoro salva il file **`.slope`** (o sul cloud con l'account). All'apertura di un esempio o di un nuovo file, l'app **avvisa** se c'è un progetto in corso.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Slope%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/slope/docs/it/faq.md).*
