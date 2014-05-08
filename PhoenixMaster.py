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
		time.sleep(5)
		self.killOnInterrupt()

	def killOtherPythonProcesses(self):
		processes = subprocess.check_output('pgrep python', shell=True).split("\n")
		this_id = str(os.getpid())
		processes.remove(this_id)
		for process in processes:
			if process:
				subprocess.call('sudo kill ' + process, shell=True)		
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
#	import DashApp
#	import lockNode
	PhoenixMaster([dummySpeedNode.run, allNode.run]) #, DashApp.run, lockNode.run])
