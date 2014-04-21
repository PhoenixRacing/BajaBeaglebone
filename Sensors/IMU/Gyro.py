import l3gd20
from termcolor import colored
from time import sleep
from Sensor import *
import Adafruit_BBIO.ADC as ADC

class Gyro(Sensor):

	def __init__(self, pins, name, numPoints=5, delay=.05):
		super(self.__class__, self).__init__(pins, numPoints, name)
		ADC.setup()
		self.delay = delay
		bus = l3gd20.setup_bus(1) 					# bus: 3 indicates /dev/i2c-3
		S = l3gd20.setup_gyro(bus,l3gd20.DPS2000)	# gyro scale +/- 2000.0 dps

	def run(self):
		while True:
			W = l3gd20.get_gyro(bus,S)
			val = (W[0],W[1],W[2])
			
			self.setSenorVal(val)
			time.sleep(self.delay)
			self.publish()


if __name__=="__main__":
	g = Gyro([],'gyro',1,.05)
	g.run
