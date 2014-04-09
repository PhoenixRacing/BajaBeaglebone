from pydispatch import dispatcher
import time
from random import randint

def run():
    while True:
        dispatcher.send(signal=randint(1,100), sender="speed")
        time.sleep(1)

if __name__=="__main__":
    run()
