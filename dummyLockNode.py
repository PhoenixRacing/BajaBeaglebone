from pydispatch import dispatcher
import time
from random import randint
import json

def run():
	while True:
		sig = json.dumps({"spin": randint(0,1), "lock": randint(0,1)})
		dispatcher.send(signal= sig, sender = "spinlock")
		time.sleep(5)

if __name__=="__main__":
	run()