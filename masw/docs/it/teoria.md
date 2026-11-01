# Cenni teorici

Questa pagina riassume che cosa misura la prova MASW e come MASW NX passa dalle tracce al
profilo di V~s~ e alla categoria di sottosuolo. Le formule sono le stesse del
[documento di validazione](validazione.md).

## La prova MASW

La **MASW** (Multichannel Analysis of Surface Waves) ricava il profilo di velocità delle
onde di taglio dalla **dispersione delle onde di superficie di Rayleigh**. In un terreno
stratificato le onde di frequenza diversa hanno lunghezze d'onda diverse e quindi
«sentono» spessori diversi: le basse frequenze (lunghezze d'onda lunghe) campionano il
terreno in profondità, le alte frequenze solo gli strati superficiali. La velocità di fase
dipende dunque dalla frequenza, e questa dipendenza, la **curva di dispersione**, contiene
l'informazione sul profilo di V~s~.

Nella prova **attiva** una sorgente (di solito una mazza su una piastra) genera le onde
all'estremità di uno **stendimento** lineare di geofoni verticali a passo costante dx (di
norma 12 o 24 geofoni da 4,5 Hz, a 1–3 m). Un sismografo registra le tracce. La geometria
condiziona il risultato:

- la **lunghezza dello stendimento** limita la lunghezza d'onda massima risolta, e quindi la
  profondità d'indagine;
- l'**interdistanza** dx limita la lunghezza d'onda minima, e quindi la risoluzione in
  superficie;
- la **distanza della sorgente** dal primo geofono serve a far arrivare un'onda di
  superficie già formata, senza lasciarla attenuare troppo.

## Lo spettro f-v

Lo spettro velocità di fase – frequenza si calcola con il metodo **phase-shift** (Park,
Miller e Xia, 1998–1999), una somma pesata (slant-stack) in frequenza:

1. di ogni traccia u~j~(t), al geofono di posizione x~j~, si calcola la trasformata di
   Fourier U~j~(f);
2. per ogni frequenza f e per ogni velocità di prova v si rimettono in fase le tracce per
   quella velocità e si sommano:

    E(f, v) = | Σ~j~ U~j~(f) / |U~j~(f)| · exp(i·2π·f·x~j~/v) |

3. ogni colonna (frequenza) è normalizzata al suo massimo.

Dove v è la vera velocità di fase di un modo a quella frequenza, le tracce si sommano in
fase e la mappa mostra un massimo. Le creste della mappa sono le curve di dispersione dei
**modi** di Rayleigh: il **fondamentale** (modo 0) e i **modi superiori**.

### Curva apparente e regressione

Il massimo di ogni colonna dà la **curva apparente**. MASW NX ne esclude i massimi uguali al
minimo o al massimo dell'intera curva (bordi della mappa) e ci fa passare una **regressione
polinomiale** di grado 2–10. È un aiuto alla lettura, come nel desktop: dove più modi hanno
energia simile, la curva apparente salta da un modo all'altro.

### Lunghezza d'onda e profondità

Ogni punto (f, v) della curva ha lunghezza d'onda λ = v / f. Come regola pratica, un'onda di
Rayleigh di lunghezza d'onda λ è sensibile soprattutto al terreno fino a una profondità
dell'ordine di λ/2 – λ/3. Su questo si basano la stima delle V~s~ iniziali e la proposta
degli strati (sotto).

## Il picking automatico sulle creste

Il picking **Automatico** cerca le creste della mappa:

1. per ogni colonna, i massimi locali della colonna smussata con ampiezza e prominenza
   sufficienti; le colonne quasi piatte e i picchi con lunghezze d'onda fuori dalla portata
   dello stendimento si scartano;
2. i picchi di colonne vicine con piccolo salto di velocità formano creste; restano quelle
   lunghe (almeno 4 Hz) e forti;
3. ogni cresta va al modo del modello sintetico più vicino, se c'è, altrimenti ai modi in
   ordine di velocità;
4. le creste si campionano a passo regolare in frequenza e, dove la mappa lo consente, si
   prolungano alle basse frequenze.

È una proposta: dove il fondamentale non forma una cresta il picking non lo raggiunge.

## Il problema diretto

Dato un modello a strati piano-paralleli, ciascuno con spessore h, V~s~, V~p~ e densità ρ,
sopra un semispazio, le curve di dispersione dei modi di Rayleigh si calcolano con il metodo
delle **matrici di propagazione** di Thomson (1950) e Haskell (1953), nella formulazione
stabile di Dunkin (1965). Il codice è il porting del calcolo di Geopsy (Wathelet, 2005, codice
aperto con licenza LGPL), lo stesso motore di Easy-MASW desktop, e coincide a precisione
macchina con la libreria del desktop.

V~p~ si ricava da V~s~ e dal coefficiente di Poisson ν dello strato:

V~p~ = V~s~ · √[ 2(1 − ν) / (1 − 2ν) ]

## Inversione

L'inversione cerca il modello le cui curve teoriche riproducono meglio il picking. Le
incognite sono gli spessori e le V~s~ degli strati non bloccati, ciascuna entro i suoi
limiti Min e Max; ν e ρ restano quelli assegnati. La ricerca usa il **simplesso di Nelder e
Mead** (1965) con vincoli e reinizializzazione, partendo dal modello iniziale e da punti
casuali: due corse danno soluzioni un po' diverse.

La funzione obiettivo (**misfit**) confronta, punto per punto e modo per modo, la velocità
osservata v~oss~ con quella calcolata v~calc~:

misfit = (1 + n~D~ − n~R~) · √[ Σ ((v~oss~ − v~calc~) / v~oss~)² / n~R~ ]

con n~D~ punti osservati e n~R~ punti per cui il modello ha il modo corrispondente: un modello
che «perde» un modo è penalizzato. L'**errore percentuale** è:

errore % = media[(v~oss~ − v~calc~)²] / media[v~oss~²] · 100

### Stima iniziale e proposta degli strati

- **Stima iniziale dal picking**: ogni punto dà tre profondità, v~min~/(2f), v/(2f) e
  v~max~/(2f), dove v~min~ e v~max~ sono gli estremi della sua barra d'incertezza. La V~s~
  iniziale di uno strato è la media delle velocità le cui profondità cadono nello strato;
  Min e Max sono metà e doppio.
- **Proponi strati**: primo strato h~1~ ≈ λ~min~/2 (almeno 0,5 m), profondità del
  semispazio z ≈ λ~max~/3 limitata fra 5 e 40 m, spessori in progressione geometrica
  h~1~·r<sup>k</sup> fino a z, arrotondati al mezzo metro, con margine ±50 %; poi la stima iniziale.

## V~s,eq~ e categoria di sottosuolo

Secondo le NTC 2018 (§3.2.2):

V~s,eq~ = H / Σ~i~ (h~i~ / V~s,i~)

con h~i~ e V~s,i~ spessore e velocità degli strati fra il piano di posa e la profondità H del
**substrato**, il primo strato con V~s~ ≥ 800 m/s. Se il substrato è oltre 30 m, H = 30 m. Le
NTC 2008 usano V~s,30~, la media armonica sui 30 m sotto il piano di posa.

## Parametri elastici e correlazioni

Dalla densità ρ e dalle velocità:

| Grandezza | Formula |
|---|---|
| Coefficiente di Poisson | ν = (q/2 − 1) / (q − 1), con q = (V~p~/V~s~)² |
| Modulo di taglio | G~0~ = ρ·V~s~² |
| Modulo edometrico | E~d~ = ρ·V~p~² |
| Modulo di compressibilità volumetrica | M~0~ = E~d~ − 4/3·G~0~ = ρ·(V~p~² − 4/3·V~s~²) |
| Modulo di Young | E = 2·ρ·V~s~²·(1 + ν) |

Le correlazioni empiriche, invertite per ricavare il parametro da V~s~:

- **Ohta e Goto** (1978): V~s~ = 54,33 · N<sup>0,173</sup> · α · β · (z / 0,303)<sup>0,193</sup>, con z la
  profondità media dello strato, α il fattore di età (1 per i depositi olocenici, 1,303 per
  i pleistocenici) e β il fattore di composizione (1 limi e argille, 1,09 sabbie, 1,19
  sabbie e ghiaie);
- **Jamiolkowski** (1985): V~s~ = α · q~c~<sup>β</sup>, con α e β dipendenti dal tipo di terreno.

## Funzione di trasferimento

L'amplificazione delle onde SH a incidenza verticale attraverso gli strati della soluzione,
con il semispazio come substrato e smorzamento dell'1 %, si calcola con la propagazione 1D
in un mezzo a strati. Per uno strato omogeneo di spessore H su substrato rigido la prima
risonanza è a f~0~ = V~s~ / 4H.

## Bibliografia

- Park C.B., Miller R.D., Xia J. (1999). *Multichannel analysis of surface waves*.
  Geophysics, 64(3), 800–808.
- Thomson W.T. (1950). *Transmission of elastic waves through a stratified solid medium*.
  Journal of Applied Physics, 21, 89–93.
- Haskell N.A. (1953). *The dispersion of surface waves on multilayered media*. Bulletin of
  the Seismological Society of America, 43, 17–34.
- Dunkin J.W. (1965). *Computation of modal solutions in layered, elastic media at high
  frequencies*. Bulletin of the Seismological Society of America, 55, 335–358.
- Wathelet M. (2005). *Array recordings of ambient vibrations: surface-wave inversion*. Tesi
  di dottorato, Université de Liège.
- Nelder J.A., Mead R. (1965). *A simplex method for function minimization*. The Computer
  Journal, 7, 308–313.
- Ohta Y., Goto N. (1978). *Empirical shear wave velocity equations in terms of
  characteristic soil indexes*. Earthquake Engineering and Structural Dynamics, 6, 167–187.
- Jamiolkowski M. et al. (1985). *New developments in field and laboratory testing of
  soils*. Proc. XI ICSMFE, San Francisco.
- Ministero delle Infrastrutture e dei Trasporti (2018). *Aggiornamento delle Norme tecniche
  per le costruzioni* (NTC 2018), §3.2.2.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MASW%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/it/teoria.md).*
