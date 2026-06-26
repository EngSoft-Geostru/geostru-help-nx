# Format de fichier

## .dprobe — format natif NX

Le fichier `.dprobe` est le format de projet de Dynamic Probing NX. C'est un fichier **JSON** en clair, lisible avec n'importe quel éditeur de texte. Il contient :

- Métadonnées du projet (nom, site, maître d'ouvrage, coordonnées)
- Liste des essais avec toutes les mesures
- Bibliothèque d'appareils intégrée au fichier
- Stratigraphie interprétée (couches, profondeurs, type, γ)
- Paramètres des corrélations (auteurs préférés)
- Résultats calculés (corrélations, catégorie de sol, portances, estimation des paramètres)

Le fichier est **autonome et portable** : copiez-le sur un autre PC, ouvrez-le dans Dynamic Probing NX — tout fonctionne sans configuration supplémentaire.

## .dypx — format bureau GeoStru (importation)

Le fichier `.dypx` est le format d'exportation texte du logiciel bureau GeoStru Dynamic Probing. Dynamic Probing NX peut l'importer depuis l'écran d'accueil avec **Importer .dypx…**. Lors de l'import, sont lus :

- Tous les essais avec les mesures de coups
- Les données de l'appareil (type, β si présent)
- Les coordonnées des essais (si elles sont enregistrées dans le fichier bureau)

La stratigraphie et les corrélations ne sont pas importées depuis le bureau — elles doivent être ressaisies dans NX.

## CSV datalogger

De nombreux datalogger pour essais dynamiques exportent les données au format CSV ou TXT. Dynamic Probing NX reconnaît automatiquement le format si les colonnes sont structurées comme suit :

```
profondità, colpi
0.10, 8
0.20, 9
0.30, 11
...
```

Les colonnes peuvent être séparées par une virgule, un point-virgule ou une tabulation. Si le fichier comporte un en-tête avec les coordonnées du site (lat, lon, cote), elles sont lues automatiquement.

Pour importer : dans l'onglet **Mesures** de l'éditeur, cliquez sur **Importer des mesures depuis un fichier…** et sélectionnez le CSV. Vous pouvez aussi coller le contenu directement dans le champ texte de la fenêtre.

## AGS4 (.ags)

Dynamic Probing NX exporte au format AGS4 (v4.2) mais n'importe pas depuis AGS4. Voir [Exportation →](export.md).
