import time
import threading
import subprocess
import sys
import os
import logging

""" Starts each program as a separate Python thread
These all die when the main thread is interrupted
Intended to be master script for starting pubsub nodes """
class PhoenixMaster(object):

	def __init__(self, thread_nodes, process_nodes=[]):
		if '-nokill' not in sys.argv:
			self.killOtherPythonProcesses()
		self.configLogger()
		for thread_node in thread_nodes:
			self.addNode(thread_node)
                for process_node in process_nodes:
                        self.startProcess(process_node)
		self.run()

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

	def killOtherPythonProcesses(self):
		processes = subprocess.check_output('pgrep python', shell=True).split("\n")
		this_id = str(os.getpid())
		processes.remove(this_id)
		for process in processes:
			if process:
				subprocess.call('sudo kill ' + process, shell=True)		

	def startProcess(self, process_node):
		subprocess.Popen(process_node, shell=True) #, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	def addNode(self, node):
		thread = threading.Thread(target=node)
		thread.daemon = True
                thread.start()
		
	def run(self):
		self.killOnInterrupt()

	def killOnInterrupt(self):
		try:
			while True: 
				time.sleep(1000) #so we don't waste cycles
		except:
			subprocess.call("pkill python", shell=True)

if __name__=="__main__":

	debugMode = "LOCAL" # "LOCAL" or "BB"

	if debugMode == "LOCAL":	
		import dashAppNode
		import allNode
		import printNode
		import lockNode
		import speedNode
		import herokuNode
		import dummySpeedNode
		import dummyLockNode
		import dummyBrakeThrNode
		import dummyPitNode
		import jsonLoggerNode
 
		PhoenixMaster([
				dashAppNode.run,
				dummySpeedNode.run,
				dummyLockNode.run,
				dummyBrakeThrNode.run,
				dummyPitNode.run] + 
			      [ printNode.run,
			        allNode.run,
			        lockNode.run,
			        speedNode.run,
			        herokuNode.run,
			        jsonLoggerNode.run,
			      ], 
			      ['python dashAppHelper.py']
	        )

	elif debugMode == "BB":
		import dashAppNode
		import gpioNode
		import allNode
		import printNode
		import lockNode
		import speedNode
		import herokuNode
		import loggerNode
		import GPSNode

		PhoenixMaster([ dashAppNode.run ] + 
			      [ sensor.run for sensor in gpioNode.sensors] +
			      [ printNode.run,
			        allNode.run,
			        lockNode.run,
			        speedNode.run,
			        herokuNode.run,
			        jsonLoggerNode.run,
			        GPSNode.run,
			       ], 
			       ['python dashAppHelper.py']
		)
