import time
from collections import deque

class HallEffect(object):

	def __init__(self, magnets, numPoints=10):
		self.magnets = magnets
		self.lastEdge = None
		self.currentEdge = time.time()
		self.currentRPM = 0
		self.RPMMemory = deque(maxlen=numPoints)

	def risingEdge(self):
		self.lastEdge = self.currentEdge
		self.currentEdge = time.time()
		self.updateRPM()

	def updateRPM(self):
		rawRPM = 1 / ((self.currentEdge - self.lastEdge) * self.magnets) * 60.0
		self.RPMMemory.append(rawRPM)
		self.setCurrentRPM(sum(self.RPMMemory) / len(self.RPMMemory))

	def setCurrentRPM(self, RPM): 
		self.currentRPM = RPM

	def getCurrentRPM(self):
		return self.currentRPM

	def __repr__(self):
		return "RPM: %s \t Num Points: %d"%(self.getCurrentRPM(), len(self.RPMMemory)) 


if __name__=='__main__':

	import random

	h = HallEffect(2)

	for i in range(1000):
		time.sleep((.95 + random.random()/10) / 100)
		h.risingEdge()
		print h
