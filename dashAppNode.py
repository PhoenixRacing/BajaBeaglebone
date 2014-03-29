from pydispatch import dispatcher
import urllib2

def handleSpeed(sender, signal):
	urllib2.Request('localhost:5000/update_speed', { 'speed' : signal})

dispatcher.connect(handleSpeed, sender="speed")

handleSpeed("", 5)