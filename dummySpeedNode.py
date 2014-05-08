from PubSub import PubSub
import time
from random import randint

def run():
    p = PubSub()
    while True:
        p.publish("speed", randint(1,30))
        print 'published speed'
        time.sleep(1)

if __name__=="__main__":
    run()
