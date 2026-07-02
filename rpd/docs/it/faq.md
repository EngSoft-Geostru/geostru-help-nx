---
title: Domande frequenti
---

# Domande frequenti

## Perché il "parametro di distribuzione statistica" (Z_R) è negativo?

È corretto. Z_R è la **deviata normale standard** legata all'affidabilità R nell'equazione AASHTO: è negativa per ogni R maggiore del 50% (con R = 90% vale −1,282). Più alta è l'affidabilità, più negativa è Z_R e più cauto è il progetto. Vedi [Metodo empirico AASHTO](aashto.md#affidabilita-r-e-coefficiente-z_r).

## I metodi (AASHTO 1993, Ivanov, Westergaard) sono datati?

Sono metodi **classici e consolidati**, tuttora **standard di riferimento** nella pratica professionale e nel *Catalogo Italiano delle Pavimentazioni Stradali (CNR)*. Rappresentano la base normativa più usata per il dimensionamento e la verifica. L'evoluzione più recente è l'approccio *meccanicistico-empirico*, più sofisticato ma più esigente in dati e calibrazioni.

## Perché non c'è il pulsante "Calcola"?

Il calcolo parte **automaticamente** quando apri la scheda **Risultati** — ma solo se hai **cambiato qualcosa** dall'ultimo calcolo. Se i dati non sono cambiati, RPD NX mostra il risultato già calcolato senza rieseguire il calcolo.

## La verifica non è soddisfatta: come rientro?

Con FS < 1 compare la card **Come rientrare in verifica**: proponendo, in alternativa, di **aumentare uno strato** (ogni proposta è cliccabile e applica lo spessore ricalcolando) oppure di inserire una **geogriglia** con un dato **TBR**. Dopo l'applicazione puoi **annullare** e provare un'altra soluzione.

## A cosa serve il TBR della geogriglia?

Il **Traffic Benefit Ratio** è il moltiplicatore degli assi ammissibili dovuto al rinforzo con geogriglia bitumata. Nel metodo AASHTO gli assi ammissibili vengono moltiplicati per il TBR (default 1 = nessun effetto). Il valore reale va preso dalla **scheda tecnica del produttore**.

## Il pacchetto è sovradimensionato: posso ridurlo?

Sì. Quando la verifica è soddisfatta con ampio margine, compare la card **Ottimizzazione del pacchetto**: propone di **ridurre** lo spessore di uno strato mantenendo la verifica, per risparmiare materiale.

## In che unità è lo Structural Number?

Lo Structural Number è espresso in **inch** (con l'equivalente in cm mostrato accanto), come da metodo AASHTO. Gli spessori degli strati si inseriscono invece in **cm**.

## In quante lingue è disponibile RPD NX?

In **7 lingue**: italiano, inglese, francese, spagnolo, tedesco, rumeno e danese. Si cambia dal menu bandiera in alto a destra.

## Dove trovo i documenti teorici dei metodi?

Dal menu **?** dell'app → scheda *Risorse* → sezione "Documentazione metodi": trovi i PDF "Metodo empirico" e "Metodo razionale — Ivanov".

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20RPD%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rpd/docs/it/faq.md).*
