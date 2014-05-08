import time
import subprocess
import sys
import os
import logging
from multiprocessing import Process

class PhoenixMaster(object):

	def __init__(self, processes):
		print 'code called'
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
	import dummySpeedNode
	import allNode
	import lockNode
	import herokuNode
	def dashApp():
		import subprocess
		subprocess.call("python DashApp/__init__.py", shell=True)

	PhoenixMaster([dummySpeedNode.run, 
		       allNode.run, 
		       lockNode.run, 
		       herokuNode.run,
		       dashApp])
