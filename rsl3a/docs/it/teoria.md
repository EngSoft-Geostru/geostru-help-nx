# Cenni teorici

## Regolarizzazione (Appendice 1)

Con SA(T) lo spettro MS3 in accelerazione:

- T~A~ è il periodo del massimo di SA; **SA~m~** = (1/T~A~)·∫ SA(T) dT fra 0,5·T~A~ e 1,5·T~A~;
- SV(T) = SA(T)·T/2π; T~V~ è il periodo del massimo di SV; **SV~m~** = (1/(0,4·T~V~))·∫ SV(T) dT fra 0,8·T~V~ e 1,2·T~V~;
- **T~C~** = 2π·SV~m~/SA~m~; **T~B~** = T~C~/3;
- **a~max~** = (Se(0,01)/SA~m~ − 0,01/T~B~)·SA~m~/(1 − 0,01/T~B~): ordinata a T = 0 della retta per (0,01 s; Se(0,01 s)) e (T~B~; SA~m~);
- **T~D~** = 4·a~max~/g + 1,6 s; **F~0~** = SA~m~/a~max~.

Lo spettro regolarizzato ha la forma dello spettro di norma con a~g~ = a~max~, ξ = 5 %, η = 1, S~S~ = S~T~ = 1 (valori fittizi). Le medie
integrali si calcolano esattamente sulla spezzata dei dati.

## Spettro semplificato NTC 2018 (§3.2.3.2.1)

S = S~S~·S~T~; T~C~ = C~C~·T~c~*; T~B~ = T~C~/3; **T~D~ = 4,0·a~g~/g + 1,6**; con η = 1:

| Ramo | Se(T) |
|---|---|
| 0 ≤ T < T~B~ | a~g~·S·[F~0~·T/T~B~ + (1 − T/T~B~)] |
| T~B~ ≤ T < T~C~ | a~g~·S·F~0~ |
| T~C~ ≤ T < T~D~ | a~g~·S·F~0~·T~C~/T |
| T ≥ T~D~ | a~g~·S·F~0~·T~C~·T~D~/T² |

S~S~ e C~C~ dalla Tab. 3.2.IV, S~T~ dalla Tab. 3.2.V (valore in cresta).

## Confronto (Ordinanza §3.2)

Nell'intervallo [T~min~, 2·T~max~]: condizione 1 se max(Se,MS3/Se,NTC) > 1,30; condizione 2 se (A~MS3~ − A~NTC~)/A~NTC~ > 0,20. Gli integrali si
calcolano in forma chiusa, ramo per ramo. Con 2·T~max~ > 1,1 s il confronto non si fa.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20RSL%20III%20A%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rsl3a/docs/it/teoria.md).*
