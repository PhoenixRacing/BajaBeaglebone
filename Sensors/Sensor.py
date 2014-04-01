from collections import deque

"""Abstract class for sensors on Baja car"""
class Sensor(object):

	def __init__(self, pins, numPoints, name):
		self.pins = pins
		self.memory = deque(maxlen=numPoints)
		self.val = 0
		self.name = name

	def clearMemory(self):
		self.memory.clear()

	def getName(self):
		return self.name

	def setSensorVal(self, val):
		self.val = val

	def getSensorVal(self):
		return self.val

	def addToMemory(self, val):
		self.memory.append(val)

	def measureProcessAndSet(self, data, process_type):
		self.addToMemory(data)
		self.setSensorVal(self.processMemory(process_type))

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

	def setPublishFunc(self, func):
		self.publish = func

	def publish(self):
		print self

	def __repr__(self):
		return "Sensor: %s \t Val: %.3f \t Num Points: %d \t Pins: %s"%(self.name, self.getSensorVal(), len(self.memory), self.pins) 
