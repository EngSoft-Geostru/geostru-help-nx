# Portanza fondazioni

## Fondazioni superficiali

Dynamic Probing NX calcola la **pressione ammissibile** per fondazioni superficiali su terreni granulari e coesivi secondo i metodi di riferimento della letteratura geotecnica. I risultati sono espressi in kPa.

### Metodi disponibili

| Metodo | Tipo di terreno | Note |
|---|---|---|
| **Terzaghi-Peck** | Sabbie, ghiaie | Classico da N_SPT, include correzione cedimento |
| **Meyerhof** | Sabbie, ghiaie | Tiene conto di forma e profondità della fondazione |
| **Bazaraa** | Sabbie, ghiaie | Alternativa conservativa al Meyerhof |
| **Peck-Hanson-Thornburn** | Sabbie, ghiaie | Con limite di cedimento ammissibile |
| **Meigh-Hobbs** | Argille | Da N_SPT per terreni coesivi |
| **De Beer-Martens** | Sabbie | Metodo europeo |

### Input richiesto

Nella tab **Portanze** imposta:

- **Larghezza fondazione B** (m)
- **Profondità di posa D** (m da p.c.)
- **Cedimento ammissibile** (mm) — tipicamente 25 mm per fondazioni continue, 25–50 mm per fondazioni isolate
- **Strato di calcolo**: il metodo usa N_SPT dello strato in cui è immersa la fondazione

### Lettura del risultato

La tabella mostra la pressione ammissibile q_amm per ogni metodo. Il report riporta tutti i metodi a confronto — scegli quello più adatto al contesto stratigrafico.

!!! warning "Fondazioni su argille"
    Per fondazioni su argille, il calcolo si basa su Cu derivato dalla correlazione N_SPT → Cu. Integra con prove di laboratorio (triassiale, consolidazione) per i progetti definitivi.

## Fondazioni profonde — palo infisso (Meyerhof)

Per i pali infissi, l'app implementa il metodo di **Meyerhof** che stima separatamente:

- **Q_p**: portanza sulla punta (contributo di strato sotto la punta)
- **Q_l**: portanza laterale (contributo degli strati attraversati dal palo)
- **Q_tot = Q_p + Q_l − W_p**: portanza totale al netto del peso proprio del palo

### Input richiesto

- **Diametro palo** D (m)
- **Lunghezza palo** L (m)
- **Tipo palo**: il metodo Meyerhof distingue tra pali infissi in sabbia e in argilla

Il calcolo usa i valori N_SPT degli strati secondo la distribuzione di profondità definita nella stratigrafia. La portanza totale viene riportata in kN.

!!! info "Coefficiente di sicurezza"
    La portanza ammissibile si ottiene dividendo la portanza ultima per il coefficiente di sicurezza globale. Dynamic Probing NX riporta la portanza ultima — l'applicazione del coefficiente di sicurezza è di competenza del progettista secondo la normativa applicabile.
