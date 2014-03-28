from collections import deque

"""Abstract class for sensors on Baja car"""
class Sensor(object):

	def __init__(self, pins, numPoints):
		self.pins = pins
		self.memory = deque(maxlen=numPoints)
		self.val = None

	def clearMemory(self):
		self.memory = deque(maxlen=numPoints)

	def setSensorVal(self, val):
		self.val = val

	def getSensorVal(self):
		return self.val

	def addToMemory(self, val):
		self.memory.append(val)

	def processMemory(self, method):
		if method=='average':
			return self.average()
		elif method=='median':
			return self.median()
		else:
			return None

	def average(self):
		if not self.memory:
			return 0
		return sum(self.memory) / len(self.memory)

	def median(self):
		if not self.memory:
			return 0
		return sorted(self.memory)[len(self.memory)//2]

	def publish(self):
		print self

	def __repr__(self):
		return "Sensor: %s \t Val: %.3f \t Num Points: %d \t Pins: %s"%(type(self).__name__, self.getSensorVal(), len(self.memory), self.pins) 
