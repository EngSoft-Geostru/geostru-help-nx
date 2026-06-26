# Équipements — DPL · DPM · DPH · DPSH · SPT en forage

## Essais dynamiques continus

Dans l'essai dynamique continu, le mouton tombe de façon répétée et l'on compte le nombre de coups nécessaires pour faire avancer la pointe d'un pas fixe (typiquement 10 ou 20 cm). La séquence coups/profondeur est la matière première de tout le traitement.

Dynamic Probing NX prend en charge les quatre types normalisés par la **UNI EN ISO 22476-2** :

| Sigle | Type | Énergie par coup |
|---|---|---|
| **DPL** | Léger | basse |
| **DPM** | Moyen | moyenne |
| **DPH** | Lourd | élevée |
| **DPSH** | Super lourd | très élevée |

Chaque type possède une masse de mouton, une hauteur de chute et un diamètre de pointe définis par la norme. La bibliothèque d'équipements de l'application contient les modèles les plus répandus sur le marché, déjà tabulés — vous pouvez également ajouter un équipement personnalisé avec vos propres données d'étalonnage.

### Le coefficient de corrélation β

Le coefficient β convertit le nombre de coups de l'essai dynamique (N_DPM, N_DPSH…) en l'équivalent N_SPT. La valeur dépend de l'équipement et se détermine par des essais comparatifs in situ. Chaque équipement du catalogue possède un β par défaut ; vous pouvez le remplacer par la valeur de votre étalonnage spécifique.

## Essais SPT en forage

L'essai SPT (Standard Penetration Test, **UNI EN ISO 22476-3**) se réalise à l'intérieur d'un forage de sondage. Le carottier est battu sur 45 cm en trois tronçons de 15 cm :

- **N1** : premier tronçon (mise en place) — non comptabilisé
- **N2** + **N3** : deuxième et troisième tronçons → **N_SPT = N2 + N3**

Ajoutez un essai SPT en forage depuis le Tableau de bord avec le bouton **+ Essai en forage**. Définissez les cotes de début de chaque battage (par ex. 1,0 m — 2,5 m — 4,0 m) et, pour chacune, saisissez N1, N2, N3. L'application calcule automatiquement N_SPT et construit le profil.

### Stratigraphie des essais en forage

Pour les essais SPT en forage, la stratigraphie se saisit manuellement dans la section **Stratigraphie interprétée**, couche par couche, exactement comme pour les essais continus. Le N_SPT moyen par couche est calculé à partir des battages qui tombent dans la plage de profondeur de la couche.

## Bibliothèque d'équipements

Allez dans **Équipements** depuis la barre de navigation pour accéder à la bibliothèque. Vous pouvez :

- Visualiser les paramètres de chaque équipement (masse, hauteur de chute, diamètre de pointe, angle de pointe, pas, β)
- Ajouter un équipement personnalisé
- Modifier le β d'un modèle existant pour votre datalogger spécifique

Les équipements sont enregistrés dans le fichier de projet `.dprobe` — le fichier est autonome et portable sur un autre PC sans perdre les données d'étalonnage.
