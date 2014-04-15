import IMU.lsm303
from termcolor import colored
from time import sleep
from Sensor import *


class Accelerometer(Sensor):

	def __init__(self, pins, name, delay=.05):
		super(self.__class__, self).__init__(pins,1, name)
		self.delay = delay
		self.bus = IMU.lsm303.setup_bus(1) 					# bus: 3 indicates /dev/i2c-3
		self.Sa = IMU.lsm303.setup_acc(self.bus,IMU.lsm303.SCALE_A_8G)		# acc. scale +/- 8.0 g
		self.Sm = IMU.lsm303.setup_mag(self.bus,IMU.lsm303.SCALE_M_81G)		# mag. scale +/- 8.1 gauss
	def run(self):
		while True:
			a = IMU.lsm303.get_acc(self.bus,self.Sa)
			m = IMU.lsm303.get_mag(self.bus,self.Sm)
			val = {}
			val['Accelerometer'] = (a[0],a[1],a[2])
			val['Compass'] = (m[0],m[1],m[2])
			
			self.setSensorVal(str(val))
			sleep(self.delay)
			self.publish()


if __name__ == "__main__":
	A = Accelerometer([],'Accelerometer',.05)
	A.run()
