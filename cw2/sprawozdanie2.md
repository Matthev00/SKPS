# LABORATORIUM 2
## Autorzy 
Michał Sadowski 325221
Mateusz Ostaszewski 325203

## Instalacja OpenWRT

### Uruchomienie i instalacja operwrt

Uruchomiliśmy system system 
![Alt text](screenshots/uruchomienie_1.png)

Pobraliśmy system 

![Alt text](screenshots/2_pobrany_opeen_wrt.png)

Rozpakowaliśmy system

![Alt text](screenshots/3_rozpakowanie.png)

Montujemy 1 partycje oraz 2 partyce (tutaj się pojawiła literówka która poźniej naprawiliśmy)
![Alt text](screenshots/montowanie_4.png)

Kopiujemy pliki

![Alt text](screenshots/5_kopiowanie_plikow.png)

Napotkaliśmy błąd, literówka podczas montowania pliku

Jeszcze raz zamontowaliśmy oraz zwiększyliśmy rozmiar

![Alt text](screenshots/6_poprawa_i_resize.png)

Po tym zrebootowalismy system

### Konfiguracja sieciowa 

W pliku /etc/config/network zmodyfikowliśmy konfiguracje 
![Alt text](screenshots/10-config-net.png)

Następnie przy używając polecenia /etc/init.d/network reload zersetowalismy siec

### Interfejs HTTP
![Alt text](screenshots/11-logingrpi.png)

Przy pomocy interfejsu http zainstalowalismy pakiety: 
- gpio-tools
- spi-tools
- i2c-tools 
- python3 
- pyhton3-pip
- python3-smbus 
- python3-gpiod
## Zadania

### zadanie 1

Zawartość kodu w pliku zad1.py

### zadanie 2

Zawartość kodu w pliku zad2.py

### zadanie 3

Zawartość kodu w pliku zad3.py

### zadanie 4

Zawartość kodu w pliku zad4.py

Schemat podłączenia buzzera
![Alt text](screenshots/schemat1.png)

