import time
import threading
import subprocess
import sys

""" Starts each program as a separate Python thread
These all die when the main thread is interrupted
Intended to be master script for starting pubsub nodes """
class PhoenixMaster(object):

	def __init__(self, thread_nodes, process_nodes=[]):
		for thread_node in thread_nodes:
			self.addNode(thread_node)
                for process_node in process_nodes:
                        self.startProcess(process_node)
		self.run()

	def startProcess(self, process_node):
		subprocess.call(process_node, shell=True)

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
		except (KeyboardInterrupt, SystemExit):
			sys.exit()

if __name__=="__main__":
	import dashAppNode
	import hallNode
	import allNode
	import loggerNode
	import lockNode
	import speedNode
	import dummySpeedNode
        PhoenixMaster([
                dashAppNode.run,
#		dummySpeedNode.run,
		hallNode.frontLeftHall.run, 
		hallNode.frontRightHall.run,
		hallNode.backLeftHall.run,
		hallNode.backRightHall.run,
		loggerNode.run,
		allNode.run,
		lockNode.run,
		speedNode.run,
                ], ['python dashAppHelper.py']
	)
