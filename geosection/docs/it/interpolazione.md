# Interpolazione della sezione

Quando hai caricato il profilo topografico e almeno 2 sondaggi, GeoSection
costruisce la **sezione geologica continua** interpolando i contatti
stratigrafici tra i sondaggi proiettati sulla traccia.

## Proiezione dei sondaggi sulla traccia

Ogni sondaggio ha coordinate `(x, y)` nel piano. La traccia di sezione è una
polilinea sullo stesso piano. La proiezione è la **distanza ortogonale** del
sondaggio sul tratto della polilinea più vicino:

- distanza progressiva sulla traccia: ascissa del piede della perpendicolare;
- distanza laterale: quanto è lontano il sondaggio dalla traccia (mostrata in
  legenda — un sondaggio a >50 m dalla traccia va valutato con cautela).

I sondaggi appaiono nella sezione come **colonne verticali** alla loro ascissa
proiettata, con la testa alla quota indicata e gli strati colorati a profondità.

## Interpolazione dei contatti stratigrafici

L'algoritmo classico è una **interpolazione lineare a tratti** tra contatti
omologhi (stesso codice strato `layer`) di sondaggi adiacenti:

1. Per ciascun sondaggio si calcolano le **quote assolute** dei contatti
   (quota_testa - profondità).
2. Tra due sondaggi adiacenti che hanno entrambi un contatto del layer X,
   si traccia un segmento di retta che li unisce.
3. Se uno dei due manca, il contatto **si estende orizzontalmente** fino al
   bordo del dominio o al sondaggio successivo dove ricompare.

Il risultato è una serie di **poligoni stratigrafici** colorati che riempiono
la sezione tra topografia e contatti.

## AI: descrizione automatica della sezione

Premendo *AI → Descrivi sezione* il chat invia un riepilogo testuale della
geometria al modello multimodale:
- numero di strati e relativa codifica;
- successione stratigrafica (dall'alto in basso);
- presenza di lenti, eteropie, discontinuità riconoscibili;
- profondità della falda e estensione.

Restituisce un paragrafo descrittivo da incollare nella relazione tecnica.
Usa Gemini 1.5 Pro lato server.

!!! note "Quando l'AI sbaglia"
    L'interpretazione AI è **descrittiva**, non geomeccanica: descrive cosa
    vede sulla sezione, non sostituisce il giudizio del geologo. Su sezioni
    con strati molto sottili (<50 cm) o sondaggi molto distanti (>200 m) la
    descrizione tende a generalizzare troppo.

## Falda

Se nei sondaggi è indicato il livello della falda (campo `wstk_depth` in AGS4
o colonna analoga in CSV), GeoSection traccia una **linea blu spezzata**
che congiunge i livelli idrici dei sondaggi adiacenti. Non interpola fra strati
permeabili e impermeabili — è una proiezione geometrica.

Per modificare manualmente la falda: pannello *Discontinuità → Falda* →
edita i punti.

## Lenti e contatti manuali

Per casi che l'algoritmo lineare non gestisce bene (es. lenti chiuse, strato
mancante al centro per discordanza erosiva) si usano i **contatti manuali**:

1. Pannello *Stratigrafia → Contatti*.
2. Aggiungi un contatto digitando ascissa progressiva (m) + quota (m s.l.m.) +
   layer di sopra/sotto.
3. La sezione si rigenera automaticamente includendo il contatto manuale.

Questo permette di rappresentare lenti, discordanze, faglie, intrusioni —
anche quando i sondaggi non le intercettano direttamente.
