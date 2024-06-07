
from RPLCD.i2c import CharLCD
import threading
import time
import dht11
import os

TEMPERATURE = 0
HUMIDITY = 0

# Constants to initialise the LCD
lcdmode = 'i2c'
cols = 16
rows = 2
charmap = 'A00'
i2c_expander = 'PCF8574'
address = 0x27 # Address found using i2cdetect
port = 1 # 0 on an older Raspberry Pi

# Initialise the LCD
lcd = CharLCD(i2c_expander, address, port=port, charmap=charmap, cols=cols, rows=rows)

# GPIO setup for DHT11
DHT_PIN = 4
BUZZER_PIN = 18

# Setup for DHT11 sensor
instance = dht11.DHT11(pin=DHT_PIN)

# Function to export and set GPIO direction
def gpio_export(pin):
    with open("/sys/class/gpio/export", "w") as f:
        f.write(str(pin))

def gpio_unexport(pin):
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(str(pin))

def gpio_direction(pin, direction):
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write(direction)

def gpio_write(pin, value):
    with open(f"/sys/class/gpio/gpio{pin}/value", "w") as f:
        f.write(str(value))

def gpio_read(pin):
    with open(f"/sys/class/gpio/gpio{pin}/value", "r") as f:
        return int(f.read().strip())

def buzzer():
    gpio_export(BUZZER_PIN)
    gpio_direction(BUZZER_PIN, "out")

    while True:
        if HUMIDITY > 50:
            gpio_write(BUZZER_PIN, 1)
            time.sleep(0.5)
            gpio_write(BUZZER_PIN, 0)
            time.sleep(0.5)
        else:
            time.sleep(1)

    gpio_unexport(BUZZER_PIN)

def read_sensor():
    global TEMPERATURE, HUMIDITY

    while True:
        result = instance.read()
        if result.is_valid():
            TEMPERATURE = result.temperature
            HUMIDITY = result.humidity
            lcd.cursor_pos = (0, 0)
            lcd.write_string(f"Temp: {result.temperature:0.1f} C")
            lcd.cursor_pos = (1, 0)
            lcd.write_string(f"Humidity: {result.humidity:0.1f} %")
        time.sleep(1)

if __name__ == "__main__":
    # Initialize GPIO
    os.system("echo {} > /sys/class/gpio/export".format(DHT_PIN))
    os.system("echo out > /sys/class/gpio/gpio{}/direction".format(DHT_PIN))

    # Start threads
    threading.Thread(target=buzzer).start()
    threading.Thread(target=read_sensor).start()

