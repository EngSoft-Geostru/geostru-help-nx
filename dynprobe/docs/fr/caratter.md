# Valeurs caractéristiques EC7 / NTC §6.2.2

## Pourquoi les valeurs caractéristiques

La norme géotechnique européenne (EC7 §2.4.5.2) et italienne (NTC 2018 §6.2.2) impose de concevoir sur les **valeurs caractéristiques** des paramètres, et non sur les valeurs moyennes. La valeur caractéristique tient compte de la variabilité naturelle du sol et de l'incertitude d'échantillonnage.

## Comment fonctionne le calcul

Dynamic Probing NX estime la valeur caractéristique de N_SPT pour chaque couche en appliquant des méthodes statistiques à la série de valeurs N recueillies dans la couche. Les méthodes disponibles sont :

| Méthode | Description |
|---|---|
| **Normale** | Estimation basée sur la moyenne et l'écart-type avec distribution gaussienne |
| **Lognormale** | Utile lorsque N_SPT présente une distribution asymétrique (fréquente avec des valeurs faibles) |
| **Student-t** | Corrigée pour les petits échantillons (n < 30) — tient compte de l'incertitude sur la moyenne |

Le niveau de confiance appliqué correspond à celui indiqué par EC7 pour la valeur caractéristique inférieure (5ᵉ percentile côté conservatif).

## Comment l'utiliser

Dans l'onglet **Estimation des paramètres** de l'Éditeur :

1. Sélectionnez la méthode statistique (Normale / Lognormale / Student-t).
2. Pour chaque couche sont affichés : la moyenne, l'écart-type, le nombre d'échantillons et la valeur caractéristique calculée.
3. La valeur caractéristique de N_SPT est propagée aux corrélations pour obtenir les valeurs caractéristiques de Cu, φ, Mo, Ey, etc.

!!! info "Échantillons minimaux"
    Avec moins de 3 mesures par couche, le calcul statistique a une faible significativité. L'application signale les cas avec n < 3 par un avertissement — dans ces cas, il est préférable d'utiliser une approche d'ingénierie conservative (par ex. minimum des valeurs observées).

## Valeurs caractéristiques dans le rapport

Le rapport Word exporté inclut le tableau des valeurs caractéristiques avec la méthode utilisée, la taille de l'échantillon et la valeur résultante — prêt à être annexé au rapport géotechnique.
