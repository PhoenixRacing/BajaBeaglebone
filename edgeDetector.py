from Sensor import *
import time
import Adafruit_BBIO.GPIO as GPIO

class EdgeDetector(Sensor):

	def __init__(self, pins, magnets, numPoints=10):
		super(self.__class__, self).__init__(pins, numPoints)
		GPIO.setup(pins[0], GPIO.IN)
		self.magnets = magnets
		self.lastEdge = None
		self.currentEdge = time.time()

	def risingEdge(self):
		self.lastEdge = self.currentEdge
		self.currentEdge = time.time()
		self.updateRPM()

	def updateRPM(self):
		self.addToMemory(self.calculateRPM())
		self.setSensorVal(self.processMemory('median'))

	def calculateRPM(self):
		return 1 / ((self.currentEdge - self.lastEdge) * self.magnets) * 60.0

	def run(self):
		while True:
			GPIO.wait_for_edge(self.pins[0], GPIO.RISING)
			self.risingEdge()
			print self

if __name__=='__main__':
	h = EdgeDetector(["P8_10"], 1, numPoints=5)
	h.run()
	
	
