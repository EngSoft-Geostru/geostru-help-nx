# Cenni teorici

## L'idea

Le onde di Rayleigh viaggiano a velocità diverse secondo la frequenza: le frequenze basse «sentono» il terreno più profondo.
La curva velocità-frequenza (**curva di dispersione**) dipende dal profilo di V~s~, e invertendola si risale al profilo.

## Spettro f-v

Per ogni frequenza e velocità di prova si rimettono in fase le tracce e si somma (Park, Miller e Xia, 1999):

```text
S(f, v) = Σ_k U_k(f) · exp(−i · 2π · f · x_k / v)
```

Il modulo, normalizzato sul massimo di ogni colonna, è la mappa. Se v è giusta le tracce si sommano in fase e |S| è grande.

## Modello diretto

La curva teorica di un profilo a strati è calcolata con il propagatore di Thomson-Haskell e Dunkin. Il motore deriva da
Geopsy/gpdc (M. Wathelet) ed è stato validato a precisione macchina contro la libreria nativa del desktop.

## Inversione

L'ottimizzatore è il simplesso di Nelder e Mead (1965), con vincoli e reinizializzazione. La funzione obiettivo è

```text
misfit = (1 + nD − nR) · √( Σ ((v_oss − v_calc) / v_oss)² / nR )
```

con n~D~ punti del picking e n~R~ quelli per cui il modo esiste. L'errore percentuale è il rapporto fra media di
(v~oss~ − v~calc~)² e media di v~oss~², per 100.

## Parametri

G = ρV~s~², E~d~ = ρV~p~², K = ρ(V~p~² − 4/3 V~s~²), E = 2ρV~s~²(1+ν).

## Bibliografia

Park C.B., Miller R.D., Xia J. (1999), *Multichannel analysis of surface waves*, Geophysics 64(3). Thomson W.T. (1950), J. Appl. Phys. 21.
Haskell N.A. (1953), BSSA 43. Dunkin J.W. (1965), BSSA 55. Wathelet M. (2005), tesi, Univ. de Liège. Nelder J.A., Mead R. (1965),
Computer Journal 7. Ohta Y., Goto N. (1978), Earthq. Eng. Struct. Dyn. 6. Jamiolkowski M. et al. (1985), Proc. XI ICSMFE.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MASW%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/it/teoria.md).*
