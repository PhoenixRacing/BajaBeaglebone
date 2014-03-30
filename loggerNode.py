from pydispatch import dispatcher
import sys

def logAll(sender, signal):
	print signal

def run():
	dispatcher.connect(logAll, sender="allNode")