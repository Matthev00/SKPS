from math import sin, pi
import time
import gpio4

gpio27 = gpio4.SysfsGPIO(27)
gpio27.export = True
gpio27.direction = 'out' # set direction to output

MAX_TIME = 10

current_time = 0
frequency = 100
step = 0.0001

while current_time < MAX_TIME:
        duty_cycle = abs(sin(current_time * pi)/2)
        if current_time % (1 / frequency) < duty_cycle * (1 / frequency):
                gpio27.value = 1
        else:
                gpio27.value = 0
        current_time += step
        time.sleep(step)


gpio27.export = False # cleanup