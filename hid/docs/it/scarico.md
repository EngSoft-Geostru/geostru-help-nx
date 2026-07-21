# Sistema di scarico

L'organo di scarico determina la portata uscente dall'invaso e quindi la
laminazione. HID ne implementa otto.

![Sistema di scarico](img/06-calcoli-verifiche.png)

## Gli organi disponibili

| Organo | Parametri | Legge |
|---|---|---|
| Portata costante | Q<sub>u,lim</sub> | Q costante, indipendente dal battente |
| Stramazzo Thomson | angolo θ | Q ∝ tan(θ/2) · h<sup>5/2</sup> |
| Stramazzo Bazin | larghezza | Q ∝ L · h<sup>3/2</sup> |
| Stramazzo Crump | larghezza | Q ∝ L · h<sup>3/2</sup> |
| Luce a battente circolare | area A | Q = 0,6 · A · √(2gh) |
| Paratoia | apertura, larghezza | Q = 0,6 · a · L · √(2gh) |
| Infiltrazione costante | K, gradiente | Q ∝ K · i · superficie |
| Pozzo disperdente | numero, diametro, lunghezza | funzione del battente e della superficie disperdente |

## Come viene scelta la portata limite

È il punto in cui si sbaglia più spesso, quindi HID segue un ordine unico:

1. **Se la normativa la impone**, vale quella. In Lombardia si ricava da area,
   coefficiente di deflusso e ambito di criticità.
2. **Altrimenti la scegli tu.** Ma il campo "portata costante uscente" ha senso
   solo per uno scarico a portata costante: per una luce a battente, uno
   stramazzo o una paratoia vale la **portata dell'organo al battente di
   progetto**.

!!! warning "Attenzione"
    Il punto 2 è la ragione per cui, cambiando tipo di scarico, il volume
    richiesto può cambiare parecchio: la portata di riferimento non è più quella
    che hai scritto nel campo, ma quella che l'organo scarica davvero.

## Battente di progetto

Per gli organi che dipendono dal battente, il valore H che inserisci è il
battente idrico utile massimo. La portata corrispondente è mostrata sotto il
blocco come **portata al battente di progetto**.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
