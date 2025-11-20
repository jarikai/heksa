import RPi.GPIO as GPIO
from time import sleep
from gpiozero import PWMLED
from gpiozero import CPUTemperature
import time

GPIO.setwarnings(False)

in2 = 27
en_a = 4

fan_low  = 40  # fan OFF below this temp, fan_min to fan_max pwm above this
fan_high = 65  # fan fan_max% pwm above this temp
fan_time = 10  # sampling time in seconds
fan_min  = .25 # minimum pwm duty cycle when running (stops stalling)
fan_max  = 1   # maximum pwm duty cycle when running


GPIO.setmode(GPIO.BCM)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en_a,GPIO.OUT)

q=GPIO.PWM(en_a,100)
q.start(100)

GPIO.output(in2,GPIO.LOW)

try:
     while(True):
        time.sleep(fan_time)
        cpu_temp = str(CPUTemperature()).split("=")
        temp = float(str(cpu_temp[1])[:-1])
        if temp >= fan_high:
            GPIO.output(in2,GPIO.HIGH)
        elif temp <= fan_low:
            GPIO.output(in2,GPIO.LOW)

except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()
