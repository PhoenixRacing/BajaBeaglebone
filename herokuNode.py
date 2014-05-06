import redis
import subprocess
from requests import post
from multiprocessing import Process, Pipe
import logging

def postToHeroku(payload):
        if not payload:
                return
#        base_url = 'http://10.7.24.26:5000/bbdebug/'
	base_url = 'http://phoenix-racing.herokuapp.com/bbdebug/'
        return post(base_url, data={"data" : payload}, timeout=1)

r = redis.Redis()
p = r.pubsub()

def run():
	p.listen("allNode", postToHeroku)

if __name__=="__main__":
	run()
