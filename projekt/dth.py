import time
import os

# GPIO setup for DHT11
DHT_PIN = 4

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

def read_dht11():
    # DHT11 data format
    MAX_TIMINGS = 85
    data = [0] * 5

    gpio_export(DHT_PIN)
    gpio_direction(DHT_PIN, "out")
    gpio_write(DHT_PIN, 0)
    time.sleep(0.018)
    gpio_write(DHT_PIN, 1)
    gpio_direction(DHT_PIN, "in")

    last_state = 1
    counter = 0
    j = 0

    for i in range(MAX_TIMINGS):
        counter = 0
        while gpio_read(DHT_PIN) == last_state:
            counter += 1
            if counter == 255:
                break

        last_state = gpio_read(DHT_PIN)

        if counter == 255:
            break

        if (i >= 4) and (i % 2 == 0):
            data[j // 8] <<= 1
            if counter > 16:
                data[j // 8] |= 1
            j += 1

    gpio_unexport(DHT_PIN)

    if (j >= 40) and (data[4] == (data[0] + data[1] + data[2] + data[3]) & 0xFF):
        humidity = data[0] + data[1] / 10.0
        temperature = data[2] + data[3] / 10.0
        return temperature, humidity
    else:
        return None, None

def main():
    while True:
        temperature, humidity = read_dht11()
        if temperature is not None and humidity is not None:
            print(f"Temperature: {temperature:.1f}°C, Humidity: {humidity:.1f}%")
        else:
            print("Failed to read from sensor, trying again...")
        time.sleep(2)

if __name__ == "__main__":
    main()

