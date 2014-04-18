from pydispatch import dispatcher
import subprocess
from requests import post
from multiprocessing import Process, Pipe

def postToHeroku(payload):
        if not payload:
                return
        base_url = 'http://10.7.24.129:5000/bbdebug/'
        return post(base_url, data=payload, timeout=.5)

# THIS LOOP RUNS IN A NEW PROCESS
# SO IT DOESNT HOG THE GIL, YO
def herokuLoop(q):
	while True:
		data = child_conn.recv()
		if data:
			try:
				postToHeroku(data)
			except:
				print 'Post to heroku failed'

def heroku(sender, signal):
	parent_conn.send(signal)

parent_conn, child_conn = Pipe()
p = Process(target=herokuLoop, args=(child_conn,))

def run():
	p.start()
	dispatcher.connect(heroku, sender="allNode")

if __name__=="__main__":
	run()
	parent_conn.send("herro")
