#! /usr/local/bin/python
#-*- coding: utf-8 -*-
import gps, os, time, sys
import subprocess

class BBGPS(object):
	
	def __init__(self, delay=1):
		if os.path.isfile('gpshelper.sh'):
			subprocess.call('chmod +x ./gpshelper.sh',shell=True)
			subprocess.Popen('./gpshelper.sh',shell=True,stderr=subprocess.PIPE)
		else:
			subprocess.call('chmod +x ../gpshelper.sh',shell=True)
			subprocess.Popen('../gpshelper.sh',shell=True,stderr=subprocess.PIPE)
		time.sleep(5)
		self.delay = delay
		self.g = gps.gps(mode=gps.WATCH_NEWSTYLE)
		self.lat = 0
		self.long = 0
		self.speed = 0

	def getSpeed(self):
		self.speed = self.g.fix.speed
		if self.speed != self.speed:
			self.speed = 0
		return self.speed

	def getLatLong(self):
		return (self.g.fix.latitude, self.g.fix.longitude)

	def updateLatLong(self):
		latlong = self.getLatLong()
		self.lat = latlong[0]
		self.long = latlong[1]

	def run(self):
		while True:
			self.g.read()
			if gps.PACKET_SET:
				self.g.stream()
			self.updateLatLong()
			self.publish()
			time.sleep(self.delay)

	def publish(self):
		print self

	def __repr__(self):
		return "Latitude: %s\nLongitude:%s\n, Speed: %s"%(self.lat, self.long, self.speed)


if __name__=="__main__":
	g = BBGPS()
	g.run()

        # print ' GPS reading'
        # print '----------------------------------------'
        # print 'latitude ' , g.fix.latitude
        # print 'longitude ' , g.fix.longitude
        # print 'time utc ' , g.utc,' + ', g.fix.time
        # print 'altitude ' , g.fix.altitude
        # print 'epc ' , g.fix.epc
        # print 'epd ' , g.fix.epd
        # print 'eps ' , g.fix.eps
        # print 'epx ' , g.fix.epx
        # print 'epv ' , g.fix.epv
        # print 'ept ' , g.fix.ept