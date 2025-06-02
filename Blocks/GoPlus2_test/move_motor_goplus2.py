from m5stack import *
from m5ui import *
from uiflow import *
import i2c_bus

def move_motor(motor, speed):
    # Inicia el bus I2C del port M5Stack
    i2c = i2c_bus.get(i2c_bus.M_BUS)

    # Controla el motor via GoPlus2 (adreça I2C: 0x38)
    if motor == '1':
        i2c.writeto(0x38, bytes([0x00, int(speed)]))
    elif motor == '2':
        i2c.writeto(0x38, bytes([0x01, int(speed)]))
