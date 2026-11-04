# Theory

## Regularisation (Appendix 1)

With SA(T) the MS3 acceleration spectrum:

- T~A~ is the period of the maximum of SA; **SA~m~** = (1/T~A~)·∫ SA(T) dT between 0.5·T~A~ and 1.5·T~A~;
- SV(T) = SA(T)·T/2π; T~V~ is the period of the maximum of SV; **SV~m~** = (1/(0.4·T~V~))·∫ SV(T) dT between 0.8·T~V~ and 1.2·T~V~;
- **T~C~** = 2π·SV~m~/SA~m~; **T~B~** = T~C~/3;
- **a~max~** = (Se(0.01)/SA~m~ − 0.01/T~B~)·SA~m~/(1 − 0.01/T~B~): ordinate at T = 0 of the line through (0.01 s; Se(0.01 s)) and (T~B~; SA~m~);
- **T~D~** = 4·a~max~/g + 1.6 s; **F~0~** = SA~m~/a~max~.

The regularised spectrum has the shape of the code spectrum with a~g~ = a~max~, ξ = 5 %, η = 1, S~S~ = S~T~ = 1 (notional values). The integral
means are computed exactly on the polyline of the data.

## NTC 2018 simplified spectrum (§3.2.3.2.1)

S = S~S~·S~T~; T~C~ = C~C~·T~c~*; T~B~ = T~C~/3; **T~D~ = 4.0·a~g~/g + 1.6**; with η = 1:

| Branch | Se(T) |
|---|---|
| 0 ≤ T < T~B~ | a~g~·S·[F~0~·T/T~B~ + (1 − T/T~B~)] |
| T~B~ ≤ T < T~C~ | a~g~·S·F~0~ |
| T~C~ ≤ T < T~D~ | a~g~·S·F~0~·T~C~/T |
| T ≥ T~D~ | a~g~·S·F~0~·T~C~·T~D~/T² |

S~S~ and C~C~ from Tab. 3.2.IV, S~T~ from Tab. 3.2.V (value at the crest).

## Comparison (Ordinance §3.2)

Over the interval [T~min~, 2·T~max~]: condition 1 if max(Se,MS3/Se,NTC) > 1.30; condition 2 if (A~MS3~ − A~NTC~)/A~NTC~ > 0.20. The integrals
are computed in closed form, branch by branch. With 2·T~max~ > 1.1 s the comparison is not made.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20RSL%20III%20A%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rsl3a/docs/en/teoria.md).*
