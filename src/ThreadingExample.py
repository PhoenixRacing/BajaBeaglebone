import time
import threading
from DashApp import dashApp
import sys

def killOnInterrupt():
	try:
		while True: 
			time.sleep(100) #so we don't waste cycles
	except (KeyboardInterrupt, SystemExit):
		sys.exit()

def phonyThread():
	while True:
		print "fart"
		time.sleep(1)
		

appthread = threading.Thread(target=dashApp.run)
appthread.daemon = True
appthread.start()

phonyThread = threading.Thread(target=phonyThread)
phonyThread.daemon = True
phonyThread.start()

killOnInterrupt()
