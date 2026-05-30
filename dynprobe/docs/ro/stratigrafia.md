# Stratigrafie interpretată

## Ce este

Stratigrafie interpretată este modelul subsolului pe care îl obții din înregistrările încercării. Definești un anumit număr de straturi — fiecare cu o adâncime inferioară, un tip de teren și greutățile volumice γ și γ_sat — iar software-ul calculează pentru fiecare valoarea reprezentativă N_SPT, din care derivă ulterior corelațiile geotehnice.

## Cum se introduce

În fila **Stratigrafie interpretată** din Editor:

1. Primul strat începe de la 0 m. Setează adâncimea sa inferioară (ex. 2,50 m).
2. Fă clic pe **+ Adaugă strat** pentru a crea stratul următor.
3. Pentru fiecare strat:
   - Setează **adâncimea inferioară** (m față de cota terenului).
   - Alege **tipul de teren**: `COES` (coeziv), `INCO` (necoeziv) sau ambele dacă este mixt — tipul determină ce corelații se aplică.
   - Introdu **γ** (greutatea volumică uscată sau naturală) și **γ_sat** (greutatea volumică saturată) în kN/m³.
   - Dacă dorești, introdu **argilă (%)** și **descrierea** litologică.

## Cele 7 metode de agregare N_SPT

Pentru fiecare strat, înregistrările care se încadrează în intervalul său de adâncime sunt agregate cu metoda aleasă de utilizator. Metodele disponibile sunt:

| Metodă | Când se folosește |
|---|---|
| **Medie** | Teren omogen, variabilitate redusă |
| **Minim** | Abordare conservativă — se folosește cea mai mică valoare |
| **Maxim** | Estimarea limitei superioare (ex. pentru capacitatea portantă pe vârf) |
| **Medie − 1σ** | Abordare statistică conservativă |
| **Medie + 1σ** | Abordare statistică neconservativă |
| **RNC** (distribuție normală) | Valoare caracteristică în probabilitate conform EC7 §2.4.5.2 |
| **RC** (distribuție log-normală) | Ca RNC dar cu distribuție log-normală — preferabilă pentru N_SPT cu valori mici |

Metoda se setează în antetul coloanei N_SPT din tabelul de stratigrafie și este valabilă pentru toate straturile simultan.

!!! info "Care este metoda potrivită?"
    Norma EC7 (și NTC §6.2.2) indică folosirea **valorii caracteristice** a parametrului, definită ca valoarea cu probabilitate de 5% de a fi depășită pe latura conservativă. Metodele RNC și RC se apropie de această definiție statistică. Pentru eșantioane mici (< 6 înregistrări pe strat) media rămâne referința cea mai robustă.

## Conversia N_DPM → N_SPT

Pentru încercările continue, N_SPT de strat se obține din N_DPM aplicând coeficientul β (vezi [Instrumente →](strumenti.md)). Produsul N_DPM × β este N_SPT echivalent pentru fiecare înregistrare; agregarea se aplică ulterior pe aceste valori echivalente.

## Insigna Σ straturi / încercare

În partea de jos a ecranului de stratigrafie apare insigna:

```
Σ straturi  X,XX m  /  încercare  Y,YY m
```

- **Verde** (✓): suma adâncimilor straturilor coincide cu adâncimea încercării — stratigrafie acoperă întreaga încercare fără lacune.
- **Galben** (⚠): abatere între Σ straturi și adâncimea încercării — verifică că ultimul strat ajunge la finalul încercării.
