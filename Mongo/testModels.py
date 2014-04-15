from mongoengine import connect
from models import DataSession
from pprint import pprint
from json import loads

connect('baja_beaglebone')
session = DataSession.objects().first()
print session