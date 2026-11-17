# Glossario

Termini e simboli usati in GeoTheis NX, in ordine alfabetico. Le formule sono spiegate in [Cenni teorici](teoria.md).

!!! note "Nota"
    La lettera **B** ha due significati: nella prova a gradini è il coefficiente della perdita lineare dell'acquifero (s = BQ + CQ²);
    in falda semiconfinata è il fattore di drenanza di Hantush. Il contesto, e l'unità, dicono quale.

**Abbassamento (s)** — Differenza fra il livello statico e il livello misurato durante il pompaggio, in m. Nella prova a gradini è
cumulato dall'inizio della prova.

**Abbassamento critico (s~c~)** — Abbassamento nel pozzo alla portata critica, sulla curva caratteristica s = BQ + CQ². Senza prova a
gradini lo indichi tu nella portata critica nota.

**Abbassamento residuo (s′)** — Abbassamento che resta durante la risalita, misurato dal livello statico.

**Abbassamenti stabilizzati** — Abbassamenti a regime nel pozzo e nei piezometri, quando il cono non si allarga più. Servono a
Dupuit-Thiem.

**Abbassamento specifico (s/Q)** — Abbassamento diviso la portata. Nella prova a gradini s/Q = B + C·Q è una retta.

**Affidabilità** — Giudizio del programma su ogni metodo: *affidabile*, *indicativo*, *non affidabile*, *da verificare*. Vedi
[Risultati](risultati.md).

**Coefficiente di immagazzinamento (S)** — Volume d'acqua rilasciato da una colonna di acquifero di base unitaria per un abbassamento
unitario del carico. Adimensionale, fra 0 e 1. In falda confinata è piccolo (10⁻⁵–10⁻³), in falda libera si avvicina alla porosità
efficace. Si ricava dai piezometri, non dal pozzo di emungimento.

**Coefficiente di perdita del pozzo (C)** — Coefficiente della perdita quadratica CQ² nella prova a gradini; in SI s²/m⁵, nelle classi
di Walton min²/m⁵. Cresce con l'intasamento del pozzo.

**Coefficiente di perdita dell'acquifero (B)** — Coefficiente della perdita lineare BQ nella prova a gradini, in s/m².

**Completamento** — Come è costruito il pozzo: perforazione, colonna (tratti ciechi, filtri, decantatore), intercapedine (dreno,
cementazione, tamponi), avampozzo, pompa.

**Cono di depressione** — Superficie del livello abbassato intorno al pozzo durante il pompaggio; si annulla al raggio d'azione.

**Curva caratteristica** — Curva s(Q) del pozzo, s = BQ + CQ², ricavata dalla prova a gradini. Su di essa si sceglie la portata
critica.

**Curva tipo** — Curva teorica W(u) di Theis o W(u, r/B) di Hantush a cui si sovrappongono le letture del piezometro.

**Distanza-abbassamento** — Metodo che usa gli abbassamenti di più piezometri allo stesso tempo, contro il logaritmo della distanza.

**Drenanza** — Acqua ceduta all'acquifero semiconfinato dallo strato semipermeabile quando il carico cala.

**Efficienza del pozzo (E)** — Quota dell'abbassamento dovuta all'acquifero: E = BQ/(BQ + CQ²). Cala al crescere della portata; vale
50 % alla portata Q = B/C.

**Falda confinata (in pressione, artesiana)** — Acquifero chiuso fra due strati impermeabili; il livello statico sta sopra il tetto
dell'acquifero.

**Falda libera (freatica)** — Acquifero la cui superficie è a pressione atmosferica e si abbassa pompando.

**Falda semiconfinata** — Acquifero sotto uno strato semipermeabile che lo alimenta per drenanza; in GeoTheis NX *libera* o *in
pressione* (nel desktop «semilibera» e «semiartesiana»).

**Fattore di drenanza (B)** — B = √(T·c), in m, con c la resistenza idraulica dello strato semipermeabile. Più B è grande, meno la
drenanza pesa.

**Fitting** — Adattamento automatico della curva tipo alle letture ai minimi quadrati (Levenberg-Marquardt), che dà T, S (e r/B) con
gli intervalli al 95 %.

**Funzione di pozzo W(u)** — Integrale esponenziale della soluzione di Theis.

**Livello dinamico** — Livello dell'acqua nel pozzo durante il pompaggio.

**Livello statico** — Livello dell'acqua a riposo, prima del pompaggio; nella scheda Pozzo è una quota in m s.l.m.

**Perdite di carico** — Abbassamento nel pozzo diviso in perdite dell'acquifero (lineari, BQ, flusso laminare) e perdite del pozzo
(quadratiche, CQ², flusso turbolento nei filtri e nel dreno).

**Permeabilità o conducibilità idraulica (K)** — Velocità di filtrazione sotto gradiente unitario, in m/s; a video anche in m/giorno.
K = T/b (o T/H~1~).

**Piezometro** — Pozzo o tubo di osservazione a distanza nota dal pozzo di emungimento, in cui si misura l'abbassamento senza pompare.
Serve per ricavare S e il raggio d'azione.

**Portata concedibile** — Portata che il programma propone per l'esercizio del pozzo: di norma la portata ottimale, limitata dalla
portata massima provata e dai vincoli sul livello dinamico. Vedi [Risultati](risultati.md#portata-concedibile).

**Portata critica (Q~c~)** — Portata oltre la quale le perdite del pozzo crescono in modo sproporzionato. La scegli sulla curva
caratteristica; senza scelta il programma propone Q = B/C.

**Portata critica nota** — Q~c~ e s~c~ che indichi nella scheda Prova senza una prova a gradini (da prove vicine o dal collaudo), con
il raggio d'azione presunto, per i pozzi singoli.

**Portata di esercizio** — Portata che confermi per il pozzo; alimenta relazione e cono di depressione.

**Portata ottimale (Q~ott~)** — 0,9·Q~c~.

**Portata specifica (Q/s)** — Portata per metro di abbassamento: l'inverso dell'abbassamento specifico.

**Pozzo completo / incompleto** — Completo se i filtri attraversano tutto lo spessore dell'acquifero, incompleto (parzialmente
penetrante) se ne attraversano solo una parte.

**Pozzi singoli** — Metodi che stimano T e K dalla sola coppia critica (Q~c~, s~c~) e da un raggio d'azione presunto, come se fosse un
regime stazionario. Danno valori indicativi.

**Prova a gradini di portata** — Pompaggio a portate crescenti per gradini di uguale durata; dà la curva caratteristica, le perdite di
carico, l'efficienza e la portata critica.

**Prova a portata costante** — Pompaggio a portata fissa con letture nel tempo nel pozzo e nei piezometri, di solito seguito dalla
risalita; dà T, S e R.

**Punto di coincidenza** — Punto (W, u, s, t/r²) letto sovrapponendo dati e curva tipo; da esso T e S. In GeoTheis NX è il risultato di
un ritocco o un punto importato dal desktop.

**Raggio d'azione (R)** — Distanza dal pozzo a cui l'abbassamento si annulla. Dalla retta di Thiem sui piezometri, dal raggio
transitorio R(t) = √(2,25·T·t/S), o presunto nei pozzi singoli.

**Raggio del pozzo (r~w~)** — Raggio del pozzo di emungimento, in m (non il diametro).

**Resistenza idraulica (c)** — Spessore dello strato semipermeabile diviso la sua permeabilità verticale, in s.

**Risalita** — Risalita del livello dopo l'arresto della pompa; t′ è il tempo dall'arresto.

**Spessore dell'acquifero (b)** — Tetto meno substrato dell'acquifero confinato o semiconfinato: b = TI − SI.

**Spessore saturo (H~1~)** — In falda libera, livello statico meno substrato: H~1~ = LS − SI.

**Substrato impermeabile (SI)** — Base dell'acquifero.

**Tetto impermeabile (TI)** — Limite superiore dell'acquifero confinato.

**Trasmissività (T)** — Portata che attraversa una striscia di acquifero larga 1 m, per tutto lo spessore, sotto gradiente unitario:
T = K·b (o K·H~1~), in m²/s; a video anche in m²/giorno.

**u** — Variabile adimensionale di Theis, u = r²S/(4Tt). Cooper-Jacob vale per u < 0,05.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/it/glossario.md).*
