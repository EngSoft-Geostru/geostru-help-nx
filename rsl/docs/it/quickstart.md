# Quickstart — il tuo primo calcolo in 5 minuti

In 5 minuti vedi RSL III al lavoro su una colonna stratigrafica di esempio.

## 1. Apri l'app

Vai su [`nx.geostru.ai/rsl/`](https://nx.geostru.ai/rsl/).

## 2. Carica un esempio

Toolbar in alto → **Esempi** → scegli un caso pronto (es. *"Sabbia satura su
bedrock — Centro Italia M=6.0"*).

L'esempio popola:

- **Stratigrafia**: 4-6 strati con Vs, γ, curve G/Gmax e ξ realistiche
- **Accelerogramma di input**: registrazione sismica reale (es. da ITACA)
- **Bedrock di riferimento** (Vs > 800 m/s) come base della colonna

## 3. Esegui il calcolo

Premi **Esegui calcolo** in alto. RSL III:

1. Discretizza la colonna in sotto-strati (passo automatico in base a Vs e f_max)
2. Inizializza G = G_max e ξ = ξ_min per ogni strato
3. Calcola la **funzione di trasferimento** dalla bedrock alla superficie
   (metodo dei coefficienti di riflessione/trasmissione, dominio frequenziale)
4. Stima γ_max in ogni strato; aggiorna G e ξ leggendo le curve di degradazione
5. **Itera** finché γ_eff cambia meno della tolleranza (~0.5%) — tipico 4-8 iterazioni

Tempo: 1-3 secondi per una colonna di 20-50 m.

## 4. Esamina i risultati

I principali output che vedi:

### Spettro di risposta in superficie

Il **PSA** (Pseudo Spectral Acceleration) confrontato con lo spettro NTC di
riferimento per il sito. Le aree dove il PSA RSL **supera** quello NTC sono
zone di **amplificazione locale** che il sito impone all'edificato.

### Profili γ_max, a_max, σ_max

Per ogni profondità lungo la colonna, mostra:

- **γ_max** (deformazione tagliante massima, in %) — strati con γ > 0.1% sono in
  campo non lineare significativo
- **a_max** (accelerazione di picco) — l'amplificazione dalla bedrock alla
  superficie
- **σ_max** (taglio massimo) — utile per verifiche di liquefazione e stabilità

### Fattori di amplificazione ICMS

I **FA** (factor di amplificazione, brevi periodi 0.1-0.5 s), **FH** (alti
periodi 0.4-0.8 s) e **FT** (tutti periodi) — sono i tre indicatori richiesti
dalla microzonazione sismica di Livello 3 italiana (ICMS 2008/2018).

[Approfondisci i fattori ICMS →](icms.md)

## 5. Esporta il Report Word

Toolbar → **Report**. Scarica il `.docx` con:

- Frontespizio + dati di input
- Stratigrafia tabellata + curve di degradazione
- Accelerogramma di input + Fourier
- Spettro di risposta in superficie + confronto NTC
- Profili γ_max, a_max, σ_max
- Fattori di amplificazione ICMS
- Conclusioni

---

## Prossimi passi

- [**Workflow completo**](workflow.md) — un progetto reale dall'inizio alla fine
- [**Metodo lineare equivalente**](metodo.md) — come funziona il calcolo
- [**ICMS**](icms.md) — i fattori di amplificazione per la microzonazione
- [**Dati di input**](dati-input.md) — descrizione completa di ogni campo

---

*Pagina utile? Hai dubbi? [Scrivici](mailto:info@geostru.ai?subject=Help%20RSL%20III%20-%20Quickstart).*
