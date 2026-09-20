# Le fonti

Il catalogo delle fonti che il fascicolo interroga. Sono tutte **pubbliche**, con licenza
dichiarata; ogni evidenza riporta l'ente, la licenza, la data e l'ora della richiesta (UTC),
l'esito e il link all'interrogazione originale. Nel Word, al posto degli indirizzi tecnici,
trovi il **portale** dell'ente dove le stesse carte si consultano.

## Ubicazione

| Fonte | Ente · licenza | Cosa restituisce |
|---|---|---|
| Limiti amministrativi | ISPRA — Servizio Geologico d'Italia · CC BY 4.0 | Regione, Provincia, Comune e codice ISTAT del punto. È la prima interrogazione: le altre ne hanno bisogno |
| Particella catastale al punto | Agenzia delle Entrate — cartografia catastale INSPIRE · CC BY 4.0 | Comune catastale, foglio, allegato e particella. **Identificazione cartografica, senza valore certificativo**; con un perimetro, le particelle campionate |
| Inquadramento territoriale | base cartografica configurata | Tavola 8 km su base stradale |
| Ubicazione su immagine satellitare | immagini del fornitore configurato | Tavola 1 km su satellite |

## Geologia

| Fonte | Ente · licenza | Cosa restituisce |
|---|---|---|
| Carta Geologica d'Italia 1:100.000 | ISPRA — SGI · CC BY 4.0 | L'unità geologica al punto (legenda, sigla, foglio); con un perimetro, tutte le unità intersecate |
| Tavola geologica 1:100.000 | ISPRA — SGI · CC BY 4.0 | Tavola 6 km della stessa carta |
| Carta litologica (CARG) | ISPRA — SGI · CC BY 4.0 | La litologia al punto **dove la carta esiste** (oggi: Valle d'Aosta, Sardegna, Marche); altrove l'esito è «nulla al punto» |

!!! note "Scala"
    La carta 1:100.000 è un inquadramento: le unità cartografiche non assegnano spessori né
    proprietà al sottosuolo. Le carte regionali di dettaglio sono in programma.

## Sismicità

| Fonte | Ente · licenza | Cosa restituisce |
|---|---|---|
| Classificazione sismica e accelerazioni massime | ISPRA (dati INGV-DPC) · CC BY 4.0 | La zona sismica del Comune nelle classificazioni 1984, 1998 e 2003, con l'a~g~ di riferimento |
| Parametri sismici di base NTC 2018 | GeoStru Parametri Sismici NX (reticolo All. B NTC 2008) | a~g~, F~0~, T~C~* per SLO, SLD, SLV e SLC al sito, classe d'uso II e V~N~ = 50 anni; il link apre Parametri Sismici NX per spettri e altre classi |
| Faglie capaci (ITHACA) | ISPRA · CC BY 4.0 | Le faglie capaci nei dintorni del punto (nome, sistema, attività, cinematica) |
| Eventi sismici nel raggio | INGV — servizio FDSN · CC BY 4.0 | Fino a 50 eventi con M ≥ 4 dal 1900 entro 30 km, dal più forte |

## Frane e alluvioni

| Fonte | Ente · licenza | Cosa restituisce |
|---|---|---|
| Pericolosità da frana (mosaico PAI) | ISPRA — IdroGEO · CC BY 4.0 | Le classi P1–P4 e le aree di attenzione al punto (o campionate nel perimetro) |
| Frane censite (inventario IFFI) | ISPRA — IdroGEO · CC BY 4.0 | Le frane dell'inventario al punto |
| Tavola pericolosità da frana | ISPRA — IdroGEO · CC BY 4.0 | Tavola 3 km con legenda |
| Indicatori di rischio del Comune (PAI) | ISPRA — IdroGEO · CC BY 4.0 | Percentuali del territorio comunale nelle classi P1–P3 e popolazione esposta |
| Pericolosità da valanga (IdroGEO) | ISPRA — IdroGEO · CC BY 4.0 | Le aree a pericolosità da valanga del mosaico PAI (vuota fuori dall'arco alpino) |
| Rischio da frana PAI (R1–R4) | MASE — Portale Cartografico Nazionale · CC BY 4.0 | La classe di **rischio** (R1 moderato … R4 molto elevato), che incrocia pericolosità ed elementi esposti; con autorità di bacino, piano e delibera |
| Pericolosità idraulica (mosaico PGRA/PAI) | ISPRA — IdroGEO · CC BY 4.0 | Gli scenari di pericolosità idraulica al punto |
| Rischio da alluvione PAI (R1–R4) | MASE — Portale Cartografico Nazionale · CC BY 4.0 | La classe di rischio idraulico, come sopra |
| Bacino idrografico (ISPRA) | ISPRA — Servizio Geologico d'Italia · CC BY 4.0 | Il bacino principale e il sottobacino in cui cade il sito, il corso d'acqua, l'ordine, l'autorità |
| Tavola pericolosità idraulica | ISPRA — IdroGEO · CC BY 4.0 | Tavola 3 km con legenda |

## Microzonazione sismica

| Fonte | Ente · licenza | Cosa restituisce |
|---|---|---|
| Zone stabili, livello 1 e livello 3 | WebMS — CentroMS / Dipartimento della Protezione Civile · CC BY 4.0 | Le microzone stabili o suscettibili di amplificazione (codice zona, livello, fattori F~a~, F~v~ dove lo studio li riporta) |
| Zone instabili (tutti i livelli) | WebMS · CC BY 4.0 | Le zone di instabilità al punto |
| Tavola microzonazione livello 1 | WebMS · CC BY 4.0 | Tavola 2 km con legenda |

!!! warning "Un codice di microzona non è una categoria di sottosuolo"
    Le zone MS descrivono lo studio comunale. Categoria di sottosuolo, V~S,30~ e parametri di
    progetto vanno determinati con dati pertinenti al sito.

## Indagini

| Fonte | Ente · licenza | Cosa restituisce |
|---|---|---|
| Perforazioni censite nell'intorno (L. 464/84) | ISPRA · CC BY 4.0 | Pozzi e sondaggi dell'archivio nazionale entro **circa 1 km**: codice, opera, profondità, presenza di acqua e di stratigrafia, link alla scheda ISPRA |

## Uso del suolo

| Fonte | Ente · licenza | Cosa restituisce |
|---|---|---|
| Uso del suolo (Corine Land Cover 2018) | EEA — Copernicus · libero con attribuzione | La classe CLC al punto (codice ed etichetta) |

## Come si legge un esito

- **trovata**: la fonte ha restituito elementi; i record sono nel dettaglio e nel Word.
- **nulla al punto**: la fonte ha risposto e alla scala della sua cartografia non risulta nulla.
  Non è una prova di assenza di pericolosità o vincoli.
- **non disponibile**: il servizio non ha risposto entro il tempo massimo. Il fascicolo si
  completa lo stesso e il Word lo elenca fra le verifiche da completare. Puoi **rilanciare** il
  fascicolo da *I miei fascicoli*.

Le fonti vengono controllate ogni notte su siti campione: se un ente è giù, ce ne accorgiamo
prima di te.
