# Exportation et rapport

## Rapport Word (.docx)

Le rapport Word est le rapport de calcul complet, prêt à être joint à la documentation de projet. Il se génère depuis le menu **Exporter → Rapport**.

Le document comprend :

- En-tête avec les données du site (nom, maître d'ouvrage, coordonnées, date)
- Fiche de l'appareil : type, paramètres techniques, β utilisé
- Profil des mesures coups N/profondeur (graphique)
- Tableau de stratigraphie : couches, profondeurs, type de sol, N_SPT par couche
- Tableau des corrélations géotechniques pour chaque couche (auteurs sélectionnés)
- Catégorie de sous-sol : V_s,eq, catégorie attribuée, tableau des couches
- Portance des fondations (si calculée) : tableau comparatif des méthodes
- Valeurs caractéristiques EC7 / NTC §6.2.2 (si calculées)

## AGS4 (.ags)

Le format **AGS4** est le standard ouvert pour l'échange de données géotechniques (AGS Data Format v4.2). Exportez-le depuis le menu **Exporter → AGS4** pour partager les données d'essai avec d'autres logiciels ou avec le maître d'ouvrage.

Les groupes inclus dans l'export AGS4 : TRAN, PROJ, LOCA, GEOL, DPRG (paramètres de l'essai dynamique), DPRB (mesures).

## GeoSection (.geosection)

Exportez les essais avec la stratigraphie interprétée vers **GeoSection NX** pour construire la coupe géologique. Depuis le menu **Exporter → GeoSection** : sélectionnez les essais à inclure (ceux qui ont des coordonnées), cliquez sur **Exporter**. Le fichier `.geosection` s'ouvre directement dans l'application GeoSection.

## Plan (image PNG)

Si les essais ont des coordonnées attribuées, le menu **Exporter → Plan (image)** permet d'obtenir une image PNG du plan avec la position des essais, les cotes et les distances entre essais. Disponible uniquement avec au moins 2 essais géoréférencés.

## KMZ (Google Earth)

Le menu **Exporter → KMZ** génère un fichier visualisable dans Google Earth avec la position de tous les essais géoréférencés du projet.

## Fichier de projet (.dprobe)

Le fichier `.dprobe` est le format natif de Dynamic Probing NX — un JSON lisible qui contient toutes les informations du projet (essais, appareils, stratigraphie, corrélations, données du site). Il se sauvegarde depuis le menu **Fichier → Enregistrer** et se rouvre depuis l'Accueil avec **Ouvrir un fichier…**.

!!! tip "Compatibilité bureau"
    Vous pouvez importer un fichier `.dypx` (format texte du logiciel bureau GeoStru Dynamic Probing) depuis l'Accueil de Dynamic Probing NX. En revanche, le fichier `.dprobe` NX n'est pas ouvrable avec la version bureau.
