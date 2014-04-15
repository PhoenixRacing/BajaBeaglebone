from mongoengine import connect
from models import DataSession
connect('baja_beaglebone')
print DataSession.objects()