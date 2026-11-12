# Collegamenti con le altre app NX

Hydrogeo NX è il passaggio dei dati in una catena che va dal sito del progetto al
dimensionamento delle opere, con **un solo account** e **un solo portafoglio crediti**.

```text
Atlante NX → Hydrogeo NX → Runoff Lab NX → HID NX
  sito         dati di        statistica e     invarianza
               pioggia        curva h = a·tⁿ   idraulica
```

## Atlante NX → Hydrogeo NX

In [Atlante NX](https://help.nx.geostru.ai/atlante/it/) descrivi il sito del progetto. Tra
le app suggerite per i profili idraulico, agronomico e geologico c'è Hydrogeo NX: il
collegamento apre la mappa **centrata sul sito**, con il segnaposto rosso **Sito (Atlante
NX)**.

Da lì chiedi all'[assistente](assistente.md) le stazioni vicine, per esempio «Pluviometri
entro 20 km dal sito con almeno 20 anni di dati».

## Hydrogeo NX → Runoff Lab NX

[Runoff Lab NX](https://help.nx.geostru.ai/runofflab/it/) fa l'analisi statistica che
Hydrogeo NX non fa.

1. In Runoff Lab NX apri **Importa → Da Hydrogeo NX…**.
2. Cerca la stazione per nome e premi **Cerca**.
3. Fai clic sulla stazione: le serie dei **massimi annui per durata** arrivano nello studio,
   insieme all'anagrafica.

Non serve scaricare e ricaricare un file. Le stazioni con solo piogge giornaliere compaiono
disattivate, con la nota «solo piogge giornaliere», perché non hanno una serie di massimi da
analizzare.

In Runoff Lab NX adatti poi le distribuzioni di probabilità (Gumbel con il metodo dei momenti
o della massima verosimiglianza, GEV, Pearson III, TCEV ai livelli da 0 a 3) e ottieni le
curve di possibilità pluviometrica h = a·tⁿ, gli ietogrammi di progetto e gli idrogrammi.

L'importazione di una stazione usa crediti di Hydrogeo NX; un'importazione che non porta
nessuna serie non viene addebitata.

## Runoff Lab NX → HID NX

I parametri **a** e **n** della curva sono i dati di pioggia che
[HID NX](https://help.nx.geostru.ai/hid/it/) chiede per dimensionare le opere di laminazione
richieste dall'**invarianza idraulica**. Li inserisci a mano in HID NX, nella sezione
**Curva di probabilità pluviometrica**.

## GeoDropbox NX

Gli studi di Runoff Lab NX si salvano in **GeoDropbox NX**, il cloud dei progetti GeoStru,
accanto agli altri file del progetto.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Hydrogeo%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hydrogeo/docs/it/integrazioni.md).*
