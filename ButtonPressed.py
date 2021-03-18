from gpiozero import LED,Button
from signal import pause

led = LED(4)
right_button = Button(15)
left_button = Button(14)
    
# Set up callbacks
right_button.when_pressed = led.toggle

left_button.when_pressed = led.on
left_button.when_released = led.off

try:
    pause()
except :
    led.off()
    exit()
