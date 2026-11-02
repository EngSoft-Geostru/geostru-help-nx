# Cenni teorici

## Il rapporto H/V

Il suolo vibra di continuo per vento, mare e attività umane. Il rapporto fra lo spettro orizzontale e quello verticale di questo rumore ha un picco
alla frequenza di risonanza del sito quando un terreno soffice poggia su uno più rigido (Nakamura 1989). Per un solo strato di spessore H e
velocità V~s~ su un substrato rigido la risonanza vale circa:

```text
f0 ≈ Vs / (4 H)
```

Con 20 m a 200 m/s fa 2,5 Hz. È un ordine di grandezza: il massimo dell'ellitticità si avvicina a questo valore solo con un contrasto forte.
Con contrasto 10 lo scarto è nullo, con contrasto 4 è del 28 %.

## La catena di calcolo

1. **Finestre** di campioni dalla registrazione.
2. **Taper** di Tukey e **trasformata di Fourier**, con zero-padding alla potenza di 2 successiva.
3. **Lisciamento** e ricampionamento sulla griglia di frequenze.
4. **Spettri medi**: media aritmetica delle ampiezze sulle finestre incluse.
5. **H/V**: orizzontale combinata diviso verticale, sugli spettri medi.
6. **σ**: deviazione delle H/V di finestra attorno alla curva media, divisa per la media.

La curva è un **rapporto di medie**, non una media di rapporti: è la scelta del desktop, mantenuta. La σ è relativa e viene sommata alla curva per
disegnare la banda, come nel desktop. Il testo SESAME usa invece la media geometrica delle curve di finestra e un fattore σ~A~, che HVSR NX applica se
scegli i criteri del testo: vedi [Spettro H/V](spettro-hv.md).

## L'ellitticità

L'**ellitticità** è il rapporto fra gli spostamenti orizzontale e verticale di un'onda di Rayleigh. Dipende da frequenza e stratigrafia: per questo la
curva H/V si può interpretare come ellitticità del modo fondamentale. L'interpretazione è un'approssimazione: la curva misurata contiene anche onde di
Love, modi superiori e onde di volume (Fäh et al. 2001).

## SESAME

Il progetto europeo SESAME ha pubblicato nel 2004 le linee guida sulla tecnica: durate, condizioni di misura, criteri di affidabilità. I criteri sono
in [Spettro H/V](spettro-hv.md). Che il picco passi i criteri non dice che sia stratigrafico.

## V~s,eq~

Vedi [V~s,eq~ e categoria](categoria.md).

## Bibliografia

- SESAME (2004), *Guidelines for the implementation of the H/V spectral ratio technique on ambient vibrations*, Deliverable D23.12.
- Nakamura Y. (1989), Quarterly Report of RTRI 30(1), 25–33.
- Konno K., Ohmachi T. (1998), Bull. Seism. Soc. Am. 88(1), 228–241.
- Fäh D., Kind F., Giardini D. (2001), Geophys. J. Int. 145(2), 535–549.
- Wathelet M. (2005), tesi di dottorato, Université de Liège.
- Nelder J.A., Mead R. (1965), Computer Journal 7(4), 308–313.
- D.M. 17/01/2018, Norme tecniche per le costruzioni, §3.2.2.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20HVSR%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hvsr/docs/it/teoria.md).*
