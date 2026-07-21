# Formats de fichier

## Projet `.hid`

HID enregistre le projet dans un fichier `.hid`, qui est du JSON lisible avec
n'importe quel éditeur de texte.

```json
{
  "schemaVersion": 2,
  "name": "Esempio 9.4 — Procedura dettagliata",
  "general": { "country": "IT", "region": "", "regulationVersion": "rr-2017" },
  "surfaces": [ { "description": "Area impermeabile", "areaM2": 4000, "runoffPost": 0.95 } ],
  "rainfall": { "kind": "twoParameters", "a": 35.04, "n": 0.421 }
}
```

Le champ `schemaVersion` protège contre l'ouverture de fichiers produits par des
versions plus récentes de l'application : si le numéro est supérieur à celui
pris en charge, HID refuse le fichier plutôt que de le lire de travers.

!!! note "Remarque"
    Les données d'entrée exigées par la réglementation résident dans un
    dictionnaire `jurisdictionInputs`. C'est ainsi que l'ajout de la prise en
    charge d'un nouveau pays ne modifie pas le format du fichier : les projets
    déjà enregistrés restent lisibles.

## Enregistrement et ouverture

- **Enregistrer** télécharge le fichier `.hid` sur votre ordinateur.
- **Ouvrir** charge un fichier `.hid` existant.
- **GeoDropbox** enregistre et rouvre le projet depuis l'espace cloud GeoStru,
  accessible depuis la même barre d'outils.

## Note de calcul

Depuis le menu **Note de calcul**, choisissez le format :

| Format | Extension | Remarques |
|---|---|---|
| Word | `.docx` | Toujours disponible |
| PDF | `.pdf` | Nécessite le convertisseur côté serveur |
| Word 97 | `.doc` | Nécessite le convertisseur côté serveur |

Si PDF et Word 97 n'apparaissent pas dans le menu, c'est que le convertisseur
n'est pas disponible sur ce serveur : utilisez le format Word.

La note de calcul contient les références réglementaires, les données générales,
les surfaces actives, la courbe IDF, les paramètres hydrologiques, le
hyétogramme, le dimensionnement, le système de rejet, les vérifications finales
et l'hydrogramme, avec les graphiques incorporés.

!!! tip "Conseil"
    La note de calcul est produite dans la langue sélectionnée dans la barre
    d'outils. Changez de langue avant de la générer si vous la remettez à une
    autorité étrangère.

---

*Vous avez trouvé une erreur sur cette page ? [Signalez-la-nous](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
