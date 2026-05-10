# Metodi di calcolo

LiquiTer NX implementa **4 metodi semi-empirici** per il calcolo di CRR
(Cyclic Resistance Ratio) e quindi del fattore di sicurezza alla
liquefazione. La scelta dipende dalla **prova in sito disponibile**:

| Prova in sito | Metodo consigliato |
|---|---|
| **SPT** (Standard Penetration Test) | Seed (1971), Tokimatsu (1983) |
| **CPT** (Cone Penetration Test) | Boulanger-Idriss (2014) |
| **Cross-hole / Down-hole** (Vs) | Andrus-Stokoe (2000) |

Tutti i metodi calcolano CSR allo stesso modo (Seed-Idriss 1971); cambia
solo il modo di stimare CRR.

## CSR — Cyclic Stress Ratio

Comune a tutti i metodi:

$$
\text{CSR} = 0{,}65 \cdot \frac{a_{\max}}{g} \cdot \frac{\sigma_v}{\sigma'_v} \cdot r_d
$$

dove:

- **a_max** = accelerazione di picco al suolo
- **σ_v / σ'_v** = tensione totale / efficace alla profondità z
- **r_d** = coefficiente riduttivo della profondità (Liao-Whitman 1986 o
  Idriss-Boulanger 2008 a seconda del metodo)

## 1. Seed (1971)

**Su SPT — il metodo classico, ancora il più usato in Italia.**

CRR si stima dalla **N1,60,cs** (numero SPT corretto per:
energia, pressione di confinamento, contenuto fine "clean-sand equivalent")
tramite la curva semi-empirica originale di Seed et al. (1985).

### Quando usarlo

- Hai SPT come prova principale
- Il sito ha sabbie/sabbie limose
- Vuoi un risultato confrontabile con la letteratura italiana storica

### Limiti

- Non distingue bene sabbie pulite e limose (la correzione clean-sand è
  approssimata)
- Curva di base derivata da terremoti M = 7.5 — applicare il fattore
  di scala MSF per altre magnitudo

### Riferimenti

- Seed H.B., Idriss I.M. (1971) — *Simplified procedure for evaluating soil
  liquefaction potential*. JGED, ASCE
- Seed H.B., Tokimatsu K., Harder L.F., Chung R.M. (1985) — *Influence of
  SPT procedures in soil liquefaction resistance evaluations*. JGED

## 2. Tokimatsu (1983)

**Su SPT — variante che distingue sabbie pulite/limose con curve dedicate.**

Stessa logica di Seed ma usa:

- Curve CRR(N1) **separate** per sabbie pulite e limose
- Diversa correzione per pressione di confinamento

### Quando usarlo

- Hai SPT + buona caratterizzazione granulometrica (sai bene se sabbia pulita
  o limosa)
- Vuoi confrontare con Seed per verifica

### Riferimenti

- Tokimatsu K., Yoshimi Y. (1983) — *Empirical correlation of soil
  liquefaction based on SPT N-value and fines content*. Soils and Foundations

## 3. Boulanger-Idriss (2014)

**Su CPT — il metodo più recente, raccomandato quando hai CPT continuo.**

CRR si stima dalla **qc1N,cs** (resistenza CPT normalizzata e clean-sand
equivalent) tramite la curva Boulanger-Idriss (2014).

Vantaggi rispetto a SPT:

- Profilo continuo lungo la verticale (ogni 1-2 cm), non a step di 1 m
- Misura più ripetibile (operatore-indipendente)
- Correzioni per fines content basate su Ic (indice di tipo di
  comportamento del suolo) — più robuste

### Quando usarlo

- Hai CPT (CPTU se possibile)
- Vuoi un calcolo "continuo" lungo la verticale
- Stato dell'arte normativo internazionale

### Riferimenti

- Boulanger R.W., Idriss I.M. (2014) — *CPT and SPT based liquefaction
  triggering procedures*. UC Davis Report UCD/CGM-14/01
- Idriss I.M., Boulanger R.W. (2008) — *Soil liquefaction during earthquakes*.
  EERI Monograph

## 4. Andrus-Stokoe (2000)

**Su Vs — utile quando hai cross-hole/down-hole o sismica passiva.**

CRR si stima dalla **Vs1,cs** (Vs normalizzata e clean-sand equivalent) con
curva Andrus-Stokoe (2000).

### Quando usarlo

- Hai velocità onde di taglio Vs (cross-hole, down-hole, sismica passiva, MASW)
- Lo strato è gravelly o presenta cobble (SPT/CPT problematici)
- Sito su pendio dove SPT/CPT sono difficili

### Limiti

- Vs è meno sensibile a piccole variazioni di addensamento rispetto a SPT/CPT
- Affidabilità minore in sabbie molto sciolte

### Riferimenti

- Andrus R.D., Stokoe K.H. (2000) — *Liquefaction resistance of soils from
  shear-wave velocity*. JGGE, ASCE

## Fattori di scala

Tutti i metodi applicano **fattori correttivi** al FSL grezzo:

### MSF — Magnitude Scaling Factor

Corregge la durata della scossa, dato che le curve CRR di base sono per
M = 7.5. Per M minori il sisma è più breve → meno cicli → CRR più alto:

$$
\text{MSF} = \left(\frac{M_w}{7{,}5}\right)^{-2{,}56}
$$

(formulazione Idriss 1999, accettata da NTC 2018)

### K_σ — Overburden Correction

Corregge per pressione di confinamento. Per σ'_v > 100 kPa il CRR
diminuisce (sabbie sciolte) o aumenta lievemente (sabbie addensate):

$$
K_\sigma = 1 - C_\sigma \cdot \ln\left(\frac{\sigma'_v}{p_a}\right)
$$

con C_σ funzione del DR (densità relativa).

### K_α — Static Shear Stress Correction

Per pendii (in LiquiTer non implementato — assumiamo terreno orizzontale).

## FSL — Fattore di sicurezza

$$
\text{FSL} = \frac{\text{CRR} \cdot \text{MSF} \cdot K_\sigma}{\text{CSR}}
$$

Soglia di liquefazione: **FSL < FSL_limite** (default 1.25 per NTC 2018,
1.0 per EC8).

## IPL — Indice del potenziale di liquefazione

Iwasaki et al. (1982) — integra il "deficit" FSL < 1 sui primi 20 m:

$$
\text{IPL} = \int_0^{20} F(z) \cdot w(z) \, dz
$$

con:

- F(z) = `1 - FSL(z)` se FSL < 1, altrimenti 0
- w(z) = `10 - 0.5 z` (peso linearmente decrescente con la profondità)

| IPL | Rischio liquefazione |
|---|---|
| 0 | Trascurabile |
| 0–5 | Basso |
| 5–15 | Medio |
| > 15 | Alto |

## Cedimenti post-sismici (Ishihara-Yoshimine 1992)

Per ogni strato liquefacibile, il cedimento volumetrico ε_v è funzione di:

- FSL dello strato
- Densità relativa DR (stimata da N1,60 o qc1N)

Il **cedimento totale** è la somma dei contributi di ogni strato
liquefacibile, integrato lungo la verticale.

LiquiTer mostra:

- **Cedimento per strato** (cm)
- **Cedimento totale al p.c.** (cm)
- **Cedimento differenziale** (se rilevante)

### Riferimenti

- Ishihara K., Yoshimine M. (1992) — *Evaluation of settlements in sand
  deposits following liquefaction during earthquakes*. Soils and Foundations

---

## Quale metodo scegliere — riepilogo

| Situazione | Metodo |
|---|---|
| SPT come unica prova in sito (caso più comune in Italia) | **Seed** o **Tokimatsu** |
| Hai CPT/CPTU continuo | **Boulanger-Idriss** (state of the art) |
| Hai Vs (cross-hole, down-hole, MASW) | **Andrus-Stokoe** |
| Vuoi confronto multi-metodo | Lancia tutti, confronta IPL |
| Sito ghiaioso o con cobble | **Andrus-Stokoe** (Vs poco influenzato da granuli) |

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20LiquiTer%20NX%20-%20Metodi).*
