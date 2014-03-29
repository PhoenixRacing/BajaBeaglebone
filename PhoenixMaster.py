import time
import threading
import sys

""" Starts each program as a separate Python thread
These all die when the main thread is interrupted
Intended to be master script for starting pubsub nodes """
class PhoenixMaster(object):

	def __init__(self, process=None, *nodes):
		self.nodes = []
		for node in nodes:
			self.addNode(node)
		if process:
			self.addProcess(process)
		self.run()

	def addProcess(self, no):
		return

	def addNode(self, node):
		thread = threading.Thread(target=node)
		thread.daemon = True
		self.nodes.append(thread)
		
	def run(self):
		for node in self.nodes:
			node.start()
		self.killOnInterrupt()

	def killOnInterrupt(self):
		try:
			while True: 
				time.sleep(1000) #so we don't waste cycles
		except (KeyboardInterrupt, SystemExit):
			sys.exit()

if __name__=="__main__":
	from dummySpeedPub import sendSpeed
	import dashAppNode
	import hallNode
        PhoenixMaster(
#		dashAppNode.run, 
		sendSpeed, 
		hallNode.frontLeftHall.run, 
		hallNode.frontRightHall.run
	)
