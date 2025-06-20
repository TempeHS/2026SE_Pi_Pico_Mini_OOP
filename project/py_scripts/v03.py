from machine import Pin
from time import sleep, time

class Led_Light(Pin)
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        #self.led_light_state
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing

    def on(self):
        self.high()
        if self.__debug:
            print(f"LED is connected to Pin {self.__pin} is")

    def off(self):
        self.low()
        if self.__debug:
            print(f"LED is connected to Pin {self.__pin} is")

    def toggle(self):
        if self.value():
            self.on()
        else:
            self.off()

    @property
    def led_light_state(self):
        return self.value()
    
    @led_light_state
    def led_light_state(self, value):
        if value == 0:
            self.off()
        elif value == 1:
            self.on()

red_light = Led_Light(3, False, True)

while True:
    red_light.on()
    sleep(0.5)
    red_light.off()
    sleep(0.5)