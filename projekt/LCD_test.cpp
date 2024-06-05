#include <iostream>
#include <fstream>
#include <linux/i2c-dev.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <cstring>
#include <cmath>
#include <chrono>
#include <thread>

#define I2C_ADDR 0x27 // Adres I2C Twojego wyświetlacza
#define DHT_PIN 4 // Pin czujnika DHT11
#define MAX_TIMINGS 85

// Definicje poleceń LCD
#define LCD_CHR 1 // Tryb znaków
#define LCD_CMD 0 // Tryb poleceń

#define LINE1 0x80 // Adres DDRAM linii 1
#define LINE2 0xC0 // Adres DDRAM linii 2

#define LCD_BACKLIGHT 0x08 // Podświetlenie LCD włączone
#define ENABLE 0b00000100 // Bit umożliwiający transmisję danych

void lcd_init(int fd);
void lcd_byte(int fd, int bits, int mode);
void lcd_toggle_enable(int fd, int bits);
void lcd_string(int fd, const char* message, int line);
void read_dht11_dat(int& temperature, int& humidity);

void gpio_export(int pin) {
    std::ofstream fs;
    fs.open("/sys/class/gpio/export");
    fs << pin;
    fs.close();
}

void gpio_unexport(int pin) {
    std::ofstream fs;
    fs.open("/sys/class/gpio/unexport");
    fs << pin;
    fs.close();
}

void gpio_direction(int pin, std::string dir) {
    std::ofstream fs;
    fs.open("/sys/class/gpio/gpio" + std::to_string(pin) + "/direction");
    fs << dir;
    fs.close();
}

void gpio_write(int pin, int value) {
    std::ofstream fs;
    fs.open("/sys/class/gpio/gpio" + std::to_string(pin) + "/value");
    fs << value;
    fs.close();
}

int gpio_read(int pin) {
    std::ifstream fs;
    fs.open("/sys/class/gpio/gpio" + std::to_string(pin) + "/value");
    int value;
    fs >> value;
    fs.close();
    return value;
}

int main() {
    int fd;
    char *i2c_device = (char*)"/dev/i2c-1";

    if ((fd = open(i2c_device, O_RDWR)) < 0) {
        std::cerr << "Failed to open the i2c bus" << std::endl;
        return 1;
    }

    if (ioctl(fd, I2C_SLAVE, I2C_ADDR) < 0) {
        std::cerr << "Failed to acquire bus access and/or talk to slave" << std::endl;
        return 1;
    }

    lcd_init(fd); // Inicjalizacja LCD

    // Setup GPIO for DHT11
    gpio_export(DHT_PIN);
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    
    int temperature, humidity;
    
    while (true) {
        read_dht11_dat(temperature, humidity);
        if (true) {
            char temp_str[16];
            char hum_str[16];
            snprintf(temp_str, sizeof(temp_str), "Temp: %-3d.%d C", temperature / 10, temperature % 10);
            snprintf(hum_str, sizeof(hum_str), "Humidity: %-3d.%d%%", humidity / 10, humidity % 10);
            lcd_string(fd, temp_str, LINE1);
            lcd_string(fd, hum_str, LINE2);
        }
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }

    close(fd);
    gpio_unexport(DHT_PIN);
    return 0;
}

void lcd_init(int fd) {
    lcd_byte(fd, 0x33, LCD_CMD); // Tryb 4-bitowy
    lcd_byte(fd, 0x32, LCD_CMD); // Tryb 4-bitowy
    lcd_byte(fd, 0x06, LCD_CMD); // Ustawienie kursora w prawo
    lcd_byte(fd, 0x0C, LCD_CMD); // Włączenie LCD, wyłączenie kursora
    lcd_byte(fd, 0x28, LCD_CMD); // 2 linie, tryb 5x7
    lcd_byte(fd, 0x01, LCD_CMD); // Wyczyść wyświetlacz
    usleep(500);
}

void lcd_byte(int fd, int bits, int mode) {
    int bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT;
    int bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT;

    char data[4];
    data[0] = bits_high;
    data[1] = bits_high | ENABLE;
    data[2] = bits_high & ~ENABLE;
    data[3] = bits_low;
    write(fd, data, 4);
    lcd_toggle_enable(fd, bits_high);
    lcd_toggle_enable(fd, bits_low);
}

void lcd_toggle_enable(int fd, int bits) {
    usleep(500);
    char data[1];
    data[0] = (bits | ENABLE);
    write(fd, data, 1);
    usleep(500);
    data[0] = (bits & ~ENABLE);
    write(fd, data, 1);
    usleep(500);
}

void lcd_string(int fd, const char* message, int line) {
    lcd_byte(fd, line, LCD_CMD);
    while (*message) {
        lcd_byte(fd, *message++, LCD_CHR);
    }
}

void read_dht11_dat(int& temperature, int& humidity) {
    uint8_t laststate = 1;
    uint8_t counter = 0;
    uint8_t j = 0, i;
    int dht11_dat[5] = {0, 0, 0, 0, 0};

    gpio_direction(DHT_PIN, "out");
    gpio_write(DHT_PIN, 0);
    std::this_thread::sleep_for(std::chrono::milliseconds(18));
    gpio_write(DHT_PIN, 1);
    std::this_thread::sleep_for(std::chrono::microseconds(40));
    gpio_direction(DHT_PIN, "in");

    for (i = 0; i < MAX_TIMINGS; i++) {
        counter = 0;
        while (gpio_read(DHT_PIN) == laststate) {
            counter++;
            std::this_thread::sleep_for(std::chrono::microseconds(1));
            if (counter == 255) {
                break;
            }
        }
        laststate = gpio_read(DHT_PIN);

        if (counter == 255) break;

        if ((i >= 4) && (i % 2 == 0)) {
            dht11_dat[j / 8] <<= 1;
            if (counter > 16) dht11_dat[j / 8] |= 1;
            j++;
        }
    }

    if ((j >= 40) &&
        (dht11_dat[4] == ((dht11_dat[0] + dht11_dat[1] + dht11_dat[2] + dht11_dat[3]) & 0xFF))) {
        humidity = dht11_dat[0] * 10 + dht11_dat[1];
        temperature = dht11_dat[2] * 10 + dht11_dat[3];
    } else {
	temperature = -1;
	humidity = -1;
    }
}
