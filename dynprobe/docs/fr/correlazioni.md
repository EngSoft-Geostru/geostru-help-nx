# Corrélations géotechniques

## Ce qu'elles sont

Les corrélations géotechniques transforment N_SPT en paramètres de résistance et de déformabilité du sol. Ce sont des formules empiriques issues de la littérature internationale — leur utilisation est consolidée dans la pratique géotechnique, mais elles restent des estimations : complétez-les toujours par des données de laboratoire lorsqu'elles sont disponibles.

## Comment les lire

Dans l'onglet **Corrélations** de l'Éditeur, pour chaque couche de la stratigraphie apparaît un tableau présentant les valeurs calculées. La colonne de gauche indique le paramètre, les colonnes suivantes les valeurs selon les différents auteurs de référence. Vous pouvez activer ou désactiver chaque auteur à l'aide des interrupteurs en haut de la colonne.

La **valeur préférée** (⭐) alimente l'onglet **Synthèse des paramètres** et le rapport Word.

## Paramètres pour sols cohérents (COES)

| Paramètre | Signification |
|---|---|
| **Cu** | Cohésion non drainée (kPa) |
| **Mo** | Module œdométrique (MPa) |
| **Ey** | Module de Young (MPa) |
| **Vs** | Vitesse des ondes de cisaillement (m/s) |
| **γ** | Poids volumique (kN/m³) |
| **Classification** | Consistance (très molle → très raide) |

Auteurs de référence cités dans la littérature géotechnique italienne et internationale : Terzaghi-Peck, Schmertmann, Ohta-Goto, et d'autres.

## Paramètres pour sols pulvérulents (INCO)

| Paramètre | Signification |
|---|---|
| **Dr** | Densité relative (%) |
| **φ** | Angle de frottement interne (°) |
| **φ_160** | Angle de frottement sur N_1,60 normalisé (°) |
| **Mo** | Module œdométrique (MPa) |
| **Ey** | Module de Young (MPa) |
| **Vs** | Vitesse des ondes de cisaillement (m/s) |
| **ν** | Coefficient de Poisson |
| **G** | Module de cisaillement (MPa) |

Auteurs de référence : Meyerhof, Peck, Hanson, Thornburn, Ohta-Goto, Seed-Idriss, et d'autres.

!!! warning "Limites de validité"
    Chaque corrélation a été développée sur une certaine plage de N_SPT et sur des types de sol spécifiques. Lorsque N_SPT est très faible (< 3) ou très élevé (> 50), les résultats doivent être interprétés avec prudence. L'application met en évidence les valeurs hors plage.

## Enveloppe des paramètres

Lorsque vous disposez de plusieurs essais sur le même site, l'onglet **Enveloppe** affiche pour chaque couche la plage min-max des paramètres entre tous les essais, avec le **critère de projet** sélectionnable (minimum / moyenne / maximum / valeur préférée ⭐). La valeur de projet alimente automatiquement la Synthèse.

## Synthèse des paramètres

L'onglet **Synthèse** rassemble dans un seul tableau les valeurs géotechniques caractéristiques de chaque couche — utile comme tableau récapitulatif à insérer dans le rapport géotechnique. Le rapport Word l'inclut automatiquement.
