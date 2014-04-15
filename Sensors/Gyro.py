import IMU.l3gd20
from termcolor import colored
from time import sleep
from Sensor import *


class Gyro(Sensor):

	def __init__(self, pins, name, delay=.05):
		super(self.__class__, self).__init__(pins, 1, name)
		
		self.delay = delay
		self.bus = IMU.l3gd20.setup_bus(1) 					# bus: 3 indicates /dev/i2c-3
		self.S = IMU.l3gd20.setup_gyro(self.bus,IMU.l3gd20.DPS2000)	# gyro scale +/- 2000.0 dps

	def run(self):
		while True:
			W = IMU.l3gd20.get_gyro(self.bus,self.S)
			val = (W[0],W[1],W[2])
			self.setSensorVal(val)
			sleep(self.delay)
			self.publish()


if __name__=="__main__":
	g = Gyro([],'gyro',delay=.05)
	g.run()
