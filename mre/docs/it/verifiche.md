# Verifiche esterne e interne

## Verifiche esterne

Nell'ordine: **ribaltamento**, **scorrimento**, **capacità portante** (Hansen con
fattori di inclinazione del carico). Ogni card mostra il FS della combinazione
governante in grande e, sotto, il FS di ciascuna combinazione col badge *governante*;
la striscia in alto dichiara nome e coefficienti di ogni combinazione.

- **Ribaltamento**: momenti rispetto al piede a valle; FS = M~s~/M~r~. In sismica il
  coefficiente sismico è maggiorato del 50% (NTC §7.11.6.2.1).
- **Scorrimento**: resistenza W·tanφ~f~ sul piano di posa contro la spinta.
- **Capacità portante**: q~lim~ di Hansen contro il carico verticale.

![Card delle verifiche esterne con il FS della combinazione governante](img/09-verifiche.png)

## Verifiche interne

Per ogni livello di rinforzo: **sfilamento** (la lunghezza efficace è il tratto oltre
il cuneo di rottura) e **rottura** (R~d~ contro l'azione). In approccio Progetto la
lunghezza necessaria è dedotta livello per livello; in Verifica è controllata quella
imposta. Se un livello ricade interamente nel cuneo il programma lo segnala.

Il verdetto complessivo («Tutte le verifiche sono soddisfatte») richiede FS ≥ 1 su
esterne e interne, più stabilità globale e verifiche tieback/compound se calcolate.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MRE%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mre/docs/it/verifiche.md).*
