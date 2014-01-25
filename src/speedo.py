import Adafruit_BBIO.GPIO as GPIO

GPIO.add_event_detect("P8_3", GPIO.RISING)

try:
    while True:
        if GPIO.event_detected("P8_3"):
            print "input rising"
except KeyboardInterrupt:
    GPIO.cleanup()