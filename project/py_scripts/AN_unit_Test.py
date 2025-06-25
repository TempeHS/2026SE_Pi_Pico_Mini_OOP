from audio_notfication import Audio_Notification
from time import sleep, time
from machine import Pin

Buzzer = Audio_Notification(27)


buzzer.warning_on()
sleep(1)
buzzer.warning_off()