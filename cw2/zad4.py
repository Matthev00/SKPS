import time
import gpio4

gpio19 = gpio4.SysfsGPIO(19)
gpio19.export = True
gpio19.direction = 'out' # set direction to output

frequencies = [
261.63, # C4
293.66, # D4
329.63, # E4
349.23, # F4
392.00, # G4
440.00, # A4
493.88, # B4
523.25, # C5
587.33, # D5
659.25, # E5
698.46, # F5
783.99, # G5
880.00, # A5
987.77, # B5
1046.50, # C6
]


while True:
        for f in frequencies:
                duration = 0.5
                start_time = time.time()
                while time.time() - start_time < duration:
                        gpio19.value = 1
                        time.sleep(1 / (f*2))
                        gpio19.value = 0
                        time.sleep(1 / (f*2))


gpio19.export = False # cleanup