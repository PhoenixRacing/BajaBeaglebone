#! /usr/bin/python
 
import os
from gps import *
from time import sleep
        
class BBGPS(gps):

        def __init__(self):
		gps.__init__(self, mode=WATCH_ENABLE)
 	
	def getLatLong(self):
		return self.gps.fix.latitude, self.gps.fix.longitude

bbgps = BBGPS()

if __name__ == '__main__':
        gpsd = BBGPS() 
        while True:
		print gpsd
		time.sleep(1)
		

