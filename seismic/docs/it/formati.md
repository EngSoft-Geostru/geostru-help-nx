# Formati ed export

PS Advanced permette di esportare i risultati e di salvare il progetto per
riaprirlo o condividerlo tra le app della suite NX.

## Report TXT

Riepilogo **testuale** di input e risultati: coordinate del sito, vita nominale
e classe d'uso, periodi di ritorno e parametri ($a_g$, $F_0$, $T_C^*$) dei
quattro stati limite. Formato leggero, adatto ad allegati rapidi o al
copia-incolla in una relazione.

## Report PDF

Documento **formattato** e stampabile che raccoglie:

- i dati del sito (coordinate, datum),
- vita nominale, classe d'uso e periodo di riferimento $V_R$,
- i parametri dei **quattro stati limite**,
- la **categoria di sottosuolo** e la **categoria topografica** con $S_S$,
  $C_C$, $S_T$, $a_{max}$,
- i **coefficienti sismici** $k_h$ e $k_v$,
- lo **spettro** (elastico e di progetto) dello stato limite selezionato.

!!! warning "Rigenera prima di esportare"
    Il PDF usa i dati dell'ultimo calcolo mantenuti in sessione. Se cambi sito,
    vita nominale, categorie o parametri di spettro, **ricalcola gli spettri**
    prima di generare il PDF: in caso contrario l'app segnala che i dati
    sismici non sono disponibili e non produce un file corrotto.

## Salvataggio progetto (GeoDropbox)

Il pulsante **GeoDropbox** salva il progetto — posizione del sito e impostazioni
di calcolo — nello spazio cloud GeoStru. Da lì puoi:

- **riaprire** il progetto in una sessione successiva,
- **condividerlo** con altri utenti/app della suite NX,
- mantenere una copia versionata indipendente dal browser.

Il widget GeoDropbox è lo stesso in tutte le app NX: quello che salvi qui è
riconoscibile e gestibile dalla stessa interfaccia.

## Assistente AI

L'app include un **assistente AI** integrato: puoi chiedere spiegazioni sui
parametri, sul significato di uno stato limite o su come impostare le
categorie. L'assistente risponde nel contesto del sito e dei dati correnti.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20PS%20Advanced%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/seismic/docs/it/formati.md).*
