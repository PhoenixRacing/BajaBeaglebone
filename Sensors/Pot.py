from Sensor import *
import time
import Adafruit_BBIO.GPIO as GPIO

class Pot(Sensor):

	def __init__(self, pins, name, numPoints=10):
		super(self.__class__, self).__init__(pins, numPoints, name)
		GPIO.setup(pins[0], GPIO.IN)

	def run(self):
		while True:
			self.measureProcessAndSet(GPIO.input(self.pins[0]), 'average')
			self.publish()
			time.sleep(.01)

if __name__=="__main__":
	p = Pot(["P8_10"], "pot")
	p.run()