from pydispatch import dispatcher
from BBGPS import BBGPS

nodeName = "GPS"

gps = BBGPS()

def dispatch():
    dispatcher.send(signal=gps.getLatLong(), sender=nodeName)

gps.publish = dispatch

def run():
    gps.run()

if __name__=="__main__":
    gps.run()        
