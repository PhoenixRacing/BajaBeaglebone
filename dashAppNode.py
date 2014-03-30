from pydispatch import dispatcher
import urllib2
import urllib

def handleSpeed(sender, signal):
	data = {'speed' : signal}
        encoded = urllib.urlencode(data)
	req = urllib2.Request('http://localhost:5000/updatespeed')
        req.add_data(encoded)
	try:
	        urllib2.urlopen(req)
	except:
		print 'Request failed. Dashboard might not be spun up'

def run():
	dispatcher.connect(handleSpeed, sender="speed")

if __name__=="__main__":
        handleSpeed("", 5)
