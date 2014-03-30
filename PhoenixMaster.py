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
	import dummySpeedPub
	import dashAppNode
	import hallNode
	import allNode
	import loggerNode
        PhoenixMaster([
                dummySpeedPub.sendSpeed, 
                dashAppNode.run,
		hallNode.frontLeftHall.run, 
		hallNode.frontRightHall.run,
		loggerNode.run,
		allNode.run,
                ], ['python dashAppHelper.py']
	)
