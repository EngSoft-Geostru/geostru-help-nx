# Guide rapide

Cinq minutes entre l'ouverture de l'application et le volume de rétention
vérifié. Nous utiliserons l'exemple préchargé du manuel, afin que les valeurs
affichées soient comparables.

## 1. Ouvrez l'application et chargez l'exemple

Rendez-vous sur [nx.geostru.ai/hid](https://nx.geostru.ai/hid/). Au démarrage,
l'**exemple 9.4 — Procédure détaillée** est déjà chargé : trois surfaces pour un
total de 10 000 m².

![Barre d'outils de HID](img/00-toolbar.png)

Toutes les commandes se trouvent dans la barre supérieure : **Nouveau**,
**Ouvrir**, **Enregistrer**, **Note de calcul**, et à droite le bouton
**Calculer**.

## 2. Contrôlez les surfaces

Ouvrez la section **2. Surfaces et méthodes**. Chaque ligne est une surface avec
son aire et son coefficient de ruissellement φ.

![Définition des surfaces et choix des méthodes](img/02-aree-metodi.png)

Le bandeau coloré affiche les valeurs agrégées : surface totale, φ pondéré,
surface active équivalente et débit de fuite. En dessous, choisissez les méthodes
à comparer.

!!! tip "Conseil"
    Laissez plusieurs méthodes actives. HID les calcule toutes et retient le
    maximum : c'est la condition la plus sécuritaire et cela vous évite de
    refaire le travail si le service instructeur demande une autre méthode.

## 3. Vérifiez la courbe de pluie

Section **3. Courbe IDF**. Avec la courbe à deux paramètres, saisissez `a` et
`n` ; avec la GEV, saisissez les paramètres de la distribution et la période de
retour.

![Courbe intensité-durée-fréquence](img/03-curva-pluviometrica.png)

## 4. Calculez

Appuyez sur **Calculer** en haut à droite. Allez à la section **6. Calculs et
vérifications**.

![Résultats du dimensionnement](img/06-calcoli-verifiche.png)

Chaque méthode dispose de sa fiche avec le volume calculé. Le bandeau inférieur
indique le **volume admissible** retenu, la hauteur correspondante et le temps de
vidange.

Pour l'exemple 9.4, vous devez lire : méthode directe 234,89 m³, isochrones
169,51 m³, procédure détaillée 175,74 m³, méthode des pluies 175,58 m³. Le volume
retenu est de **234,89 m³**.

## 5. Produisez la note de calcul

Ouvrez le menu **Note de calcul** dans la barre et choisissez le format : Word,
PDF ou Word 97. Le document est produit dans la langue sélectionnée dans
l'application.

---

*Vous avez trouvé une erreur sur cette page ? [Signalez-la-nous](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
