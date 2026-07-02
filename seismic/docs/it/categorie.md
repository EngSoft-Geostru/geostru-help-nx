# Categorie di sottosuolo e topografia

I parametri $a_g$, $F_0$, $T_C^*$ valgono su **suolo rigido e superficie
orizzontale**. Il terreno reale e la forma del rilievo **amplificano** l'azione
sismica: le NTC lo tengono in conto con la categoria di sottosuolo e la
categoria topografica.

## Categoria di sottosuolo

Si assegna in base alla velocità equivalente delle onde di taglio nei primi
30 m ($V_{S,eq}$, o $V_{S,30}$):

| Cat. | Descrizione | $V_{S,eq}$ (m/s) |
|---|---|---|
| **A** | Ammassi rocciosi o terreni molto rigidi | > 800 |
| **B** | Rocce tenere e depositi molto addensati/consistenti | 360 – 800 |
| **C** | Depositi mediamente addensati/consistenti | 180 – 360 |
| **D** | Depositi scarsamente addensati/consistenti | 100 – 180 |
| **E** | Strati C o D (spessore 5–20 m) su substrato più rigido (A) | – |

Dalla categoria derivano due coefficienti:

- **$S_S$** — coefficiente di amplificazione **stratigrafica**
- **$C_C$** — coefficiente che modifica il periodo $T_C$ dello spettro:

$$ T_C = C_C \cdot T_C^* $$

$S_S$ e $C_C$ dipendono dalla categoria e da $F_0$, $a_g$ secondo le formule
della Tabella 3.2.IV delle NTC. PS Advanced li calcola in automatico una volta
scelta la categoria.

## Categoria topografica

Tiene conto dell'amplificazione dovuta alla morfologia (creste, pendii):

| Cat. | Descrizione | $S_T$ (max) |
|---|---|---|
| **T1** | Superficie pianeggiante, pendii isolati con inclinazione ≤ 15° | 1.0 |
| **T2** | Pendii con inclinazione > 15° | 1.2 |
| **T3** | Rilievi con larghezza in cresta molto minore che alla base, inclinazione 15°–30° | 1.2 |
| **T4** | Rilievi con larghezza in cresta molto minore che alla base, inclinazione > 30° | 1.4 |

Il coefficiente **$S_T$** varia con la posizione lungo il rilievo (massimo in
cresta, decrescente verso la base). Per T1 vale sempre 1.0.

## Accelerazione massima al sito

Combinando i due effetti si ottiene il coefficiente di amplificazione
complessivo e l'accelerazione massima attesa **alla superficie del sito**:

$$ S = S_S \cdot S_T \qquad a_{max} = S \cdot a_g $$

$a_{max}$ è il valore che entra nel calcolo dei
[coefficienti sismici](coefficienti.md) e definisce l'ordinata di partenza
dello [spettro](spettri.md).

!!! warning "La categoria di sottosuolo va giustificata"
    $S_S$ e $C_C$ incidono in modo forte sull'azione di progetto. La categoria
    di sottosuolo deve poggiare su indagini geofisiche o geotecniche adeguate:
    sceglierla "a favore di sicurezza" senza dati può sovrastimare l'azione, ma
    sceglierla troppo ottimisticamente la sottostima. Per un'analisi 1D
    completa della risposta sismica locale vedi
    [RSL III](https://help.nx.geostru.ai/rsl/).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20PS%20Advanced%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/seismic/docs/it/categorie.md).*
