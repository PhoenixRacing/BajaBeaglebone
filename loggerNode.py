from pydispatch import dispatcher
import json
import os

def logAll(sender, signal):
	os.system('cls' if os.name == 'nt' else 'clear')
	for key, item in json.loads(signal).items():
		print key, item

def run():
	dispatcher.connect(logAll, sender="allNode")
