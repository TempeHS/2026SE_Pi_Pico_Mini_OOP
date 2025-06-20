from machine import Pin, PWM, time_pulse_us
from time import sleep, sleep_us

sleep(0.1)

TRIG_PIN = 12
ECHO_PIN = 11
servo_pin = 10

servo = PWM(Pin(servo_pin))

servo.freq(50)

trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

def set_angle(angle):
    angle = min(max(angle, 0), 180)
    return int(500 + (angle / 180) * 2000)

def map_range(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def get_distance():
    trig.value(0)
    sleep_us(2)
    trig.value(1)
    sleep_us(10)
    trig.value(0)

    try:
        pulse_time = time_pulse_us(echo, 1, 30000)
    except OSError as ex:
        if ex.args[0] == 110:
            return None
        raise ex
    
    distance_cm = (pulse_time / 2) / 29.1
    return distance_cm

while True:
    dist = get_distance()
    if dist is not None:
        mapped_value = map_range(dist, 0, 410, 0, 180)
        servo.duty_ns(set_angle(mapped_value)*1000)
    else:
        print('Out of Range')
    print(f"Distance: {dist} , Servo: {servo.duty_ns()}")
    sleep(0.1)