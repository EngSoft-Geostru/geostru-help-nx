# Geometria della sezione

- **H** — altezza della terra rinforzata [m].
- **B** — base del blocco rinforzato [m].
- **α** — inclinazione del paramento esterno [°], valori tipici 45÷90. Definisce la
  forma della sezione (2D/3D); le verifiche del kernel usano la parete verticale
  equivalente, a favore di sicurezza per paramenti inclinati.
- **α~s~ (scavo interno)** — inclinazione della faccia a monte del blocco: **0 =
  parallela al paramento**; se impostata deve stare fra l'angolo di resistenza al
  taglio del terreno spingente e 90° (uno scavo non sostenuto più dolce di φ non è
  congruente).
- **β** — inclinazione del terrapieno a monte [°]; deve essere minore di φ del
  terreno spingente.
- **D** — profondità del piano di posa [m].

I colori di terrapieno e piano di posa si scelgono direttamente nella card Geometria;
quelli dei terreni nelle rispettive card dei Parametri geotecnici.

!!! warning "Passo dei rinforzi e altezza"
    Se H è un multiplo esatto del passo s, l'ultimo rinforzo cadrebbe alla base dove
    il cuneo ha lunghezza nulla: il programma lo segnala e chiede di variare
    leggermente s o H.
