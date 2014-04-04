from pydispatch import dispatcher
import sys
import time
import json

nodeName = "allNode"

vals = {}
def pubAll(sender, signal):
	if sender==nodeName:
		return
	print sender, signal	
	vals[sender] = signal

def stringify(dic):
	vals['timestamp'] = time.time()
	return json.dumps(vals)

def run():
	dispatcher.connect(pubAll, sender=dispatcher.Any)
	while True:
		dispatcher.send(signal=stringify(vals), sender=nodeName)
		time.sleep(.1)
