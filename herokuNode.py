from pydispatch import dispatcher
import subprocess
from requests import post

def postToHeroku(payload):
        if not payload:
                return
        base_url = 'http://10.7.24.129:5000/bbdebug/'
        return post(base_url, data=payload, timeout=1)

def heroku(sender, signal):
	try:
		postToHeroku(signal)
	except:
		print 'Post to heroku failed'

def run():
	dispatcher.connect(heroku, sender="allNode")

if __name__=="__main__":
	import json
	post(json.dumps("5"))