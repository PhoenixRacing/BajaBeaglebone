import Adafruit_BBIO.GPIO as GPIO
GPIO.setup("P8_10", GPIO.IN)
GPIO.wait_for_edge("P8_10", GPIO.RISING)
