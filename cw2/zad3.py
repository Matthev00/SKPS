import gpio4
import time

gpio27 = gpio4.SysfsGPIO(27)
gpio27.export = True
gpio27.direction = "out"

gpio18 = gpio4.SysfsGPIO(18)
gpio18.export = True
gpio18.direction = "in"

try:
    while True:
        if gpio18.value:
            gpio27.value = abs(gpio27.value - 1)
        time.sleep(0.1)
except KeyboardInterrupt:
    gpio27.export = False
    gpio18.export = False
    print("GPIO cleanup finished")