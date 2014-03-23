from pydispatch import dispatcher
import time
from random import randint

def sendMessageA():
    while True:
        dispatcher.send(signal=randint(1,100), sender="PubA")
        time.sleep(1)
