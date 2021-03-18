from gpiozero import LED
from time import sleep

led = LED(25)

while True:
    led.on()
    print("on")
    sleep(1)
    led.off()
    print("Off")
    sleep(1)
    