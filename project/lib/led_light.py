from machine import Pin
from time import sleep, time

class Led_Light(Pin)
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        #self.led_light_state
        #self.led_light_state
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing
        self.__last_toggle_time = time()

    def on(self):
        self.high()
        if self.__debug:
            print(f"LED is connected to Pin {self.__pin} is {self.led_light_state}")

    def off(self):
        self.low()
        if self.__debug:
            print(f"LED is connected to Pin {self.__pin} is {self.led_light_state}")

    def toggle(self):
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
            self.off()

    @property
    def led_light_state(self):
        return self.value()
    
    @led_light_state.setter
    def led_light_state(self, value):
        if value == 1:
            self.off()
        elif value == 0:
            self.on()

def flash(self):
    now = time()
    if self.__flashing and now - self.__last_toggle_time >= 0.5:
        self.toggle()
        self.__last_toggle_time = now
