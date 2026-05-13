# Idrogrammi SCS-CN

Il metodo **SCS-CN** (Soil Conservation Service, ora NRCS) trasforma un
ietogramma di progetto nell'**idrogramma di piena** di una sezione di
bacino. Combina due passaggi:

1. **Pioggia netta** dalla pioggia totale, attraverso il *Curve Number*;
2. **Convoluzione** con l'idrogramma unitario SCS, scalato sul tempo di lag.

## Passo 1 — pioggia netta

Il modello considera che parte della pioggia viene assorbita (perdite
iniziali \(I_a\)) o si accumula come ritenzione potenziale \(S\):

$$
S = \frac{25400}{\text{CN}} - 254
\qquad
I_a = 0.2 \cdot S
$$

Con \(S\) in mm e CN in \([0, 100]\). Per una pioggia cumulata totale \(P\):

$$
P_e =
\begin{cases}
0 & \text{se } P \le I_a \\[1mm]
\dfrac{(P - I_a)^2}{P - I_a + S} & \text{se } P > I_a
\end{cases}
$$

\(P_e\) è la **pioggia netta** cumulata. Le perdite iniziali rappresentano
intercezione vegetale + invasi superficiali. Sotto \(I_a\) tutto si infiltra.

### Curve Number

Il CN dipende dal tipo idrologico del suolo (A, B, C, D — da molto permeabile
a impermeabile) e dalla **copertura del suolo**. Esempi:

| Copertura | A | B | C | D |
|-----------|---|---|---|---|
| Boschi mediamente coperti | 30 | 55 | 70 | 77 |
| Prati permanenti | 39 | 61 | 74 | 80 |
| Seminativi puliti | 67 | 78 | 85 | 89 |
| Aree urbane impermeabili | 98 | 98 | 98 | 98 |

!!! tip "Wizard CN integrato"
    Nel pannello idrogrammi un wizard interattivo ti permette di:
    1. dividere il bacino in più aree;
    2. assegnare a ciascuna **suolo idrologico** e **copertura**;
    3. ottenere il **CN pesato sull'area** del bacino.

    Sotto, sezione [Tabelle SCS](#tabelle-cn-complete) c'è la tabella completa.

## Passo 2 — idrogramma unitario SCS

L'idrogramma unitario adimensionale SCS è un triangolo con:

- **tempo al picco** \(t_p = 0.5\,D + T_{\text{lag}}\), dove \(D\) è la durata
  della pioggia netta e \(T_{\text{lag}}\) il tempo di lag del bacino;
- **portata al colmo** dell'unitario \(q_p = 484 \cdot A / t_p\) (in unità US;
  in SI: \(q_p = 0.208 \cdot A / t_p\) con A in km² e \(t_p\) in ore);
- **tempo di base** \(t_b = 2.67 \cdot t_p\).

L'idrogramma totale è la **convoluzione** della sequenza \(\Delta P_e(t)\) con
l'unitario:

$$
Q(t) = \sum_{k} \Delta P_e(k) \cdot u(t - k)
$$

## Tempo di lag — \(T_{\text{lag}}\)

\(T_{\text{lag}}\) è il tempo che intercorre tra il baricentro della pioggia
netta e il picco dell'idrogramma. Stime tipiche:

- **Formula SCS**: \(T_{\text{lag}} = 0.6 \cdot T_c\) (Tc = tempo di
  corrivazione).
- **Tempo di corrivazione**: Kirpich, Giandotti, Pasini, Pezzoli, secondo
  morfometria del bacino.

!!! tip "Wizard Tlag"
    Nel pannello, il calcolatore Tlag accetta:
    - area del bacino A (km²);
    - lunghezza dell'asta principale L (km);
    - pendenza media i (%);

    Restituisce il \(T_c\) con quattro formule classiche + il \(T_{\text{lag}}\)
    proposto come 0.6 \(T_c\). Scegli il valore che giudichi più adatto al
    tipo di bacino.

## Come si usa in Runoff Lab

1. Vai nel pannello **Idrogrammi** → *Aggiungi*.
2. Sorgente: un **pluviogramma sintetico** già costruito (o una curva diretta).
3. Inserisci:
   - **Area del bacino** A (km²);
   - **CN** (da wizard o manuale);
   - **Tlag** (da wizard o manuale).
4. Conferma → grafico \(Q(t)\), tabella con:
   - **\(Q_p\)** (portata al colmo, m³/s);
   - **\(t_p\)** (tempo al picco, h);
   - **\(V_{\text{tot}}\)** (volume totale ruscellato, m³);
   - **\(P_e\)** (pioggia netta totale, mm);
   - rapporto pioggia netta / pioggia lorda (runoff ratio).

## Limiti del metodo SCS-CN

- Sviluppato originariamente per bacini agricoli statunitensi piccoli
  (≤ 250 km²). Per bacini grandi conviene un modello distribuito.
- L'assunzione \(I_a = 0.2 S\) è una semplificazione: per bacini urbani molto
  impermeabili può essere meglio usare \(I_a = 0.05 S\).
- Tlag costante (lineare) — non cattura non linearità delle perdite per piene
  estreme.

## Bibliografia

- Soil Conservation Service (1972, 1986), *National Engineering Handbook,
  Section 4: Hydrology*. USDA.
- Mockus V. (1957), *Estimation of total (and peak rates of) surface runoff
  for individual storms*, USDA.
- Maidment D.R. (ed., 1993), *Handbook of Hydrology*, McGraw-Hill — cap. 9 (SCS).

## Tabelle CN complete

(Per brevità qui un estratto; il wizard in app ha tabelle complete per:
boschi, prati, coltivazioni, aree urbane, residenziali, commerciali,
infrastrutture, naturali nudi.)
