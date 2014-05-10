from PubSub import PubSub
import urllib2
import urllib
from random import randint

def handleSpeed(sender, signal):
	data = {'speed' : signal}
	encoded = urllib.urlencode(data)
	req = urllib2.Request('http://localhost:5000/updatespeed')
	req.add_data(encoded)
	try:
		urllib2.urlopen(req)
	except:
		print 'Speed request failed. Dashboard might not be spun up'

def handleLockSpin(sender, signal):
	sig = signal
	l = sig.get('lock')
	s = sig.get('spin')
	data = {'lock': l, 'spin': s}
	encoded = urllib.urlencode(data)
	req = urllib2.Request('http://localhost:5000/updatespinlock')
	req.add_data(encoded)
	try:
		urllib2.urlopen(req)
	except:
		print 'Lock request Failed. Dashboard might not be spun up'

def handleBrakeThrot(sender, signal):
	s = signal
	b = s.get('brake')
	t = s.get('throttle')
	data = {'brake': b, 'throttle': t}
	encoded = urllib.urlencode(data)
	req = urllib2.Request('http://localhost:5000/updatebrakethrottle')
	req.add_data(encoded)
	try:
		urllib2.urlopen(req)
	except:
		print 'BrThr request Failed. Dashboard might not be spun up'

def handlePit(sender, signal):
	data = {'pit': signal}
	encoded = urllib.urlencode(data)
	req = urllib2.Request('http://localhost:5000/updatepit')
	req.add_data(encoded)
	try:
		urllib2.urlopen(req)
	except:
		print 'Pit request failed. Dashboard might not be spun up'


p1 = PubSub()
p2 = PubSub()
p3 = PubSub()
p4 = PubSub()
def run():
	p1.subscribe("speed", handleSpeed)
	p2.subscribe("spinLock", handleLockSpin)
	p3.subscribe("brakeThrot", handleBrakeThrot)
	p4.subscribe("pit", handlePit)

if __name__=="__main__":
	handleLockSpin("", {0:0})
	handleSpeed("", 5)
	handleBrakeThrot("", {0:0})
	handlePit("", 0)

