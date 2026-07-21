# Aree e metodi di calcolo

## Superfici scolanti

Ogni riga della tabella è una superficie omogenea per uso e permeabilità. Servono
descrizione, tipo, area in m² e coefficiente di deflusso φ post operam.

![Definizione delle aree](img/02-aree-metodi.png)

Il tipo area (impermeabile, semi-impermeabile, permeabile) è un'etichetta
descrittiva che suggerisce l'ordine di grandezza di φ; il valore che entra nel
calcolo è sempre quello che scrivi tu.

HID calcola il **coefficiente di deflusso ponderale**:

$$\varphi_{pond} = \frac{\sum \varphi_i \cdot S_i}{\sum S_i}$$

e la **superficie ponderata** $S_{pond} = S_{tot} \cdot \varphi_{pond}$, che è la
superficie impermeabile equivalente.

## I metodi di dimensionamento

HID distingue i metodi **universali**, validi ovunque, da quelli **di
giurisdizione**, che esistono solo dove la normativa li prescrive.

### Requisiti minimi

Volume specifico per ettaro imposto dalla normativa in funzione dell'ambito di
criticità. In Lombardia vale 800, 500 o 400 m³/ha secondo l'ambito A, B o C e la
versione regolamentare. Dove la normativa non lo prescrive, il volume minimo lo
imponi tu.

### Metodo delle sole piogge

Bilancia il volume affluito con quello scaricato a portata costante, cercando la
durata che massimizza l'invaso. È il metodo più diffuso per le verifiche
speditive.

!!! note "Durate inferiori all'ora"
    Quando la durata critica scende sotto l'ora, HID usa l'esponente n₁ della
    curva, come previsto. Non arrotonda la durata a un'ora: farlo sottostima il
    volume, ed è un errore che abbiamo corretto validando l'app contro la
    versione precedente.

### Metodo della corrivazione

Introduce il tempo di corrivazione del bacino, quindi tiene conto della forma
dell'idrogramma. Restituisce durata critica e volume.

### Metodo diretto

Confronta i volumi di invaso specifici ante e post operam attraverso il rapporto
dei coefficienti di deflusso. In Emilia-Romagna e Marche la normativa prescrive
una variante a coefficienti fissi, che HID espone come metodo separato,
**Metodo diretto regionale**, visibile solo in quelle regioni.

### Procedura dettagliata

È la simulazione completa: ietogramma di progetto, depurazione, idrogramma di
piena e laminazione dell'invaso passo per passo. È il metodo più oneroso e il
più difendibile.

## Come viene scelto il volume

HID calcola tutti i metodi selezionati e adotta come volume ammissibile il
**massimo** fra i risultati. Il metodo proposto dalla normativa è indicato sotto
le caselle, ma non limita quali metodi puoi calcolare.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
