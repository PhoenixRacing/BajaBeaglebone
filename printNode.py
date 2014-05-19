from PubSub import PubSub
import os

def printAll(sender, signal):
#	os.system("clear")
	for key, item in signal.items():
		print key, item
	print

p = PubSub()
def run():
	p.subscribe("allNode", printAll)
