import time
import subprocess
import sys
import os
import logging
from multiprocessing import Process

class PhoenixMaster(object):

	def __init__(self, processes):
		self.processes = processes
		self.configLogger()
		self.startProcesses()
		self.killOnInterrupt()

	def startProcesses(self):
		for process in self.processes:
			p = Process(target=process)
			p.start()

	def killOnInterrupt(self):
		try:
			while True: 
				time.sleep(1000) #so we don't waste cycles
		except:
			subprocess.call("pkill python", shell=True)

	def configLogger(self):
		logger = logging.getLogger('PhoenixMaster')
		logger.setLevel(logging.DEBUG)
		fh = logging.FileHandler('logs/main.log')
		fh.setLevel(logging.DEBUG)
		ch = logging.StreamHandler()
		ch.setLevel(logging.ERROR)
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		fh.setFormatter(formatter)
		ch.setFormatter(formatter)
		logger.addHandler(fh)
		logger.addHandler(ch)

if __name__=="__main__":
	mode = "BB"

        def dashApp():
            import subprocess
            subprocess.call("python DashApp/__init__.py", shell=True)
 

	if mode=="LOCAL":

	    import dummySpeedNode
	    import dummyPitNode
	    import dummyLockNode
	    import dummyBrakeThrNode
	    import dashAppNode
	    import allNode
	    import lockNode
	    import herokuNode
	    import printNode
 
	    PhoenixMaster([dummySpeedNode.run, 
			   dummyPitNode.run,
			   dummyLockNode.run,
			   dummyBrakeThrNode.run,
			   dashAppNode.run,
			   allNode.run, 
			   lockNode.run, 
			   herokuNode.run,
			   dashApp,
			   printNode.run])

	elif mode=="BB":
	    import allNode
	    import herokuNode
	    import gpioNode
            import printNode
            import GPSNode
            import jsonLoggerNode
            import speedNode

	    PhoenixMaster([dashApp,
                           allNode.run, 
                           speedNode.run,
                           jsonLoggerNode.run, 
			   herokuNode.run,
                           printNode.run,
                           GPSNode.run] +
			   [sensor.run for sensor in gpioNode.sensors])
