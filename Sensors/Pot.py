from Sensor import *
import time
import Adafruit_BBIO.ADC as ADC

class Pot(Sensor):

	def __init__(self, pins, name, numPoints=10, delay=1):
		super(self.__class__, self).__init__(pins, numPoints, name)
		self.numPoints = numPoints
		ADC.setup()
		self.delay = delay

	def run(self):
		i = 0
		while True:
			val = ADC.read(self.pins[0])
			self.measureProcessAndSet(val, 'average')
			i += 1
			time.sleep(self.delay / float(self.numPoints))
			if not i%self.numPoints:
				self.publish()
				i = 0
	
if __name__=="__main__":
	p = Pot(["P9_39"], "pot")
	p.run()