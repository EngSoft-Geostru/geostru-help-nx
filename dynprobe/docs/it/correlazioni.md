# Correlazioni geotecniche

## Cosa sono

Le correlazioni geotecniche trasformano N_SPT in parametri di resistenza e deformabilità del terreno. Sono formule empiriche derivate dalla letteratura internazionale — il loro utilizzo è consolidato nella pratica geotecnica, ma restano stime: integrale sempre con dati di laboratorio quando disponibili.

## Come si leggono

Nel tab **Correlazioni** dell'Editor, per ogni strato della stratigrafia compare una tabella con i valori calcolati. La colonna di sinistra indica il parametro, quelle successive i valori secondo i diversi autori di riferimento. Puoi attivare o disattivare singoli autori con i toggle in cima alla colonna.

Il **valore preferito** (⭐) alimenta la tab **Sintesi parametri** e il report Word.

## Parametri per terreni coesivi (COES)

| Parametro | Significato |
|---|---|
| **Cu** | Resistenza al taglio non drenata (kPa) |
| **Mo** | Modulo edometrico (MPa) |
| **Ey** | Modulo di Young (MPa) |
| **Vs** | Velocità delle onde di taglio (m/s) |
| **γ** | Peso di volume (kN/m³) |
| **Classificazione** | Consistenza (molto molle → molto rigida) |

Autori di riferimento citati nella letteratura geotecnica italiana e internazionale: Terzaghi-Peck, Schmertmann, Ohta-Goto, e altri.

## Parametri per terreni incoerenti (INCO)

| Parametro | Significato |
|---|---|
| **Dr** | Densità relativa (%) |
| **φ** | Angolo di attrito interno (°) |
| **φ_160** | Angolo di attrito su N_1,60 normalizzato (°) |
| **Mo** | Modulo edometrico (MPa) |
| **Ey** | Modulo di Young (MPa) |
| **Vs** | Velocità delle onde di taglio (m/s) |
| **ν** | Coefficiente di Poisson |
| **G** | Modulo di taglio (MPa) |

Autori di riferimento: Meyerhof, Peck, Hanson, Thornburn, Ohta-Goto, Seed-Idriss, e altri.

!!! warning "Limiti di validità"
    Ogni correlazione è stata sviluppata su un certo range di N_SPT e su specifiche tipologie di terreno. Quando N_SPT è molto basso (< 3) o molto alto (> 50), i risultati vanno interpretati con cautela. L'app evidenzia i valori fuori range.

## Inviluppo dei parametri

Quando hai più prove sullo stesso sito, il tab **Inviluppo** mostra per ogni strato il range min-max dei parametri tra tutte le prove, con il **criterio di progetto** selezionabile (minimo / media / massimo / valore preferito ⭐). Il valore di progetto alimenta automaticamente la Sintesi.

## Sintesi parametri

La tab **Sintesi** raccoglie in una sola tabella i valori geotecnici caratteristici di ogni strato — utile come prospetto da inserire nella relazione geotecnica. Il report Word la include automaticamente.
