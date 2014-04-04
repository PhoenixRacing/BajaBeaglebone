from pydispatch import dispatcher
import time
from random import randint

def run():
	while True:
		dispatcher.send(signal=randint(0,1), sender = "lock")
		time.sleep(1)

if __name__=="__main__":
	run()