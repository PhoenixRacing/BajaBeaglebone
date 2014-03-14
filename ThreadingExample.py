
import time
import Queue
import threading
def pooping():
	while 1 == 1:
		for i in range(5):
			print i
			time.sleep(1)

def farting():
	while 1 == 1:
		print 'fart'
		time.sleep(1)

t1 = threading.Thread(target=pooping)
t2 = threading.Thread(target=farting)


t1.start()
t2.start()