import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_14", GPIO.IN)
if GPIO.input("P8_14"):
    print 'high'
else:
    print 'low'