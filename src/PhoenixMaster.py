import time
import threading
import sys
from PubA import sendMessageA
from SubA import listenForMessageA

""" Starts each program as a separate Python thread
These all die when the main thread is interrupted
Intended to be master script for starting pubsub nodes """
class PhoenixMaster(object):

	def __init__(self, *nodes):
		self.nodes = []
		for node in nodes:
			self.addNode(node)
		self.run()

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

PhoenixMaster(sendMessageA, listenForMessageA)
