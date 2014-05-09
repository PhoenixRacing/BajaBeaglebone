import time
import subprocess
import sys
import os
import logging
from multiprocessing import Process

class PhoenixMaster(object):

	def __init__(self, processes):
		self.processes = processes
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

if __name__=="__main__":
	mode = "LOCAL"

	if mode=="LOCAL":

	    import dummySpeedNode
	    import allNode
	    import lockNode
	    import herokuNode
	    import printNode

	    def dashApp():
		    import subprocess
		    subprocess.call("python DashApp/__init__.py", shell=True)

	    PhoenixMaster([dummySpeedNode.run, 
			   allNode.run, 
			   lockNode.run, 
			   herokuNode.run,
			   dashApp,
			   printNode.run])

	elif mode=="BB":
	    import dummySpeedNode
	    import allNode
	    import lockNode
	    import herokuNode
	    import gpioNode

	    def dashApp():
		    import subprocess
		    subprocess.call("python DashApp/__init__.py", shell=True)

	    PhoenixMaster([dummySpeedNode.run, 
			   allNode.run, 
			   lockNode.run, 
			   herokuNode.run] +
			   [sensor.run for sensor in gpioNode.sensors])
