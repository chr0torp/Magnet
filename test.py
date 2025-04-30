import time
import RPi.GPIO as GPIO
import keyboard

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
    while True:
        time.sleep(0.5)
        if keyboard.is_pressed('s'):
            print("'s' pressed")
            GPIO.output(17, GPIO.HIGH)
            
        if keyboard.is_pressed('q'):
            print("'q' pressed")
            GPIO.output(17, GPIO.LOW)
            break

        time.sleep(0.01)

except KeyboardInterrupt:
    print("Ctrl+C pressed, exiting.")

finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()
    print("GPIO Cleanup Done.")