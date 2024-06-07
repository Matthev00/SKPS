import gpio4
import time
import threading
import http.server
import socketserver

buzzer = gpio4.SysfsGPIO(17)
buzzer.export = True
buzzer.direction = "out"

sensor = gpio4.SysfsGPIO(27)
sensor.export = True
sensor.direction = "in"

trigger = gpio4.SysfsGPIO(19)
trigger.export = True
trigger.direction = "out"

def measure(sensor, trigger):
    trigger.value = 0
    time.sleep(0.1)
    trigger.value = 1
    time.sleep(0.1)
    trigger.value = 0
    while sensor.value == 0:
        pass

    t = time.time()
    while sensor.value == 1:
        pass

    distance = (time.time() - t) * 34300 / 2
    print(distance)
    if distance < 10:
        threading.Thread(target=buzzer_beep, args=(0.5,)).start()
    else:
        buzzer.value = 0
    return distance

def buzzer_beep(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        buzzer.value = 1
        time.sleep(0.001)
        buzzer.value = 0
        time.sleep(0.001) 
    buzzer.value = 0

HOST, PORT = "10.42.0.124", 9005

class RandomNumberHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        distance = measure(sensor, trigger)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(f'{{"distance": {distance}}}\n', "utf-8"))

with socketserver.TCPServer((HOST, PORT), RandomNumberHandler) as httpd:
    print(f"Serwer działa na adresie {HOST}:{PORT}")
    httpd.serve_forever()
