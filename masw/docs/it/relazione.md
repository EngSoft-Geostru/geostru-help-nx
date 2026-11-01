# Relazione, DXF e crediti

## Relazione Word

La scheda mostra l'**Anteprima**, gratuita. **Genera Word** produce il documento nella lingua dell'interfaccia: dati generali,
tracce, analisi spettrale, curva di dispersione, inversione, risultati, parametri geotecnici. L'intestazione viene dai dati
dello studio tecnico in Dati generali.

![Scheda Relazione con anteprima](img/07-relazione.png)

La relazione chiude con il blocco **Codice di calcolo** chiesto dal §10.2 NTC: software, versione del motore, codice del
documento e impronta dei dati. Il codice si verifica su `geostru.ai/verify/<codice>`. La verifica dice che il documento è
stato emesso, non che i calcoli sono esenti da errori.

Se i dati sono cambiati dopo l'inversione, la relazione non si genera finché non rifai la corsa.

## DXF e CSV

**Esporta DXF** produce la tavola della curva di dispersione o del profilo V~s~. Le mappe a colori non entrano in un DXF.
La **colonna stratigrafica** della soluzione, con i colori e i retini scelti per strato, si esporta in DXF e in PDF A4.
I **CSV** di curva di dispersione e profilo sono gratuiti.

## Che cosa consuma crediti

| Azione | Crediti |
|---|---|
| Tracce, spettro, picking, curve sintetiche, categoria, anteprima, CSV | gratis |
| Corsa di inversione | sì, a soluzioni consegnate |
| Relazione Word | sì, a documento prodotto |
| Tavola DXF o PDF | sì, a file prodotto |
| Messaggio all'assistente | sì, a risposta riuscita |

Se un'operazione fallisce o la interrompi, non paghi. Ripetere la stessa operazione sugli stessi dati dopo un successo non si
paga di nuovo. Il saldo e la scadenza dei crediti sono nel menu utente.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MASW%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/it/relazione.md).*
