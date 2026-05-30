# Stratigrafia interpretata

## Cos'è

La stratigrafia interpretata è il modello del sottosuolo che ricavi dalle letture della prova. Definisci un certo numero di strati — ognuno con una profondità inferiore, un tipo di terreno e i pesi di volume γ e γ_sat — e il software calcola per ciascuno il valore di N_SPT rappresentativo, da cui derivano poi le correlazioni geotecniche.

## Come si inserisce

Nel tab **Stratigrafia interpretata** dell'Editor:

1. Il primo strato parte da 0 m. Imposta la sua profondità inferiore (es. 2,50 m).
2. Clicca **+ Aggiungi strato** per creare lo strato successivo.
3. Per ogni strato:
   - Imposta la **profondità inferiore** (m da p.c.).
   - Scegli il **tipo di terreno**: `COES` (coesivo), `INCO` (incoerente) o entrambi se misto — il tipo determina quali correlazioni vengono applicate.
   - Inserisci **γ** (peso di volume secco o naturale) e **γ_sat** (peso saturo) in kN/m³.
   - Se vuoi, inserisci **clay (%)** e la **descrizione** litologica.

## I 7 metodi di aggregazione N_SPT

Per ogni strato, le letture che cadono nel suo range di profondità vengono aggregate con il metodo scelto dall'utente. I metodi disponibili sono:

| Metodo | Quando usarlo |
|---|---|
| **Media** | Terreno omogeneo, variabilità contenuta |
| **Minimo** | Approccio conservativo — si usa il valore peggiore |
| **Massimo** | Stima dell'upper bound (es. per portanza su punta) |
| **Media − 1σ** | Approccio statistico conservativo |
| **Media + 1σ** | Approccio statistico non conservativo |
| **RNC** (distribuzione normale) | Valore caratteristico in probabilità secondo EC7 §2.4.5.2 |
| **RC** (distribuzione log-normale) | Come RNC ma con distribuzione log-normale — preferibile per N_SPT con valori bassi |

Il metodo si imposta nell'header della colonna N_SPT della tabella stratigrafia, ed è valido per tutti gli strati contemporaneamente.

!!! info "Qual è il metodo giusto?"
    La norma EC7 (e NTC §6.2.2) indica di usare il **valore caratteristico** del parametro, definito come il valore con probabilità del 5 % di essere inferiore. I metodi RNC e RC si avvicinano a questa definizione statistica. Per campioni piccoli (< 6 letture per strato) la media resta il riferimento più robusto.

## Correlazione N_DPM → N_SPT

Per le prove continue, N_SPT di strato si ottiene da N_DPM applicando il coefficiente β (vedi [Strumenti →](strumenti.md)). Il prodotto N_DPM × β è il N_SPT equivalente per ogni lettura; l'aggregazione viene poi applicata su questi valori equivalenti.

## Badge Σ strati / prova

In basso nella schermata stratigrafia compare il badge:

```
Σ strati  X,XX m  /  prova  Y,YY m
```

- **Verde** (✓): la somma delle profondità degli strati coincide con la profondità della prova — la stratigrafia copre l'intera prova senza vuoti.
- **Giallo** (⚠): scarto tra Σ strati e profondità prova — controlla che l'ultimo strato arrivi a fine prova.
