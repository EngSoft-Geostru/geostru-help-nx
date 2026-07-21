# Dimensionnement de l'ouvrage de rétention

## Hyétogramme de projet

Le hyétogramme répartit dans le temps la hauteur de pluie donnée par la courbe.

| Type | Quand l'utiliser |
|---|---|
| **Chicago** | Le plus répandu : pic positionnable avec le coefficient r |
| **Uniforme** | Intensité constante pendant toute la durée |
| **Sifalda** | Trois tronçons, forme trapézoïdale |
| **Triangulaire** | Montée et descente linéaires |

Pour le hyétogramme de Chicago, le **coefficient de position r** indique où tombe
le pic : 0,4 signifie à 40 % de la durée.

![Hyétogramme et pertes à l'écoulement](img/05-depurazione-piogge.png)

## Pertes à l'écoulement

Elles transforment la pluie brute en pluie nette, c'est-à-dire celle qui devient
ruissellement.

- **Pourcentage** — multiplie par le coefficient de ruissellement φ de la
  surface. C'est le modèle le plus simple et le plus utilisé.
- **Horton** — infiltration décroissante dans le temps selon la classe de sol.
- **SCS-CN** — méthode du curve number, avec condition d'humidité antécédente
  AMC I, II ou III.

!!! warning "Lombardia"
    La méthode SCS-CN n'est pas admise par le règlement régional.

## Hydrogramme

Il transforme la pluie nette en débit :

- **Isochrones** — utilise le temps de concentration de la surface.
- **Nash** — cascade de n réservoirs linéaires de constante K, pour les bassins
  plus complexes.

## Laminage

L'ouvrage de rétention est routé pas à pas en résolvant le bilan de masse entre
le débit entrant, le débit sortant de l'organe de rejet et le volume stocké. Le
maximum du volume est le résultat de la procédure détaillée.

![Calculs et vérifications](img/06-calcoli-verifiche.png)

## Les vérifications finales

| Vérification | Condition |
|---|---|
| Hauteur utile | H de projet ≥ hauteur requise |
| Volume utile | V de projet ≥ volume admissible |
| Temps de vidange | T ≤ temps admis (en règle générale 48 h) |

Le temps de vidange n'est calculé que pour les rejets à débit constant et pour
l'infiltration constante : pour les autres organes, le débit dépend de la charge
et varie au cours de la vidange.

---

*Vous avez trouvé une erreur sur cette page ? [Signalez-la-nous](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
