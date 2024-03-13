# LABORATORIUM 1
## Autorzy 
Michał Sadowski 325221
Mateusz Ostaszewski 325203

## 1. Złożeznie stanowiska laboratyjnego: zestaw z Raspberry Pi 4B (RPi)

Udało się złożyć stanowisko i zosatło to zatwierdzone przez prwoadzącego

## 2. Pierwsze uruchomienie RPi, sprawdzenie połączenia sieciowego, wykonanie próbnych transferów plików

### Pierwsze uruchoniemie RPi

![Alt text](screenshots/po%C5%82%C4%85czenie_terminana_uart.png)

Po włączeniu zalislania wyświetliły się logi

Zalogowaliśmy się jako root

Został przynany adres ip

![Alt text](screenshots/przyznanie_adresu_ip.png)

### Sprawdzenie połączenia sieciowego

![Alt text](screenshots/pingowanie.png)
![Alt text](screenshots/ping_host.png)

Pingowanie w obie strony działa więc połączenie sieciowe się udało

### Wykonanie próbnych transferów plików

![Alt text](screenshots/udostepnienie_katalogu.png)

![Alt text](screenshots/pobieranie_pliku.png)

Udało sie przesłać plik testowy z hosta na Rpi 

## 3. Zbudowanie za pomocą buildroot obrazu linuxa dla Rpi z init RAM fs

### Zgodnie z wykładu 1 i 2 zbudowaliśmy system linux w BR. 

    - #make raspberrypi4_64_defdonfig
    - #make menuconfig
        - Toolchain -> Toolchain type: External toolchain
        - Uaktywniona opcja cpio the root filesystem
        - Uaktywniona opcja inital RAM filesystem
        - Dezaktywowana opcja ext/2/3/4
    - #make

![Alt text](screenshots/main_koniec.png)    

Make zakończył się błędem lecz był on spodziewany ponieważ wyłączyliśmy ext4 

### Kopiowanie plików image, cmdline.txt i bcm2711-rpi-4-b.dtb

Kopiujemy wyżej wymienione pliki z hosta na RPi korzystając z komunkacji przez serwer http.server

![Alt text](screenshots/zapisane_pliki.png)

### Montujemy partycje 1 (boot) karty SD 

Przy pomocy polecenia mount montujhemy partycje w katalogu /mnt

Kopiujemy pliki image, cmdline.txt i bcm2711-rpi-4-b.dtb do /mnt/user

Zmieniamy nazwę pliku image na kernel8.img

![Alt text](screenshots/kopia_plikow_partycja_1.png)

### Resrart RPi

Wykonumemy restart RPi przy pomocy reboot

![Alt text](screenshots/zbudowany_linux.png)

## 4. Zbudowanie za pomocą buildroot obrazu linuxa dla Rpi z systemem plików na trwałym nośniku 

### Usunięcie poprzedniego obrazu

Wykonujemy to za pomocą polecienia:
 #make linux-dirclean
![Alt text](screenshots/make_linux_dirclea.png)
### Wprowadzenie zmian w menu config
    - Toolchain -> Toolchain type: External toolchain
    - Uaktywniona opcja cpio the root filesystem
    - Dezaktywowana opcja inital RAM filesystem
    - Aktywowana opcja ext/2/3/4
    - Zmiana rozmiaru partycji boot na dwa razy większą
    Rekompilacja poleceniem make

 ![Alt text](screenshots/zmieninoy%20_rozmiar.png)   

### Wynikowy obraz jest mniejszy niż w poprzednim ćwiczeniu

Jest to spowodowane tym, że w poprzednim ćwiczeniu filesystem musiał być zawarty w obrazie, a w tym jest osobno pod systemem plików

### Kopiowanie plików na RPi partycję 2

Kopiujemy plik: rootfs.ext2 z host na Rpi korzystając z http.server

![Alt text](screenshots/skopiowane_br.png) 
![Alt text](screenshots/skopiowane_pliki_zad2.png)
![Alt text](screenshots/1.png)

### Test czy system rzeczywiście korzysta z systemu plików

Tworzymy plik test.txt 

Następnie restartujemy buildroot.
