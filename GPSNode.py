from PubSub import PubSub
from BBGPS import BBGPS

nodeName = "GPS"

gps = BBGPS(delay=.1)

p = PubSub()

def dispatch():
    p.publish(nodeName, gps.getLatLong())

gps.publish = dispatch

def run():
    gps.run()

if __name__=="__main__":
    gps.run()        
