---
title: Traffico di progetto (ESAL)
---

# Traffico di progetto (assi standard equivalenti)

Tutti i metodi partono dal **traffico di progetto**: il numero di **assi standard equivalenti** da 8,2 t (ESAL) che transiteranno sulla corsia più caricata durante la vita utile. RPD lo calcola automaticamente dai dati che inserisci.

## Perché "assi equivalenti"

I veicoli commerciali hanno numero di assi, carichi e tipologie diversi. Per confrontarli si usa l'**asse standard** da 82 kN (8,2 t): ogni asse reale viene convertito nel numero di assi standard che produce lo **stesso danno**. Il danno cresce con la **quarta potenza** del carico:

`Ceq = (x / y)⁴`  — con *x* carico dell'asse reale e *y* = 82 kN.

Il **coefficiente di equivalenza medio (Ceq)** pesa questa conversione sullo **spettro di traffico** della tipologia di strada scelta (frequenza dei vari tipi di veicolo).

## Dal TGM agli assi cumulati

Il dato di partenza è il **TGM** (traffico giornaliero medio) del primo anno. RPD lo corregge con:

- il **tasso di crescita annuo (r)** lungo la vita utile;
- la **percentuale di veicoli commerciali**;
- la **ripartizione per senso di marcia** e la **percentuale sulla corsia** di progetto;
- il **coefficiente di dispersione delle traiettorie**;
- il **coefficiente di equivalenza Ceq** (spettro di traffico + regola della 4ª potenza).

Il risultato è **N₈.₂,Calc**, gli assi standard cumulati nella vita utile, confrontato poi con gli assi ammissibili nel [metodo AASHTO](aashto.md). Per i metodi razionali si usa invece **N**, il numero di assi standard **al giorno** nell'ultimo anno di vita utile, che entra nella deflessione ammissibile.

## Dati richiesti in RPD

| Campo | Significato |
|---|---|
| TGM | Traffico giornaliero medio (veicoli/giorno), 1° anno |
| Tasso di crescita r (%) | Incremento annuo del traffico |
| Veicoli commerciali (%) | Quota di traffico pesante |
| Traffico afferente al senso di marcia (%) | Ripartizione tra le due direzioni |
| Veicoli commerciali su corsia di progetto (%) | Quota sulla corsia più caricata |
| Coefficiente dispersione traiettorie | Riduzione per la dispersione delle ruote |
| Deviazione standard S₀ | Solo AASHTO: errore su traffico e prestazioni (0,40–0,50) |

!!! note "Tipologia di strada"
    La **tipologia di strada** (in *Dati generali*) seleziona lo **spettro di traffico** usato per il calcolo di Ceq. Scegli quella corrispondente alla tua infrastruttura.

!!! tip "Predimensionamento"
    In fase preliminare sono utili i cataloghi delle pavimentazioni: in Italia il **Catalogo Italiano delle Pavimentazioni Stradali (CNR, BU 168/95)**.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20RPD%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rpd/docs/it/traffico.md).*
