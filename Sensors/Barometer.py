from time import sleep
from termcolor import colored
import subprocess
from Sensor import *


class Barometer(Sensor):

	def __init__(self, name, delay=.1):
		super(self.__class__, self).__init__([],1, name)
		
		self.delay = delay
		

	def run(self):
		subprocess.call("echo bmp085 0x77 > /sys/class/i2c-adapter/i2c-1/new_device", shell=True)
		while True:
			f = open ("/sys/bus/i2c/drivers/bmp085/1-0077/pressure0_input","r")
			pres=float(f.read())
			f = open ("/sys/bus/i2c/drivers/bmp085/1-0077/temp0_input","r")	
			temp=float(f.read())/10.0
			alti = 44330.0*(1-pow(pres/101325.0,1/5.255))
			val = (temp,pres,alti) #temp C, pressure Kpa, Altitude meter
			
			self.setSensorVal(str(val))
			sleep(self.delay)
			self.publish()

if __name__ == "__main__":
	B = Barometer('Barometer')
	B.run()
