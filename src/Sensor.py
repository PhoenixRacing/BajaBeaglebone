from collections import deque

"""Abstract class for sensors on Baja car"""
class Sensor(object):

	def __init__(self, numPoints):
		self.memory = deque(maxlen=numPoints)
		self.val = None

	def setSensorVal(self, val):
		self.val = val

	def getSensorVal(self):
		return self.val

	def addToMemory(self, val):
		self.memory.append(val)

	def processMemory(self, method):
		if method=='average':
			return sum(self.memory) / len(self.memory)
		else:
			return None

	def __repr__(self):
		return "Sensor: %s \t Val: %.3f \t Num Points: %d"%(type(self).__name__, self.getSensorVal(), len(self.memory)) 