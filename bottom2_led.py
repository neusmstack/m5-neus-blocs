from machine import Pin
import neopixel

# Inicialitza la tira de 10 LEDs al pin GPIO25
np = neopixel.NeoPixel(Pin(25), 10)

def set_led(index, r, g, b):
    if 0 <= index < 10:
        np[index] = (r, g, b)
        np.write()

def clear_all():
    for i in range(10):
        np[i] = (0, 0, 0)
    np.write()
