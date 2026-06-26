# Catégorie de sol

## À quoi elle sert

La catégorie de sol détermine l'amplification sismique attendue pour le site et conditionne la valeur du paramètre **S** (coefficient d'amplification stratigraphique) dans les spectres de réponse NTC 2018.

Dynamic Probing NX calcule automatiquement la catégorie à partir des vitesses V_s des couches, dérivées des corrélations N_SPT → Vs.

## Normes prises en charge

| Norme | Paramètre de référence | Notes |
|---|---|---|
| **NTC 2018** (D.M. 17/01/2018) | V_s,30 | Méthode principale pour bâtiments et ouvrages |
| **NTC 2008** (D.M. 14/01/2008) | V_s,30 | Compatibilité avec les projets antérieurs |
| **Eurocode 8** (EN 1998-1) | V_s,30 | Référence européenne |

## Comment se calcule V_s,30

V_s,30 est la vitesse moyenne des ondes de cisaillement dans les 30 premiers mètres de profondeur, pondérée par les épaisseurs des couches. Pour une profondeur de sondage inférieure à 30 m, l'application utilise un substratum sismique par défaut (roche) pour les mètres manquants — cette valeur est configurable dans l'onglet **Cat. de sol**.

## Comment lire le résultat

Dans l'onglet **Cat. de sol** de l'Éditeur, vous trouvez :

- **V_s,eq** : vitesse équivalente calculée (m/s)
- **Catégorie** : lettre A / B / C / D / E (NTC 2018) avec description textuelle
- **Tableau des couches** : contribution de chaque couche au calcul de V_s,30

Le calcul se met à jour automatiquement chaque fois que vous modifiez la stratigraphie ou les vitesses V_s des couches.

!!! info "Vs issu d'essais en laboratoire"
    Si vous disposez de mesures directes de V_s (MASW, down-hole, cross-hole), vous pouvez remplacer la valeur V_s de chaque couche dans la colonne dédiée du tableau — le calcul de V_s,30 utilise les valeurs saisies manuellement à la place de celles estimées par les corrélations.

## Catégories NTC 2018

| Catégorie | Description |
|---|---|
| **A** | Massifs rocheux affleurants ou sols très raides (V_s,30 > 800 m/s) |
| **B** | Dépôts de sables, graviers compacts ou argiles raides (360 < V_s,30 ≤ 800 m/s) |
| **C** | Dépôts de sables, graviers moyennement compacts ou argiles de consistance moyenne (180 < V_s,30 ≤ 360 m/s) |
| **D** | Dépôts de sols granulaires lâches ou sols cohérents mous (V_s,30 ≤ 180 m/s) |
| **E** | Profils avec couches superficielles alluvionnaires de V_s < 360 m/s et d'épaisseur comprise entre certaines limites sur un substratum de catégorie A ou B |
