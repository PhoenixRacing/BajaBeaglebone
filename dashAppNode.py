from PubSub import PubSub
import urllib2
import urllib
from random import randint
import threading

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
	print '\n',signal,'\n\n\n'
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

def handleThrot(sender, signal):
	encoded = urllib.urlencode({"throttle" : signal})
	req = urllib2.Request('http://localhost:5000/updatethrottle')
	req.add_data(encoded)
	try:
		urllib2.urlopen(req)
	except:
		print 'Throt request Failed. Dashboard might not be spun up'

def handleBrake(sender, signal):
	encoded = urllib.urlencode({"brake" : signal})
	req = urllib2.Request('http://localhost:5000/updatebrake')
	req.add_data(encoded)
	try:
		urllib2.urlopen(req)
	except:
		print 'Brake request Failed. Dashboard might not be spun up'

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

def speedHandler():
	p1.subscribe("speed", handleSpeed)

def brakeHandler():
	p2.subscribe("brake", handleBrake)

def throtHandler():
	p3.subscribe("throttle", handleThrot)

def pitHandler():
	p4.subscribe("pit", handlePit)

def run():
	threading.Thread(target=speedHandler).start()
	threading.Thread(target=brakeHandler).start()
	threading.Thread(target=throtHandler).start()
	p4.subscribe("pit", handlePit)


if __name__=="__main__":
	handleLockSpin("", {0:0})
	handleSpeed("", 5)
	handleThrot("", 0)
	handleBrake("", 0)
	handlePit("", 0)

