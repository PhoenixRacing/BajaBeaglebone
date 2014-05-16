from PubSub import PubSub

WHEEL_DIAMETER = 2.16667 #feet
scale = 1.0

p = PubSub()
s = PubSub()
def speed(sender, signal):
	s.publish("speed", calcSpeed(signal))

def calcSpeed(RPM):
	return RPM * WHEEL_DIAMETER / 2580.0 * 60.0 / 11.0 * scale #MPH

def run():
	p.subscribe("outputShaft", speed)

if __name__=="__main__":
	run()
