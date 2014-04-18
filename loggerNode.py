from pydispatch import dispatcher
import datetime

root = "local"
base = "dump"
current = None

def makeNewFile():
	global current
	current = root + "/" + base  + datetime.datetime.now().strftime("_%m_%d__%H_%M_%S").strip(" ")
	touch(current) 

def touch(fname, times=None):
	f = open(fname, 'w')
	f.close()

def logAll(sender, signal):
	if current:
		with open(current, 'a') as f:
			f.write("\n")
			f.write(signal)

def run():
	makeNewFile()
	dispatcher.connect(logAll, sender="allNode")

if __name__=="__main__":
	makeNewFile()
	logAll("", "fart")