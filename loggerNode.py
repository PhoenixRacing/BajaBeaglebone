from pydispatch import dispatcher
import pprint
import json

def logAll(sender, signal):
	pprint.pprint(json.loads(signal))

def run():
	dispatcher.connect(logAll, sender="allNode")