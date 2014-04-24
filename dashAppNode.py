from pydispatch import dispatcher
import urllib2
import urllib
from random import randint
import json

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
	sig = json.loads(signal)
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
	s = json.loads(signal)
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


def run():
	dispatcher.connect(handleSpeed, sender="speed")
	dispatcher.connect(handleLockSpin, sender="spinlock")
	dispatcher.connect(handleBrakeThrot, sender="brakethrot")
	dispatcher.connect(handlePit, sender="pit")

if __name__=="__main__":
	handleLockSpin("", 0)
	handleSpeed("", 5)
	handleBrakeThrot("", 0)
	handlePit("", 0)

