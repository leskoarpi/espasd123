import machine
import time
import network

led = machine.Pin(2, machine.Pin.OUT)
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)


sta_if.scan()
sta_if.connect("Arpi", "20031231")

while sta_if.isconnected():
    sta_if.isconnected()
    led.value(1)
    time.sleep(0.10)
    led.value(0)
    time.sleep(0.10)
    
    
for x in range(15):    
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
    
