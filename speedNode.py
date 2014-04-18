from pydispatch import dispatcher
import json

WHEEL_DIAMETER = 2.0 #feet

def speed(sender, signal):
	dispatcher.send(signal=calcSpeed(signal), sender="speed")

def calcSpeed(RPM):
	return RPM * WHEEL_DIAMETER / 2580.0 * 60.0 #MPH

def mean(lis):
	if not lis:
		return 0
	return sum(lis) / len(lis)

def run():
	dispatcher.connect(speed, sender="frontLeftHall")
	dispatcher.connect(speed, sender="frontRightHall")

if __name__=="__main__":
	run()
