# Stratigraphie interprétée

## Qu'est-ce que c'est

La stratigraphie interprétée est le modèle du sous-sol que vous obtenez à partir des mesures de l'essai. Vous définissez un certain nombre de couches — chacune avec une profondeur inférieure, un type de terrain et les poids volumiques γ et γ_sat — et le logiciel calcule pour chacune la valeur de N_SPT représentative, dont découlent ensuite les corrélations géotechniques.

## Comment la saisir

Dans l'onglet **Stratigraphie interprétée** de l'Éditeur :

1. La première couche part de 0 m. Définissez sa profondeur inférieure (par ex. 2,50 m).
2. Cliquez sur **+ Ajouter une couche** pour créer la couche suivante.
3. Pour chaque couche :
   - Définissez la **profondeur inférieure** (m à partir du terrain naturel).
   - Choisissez le **type de terrain** : `COES` (sol cohérent), `INCO` (sol pulvérulent) ou les deux si mixte — le type détermine quelles corrélations sont appliquées.
   - Saisissez **γ** (poids volumique sec ou naturel) et **γ_sat** (poids volumique saturé) en kN/m³.
   - Si vous le souhaitez, saisissez **clay (%)** et la **description** lithologique.

## Les 7 méthodes d'agrégation N_SPT

Pour chaque couche, les mesures qui tombent dans sa plage de profondeur sont agrégées avec la méthode choisie par l'utilisateur. Les méthodes disponibles sont :

| Méthode | Quand l'utiliser |
|---|---|
| **Moyenne** | Terrain homogène, variabilité limitée |
| **Minimum** | Approche conservative — on utilise la valeur la plus défavorable |
| **Maximum** | Estimation de la borne supérieure (par ex. pour la capacité portante en pointe) |
| **Moyenne − 1σ** | Approche statistique conservative |
| **Moyenne + 1σ** | Approche statistique non conservative |
| **RNC** (distribution normale) | Valeur caractéristique en probabilité selon EC7 §2.4.5.2 |
| **RC** (distribution log-normale) | Comme RNC mais avec distribution log-normale — préférable pour des N_SPT à valeurs basses |

La méthode se définit dans l'en-tête de la colonne N_SPT du tableau de stratigraphie et s'applique à toutes les couches simultanément.

!!! info "Quelle est la bonne méthode ?"
    La norme EC7 (et NTC §6.2.2) prescrit d'utiliser la **valeur caractéristique** du paramètre, définie comme la valeur ayant 5 % de probabilité d'être inférieure. Les méthodes RNC et RC se rapprochent de cette définition statistique. Pour les petits échantillons (< 6 mesures par couche), la moyenne reste la référence la plus robuste.

## Corrélation N_DPM → N_SPT

Pour les essais continus, le N_SPT de couche s'obtient à partir de N_DPM en appliquant le coefficient β (voir [Équipements →](strumenti.md)). Le produit N_DPM × β est le N_SPT équivalent pour chaque mesure ; l'agrégation est ensuite appliquée à ces valeurs équivalentes.

## Badge Σ couches / essai

En bas de l'écran de stratigraphie apparaît le badge :

```
Σ couches  X,XX m  /  essai  Y,YY m
```

- **Vert** (✓) : la somme des profondeurs des couches coïncide avec la profondeur de l'essai — la stratigraphie couvre l'essai entier sans lacunes.
- **Jaune** (⚠) : écart entre Σ couches et la profondeur de l'essai — vérifiez que la dernière couche atteint la fin de l'essai.
