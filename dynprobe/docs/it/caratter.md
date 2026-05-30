# Valori caratteristici EC7 / NTC §6.2.2

## Perché i valori caratteristici

La normativa geotecnica europea (EC7 §2.4.5.2) e italiana (NTC 2018 §6.2.2) richiede di progettare sui **valori caratteristici** dei parametri, non sui valori medi. Il valore caratteristico tiene conto della variabilità naturale del terreno e dell'incertezza di campionamento.

## Come funziona il calcolo

Dynamic Probing NX stima il valore caratteristico di N_SPT per ogni strato applicando metodi statistici sulla serie di valori N raccolti nello strato. I metodi disponibili sono:

| Metodo | Descrizione |
|---|---|
| **Normale** | Stima basata su media e deviazione standard con distribuzione gaussiana |
| **Lognormale** | Utile quando N_SPT ha distribuzione asimmetrica (frequente con valori bassi) |
| **Student-t** | Corretto per campioni piccoli (n < 30) — tiene conto dell'incertezza sulla media |

Il livello di fiducia applicato corrisponde a quello indicato da EC7 per il valore caratteristico inferiore (5° percentile lato conservativo).

## Come si usa

Nella tab **Stima parametri** dell'Editor:

1. Seleziona il metodo statistico (Normale / Lognormale / Student-t).
2. Per ogni strato vengono mostrate: media, deviazione standard, n° campioni e valore caratteristico calcolato.
3. Il valore caratteristico di N_SPT viene propagato alle correlazioni per ottenere i valori caratteristici di Cu, φ, Mo, Ey, ecc.

!!! info "Campioni minimi"
    Con meno di 3 letture per strato il calcolo statistico ha bassa significatività. L'app segnala i casi con n < 3 con un avviso — in questi casi è preferibile usare un approccio ingegneristico conservativo (es. minimo dei valori osservati).

## Valori caratteristici nel report

La relazione Word esportata include la tabella dei valori caratteristici con il metodo usato, la dimensione del campione e il valore risultante — pronta per essere allegata alla relazione geotecnica.
