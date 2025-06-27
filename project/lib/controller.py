from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time

class TrafficLightSubsystem:
    def __init__(self, red, amber, green, debug=False):
        self.__red = red
        self.__amber = amber
        self.__green = green
        self.__debug = debug

    def show_red(self):
        if self.__debug:
            print("Traffi: Red ON")
        self.__red.on()
        self.__amber.off()
        self.__green.off()

    def show_amber(self):
        if self.__debug:
            print("Traffi: Amber ON")
        self.__red.off()
        self.__amber.on()
        self.__green.off()
    
    def show_green(self):
        if self.__debug:
            print("Traffi: Green ON")
        self.__red.off()
        self.__amber.off()
        self.__green.on()

class PedestrianSubsystem:
    def __init__(self, red, green, button, buzzer, debug=False):
        self.__red = red
        self.__green = green
        self.__button = button
        self.__buzzer = buzzer
        self.__debug = debug

    def show_stop(self):
        if self.__debug:
            print("Pedestrian: Red On")
            self.__red.on()
            self.__green.off()
            self.__buzzer.warning_off()

    def show_walk(self):
        if self.__debug:
            print("Pedestrian: Green On")
            self.__red.off()
            self.__green.on()                
            self.__buzzer.warning_on()
        
    def show_warning(self):
        if self.__debug:
            print("Pedestrian: Warning On")
            self.__red.flashing()
            self.__green.off()
            self.__buzzer.warning_off()

    def is_button_pressed(self):
        return self.__button.button_state()
        
    def reset_button(self):
        self.__button.button_state(False)

class Controller:
    def __init__(self, ped_red, ped_green, traffic_red, traffic_amber, traffic_green, button, buzzer, debug):
        self.__traffic_lights = TrafficLightSubsystem(traffic_red, traffic_amber, traffic_green, debug)
        self.__pedestrian_signals = PedestrianSubsystem(ped_red, ped_green, button, buzzer, debug)
        self.__debug = debug
        self.state = "IDLE"
        self.last_state_change = time()

    def set_idle_state(self):
        if self.__debug:
            print("System in idle state")
        self.__pedestrian_signals.show_stop()
        self.__traffic_lights.show_green()

    def set_change_state(self):
        if self.__debug:
            print("System in change state")
        self.__pedestrian_signals.show_stop()
        self.__traffic_lights.show_amber()

    def set_walk_state(self):
        if self.__debug:
            print("System in walk state")
        self.__pedestrian_signals.show_walk()
        self.__traffic_lights.show_red()

    def set_warning_state(self):
        if self.__debug:
            print("System in warning state")
        self.__pedestrian_signals.show_warning()
        self.__traffic_lights.show_red()

    def set_error_state(self):
        if self.__debug:
            print("System in error state")
        self.__traffic_lights.show_amber()

    def update(self):
        print("Running")
        now = time.now()
        if self.state == "IDLE":
            self.set_idle_state()
            if self.__pedestrian_signals.is_button_pressed() and now - self.last_state_change >= 5:
                self.state = "Changing"
                self.last_state_change = now
        elif self.state == "Changing":
            self.set_change_state()
            if now - self.last_state_change >= 5:
                self.state = "Walking"
                self.last_state_change = time.now
        elif self.state == "Walking":
            self.set_walk_state()
            if time.now - self.last_state_change >= 5:
                self.state = "Warning"
                self.last_state_change = time.now
        elif self.state == "WARNING":
            self.set_warning_state()
            if time.now - self.last_state_change >= 5:
                self.state = "IDLE"
                self.last_state_change = time.now
                self.__pedestrian_signals.reset_button()
        else:
            self.set_error_state()