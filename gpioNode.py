from PubSub import PubSub
from Sensors.EdgeDetector import EdgeDetector
from Sensors.Pot import Pot
from Sensors.Accelerometer import Accelerometer
from Sensors.Gyro import Gyro
from Sensors.Barometer import Barometer
from Sensors.Compass import Compass
import logging
import sys

logger = logging.getLogger("PhoenixMaster.gpio")

sensors = []
try:
	sensors.append(EdgeDetector(["P8_10"], 1, "frontLeftHall"))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:          
	sensor.append(EdgeDetector(["P9_12"], 1, "frontRightHall"))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(EdgeDetector(["P8_8"], 1, "backLeftHall"))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(EdgeDetector(["P9_15"], 1, "backRightHall"))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(EdgeDetector(["P8_11"], 1, "tach"))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(EdgeDetector(["P8_9"], 1, "outputShaft"))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(Pot(["P9_40"],"brakePot"))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(Pot(["P9_39"],"throttlePot"))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(Accelerometer("Accelerometer"))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(Gyro("Gyro"))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(Barometer("Barometer"))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(Compass("Compass"))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])


p = PubSub()
def dispatch(sensor):
	p.publish(sensor.getName(), sensor.getSensorVal())

for sensor in sensors:
    sensor.setPublishFunc(lambda sensor=sensor: dispatch(sensor))

if __name__=="__main__":
    from PhoenixMaster import PhoenixMaster
    PhoenixMaster([sensor.run for sensor in sensors])
