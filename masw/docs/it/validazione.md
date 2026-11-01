# Validazione e limiti

Il punto 10.2 delle NTC 2018 chiede al progettista di valutare l'affidabilità del codice. Questa pagina riassume il materiale;
è una **validazione**, non una certificazione.

## Campi di impiego

Prove MASW **attive**: sorgente in linea con uno stendimento di geofoni a passo costante. Modello 1D a strati orizzontali, fino a
5 modi.

## Limiti da valutare

- Il modello è **1D**: variazioni laterali, topografia e strati inclinati non sono rappresentati.
- L'inversione è **casuale e non unica**: profili diversi riproducono la stessa curva.
- La **profondità di indagine** è dell'ordine di λ/2 della lunghezza d'onda più lunga letta con affidabilità. Sotto, il profilo è
  estrapolato: il semispazio e una V~s,eq~ su 30 m richiedono energia alle basse frequenze.
- Il **picking** è una scelta dell'operatore e il risultato ne dipende.
- ρ e ν sono assunti; la curva è poco sensibile a entrambi.
- G, E~d~, K, E sono **moduli dinamici**; NSPT e Q~c~ sono correlazioni empiriche indicative.
- Non sono trattati: ReMi e vista f-k del desktop, sorgenti passive, onde di Love.

## Casi di prova

**Forme chiuse.** Fra gli altri: onda sintetica a 200 m/s, V~s,eq~ di 300 m/s con 10 m a 200 e 20 m a 400 m/s, substrato a 20 m
(266,67 m/s, categoria E), risonanza a V~s~/4H.

**Confronto con Easy-MASW desktop su dieci progetti.** La mappa f-v coincide entro 10⁻⁹, misfit ed errore % del modello del desktop
entro 10⁻¹², le curve teoriche entro 10⁻⁹ relativo, una corsa a seme fisso è identica. Questo dimostra che il porting non ha cambiato il
calcolo, non che il metodo sia corretto: per quello valgono le forme chiuse e la letteratura.

## Differenze dal desktop

| Desktop | MASW NX |
|---|---|
| Quote sommate in precisione singola: in un esempio H = 29,999998 m e categoria E | somme in doppia precisione: H = 30 m e categoria C |
| Campioni SEG-Y IBM letti come IEEE | conversione corretta |
| Quote dei sei strati di default incoerenti con gli spessori | quote cumulate |
| V~s,eq~ calcolata sul modello salvato | calcolata sulla soluzione scelta a video |

Restano come nel desktop: l'etichetta della colonna di frequenza, sfasata di meno di un df, e il valore v/f non dimezzato nella stima
iniziale, che tocca solo il punto di partenza.

Il documento completo è disponibile su richiesta.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MASW%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/it/validazione.md).*
