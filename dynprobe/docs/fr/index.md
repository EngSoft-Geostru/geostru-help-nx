# Dynamic Probing NX

> Traitement des **essais de pénétration dynamique** (DPL · DPM · DPH · DPSH) et des **SPT en forage** — stratigraphie automatique, corrélations géotechniques, catégorie de sol NTC 2018, capacité portante des fondations superficielles et profondes, valeurs caractéristiques EC7 / NTC §6.2.2.

[**Ouvrir l'application**](https://nx.geostru.ai/dynprobe/){ .md-button .md-button--primary }
[Guide rapide (5 minutes)](quickstart.md){ .md-button }

---

## En bref

- **Ce qu'elle fait** : lit les mesures de terrain d'un essai dynamique continu ou d'une série d'essais SPT en forage, restitue la stratigraphie interprétée avec les paramètres géotechniques caractéristiques et les vérifications de capacité portante, le tout conforme aux normes en vigueur (NTC 2018, NTC 2008, EC8, Eurocode 7).
- **Pour qui** : géologues et ingénieurs géotechniciens qui doivent traiter des sondages dynamiques, classer le profil stratigraphique et produire le rapport de calcul.
- **En combien de minutes** : 5 (cas avec fichier .dypx d'exemple) → 30 (cas réel complet avec stratigraphie, corrélations et capacité portante).

## Flux de travail type

1. Ouvrez l'application : `nx.geostru.ai/dynprobe/`
2. Créez un nouveau fichier ou importez un `.dypx` du desktop GeoStru ou un CSV depuis un datalogger.
3. Allez dans **Données générales** et complétez les informations du site (nom, coordonnées, équipement, maître d'ouvrage).
4. Saisissez (ou contrôlez) les **mesures de coups** dans l'onglet Mesures : l'application les affiche immédiatement dans le graphique N/profondeur.
5. Passez à la **Stratigraphie interprétée** : définissez le nombre de couches, les limites et le type de terrain (sol cohérent / sol pulvérulent). L'application calcule le N_SPT moyen par couche avec la méthode choisie.
6. Consultez les **Corrélations géotechniques** — pour chaque couche, un tableau avec les paramètres dérivés (Cu, φ, Mo, Ey, Vs, γ …).
7. Vérifiez la **Catégorie de sol** selon NTC 2018 / NTC 2008 / EC8.
8. Si nécessaire, calculez la **Capacité portante** d'une fondation superficielle ou profonde (pieu battu Meyerhof).
9. Lisez les **Valeurs caractéristiques** EC7 / NTC §6.2.2 dans l'onglet dédié.
10. Exportez le **rapport Word** (Report) ou le fichier de projet `.dprobe`.

## Chapitres du manuel

| Chapitre | Contenu |
|---|---|
| [Guide rapide](quickstart.md) | Du chargement du fichier au premier résultat en 5 minutes |
| [Équipements](strumenti.md) | DPL, DPM, DPH, DPSH, SPT en forage — comment les saisir et les paramètres pertinents |
| [Stratigraphie interprétée](stratigrafia.md) | Comment définir les couches, les 7 méthodes d'agrégation N_SPT |
| [Corrélations géotechniques](correlazioni.md) | Paramètres dérivés pour sols cohérents et pulvérulents, auteurs de référence |
| [Catégorie de sol](categoria.md) | NTC 2018, NTC 2008, EC8 — données d'entrée, logique de calcul, lecture du résultat |
| [Capacité portante des fondations](portanze.md) | Fondations superficielles (6 méthodes) et profondes (pieu battu Meyerhof) |
| [Valeurs caractéristiques](caratter.md) | EC7 §2.4.5.2 / NTC §6.2.2 — normale, lognormale, Student-t |
| [Exportation et rapport](export.md) | Rapport Word, AGS4, GeoSection, plan d'implantation, KMZ |
| [Format de fichier](formati.md) | `.dprobe` (JSON NX) · `.dypx` (desktop) · CSV datalogger |
| [Ressources et exemples](risorse.md) | Fichiers d'exemple téléchargeables |
| [FAQ](faq.md) | Questions fréquentes |
