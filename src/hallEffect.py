from Sensor import *
import time

class HallEffect(Sensor):

	def __init__(self, pins, magnets, numPoints=10):
		super(self.__class__, self).__init__(pins, numPoints)
		self.magnets = magnets
		self.lastEdge = None
		self.currentEdge = time.time()

	def risingEdge(self):
		self.lastEdge = self.currentEdge
		self.currentEdge = time.time()
		self.updateRPM()

	def updateRPM(self):
		self.addToMemory(self.calculateRPM())
		self.setSensorVal(self.processMemory('average'))

	def calculateRPM(self):
		return 1 / ((self.currentEdge - self.lastEdge) * self.magnets) * 60.0


if __name__=='__main__':

	import random
	h = HallEffect(["GPIO_30"], 2)

	for i in range(1000):
		time.sleep((.95 + random.random()/10) / 100)
		h.risingEdge()
		print h
