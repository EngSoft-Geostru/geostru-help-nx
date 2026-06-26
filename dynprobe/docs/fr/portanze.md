# Capacité portante des fondations

## Fondations superficielles

Dynamic Probing NX calcule la **pression admissible** pour les fondations superficielles sur sols granulaires et cohérents selon les méthodes de référence de la littérature géotechnique. Les résultats sont exprimés en kPa.

### Méthodes disponibles

| Méthode | Type de sol | Notes |
|---|---|---|
| **Terzaghi-Peck** | Sables, graviers | Classique à partir de N_SPT, inclut la correction de tassement |
| **Meyerhof** | Sables, graviers | Tient compte de la forme et de la profondeur de la fondation |
| **Bazaraa** | Sables, graviers | Alternative conservative au Meyerhof |
| **Peck-Hanson-Thornburn** | Sables, graviers | Avec limite de tassement admissible |
| **Meigh-Hobbs** | Argiles | À partir de N_SPT pour les sols cohérents |
| **De Beer-Martens** | Sables | Méthode européenne |

### Données d'entrée requises

Dans l'onglet **Capacités portantes**, définissez :

- **Largeur de la fondation B** (m)
- **Profondeur d'encastrement D** (m depuis le niveau du sol)
- **Tassement admissible** (mm) — typiquement 25 mm pour les semelles filantes, 25–50 mm pour les semelles isolées
- **Couche de calcul** : la méthode utilise N_SPT de la couche dans laquelle est encastrée la fondation

### Lecture du résultat

Le tableau affiche la pression admissible q_amm pour chaque méthode. Le rapport présente toutes les méthodes en comparaison — choisissez celle la mieux adaptée au contexte stratigraphique.

!!! warning "Fondations sur argiles"
    Pour les fondations sur argiles, le calcul se base sur Cu dérivé de la corrélation N_SPT → Cu. Complétez par des essais de laboratoire (triaxial, consolidation) pour les projets définitifs.

## Fondations profondes — pieu battu (Meyerhof)

Pour les pieux battus, l'application met en œuvre la méthode de **Meyerhof** qui estime séparément :

- **Q_p** : capacité portante en pointe (contribution de la couche sous la pointe)
- **Q_l** : capacité portante latérale (contribution des couches traversées par le pieu)
- **Q_tot = Q_p + Q_l − W_p** : capacité portante totale nette du poids propre du pieu

### Données d'entrée requises

- **Diamètre du pieu** D (m)
- **Longueur du pieu** L (m)
- **Type de pieu** : la méthode Meyerhof distingue les pieux battus dans le sable et dans l'argile

Le calcul utilise les valeurs N_SPT des couches selon la distribution de profondeur définie dans la stratigraphie. La capacité portante totale est exprimée en kN.

!!! info "Coefficient de sécurité"
    La capacité portante admissible s'obtient en divisant la capacité portante ultime par le coefficient de sécurité global. Dynamic Probing NX indique la capacité portante ultime — l'application du coefficient de sécurité relève de la compétence du concepteur selon la norme applicable.
