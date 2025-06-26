from led_light import Led_Light
from controller import TrafficLightSubsystem, PedestrianSubsystem
from audio_notification import Audio_Notification
from pedestrian_button import Pedestrian_Button
from time import sleep

led_pedestrian_red = Led_Light(19, True, True)
led_pedestrian_green = Led_Light(17, False, True)
led_traffic_red = Led_Light(3, False, True)
led_traffic_amber = Led_Light(5, False, True)
led_traffic_green = Led_Light(6, False, True)
pedestrian_button = Pedestrian_Button(22, True)
buzzer = Audio_Notification(27, True)

Light = TrafficLightSubsystem(led_traffic_red, led_traffic_amber, led_traffic_green, False)
Pedestrian = PedestrianSubsystem(led_pedestrian_red, led_pedestrian_green, pedestrian_button, buzzer, False)

def Traffic_Subsystem_Driver():
    print("Testing traffic light in 5 seconds")
    sleep(5)
    Light.show_red()
    print("Pass if: Red ON, Amber OFF & Green OFF")
    sleep(10)
    Light.show_amber()
    print("Pass if: Amber ON, Red OFF & Green OFF")
    sleep(10)
    Light.show_green()
    print("Pass if: Green ON, Amber OFF & Red OFF")
    sleep(10)

def Pedestrian_Subsystem_Driver():
    print("Testing")
    Pedestrian.show_walk()
    Pedestrian.show_warning()
    Pedestrian.show_stop()
    Pedestrian.is_button_pressed()
    Pedestrian.reset_button()

Traffic_Subsystem_Driver()