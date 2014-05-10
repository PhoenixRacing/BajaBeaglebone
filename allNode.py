from PubSub import PubSub
import sys
import time
import threading

nodeName = "allNode"

vals = {}
def handler(sender, signal):
	if sender==nodeName:
		return
	vals[sender] = vals.get(sender, []) + [signal]

def pushAllNode():
	publisher.publish(nodeName, vals)
	clear(vals)

def stringify(dic):
	vals['timestamp'] = time.time()
	return vals

def clear(dic):
	for key in dic.keys():
		dic[key] = []

p = PubSub()
publisher = PubSub()
def sub_helper():
	p.subscribe("*", handler)

def run():
 	threading.Thread(target=sub_helper).start()
	while True:
		time.sleep(1)
		pushAllNode()

#if __name__=="__main__":
#	pass
	#	run()
