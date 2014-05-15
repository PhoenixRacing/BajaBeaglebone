from PubSub import PubSub
import threading

WHEEL_DIAMETER = 2.0 #feet

p1 = PubSub()
p2 = PubSub()
s = PubSub()
def speed(sender, signal):
	s.publish("speed", calcSpeed(signal))

def calcSpeed(RPM):
	return RPM * WHEEL_DIAMETER / 2580.0 * 60.0 #MPH

def mean(lis):
	if not lis:
		return 0
	return sum(lis) / len(lis)

def frontLeftSpeed():
	p1.subscribe("frontLeftHall", speed)

def run():
	threading.Thread(target=frontLeftSpeed).start()
	p2.subscribe("frontRightHall", speed)

if __name__=="__main__":
	run()
