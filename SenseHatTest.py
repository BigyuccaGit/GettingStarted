from sense_hat import SenseHat
from time import sleep

sense=SenseHat()

sense.clear()

yellow=(255,255,0)
blue=(0,0,255)

sense.show_message("Hello World",text_colour=yellow, back_colour=blue,scroll_speed=0.05)

g=(0,255,0)
b=(0,0,255)

creeper=[
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,b,b,g,
    g,g,g,g,g,b,b,g,
    g,g,g,b,b,g,g,g,
    g,g,b,b,b,b,g,g,
    g,g,b,b,b,b,g,g,
    g,g,b,g,g,b,g,g,   
    ]

sense.set_pixels(creeper)

number=0
while number<6:
    sleep(1)
    sense.flip_h()
    number+=1

sense.clear()

