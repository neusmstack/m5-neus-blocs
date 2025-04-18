from m5stack import *
from m5ui import *
from uiflow import *
from neopixel import NeoPixel
import machine

# Inicialitzar el NeoPixel del Bottom2
np = NeoPixel(machine.Pin(25), 10)  # Bottom2 té 10 LEDs

def set_led_color(led, color):
    try:
        r, g, b = color
        np[int(led)] = (int(r), int(g), int(b))
        np.write()
    except:
        print("Error: color ha de ser una tupla (R,G,B)")
