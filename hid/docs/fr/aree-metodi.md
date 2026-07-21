# Surfaces et méthodes de calcul

## Surfaces actives

Chaque ligne du tableau correspond à une surface homogène en usage et en
perméabilité. Il faut renseigner la description, le type, l'aire en m² et le
coefficient de ruissellement φ après aménagement.

![Définition des surfaces](img/02-aree-metodi.png)

Le type de surface (imperméable, semi-imperméable, perméable) est une étiquette
descriptive qui suggère l'ordre de grandeur de φ ; la valeur qui entre dans le
calcul est toujours celle que vous saisissez.

HID calcule le **coefficient de ruissellement pondéré** :

$$\varphi_{pond} = \frac{\sum \varphi_i \cdot S_i}{\sum S_i}$$

et la **surface active équivalente** $S_{pond} = S_{tot} \cdot \varphi_{pond}$,
c'est-à-dire la surface imperméable équivalente.

## Les méthodes de dimensionnement

HID distingue les méthodes **universelles**, valables partout, de celles qui sont
**propres à un profil réglementaire** et n'existent que là où la réglementation
les prescrit.

### Exigences minimales

Volume spécifique par hectare imposé par la réglementation en fonction de la zone
de criticité. En Lombardia, il vaut 800, 500 ou 400 m³/ha selon la zone A, B ou C
et la version réglementaire. Là où la réglementation ne le prescrit pas, c'est
vous qui imposez le volume minimal.

### Méthode des pluies

Elle équilibre le volume entrant et le volume rejeté à débit constant, en
cherchant la durée qui maximise le volume de rétention. C'est la méthode la plus
répandue pour les vérifications rapides.

!!! note "Durées inférieures à l'heure"
    Lorsque la durée critique descend au-dessous de l'heure, HID utilise
    l'exposant n₁ de la courbe, comme prévu. Il n'arrondit pas la durée à une
    heure : le faire sous-estime le volume, et c'est une erreur que nous avons
    corrigée en validant l'application par rapport à la version précédente.

### Méthode des isochrones

Elle introduit le temps de concentration du bassin et tient donc compte de la
forme de l'hydrogramme. Elle restitue la durée critique et le volume.

### Méthode directe

Elle compare les volumes de rétention spécifiques avant et après aménagement à
travers le rapport des coefficients de ruissellement. En Emilia-Romagna et
Marche, la réglementation prescrit une variante à coefficients fixes, que HID
présente comme une méthode distincte, la **méthode directe régionale**, visible
uniquement dans ces régions.

### Procédure détaillée

C'est la simulation complète : hyétogramme de projet, pertes à l'écoulement,
hydrogramme de crue et laminage de l'ouvrage de rétention pas à pas. C'est la
méthode la plus lourde et la plus défendable.

## Comment le volume est retenu

HID calcule toutes les méthodes sélectionnées et adopte comme volume admissible
le **maximum** des résultats. La méthode proposée par la réglementation est
indiquée sous les cases, mais elle ne limite pas les méthodes que vous pouvez
calculer.

---

*Vous avez trouvé une erreur sur cette page ? [Signalez-la-nous](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
