# Valori caracteristice EC7 / NTC §6.2.2

## De ce valori caracteristice

Normele geotehnice europene (EC7 §2.4.5.2) și italiene (NTC 2018 §6.2.2) cer proiectarea pe **valorile caracteristice** ale parametrilor, nu pe valorile medii. Valoarea caracteristică ține cont de variabilitatea naturală a terenului și de incertitudinea de eșantionare.

## Cum funcționează calculul

Dynamic Probing NX estimează valoarea caracteristică a N_SPT pentru fiecare strat aplicând metode statistice pe seria de valori N colectate în strat. Metodele disponibile sunt:

| Metodă | Descriere |
|---|---|
| **Normală** | Estimare bazată pe medie și deviație standard cu distribuție gaussiană |
| **Lognormală** | Utilă când N_SPT are distribuție asimetrică (frecventă cu valori mici) |
| **Student-t** | Corectată pentru eșantioane mici (n < 30) — ține cont de incertitudinea asupra mediei |

Nivelul de încredere aplicat corespunde celui indicat de EC7 pentru valoarea caracteristică inferioară (percentila 5, latura conservativă).

## Cum se folosește

În fila **Estimare parametri** din Editor:

1. Selectează metoda statistică (Normală / Lognormală / Student-t).
2. Pentru fiecare strat sunt afișate: media, deviația standard, numărul de eșantioane și valoarea caracteristică calculată.
3. Valoarea caracteristică N_SPT este propagată spre corelații pentru a obține valorile caracteristice ale Cu, φ, Mo, Ey etc.

!!! info "Eșantioane minime"
    Cu mai puțin de 3 înregistrări pe strat, calculul statistic are o semnificativitate redusă. Aplicația semnalează cazurile cu n < 3 printr-un avertisment — în aceste cazuri este de preferat o abordare inginerească conservativă (ex. minimul valorilor observate).

## Valorile caracteristice în raport

Raportul Word exportat include tabelul valorilor caracteristice cu metoda utilizată, dimensiunea eșantionului și valoarea rezultată — gata de atașat la raportul geotehnic.
