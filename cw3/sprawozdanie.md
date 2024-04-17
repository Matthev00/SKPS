# Sprawozdanie SKPS lab3
## Michał Sadowski Mateusz Ostaszewski 

## zadanie 1

Pobieramy SDK opernwrt. Oraz pakiet demo

![Alt text](screens/1.png)

W pliku feeds.conf.default dopisalismy ścieżkę:

![Alt text](screens/2.png)

Update feeds i install

![Alt text](screens/3.png)
![Alt text](screens/4.png)

Dodalismy pakiety w make menuconfig

![Alt text](screens/5.png)

Skompilowalismy pakiet

![Alt text](screens/6.png)

Poprzez serwer przesłalimsy pakiet na RPi

![Alt text](screens/7.png)

Odebraliśmy pakiety na RPi

![Alt text](screens/8.png)

Zainstalowalismy pakiet

![Alt text](screens/9.png)

Wywołanie programu

![Alt text](screens/10.png)

## Zadanie 2

Analogicznie jak w 1 zadaniu dodalsmy pakiety

![Alt text](screens/11.png)

Dodalismy ściezkę

![Alt text](screens/12.png)

Przesłaliśmy pakiety na RPi

![Alt text](screens/13.png)

Instalacja pakietów

![Alt text](screens/14.png)

Uruchomienie programów

WORMS

![Alt text](screens/15.png)

BUGGY

![Alt text](screens/17.png)

## Zadanie 3

Zainstalowalismy gbd i gdbserver


![Alt text](screens/18.png)

### W 1 podpunkcie znaleźlismy niezalokowaną tablice

![Alt text](screens/19.png)

### W 2 podpunkcie znaleźliśmy błąd wychodzenia poza tablice która jest zalokowana na 1000 intów
![Alt text](screens/21.png)
