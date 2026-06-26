# Questions fréquentes

## Général

??? question "Quelle est la différence entre Dynamic Probing NX et le Dynamic Probing bureau ?"
    Le logiciel bureau GeoStru Dynamic Probing est la version historique Windows. Dynamic Probing NX est la version web, accessible depuis n'importe quel navigateur sans installation. Les fonctionnalités principales sont équivalentes ; NX ajoute la prise en charge multi-essais (gestion d'un site entier avec N essais), la carte interactive, l'export AGS4 et l'intégration avec GeoSection NX. Les données du bureau s'importent dans NX via le format `.dypx`.

??? question "Les données sont-elles enregistrées sur le serveur ?"
    Non — Dynamic Probing NX est **local-first** : les données du projet résident dans votre navigateur (localStorage) et ne sont enregistrées sur votre PC que lorsque vous exportez le fichier `.dprobe`. Aucune donnée de projet n'est envoyée aux serveurs GeoStru.

??? question "Puis-je l'utiliser hors ligne ?"
    Une connexion est nécessaire pour le chargement initial de l'application. Une fois chargée, l'application fonctionne aussi hors ligne pour la saisie des données et les calculs (sauf la génération du rapport Word, qui nécessite la connexion).

??? question "Existe-t-il une version mobile ?"
    L'application est conçue pour ordinateur de bureau/tablette. Sur smartphone, la navigation fonctionne mais la saisie des mesures sur de très petits écrans est peu pratique.

## Appareils et mesures

??? question "Comment ajouter un appareil qui n'est pas au catalogue ?"
    Allez dans **Appareils** depuis la barre de navigation → **+ Ajouter un appareil**. Saisissez : nom, type (DPL/DPM/DPH/DPSH), masse du mouton (kg), hauteur de chute (m), diamètre de la pointe (mm), angle de la pointe (°), pas d'avancement (m), et le coefficient β. L'appareil est enregistré dans le fichier de projet.

??? question "Mon CSV n'est pas reconnu correctement. Comment le formater ?"
    Assurez-vous que les deux premières colonnes soient la profondeur (m) et les coups (entier), séparées par une virgule, un point-virgule ou une tabulation. Supprimez les lignes d'en-tête qui ne respectent pas ce format, ou insérez-les comme commentaires avec `#` en début de ligne. Si les coordonnées figurent dans l'en-tête, utilisez le format : `# lat=41.9028 lon=12.4964 quota=120`.

??? question "Puis-je exclure des mesures du calcul ?"
    Oui — dans l'onglet Mesures, chaque ligne dispose d'une case à cocher pour l'exclure. Les mesures exclues n'entrent ni dans l'agrégation N_SPT par couche ni dans les corrélations. Utile pour écarter les valeurs anormales (refus anticipé, perte de boue).

## Stratigraphie

??? question "Comment choisir la méthode d'agrégation N_SPT ?"
    Cela dépend de l'objectif. Pour une estimation moyenne conservative, utilisez **Moyenne − 1σ**. Pour la valeur caractéristique EC7, utilisez **RNC** (distribution normale) ou **RC** (log-normale). Si vous avez peu de mesures par couche (< 4), préférez la Moyenne simple ou le Minimum. Voir [Stratigraphie →](stratigrafia.md) pour la description complète des 7 méthodes.

??? question "Le badge Σ couches est jaune — qu'est-ce que cela signifie ?"
    La somme des profondeurs inférieures des couches ne coïncide pas avec la profondeur de l'essai. Vérifiez que la dernière couche atteigne exactement la profondeur de fin d'essai (par ex. si l'essai fait 12,00 m, la limite inférieure de la dernière couche doit être 12,00 m).

## Corrélations

??? question "Pourquoi certaines valeurs de corrélation sont-elles affichées en — ?"
    Pour certaines combinaisons type de sol / auteur, le paramètre n'est pas défini. Par exemple, Dr (densité relative) n'est défini que pour les sols pulvérulents : dans les couches cohérentes, la cellule affiche —. De même, Cu (cohésion non drainée) n'est défini que pour les sols cohérents.

??? question "Puis-je saisir les valeurs de laboratoire au lieu des corrélations ?"
    Actuellement, l'application utilise les corrélations à partir de N_SPT comme source primaire. Pour le calcul de la portance, vous pouvez saisir directement Cu ou φ dans les champs de la couche dans la stratigraphie — ces valeurs remplacent celles obtenues par corrélation.

## Export et rapport

??? question "Le rapport Word est-il modifiable ?"
    Oui — c'est un fichier `.docx` standard ouvert dans Word, LibreOffice ou Google Docs. Vous pouvez personnaliser l'en-tête, ajouter le logo de votre bureau d'études et modifier le texte descriptif. Les tableaux numériques sont des données statiques (pas des formules Excel).

??? question "Puis-je exporter en PDF ?"
    Pas directement depuis l'application. Ouvrez le `.docx` généré dans Word et utilisez **Fichier → Imprimer → Enregistrer au format PDF**.

??? question "AGS4 : quels groupes sont exportés ?"
    Sont inclus les groupes : TRAN (données de transmission), PROJ (projet), LOCA (position des essais), GEOL (stratigraphie), DPRG (paramètres de l'essai dynamique), DPRB (mesures de coups). Les corrélations et les portances ne sont pas exportées — ces résultats élaborés ne relèvent pas du standard AGS4 pour les essais dynamiques.
