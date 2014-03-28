from Sensor import *
import time
import Adafruit_BBIO.GPIO as GPIO

class Pot(Sensor):

	def __init__(self, pins, magnets, numPoints=10):
		super(self.__class__, self).__init__(pins, numPoints)
		GPIO.setup(pins[0], GPIO.IN)

	def run():
		while True:
			self.measureProcessAndSet(GPIO.input(self.pins[0]), 'average')
			self.publish()
			time.sleep(.01)


