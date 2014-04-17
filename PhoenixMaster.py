import time
import threading
import subprocess
import sys
import os

""" Starts each program as a separate Python thread
These all die when the main thread is interrupted
Intended to be master script for starting pubsub nodes """
class PhoenixMaster(object):

	def __init__(self, thread_nodes, process_nodes=[]):
		if '-nokill' not in sys.argv:
			self.killOtherPythonProcesses()
		for thread_node in thread_nodes:
			self.addNode(thread_node)
                for process_node in process_nodes:
                        self.startProcess(process_node)
		self.run()

	def killOtherPythonProcesses(self):
		processes = subprocess.check_output('pgrep python', shell=True).split("\n")
		this_id = str(os.getpid())
		processes.remove(this_id)
		for process in processes:
			if process:
				subprocess.call('sudo kill ' + process, shell=True)		

	def startProcess(self, process_node):
		subprocess.call(process_node, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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
			print 'hi'
			sys.exit()

if __name__=="__main__":
	import dashAppNode
	import gpioNode
	import allNode
	import loggerNode
	import lockNode
	import speedNode
	import herokuNode
	import dummySpeedNode
	import dummyLockNode
	import dummyBrakeThrNode
#	from Mongo import mongoNode

        PhoenixMaster([
                dashAppNode.run,
#		dummySpeedNode.run,
#		dummyLockNode.run,
#		dummyBrakeThrNode.run] 
		]+ 
		[sensor.run for sensor in gpioNode.sensors] +
		[loggerNode.run,
		allNode.run,
		lockNode.run,
		speedNode.run,
		herokuNode.run,
#		mongoNode.run,
                ], ['python dashAppHelper.py']
	)
