from pydispatch import dispatcher
import json
import os

def printAll(sender, signal):
	os.system('cls' if os.name == 'nt' else 'clear')
	for key, item in json.loads(signal).items():
		print key, item

def run():
	dispatcher.connect(printAll, sender="allNode")
