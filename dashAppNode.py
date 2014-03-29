from pydispatch import dispatcher
import urllib2
import urllib

def handleSpeed(sender, signal):
	data = {'speed' : signal}
	print data
	print urllib2.Request('localhost:5000/update_speed', urllib.urlencode(data))

def run():
	dispatcher.connect(handleSpeed, sender="speed")

handleSpeed("", 5)