from PubSub import PubSub

def printAll(sender, signal):
	for key, item in signal.items():
		print key, item
	print

p = PubSub()
def run():
	p.subscribe("allNode", printAll)
