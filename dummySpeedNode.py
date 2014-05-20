from PubSub import PubSub
import time
from random import randint

def run():
    p = PubSub()
    while True:
        p.publish("speed", float(randint(1,30000))/float(1110))
        time.sleep(1)

#if __name__=="__main__":
#    run()
