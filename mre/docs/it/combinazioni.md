# Normativa e combinazioni

Il calcolo è organizzato a **combinazioni**: il motore esegue un giro completo di
verifiche per ciascun set di coefficienti parziali e i risultati mostrati sono, per
ogni verifica, quelli della **combinazione governante** (FS minimo).

## NTC 2018

- **Statica — A1+M1+R3 (STR+GEO)**: coefficienti della card *Coefficienti parziali*
  (γ~A~ da tab. 2.6.I, γ~M~ = 1, γ~R3~ da tab. 6.5.I: capacità portante 1,4 ·
  scorrimento 1,1 · ribaltamento 1,15). Il coefficiente sui carichi dipende dalla
  tipologia di sovraccarico.
- **Sismica** (generata automaticamente con k~h~ > 0): azioni e parametri **unitari**
  (§7.11.1), resistenze di **tab. 7.11.III** (carico limite 1,2 · scorrimento 1,0 ·
  ribaltamento 1,0), sovraccarico ridotto con **ψ₂** e, per il solo ribaltamento,
  coefficiente sismico **maggiorato del 50%** (§7.11.6.2.1).

La card Coefficienti mostra le due colonne **Statica** (modificabile) e **Sismica**
(imposta dalla norma, in sola lettura, visibile con k~h~ > 0).

## Eurocodici e Utente

- **EC 7/8**: statica A1+M1+R2 + sismica con coefficienti unitari (EN 1998-5).
- **Utente**: una sola combinazione con i coefficienti della card e il sisma
  così com'è inserito — nessun automatismo.

## Dove si vedono

Nel tab **Verifiche** ogni combinazione è dichiarata con nome e coefficienti usati e
ogni card riporta il FS di tutte le combinazioni col badge *governante*; nel tab
**Rinforzi** puoi passare dall'**inviluppo di progetto** alle singole combinazioni.
La stabilità globale usa il proprio approccio A2+M2+R2.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MRE%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mre/docs/it/combinazioni.md).*
