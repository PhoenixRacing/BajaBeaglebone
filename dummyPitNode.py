from PubSub import PubSub
import time
from random import randint

p = PubSub()
def run():
	while True:
		p.publish("pit", randint(0,1))
		time.sleep(1)

if __name__=="__main__":
	run()
