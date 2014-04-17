from pydispatch import dispatcher
import json

WHEEL_DIAMETER = 1.0 #meters?

def speed(sender, signal):
	allData = json.loads(signal)
	speed = calcSpeed(allData)
	dispatcher.send(signal=speed, sender="speed")

def calcSpeed(allData):
	left = mean(allData.get('frontLeftHall', []))
	right = mean(allData.get('frontRightHall', []))
	return (left + right) / 2.0 * WHEEL_DIAMETER

def mean(lis):
	if not lis:
		return 0
	return sum(lis) / len(lis)

def run():
	dispatcher.connect(speed, sender="allNode")

if __name__=="__main__":
	run()
