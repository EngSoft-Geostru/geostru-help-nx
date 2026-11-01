# Inversione

L'inversione cerca il profilo a strati la cui curva teorica coincide il più possibile con il picking.

## Il modello iniziale

La tabella ha una riga per strato; l'ultima è il **semispazio** (∞). Per ogni strato imposti:

| Campo | Significato |
|---|---|
| Descrizione | testo libero per la relazione |
| Spessore, Min, Max | valore e limiti; con il lucchetto non viene ottimizzato |
| V~s~ iniziale, Min, Max | valore e limiti; con il lucchetto resta fisso |
| V~s~ crescente | V~s~ non diminuisce con la profondità |
| Peso di volume, Peso saturo, Falda | usati come densità in kg/m³; con Falda vale il saturo |
| ν | coefficiente di Poisson: lega V~p~ a V~s~ |

**Stima iniziale dal picking** propone V~s~ e limiti dalla regola «l'onda di lunghezza λ vede fino a circa λ/2».
**Aggiungi strato** ed elimina adattano il numero di strati, fino a 40.

![Tabella degli strati](img/04-strati.png)

## La corsa

Imposta **N. iterazioni** e **N. modi**, poi **Calcola inversione**. Vedi l'avanzamento; **Interrompi** ferma la corsa e non
consuma crediti.

L'inversione è casuale: due corse danno soluzioni un po' diverse. Ripetere la stessa corsa, a dati identici, non si paga di
nuovo.

## Leggere le soluzioni

Il navigatore scorre i modelli trovati, ordinati per **Misfit** o per **Errore %**. Per ognuno vedi mappa con curve teoriche,
curve osservate e calcolate, profilo V~s~ a gradini e tabella del modello. La soluzione scelta è quella usata da categoria e
relazione.

![Soluzione, curve e profilo](img/05-inversione.png)

!!! warning "Risultati superati"
    Se cambi picking, strati, tracce o filtro dopo l'inversione, una striscia avvisa che i risultati non corrispondono più
    ai dati. La relazione non si genera finché non rifai la corsa.

!!! note "Misfit non vuol dire verità"
    Profili diversi possono riprodurre la stessa curva. Il misfit misura l'accordo con il picking: il giudizio geologico resta tuo.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MASW%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/it/inversione.md).*
