# Guide rapide — le premier projet en 5 minutes

Objectif : charger un fichier d'exemple, lire la stratigraphie et les principales corrélations, exporter le rapport.

## 1. Ouvrez l'application et créez un nouveau projet

Rendez-vous sur [nx.geostru.ai/dynprobe](https://nx.geostru.ai/dynprobe/). Cliquez sur **Nouveau fichier** dans le menu Fichier.  
Donnez un nom au projet (par ex. « Site rue de Rome ») et cliquez sur **Créer**.

Vous pouvez aussi utiliser un **fichier d'exemple** depuis l'écran d'accueil — vous découvrirez immédiatement toutes les sections déjà renseignées.

## 2. Ajoutez un essai

Dans le **Tableau de bord**, cliquez sur **+ Essai continu** (ou **+ Essai en forage** pour les SPT). Saisissez :

- **Sigle** : code d'identification de l'essai (par ex. `DP-1`)
- **Équipement** : sélectionnez-le dans le catalogue (DPM, DPSH, DPH, DPL…). L'équipement définit le poids du mouton, la hauteur de chute et le pas d'avancement — tous les paramètres énergétiques sont déjà tabulés en interne.
- **Coordonnées** : saisissez lat/lon pour positionner l'essai sur la carte (facultatif mais utile pour l'export du plan d'implantation).

## 3. Saisissez les mesures

Allez dans l'onglet **Mesures**. Vous disposez de trois modes :

- **Manuel** : saisissez le nombre de coups ligne par ligne.
- **Importer CSV** : collez ou chargez un fichier issu d'un datalogger — le système reconnaît automatiquement la profondeur et les coups.
- **Importer .dypx** : chargez directement un fichier exporté depuis le desktop GeoStru Dynamic Probing.

Le graphique N/profondeur se met à jour en temps réel.

## 4. Interprétez la stratigraphie

Allez dans l'onglet **Stratigraphie interprétée**. L'application propose une première couche sur toute la profondeur.

- Cliquez sur **+ Ajouter une couche** pour subdiviser le profil.
- Pour chaque couche, définissez la profondeur inférieure, le **type de terrain** (sol cohérent / sol pulvérulent / mixte) et le **poids volumique** γ.
- La méthode d'agrégation N_SPT par couche se choisit dans l'en-tête de la colonne (par défaut : moyenne). Voir [Stratigraphie →](stratigrafia.md) pour les 7 méthodes disponibles.

!!! tip "Couleurs et badges"
    Le badge **Σ couches / essai** en bas indique si la somme des profondeurs des couches coïncide avec la profondeur de l'essai (coche verte = cohérent, triangle jaune = écart à contrôler).

## 5. Lisez les corrélations

Onglet **Corrélations géotechniques** : pour chaque couche apparaît un tableau avec les paramètres estimés (Cu, φ, Mo, Ey, Vs, γ, Dr …) calculés à partir des formules de référence de la littérature géotechnique. Voir [Corrélations →](correlazioni.md).

!!! note
    Les corrélations sont des estimations empiriques. Utilisez-les comme point de départ — complétez-les toujours avec des données de laboratoire lorsqu'elles sont disponibles.

## 6. Contrôlez la catégorie de sol

Onglet **Cat. sol** : l'application calcule la vitesse équivalente V_s,30 et attribue automatiquement la catégorie NTC 2018. Voir [Catégorie →](categoria.md).

## 7. Exportez le rapport

Menu **Fichier → Enregistrer** pour télécharger le fichier `.dprobe`. Menu **Exporter → Rapport Word** pour le rapport complet.

En 5 minutes, vous avez :

- ✅ un essai avec des mesures
- ✅ une stratigraphie interprétée
- ✅ les paramètres géotechniques pour chaque couche
- ✅ la catégorie de sol
- ✅ le fichier de projet téléchargé
