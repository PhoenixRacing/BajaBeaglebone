from pydispatch import dispatcher
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
		print 'Request failed. Dashboard might not be spun up'

def handleLockSpin(sender, signal):
	data = {'spin': signal, 'lock': signal}
	encoded = urllib.urlencode(data)
	req = urllib2.Request('http://localhost:5000/updatespinlock')
	req.add_data(encoded)
	try:
		urllib2.urlopen(req)
	except:
		print 'Request Failed. Dashboard might not be spun up'

def run():
	dispatcher.connect(handleSpeed, sender="speed")
	dispatcher.connect(handleLockSpin, sender="spinlock")

if __name__=="__main__":
	handleLockSpin("", 0)
	handleSpeed("", 5)

