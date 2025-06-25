from led_light import Led_light
from time import sleep, time
from machine import Pin

red_light = Led_light(3, flashing=True, debug=True)
yellow_light = Led_light(3, flashing=True, debug=True)
green_light = Led_light(3, flashing=True, debug=True)

print("Testing On")

if led.on():
    print("Testing Pass")
    sleep(1)
elif led.off():
    print("Testing Fail")
    sleep(1)