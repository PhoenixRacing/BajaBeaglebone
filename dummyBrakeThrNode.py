from PubSub import PubSub
import time
import random

p = PubSub()
def run():
	while True:
		brake_pot = float(random.randint(0,100))/100;
		throt_pot = float(random.randint(0,100))/100;
		sig = {"brake": brake_pot, "throttle": throt_pot}
		p.publish("brakeThrot", sig)
		time.sleep(1)

if __name__=="__main__":
	run()
