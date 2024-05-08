# Sprawozdanie SKPS lab4
## Michał Sadowski Mateusz Ostaszewski 

## Zadanie 1
Przetestowaliśmy program na hoście i działa
![Alt text](screens/1.png)

## Zadanie 2
Zainstalowaliśmy SDK
![Alt text](screens/2.png)

W pliku feeds.conf.default dopisalismy ścieżkę:
![Alt text](screens/3.png)

Dodaliśmy oraz skompilowaliśmy pakiet
![Alt text](screens/4.png)![Alt text](screens/5.png)

Pobraliśmy skompilowany pakiet na Rpi
![Alt text](screens/6.png)

zainstalowalismy pakiet na Rpi
![Alt text](screens/7.png)

sprawdziliśmy i działa:
![Alt text](screens/8.png)


## Zadajnie 3

### Wariant 1 3 klientów, 1 rdzeń, pełne obciążenie
Ustawilismy liczbę rdzeni procesora na 1
![Alt text](screens/10.png)

Przy 100.000 wyrabia się
![Alt text](screens/a_100.png)

przy 200.000 nadal się wyrabia
![Alt text](screens/a_200.png)

przy 250.00 sie nie wyrabia
![Alt text](screens/a_250.png)

### Wariant 2 3 klientów, 2 rdzenie, pełne obciążenie
Ustawilismy liczbę rdzeni procesora na 2
![Alt text](screens/rdzenie2.png)

Przy 100.000 wyrabia się
![Alt text](screens/B_100.png)

Przy 300.000 wyrabia się
![Alt text](screens/B_300.png)

Przy 400.000 nie wyrabia się
![Alt text](screens/B_400.png)

### Wariant 3 3 klientów, 2 rdzenie, bez obciążenia

Przy 450.000 wyrabia się
![Alt text](screens/c_450.png)

Przy 1.000.000 nie wyrabia się
![Alt text](screens/c_1000.png)

Przy 800.000 nie wyrabia się
![Alt text](screens/c_800.png)

### Wariant 4 Czwarty wariant: 1 klient, 4 rdzenie, bez obciążenia
Ustawilismy liczbę rdzeni procesora na 4
![Alt text](screens/zmiana%20cpu4.png)

Przy 500.000 wyrabia się
![Alt text](screens/d_500.png)

Przy 1.000.000 nie wyrabia się
![Alt text](screens/d_1000.png)

Przy 700.000 wyrabia się
![Alt text](screens/d_700.png)

Przy 800.000 nie wyrabia się
![Alt text](screens/d_750.png)

## Zadanie 4

Dla czasu przetwarzania danych, stanowiącego połowę wartości, przy której system przestaje nadążać z przetwarzaniem, zbadaliśmy rozkład czasu dostarczenia danych do klienta.

Histogramy wykonaliśmy z użyciem programu histogram.py

### Wariant 1
![Alt text](screens/4_a.png)
![Alt text](Z4.1/hist.png)

### Wariant2
![Alt text](screens/4_b.png)
![Alt text](Z4.2/hist.png)

### Wariant3
![Alt text](screens/4_c.png)
![Alt text](Z4.3/hist.png)

### Wariant4
![Alt text](screens/4_d.png)
![Alt text](Z4.4/hist.png)

## Zadanie5

Zmodyfikowaliśmy aplikację kliencką cw4b tak, aby zamiast oczekiwać w uśpieniu na dane, oczekiwała aktywnie. Dodaliśmy argument wywałania version pozwala ustawić czy aktywnie oczekujemy tylko przy kliencie 0 czy przy wszystkich.

Skompilowalismy nowy pakiet
![Alt text](screens/15.png)

Przetestoewaliśmy pierwszy wariant

### Tylko klient 0
![Alt text](Z5.1/hist.png)

### Wszyscy klienci
![Alt text](Z5.2/hist.png)
