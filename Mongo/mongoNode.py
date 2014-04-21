from mongoengine import *
from models import *
from datetime import datetime
from pydispatch import dispatcher
import json


connect('baja_beaglebone')
session = DataSession()
session.start_time = datetime.now()
session.save()

def logData(sender, signal):
	try:
		data = DataPoint()
		signal = json.loads(signal)
		data.time = datetime.now()
		data.frontLeftWheel = signal.get("frontLeftHall", None)
		data.frontRightWheel = signal.get("frontRightHall", None)
		data.backLeftHall = signal.get("backLeftWheel", None)
		data.backRightWheel = signal.get("backRightHall", None)
		data.brake = signal.get("brakePot", None)
		data.throttle = signal.get("throttlePot", None)
		session.data.append(data)
		session.save()
	except:
		print 'Mongo failed'
	
def run():
	dispatcher.connect(logData, sender="allNode")