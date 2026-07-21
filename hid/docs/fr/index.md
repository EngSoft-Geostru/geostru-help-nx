# HID NX — Invariance hydraulique

HID dimensionne les ouvrages de laminage pour l'**invariance hydraulique et
hydrologique** : il vérifie qu'un aménagement du sol n'augmente pas le débit
rejeté dans le milieu récepteur par rapport à la situation antérieure.

L'application compare en parallèle les méthodes de calcul que vous sélectionnez
et retient comme volume de rétention le **maximum des résultats**, afin que la
vérification reste valable quelle que soit la méthode exigée par le service
instructeur.

[**Ouvrir l'application**](https://nx.geostru.ai/hid/){ .md-button .md-button--primary }

![Interface de HID NX, section Données générales](img/01-dati-generali.png)

## À qui s'adresse l'application

Aux concepteurs d'ouvrages de laminage des eaux pluviales : ingénieurs
hydrauliciens, géologues et maîtres d'œuvre qui doivent joindre une note de
calcul d'invariance hydraulique à un permis de construire, à un plan
d'aménagement ou à une autorisation de rejet.

## Ce que l'application calcule

| Domaine | Contenu |
|---|---|
| Pluies | Courbe intensité-durée-fréquence (IDF) GEV ou à deux paramètres |
| Hyétogrammes | Chicago, uniforme, Sifalda, triangulaire |
| Pertes à l'écoulement | Coefficient de ruissellement, Horton, SCS-CN |
| Hydrogrammes | Méthode des isochrones et Nash |
| Dimensionnement | Exigences minimales, méthode des pluies, méthode directe, isochrones, procédure détaillée |
| Rejet | Huit organes, des orifices en charge aux puits d'infiltration |
| Vérifications | Hauteur utile, volume utile, temps de vidange |

## Réglementation

HID applique des **profils réglementaires** choisis en fonction du pays et de la
région. Le profil détermine quelles méthodes sont admises, quelles données sont
nécessaires, et si le débit de fuite et le volume minimal sont imposés par la
réglementation ou choisis par vous.

- **Lombardia** — R.R. 7/2017, mise à jour 2019, R.R. 3/2025 : courbe GEV
  obligatoire, SCS-CN exclu, criticité et débit de fuite déduits de la commune.
- **Emilia-Romagna et Marche** — méthode directe régionale avec n = 0,48.
- **Tout autre pays ou région** — profil générique : méthodes librement
  combinables, débit de fuite et volume minimal choisis par vous.

!!! note "Hors d'Italie"
    Là où il n'existe pas de référentiel des communes, la région et les
    coordonnées se saisissent manuellement. Ce n'est pas une anomalie : c'est le
    mode de travail prévu dans les pays qui ne disposent pas encore d'un profil
    dédié.

## Par où commencer

- [Guide rapide](quickstart.md) — le premier dimensionnement en cinq minutes
- [Flux de travail complet](workflow.md) — un projet réel du début à la note de calcul
- [Glossaire](glossario.md) — les termes du domaine, avec les symboles utilisés dans l'application

---

*Vous avez trouvé une erreur sur cette page ? [Signalez-la-nous](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
