# Metodo lineare equivalente

RSL III implementa il **metodo lineare equivalente** di Idriss-Seed (1968,
1970), formulato originariamente per il programma SHAKE e usato negli
strumenti standard del settore (EERA, STRATA, DEEPSOIL in modalità EQL,
SHAKE2000).

## Idea di base

Il terreno reale è **non lineare**: G e ξ dipendono da γ_max raggiunto durante
il sisma. Una vera analisi non lineare risolve l'equazione del moto al passo
nel dominio del tempo, con leggi costitutive isteretiche complesse.

L'approccio **lineare equivalente** è un compromesso pratico:

1. Risolvi un'analisi **lineare** in dominio frequenziale (semplice e rapida)
2. Stima γ_max in ogni strato
3. Aggiorna G e ξ alla "secante" che corrisponde a γ_eff = 0.65 · γ_max
4. Ri-risolvi l'analisi lineare con i nuovi G e ξ
5. Itera fino a convergenza

Il γ_eff = 65% di γ_max è un'approssimazione empirica per "rappresentare"
l'effetto medio della non-linearità durante l'intera storia ciclica.

## Schema di calcolo

### Passo 1 — Discretizzazione

La colonna stratigrafica viene discretizzata in N **sotto-strati** di
spessore Δh. Criterio per evitare aliasing alle alte frequenze:

$$
\Delta h \leq \frac{V_s^{\min}}{4 \cdot f_{\max}}
$$

con f_max = 25 Hz (default). Per Vs minimo = 100 m/s → Δh ≤ 1 m.

RSL III calcola Δh automaticamente; tipicamente discretizza in 20-50
sotto-strati.

### Passo 2 — Funzione di trasferimento

Per onde S piane verticali in colonne stratificate orizzontalmente, la
funzione di trasferimento H(ω) tra superficie e bedrock si calcola con il
**metodo dei coefficienti di riflessione/trasmissione** (Haskell-Thomson,
ovvero il metodo *propagator matrix* di Aki-Richards):

$$
H(\omega) = \frac{u_{\text{surface}}(\omega)}{u_{\text{bedrock}}(\omega)}
$$

dove ogni interfaccia tra strati genera coefficienti `r` (riflessione) e
`t` (trasmissione) funzione delle impedenze acustiche `Z = ρ · Vs`.

Per N strati la trasformazione diventa un prodotto di matrici 2×2 (una per
strato). RSL III lo calcola alle ~2000-4000 frequenze del Fourier
dell'accelerogramma.

### Passo 3 — Spettro di Fourier output

$$
F_{\text{out}}(\omega) = H(\omega) \cdot F_{\text{in}}(\omega)
$$

L'antitrasformata di Fourier dà l'**accelerogramma in superficie** nel
dominio del tempo.

### Passo 4 — Stima γ_max

In ogni sotto-strato, dato il taglio massimo τ_max calcolato:

$$
\gamma_{\max} = \frac{\tau_{\max}}{G_{\text{secant}}}
$$

E quindi:

$$
\gamma_{\text{eff}} = 0{,}65 \cdot \gamma_{\max}
$$

### Passo 5 — Aggiorna G e ξ

Per ogni sotto-strato leggi le curve di degradazione al γ_eff:

- **G_new = G_max · (G/G_max)(γ_eff)**
- **ξ_new = ξ(γ_eff)**

### Passo 6 — Convergenza

Confronta γ_eff(iter) con γ_eff(iter-1). Se la massima variazione su tutti
i sotto-strati è < tolleranza (default 0.5%), **convergenza raggiunta**.
Altrimenti torna al passo 2 con i nuovi G e ξ.

Tipicamente converge in **4-8 iterazioni** per accelerogrammi standard.

## Limiti del metodo

### 1. Equivalenza media

Il γ_eff = 65% di γ_max è un proxy dell'effetto medio. Per accelerogrammi
con **un picco molto isolato** + bassa coda (es. eventi quasi-impulsivi)
sovrastima la non-linearità. Per accelerogrammi con **molti cicli a
ampiezza simile** (lunga coda) la stima è buona.

### 2. Non lineare strong-motion

Per **deformazioni γ > 1%** il metodo lineare equivalente diventa
inaccurato: le argille molto deformate hanno comportamento isteretico
asimmetrico che il modello secante non cattura. Per scuotimenti
estremi (pendii instabili in zona Friuli/L'Aquila) usa SRA non lineare
nel dominio del tempo.

### 3. 1D verticale

Assume **propagazione verticale** di onde S. Non cattura:

- Effetti **2D / 3D** di topografia (creste, valli)
- Effetti di **bacino sedimentario** (riflessioni laterali)
- **Onde di superficie** (Rayleigh, Love)

Per siti con topografia importante o geometria di bacino marcata, abbinare
analisi 2D (FLAC, PLAXIS, OpenSees).

### 4. Bedrock orizzontale

L'interfaccia bedrock-terreno è assunta orizzontale. Per bedrock molto
inclinato (es. accumuli di versante) la rappresentazione 1D è
inadeguata.

## Quando usare RSL III (e quando no)

✅ **Adatto**:

- Studi di **microzonazione sismica** Livello 3 (ICMS)
- Verifica spettro NTC vs spettro di sito per progettazione standard
- Ammassi terrigeni stratificati orizzontalmente con Vs noto
- Eventi sismici di **intensità moderata** (a_max ≤ 0.4 g, γ_max < 1%)

❌ **Non adatto** (o richiede integrazione con altri tool):

- Studi su **pendii** o crinali (servono FA topografici 2D)
- Analisi di **liquefazione** in tempo reale (RSL stima γ_max ma non il
  build-up delle pressioni neutre — usa LiquiTer per la liquefazione)
- Eventi **ad alta non-linearità** (a_max > 0.6 g, γ > 2%)
- Bacini sedimentari profondi con effetti 2D/3D

## Riferimenti

- **Idriss I.M., Seed H.B. (1968)** — *Seismic response of horizontal soil
  layers*. JSMFD, ASCE
- **Schnabel P.B., Lysmer J., Seed H.B. (1972)** — *SHAKE: A computer
  program for earthquake response analysis of horizontally layered sites*.
  EERC Report, UC Berkeley
- **Bardet J.P., Tobita T. (2001)** — *NERA / EERA: Equivalent-linear
  earthquake site response analyses*
- **Kramer S.L. (1996)** — *Geotechnical Earthquake Engineering*. Prentice Hall
- **ICMS 2008/2018** — *Indirizzi e Criteri per la Microzonazione Sismica*,
  Dipartimento della Protezione Civile

---

## Vedi anche

- [Workflow completo](workflow.md) — il metodo nel processo
- [Dati di input](dati-input.md) — quali curve scegliere
- [Fattori ICMS](icms.md) — output del metodo per la microzonazione

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20RSL%20III%20-%20Metodo).*
