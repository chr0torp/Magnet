import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
    GPIO.output(17, GPIO.HIGH)
    time.sleep(10.0)        
    GPIO.output(17, GPIO.LOW)

    time.sleep(2.0)

except KeyboardInterrupt:
    print("Ctrl+C pressed, exiting.")

finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()
    print("GPIO Cleanup Done.")