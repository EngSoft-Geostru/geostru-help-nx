# Questions fréquentes

## Pourquoi le volume change-t-il si je change de type de rejet ?

Parce que le débit de référence change. Le champ « débit constant sortant » ne
vaut que pour le rejet à débit constant ; pour un orifice en charge ou un
déversoir, HID utilise le débit que l'organe évacue réellement sous la charge de
projet. Voir [Système de rejet](scarico.md).

## Quelle méthode dois-je utiliser ?

Celle qu'exige le service instructeur. En cas de doute, laissez-en plusieurs
actives : HID retient le maximum, qui est la condition la plus sécuritaire.

## Pourquoi ne puis-je pas utiliser SCS-CN en Lombardia ?

Le règlement régional ne l'admet pas et impose la courbe GEV. HID applique la
contrainte et bloque le calcul en expliquant la raison.

## Je ne trouve pas ma commune

Le référentiel couvre les communes italiennes. Pour les autres pays, saisissez la
région et les coordonnées manuellement : le profil générique n'a pas besoin de la
commune.

## Comment travailler hors d'Italie ?

Choisissez **Autre / international** comme pays, ou cochez **Ignorer la
réglementation territoriale**. Le débit de fuite et le volume minimal, c'est vous
qui les imposez, selon ce que prescrit l'autorité locale.

## Le temps de vidange est vide

Il n'est calculé que pour le rejet à débit constant et pour l'infiltration
constante. Pour les autres organes, le débit dépend de la charge et varie au
cours de la vidange.

## Quelle différence entre méthode directe et méthode directe régionale ?

La méthode directe utilise les coefficients que vous saisissez. La méthode
régionale, prévue en Emilia-Romagna et Marche, utilise les coefficients fixes de
la réglementation (0,9 et 0,2) et l'exposant 0,48, et demande les surfaces avant
et après aménagement.

## Puis-je changer de langue une fois le travail commencé ?

Oui. Ce sont les libellés qui sont traduits, pas les données : les valeurs du
projet restent celles que vous avez saisies.

## La note de calcul sort en italien alors que l'application est en allemand

Cela ne devrait pas arriver : la note de calcul suit la langue sélectionnée. Si
c'est le cas, [signalez-le-nous](mailto:info@geostru.ai?subject=Help%20HID%20NX)
en précisant la langue et le format.

---

*Vous avez trouvé une erreur sur cette page ? [Signalez-la-nous](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
