from mongoengine import *
from datetime import datetime
from pydispatch import dispatcher

class Vector(EmbeddedDocument):
	x = FloatField(required=True)
	y = FloatField(required=True)
	z = FloatField(required=True)

class DataPoint(EmbeddedDocument):
	time = DateTimeField(required = True)	#DateTime
	gps = GeoPointField()					#Location(gps=[<lon>,<lat>])
	accel = EmbeddedDocumentField(Vector)	#[<x>,<y>,<z>]
	gyro = EmbeddedDocumentField(Vector)		#[<x>,<y>,<z>]
	throttle = FloatField()					
	brake = FloatField()
	speed = FloatField()
	tach = FloatField()
	frontLeftWheel = FloatField()
	frontRightWheel = FloatField()
	backLeftWheel = FloatField()
	backRightWheel = FloatField()

class DataSession(Document):
	driver = StringField(True)
	start_time = DateTimeField(required = True)
	end_time = DateTimeField()
	data = ListField(EmbeddedDocumentField(DataPoint))

connect('baja_beaglebone')
session = DataSession()
session.start_time = datetime.now()
session.save()

def logData(sender, signal):
	# TODO this should filter the data in a reasonable manner as well as appending it to the session.data object
	if (sender == "frontLeftHall"):
		session.data[0].frontLeftWheel = signal
	elif (sender == "backLeftHall"):
		session.data[0].backLeftWheel = signal
	elif (sender == "frontRightHall"):
		session.data[0].frontRightWheel = signal
	elif (sender == "backLeftHall"):
		session.data[0].backRightWheel = signal
	elif (sender == "brakePot"):
		session.data[0].brake = signal
	elif (sender == "backLeftHall"):
		session.data[0].throttle = signal

def run():
	dispatcher.connect(logData, sender="frontLeftHall")
	dispatcher.connect(logData, sender="frontRightHall")
	dispatcher.connect(logData, sender="backLeftHall")
	dispatcher.connect(logData, sender="backRightHall")
	dispatcher.connect(logData, sender="brakePot")
	dispatcher.connect(logData, sender="throttlePot")