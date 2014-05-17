from Sensor import *
import time
import Adafruit_BBIO.GPIO as GPIO

class EdgeDetector(Sensor):

	def __init__(self, pins, magnets, name, numPoints=10, timeout=1):
		super(self.__class__, self).__init__(pins, numPoints, name)
		GPIO.setup(pins[0], GPIO.IN)
		self.magnets = magnets
		self.lastEdge = None
		self.currentEdge = time.time()
		self.timeout = timeout

	def edgeDetected(self):
		if self.lastEdge:
			self.setNewEdge()
			self.updateRPM()
		else:
			self.setNewEdge()
		self.publish() #CRUCIAL

	def setNewEdge(self):
		self.lastEdge = self.currentEdge
		self.currentEdge = time.time()

	def updateRPM(self):
		self.addToMemory(self.calculateRPM())
		self.setSensorVal(self.processMemory('average'))

	def calculateRPM(self):
		return 1 / ((self.currentEdge - self.lastEdge) * self.magnets) * 60.0

	def setZero(self):
		self.lastEdge = None
		self.currentEdge = time.time()
		self.clearMemory()	#dont want this to be swallowed
		self.setSensorVal(0)

	def run(self):
		GPIO.add_event_detect(self.pins[0], GPIO.RISING)
		while True:
			if GPIO.event_detected(self.pins[0]):
				print "EDGE"
				self.edgeDetected()
			if time.time() - self.currentEdge > self.timeout:
				self.setZero()
				self.publish()

if __name__=='__main__':
	h = EdgeDetector(["P8_12"], 1, "hall", numPoints=5, timeout=5)
	h.run()