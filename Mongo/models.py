from mongoengine import *
from json import loads
from pprint import pprint

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

	def __repr__(self):
		return pprint(loads(self.to_json()))
