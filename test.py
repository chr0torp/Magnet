from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
    while True:
        GPIO.output(17, GPIO.HIGH)
        sleep(2.5)
        GPIO.output(17, GPIO.LOW)
        sleep(2.5)

except KeyboardInterrupt:
    GPIO.cleanup()