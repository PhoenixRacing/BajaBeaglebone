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
	driver = StringField()
	start_time = DateTimeField(required = True)
	end_time = DateTimeField()
	data = ListField(EmbeddedDocumentField(DataPoint))

connect('baja_beaglebone')
session = DataSession()
session.start_time = datetime.now()
session.save()

def logData(sender, signal):
	data = DataPoint()
	data.frontLeftWheel = signal.get("frontLeftHall", None)
	data.frontRightWheel = signal.get("frontRightHall", None)
	data.backLeftHall = signal.get("backLeftWheel", None)
	data.backRightWheel = signal.get("backRightHall", None)
	data.brake = signal.get("brakePot", None)
	data.throttle = signal.get("throttlePot", None)
	session.append(data)
	session.save()

def run():
	dispatcher.connect(logData, sender="allNode")