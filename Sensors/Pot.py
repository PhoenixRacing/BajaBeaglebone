from Sensor import *
import time
import Adafruit_BBIO.ADC as ADC

class Pot(Sensor):

	def __init__(self, pins, name, numPoints=10, delay=.1):
		super(self.__class__, self).__init__(pins, numPoints, name)
		ADC.setup()
		self.delay = delay

	def run(self):
		while True:
			val = ADC.read(self.pins[0])
			self.measureProcessAndSet(val, 'average')
			time.sleep(self.delay)
			self.publish()

if __name__=="__main__":
	p = Pot(["P9_39"], "pot")
	p.run()