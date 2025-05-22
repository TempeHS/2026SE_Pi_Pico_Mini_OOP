from machine import Pin
from time import sleep

# Wait for USB to become ready
sleep(0.1)

#store desired output pin in a variable
led_pin = 25

#configure GPIO Pin as an output pin and create and led object for Pin class
led = Pin(led_pin, Pin.OUT)

while True:
        led.value(True)  #turn on the LED
        sleep(1)   #wait for one second
        led.value(False)  #turn off the LED
        sleep(1)   #wait for one second
