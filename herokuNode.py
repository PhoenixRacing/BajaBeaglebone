from PubSub import PubSub
from requests import post
import json
import logging

def postToHeroku(sender, payload):
        if not payload:
                return
#        base_url = 'http://10.7.24.26:5000/bbdebug/'
	base_url = 'http://phoenix-racing.herokuapp.com/bbdebug/'
        return post(base_url, data={"data" : json.dumps(payload)}, timeout=1)

p = PubSub()
def run():
	p.subscribe("allNode", postToHeroku)

#if __name__=="__main__":
#	run()
