from pydispatch import dispatcher
import urllib2
import urllib
import requests
from random import randint
import json

def handleSpeed(sender, signal):
	data = {'speed' : signal}
	try:
		requests.post('http://localhost:5000/updatespeed', data=data, timeout=1)
	except:
		print 'request to dash app failed'

def handleLockSpin(sender, signal):
	s = json.loads(signal)
	l = s.get('lock')
	s = s.get('spin')
	data = {'lock': l, 'spin': s}
	encoded = urllib.urlencode(data)
	try:
		requests.post('http://localhost:5000/updatespinlock', data=data)
	except:
		print 'Request Failed. Dashboard might not be spun up'

def handleBrakeThrot(sender, signal):
	s = json.loads(signal)
	b = s.get('brake')
	t = s.get('throttle')
	data = {'brake': b, 'throttle': t}
	try:
		requests.post('http://localhost:5000//updatebrakethrottle', data=data, timeout=1)
	except:
		print 'Request Failed. Dashboard might not be spun up'

def run():
	dispatcher.connect(handleSpeed, sender="speed")
	dispatcher.connect(handleLockSpin, sender="spinlock")
	dispatcher.connect(handleBrakeThrot, sender="brakethrot")

if __name__=="__main__":
	handleLockSpin("", json.dumps({}))
	handleSpeed("", 5)
	handleBrakeThrot("", json.dumps({}))

