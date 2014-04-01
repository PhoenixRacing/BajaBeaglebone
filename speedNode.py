from pydispatch import dispatcher
import json

WHEEL_DIAMETER = 1.0 #meters?

def speed(sender, signal):
	allData = json.loads(signal)
	speed = calcSpeed(allData)
	dispatcher.send(signal=speed, sender="speed")

def calcSpeed(allData):
	left = allData.get('frontLeftHall', 0)
	right = allData.get('frontRightHall',0)
	return (left + right) / 2.0 * WHEEL_DIAMETER

def run():
	dispatcher.connect(speed, sender="allNode")

if __name__=="__main__":
	run()
