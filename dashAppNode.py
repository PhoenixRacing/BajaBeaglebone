from pydispatch import dispatcher

def handleSpeed(sender, signal):
	print signal

dispatcher.connect(handleSpeed, sender="speed")
