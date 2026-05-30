# Corelații geotehnice

## Ce sunt

Corelațiile geotehnice transformă N_SPT în parametri de rezistență și deformabilitate ai terenului. Sunt formule empirice derivate din literatura internațională — utilizarea lor este consolidată în practica geotehnică, dar rămân estimări: completează întotdeauna cu date de laborator când sunt disponibile.

## Cum se citesc

În fila **Corelații** din Editor, pentru fiecare strat din stratigrafie apare un tabel cu valorile calculate. Coloana din stânga indică parametrul, iar cele următoare valorile conform diferiților autori de referință. Poți activa sau dezactiva autorii individuali cu comutatoarele din partea de sus a coloanei.

**Valoarea preferată** (⭐) alimentează fila **Sinteză parametri** și raportul Word.

## Parametri pentru terenuri coezive (COES)

| Parametru | Semnificație |
|---|---|
| **Cu** | Rezistența la forfecare nedrenată (kPa) |
| **Mo** | Modul edometric (MPa) |
| **Ey** | Modul Young (MPa) |
| **Vs** | Viteza undelor de forfecare (m/s) |
| **γ** | Greutatea volumică (kN/m³) |
| **Clasificare** | Consistență (foarte moale → foarte rigidă) |

Autori de referință citați în literatura geotehnică italiană și internațională: Terzaghi-Peck, Schmertmann, Ohta-Goto și alții.

## Parametri pentru terenuri necoezive (INCO)

| Parametru | Semnificație |
|---|---|
| **Dr** | Densitate relativă (%) |
| **φ** | Unghi de frecare internă (°) |
| **φ_160** | Unghi de frecare pe N_1,60 normalizat (°) |
| **Mo** | Modul edometric (MPa) |
| **Ey** | Modul Young (MPa) |
| **Vs** | Viteza undelor de forfecare (m/s) |
| **ν** | Coeficientul lui Poisson |
| **G** | Modul de forfecare (MPa) |

Autori de referință: Meyerhof, Peck, Hanson, Thornburn, Ohta-Goto, Seed-Idriss și alții.

!!! warning "Limite de validitate"
    Fiecare corelație a fost dezvoltată pe un anumit interval de N_SPT și pe tipuri specifice de teren. Când N_SPT este foarte mic (< 3) sau foarte mare (> 50), rezultatele trebuie interpretate cu prudență. Aplicația evidențiază valorile în afara intervalului.

## Anvelopa parametrilor

Când ai mai multe încercări pe același sit, fila **Anvelopă** arată pentru fiecare strat intervalul min-max al parametrilor între toate încercările, cu **criteriul de proiect** selectabil (minim / medie / maxim / valoare preferată ⭐). Valoarea de proiect alimentează automat Sinteza.

## Sinteză parametri

Fila **Sinteză** reunește într-un singur tabel valorile geotehnice caracteristice ale fiecărui strat — util ca tabel de sinteză de inserat în raportul geotehnic. Raportul Word îl include automat.
