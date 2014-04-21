from pydispatch import dispatcher
import sys
import time
import json

nodeName = "allNode"

vals = {}
def pubAll(sender, signal):
	if sender==nodeName:
		return
	vals[sender] = vals.get(sender, []) + [signal]

def stringify(dic):
	vals['timestamp'] = time.time()
	return json.dumps(vals)

def clear(dic):
	for key in dic.keys():
		dic[key] = []

def run():
	dispatcher.connect(pubAll, sender=dispatcher.Any)
	while True:
		dispatcher.send(signal=stringify(vals), sender=nodeName)
		clear(vals)
		time.sleep(.1)

