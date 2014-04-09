from pydispatch import dispatcher
import time
import random
import json

def run():
	while True:
		brake_pot = float(random.randint(0,100))/100;
		throt_pot = float(random.randint(0,100))/100;
		sig = json.dumps({"brake": brake_pot, "throttle": throt_pot})
		dispatcher.send(signal= sig, sender = "brakethrot")
		time.sleep(1)

if __name__=="__main__":
	run()