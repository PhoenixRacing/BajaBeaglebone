from pydispatch import dispatcher
import pprint
import json
import os

def logAll(sender, signal):
	os.system('cls' if os.name == 'nt' else 'clear')
	pprint.pprint(json.loads(signal))

def run():
	dispatcher.connect(logAll, sender="allNode")
