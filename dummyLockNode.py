from PubSub import PubSub
import time
from random import randint

p = PubSub()
def run():
	while True:
		sig = {"spin": randint(0,1), "lock": randint(0,1)}
		p.publish("spinLock", sig)
		time.sleep(5)

if __name__=="__main__":
	run()
