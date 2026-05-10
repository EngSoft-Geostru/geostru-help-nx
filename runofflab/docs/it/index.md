# Runoff Lab NX — Curve di pioggia & trasformazione afflusso-deflusso

**Runoff Lab NX** è il software web GeoStru per la **trasformazione afflusso
→ deflusso**: a partire dai dati pluviometrici (curve IDF, ietogramma di
progetto) e dalle caratteristiche del bacino (CN, Tlag, area), calcola
l'**idrogramma di piena** per il dimensionamento di opere idrauliche.

[**Apri Runoff Lab NX**](https://nx.geostru.ai/runofflab/){ .md-button .md-button--primary }
[Quickstart in 5 minuti](quickstart.md){ .md-button }

---

## Cosa fa, in sintesi

- **Curve di pioggia** (4 tipi):
  - Curva IDF tradizionale `i = a · d^(n-1)`
  - VAPI (Valutazione delle Piene in Italia)
  - Letta da PLV GeoStru (importazione da Hydrogeo NX)
  - Custom (parametri inseriti a mano)
- **Studio del bacino**: area, CN (Curve Number SCS), tempo di
  corrivazione (Tc) e di lag (Tlag)
- **Wizard CN/Tlag**: stima automatica da geologia, copertura del suolo,
  pendenza
- **AI Import**: trascina un PDF di studio idrogeologico, l'AI estrae i
  parametri del bacino
- **Trasformazione afflusso-deflusso** con metodi standard (SCS, Cinematico,
  Idrogramma unitario)
- **Idrogramma di piena**: portata Q(t) per tempo di ritorno T
- **Esportazioni**: PDF report, CSV, Excel, PLV

## Per chi

- **Ingegneri idraulici** che dimensionano fognature, vasche di
  laminazione, sfioratori
- **Geologi** che redigono studi di compatibilità idraulica
- **Studi tecnici** per pareri di fattibilità idraulica e PSR

## Come iniziare

1. Apri [`nx.geostru.ai/runofflab/`](https://nx.geostru.ai/runofflab/)
2. **Definisci la curva di pioggia** (4 metodi, vedi sopra)
3. **Definisci il bacino** (manuale, wizard CN/Tlag, AI Import)
4. Scegli il **metodo di trasformazione** (SCS, Cinematico, IUH)
5. **Esegui calcolo** → idrogramma di piena
6. Esporta il **PDF report**

[Vedi il workflow completo →](workflow.md)

## Capitoli del manuale

### Iniziare

- [**Quickstart**](quickstart.md) — 5 minuti dall'IDF all'idrogramma
- [**Workflow completo**](workflow.md) — curva → bacino → idrogramma → export

### Riferimento

- [**FAQ**](faq.md) — domande frequenti

---

*Hai trovato un errore o vuoi suggerire un contenuto?
[Scrivici](mailto:info@geostru.ai?subject=Help%20Runoff%20Lab%20NX) — grazie!*
