from m5stack import *
from m5stack_ui import *
from uiflow import *
import module
import time

def test_servos_leds_goplus2():
    screen = M5Screen()
    screen.clean_screen()
    screen.set_screen_bg_color(0xFFFFFF)
    label0 = M5Label('Provant servos i LEDS', x=20, y=36, color=0x000, font=FONT_MONT_26)

    go_plus_2 = module.get(module.GOPLUS2)

    go_plus_2.set_servo_angle(go_plus_2.S1, 0)
    go_plus_2.set_servo_plus(go_plus_2.S2, 1500)
    rgb.setColorFrom(6, 10, 0x000000)
    rgb.setColorFrom(1, 5, 0x000000)

    for i in range(2):  # dues repeticions de la seqüència
        rgb.setColorFrom(6, 10, 0xff0000)
        rgb.setColorFrom(1, 5, 0x000099)
        go_plus_2.set_servo_angle(go_plus_2.S1, 0)
        time.sleep(1)
        go_plus_2.set_servo_plus(go_plus_2.S2, 500)
        time.sleep(1)
        go_plus_2.set_servo_angle(go_plus_2.S1, 90)
        time.sleep(1)
        go_plus_2.set_servo_plus(go_plus_2.S2, 1000)
        time.sleep(1)
        go_plus_2.set_servo_angle(go_plus_2.S1, 180)
        time.sleep(1)
        go_plus_2.set_servo_plus(go_plus_2.S2, 1500)
        time.sleep(1)
        go_plus_2.set_servo_angle(go_plus_2.S1, 90)
        time.sleep(1)
        go_plus_2.set_servo_plus(go_plus_2.S2, 1500)
        time.sleep(1)
        go_plus_2.set_servo_angle(go_plus_2.S1, 0)
        time.sleep(1)
        go_plus_2.set_servo_plus(go_plus_2.S2, 2000)
        time.sleep(1)
        rgb.setColorFrom(6, 10, 0x006600)
        rgb.setColorFrom(1, 5, 0x006600)
        time.sleep(0.1)
