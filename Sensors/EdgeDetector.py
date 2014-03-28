from Sensor import *
import time
import Adafruit_BBIO.GPIO as GPIO

class EdgeDetector(Sensor):

	def __init__(self, pins, magnets, numPoints=10, timeout=1):
		super(self.__class__, self).__init__(pins, numPoints)
		GPIO.setup(pins[0], GPIO.IN)
		self.magnets = magnets
		self.lastEdge = None
		self.currentEdge = time.time()
		self.timeout = timeout

	def risingEdge(self):
		self.lastEdge = self.currentEdge
		self.currentEdge = time.time()
		self.updateRPM()
		self.publish() #CRUCIAL

	def updateRPM(self):
		self.addToMemory(self.calculateRPM())
		self.setSensorVal(self.processMemory('median'))

	def calculateRPM(self):
		return 1 / ((self.currentEdge - self.lastEdge) * self.magnets) * 60.0

	def setZero():
		self.clearMemory()	#dont want this to be swallowed
		self.setSensorVal(0)

	def run(self):
		GPIO.add_event_detect(self.pins[0], GPIO.RISING)
		while True:
			if GPIO.event_detected(self.pins[0]):
				self.risingEdge()
				self.publish()
			if time.time() - self.lastEdge > self.timeout:
				self.setZero()
				self.lastEdge = time.time()
				self.publish()


			

if __name__=='__main__':
	h = EdgeDetector(["P8_10"], 1, numPoints=5, timeout=1)
	h.run()