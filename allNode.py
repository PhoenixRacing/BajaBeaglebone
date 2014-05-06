from PubSub import PubSub
import sys
import time
import threading
import json

nodeName = "allNode"

vals = {}
def handler(sender, signal):
	if sender==nodeName:
		return
	vals[sender] = vals.get(sender, []) + [signal]
	print vals

def pushAllNode():
	pub.publish(stringify(vals))
	clear(vals)

def stringify(dic):
	vals['timestamp'] = time.time()
	return vals

def clear(dic):
	for key in dic.keys():
		dic[key] = []

sub = PubSub("*")
pub = PubSub(nodeName)

def sub_helper():
	sub.subscribe(handler)

def run():
 	threading.Thread(target=sub_helper).start()
	while True:
		time.sleep(1)
		print 'published all node'
		pushAllNode()


if __name__=="__main__":
	run()
