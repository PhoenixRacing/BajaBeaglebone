from PubSub import PubSub
from Sensors.EdgeDetector import EdgeDetector
from Sensors.Pot import Pot
from Sensors.Accelerometer import Accelerometer
from Sensors.Gyro import Gyro
from Sensors.Barometer import Barometer
from Sensors.Compass import Compass
import logging
import sys

logging.basicConfig()
logger = logging.getLogger("PhoenixMaster.gpio")

sensors = []
try:
 	sensors.append(EdgeDetector(["P8_11"], 1, "tach"))
except:
 	logger.error("Unable to add sensor tach: %s"%sys.exc_info()[0])
#try:
#	sensors.append(EdgeDetector(["P8_9"], 2, "outputShaft", numPoints=5))
#except:
#	logger.error("Unable to add sensor output shaft: %s"%sys.exc_info()[0])
try:
	sensors.append(Pot(["P9_40"],"brake"))
except:
	logger.error("Unable to add sensor brake pot: %s"%sys.exc_info()[0])
try:
	sensors.append(Pot(["P9_39"],"throttle"))
except:
	logger.error("Unable to add sensor throttle pot: %s"%sys.exc_info()[0])
# try:
# 	sensors.append(Accelerometer("Accelerometer"))
# except:
# 	logger.error("Unable to add sensor accelerometer: %s"%sys.exc_info()[0])
# try:
# 	sensors.append(Gyro("Gyro"))
# except:
# 	logger.error("Unable to add sensor gyro: %s"%sys.exc_info()[0])
# try:
# 	sensors.append(Barometer("Barometer"))
# except:
# 	logger.error("Unable to add sensor baro: %s"%sys.exc_info()[0])
# try:
# 	sensors.append(Compass("Compass"))
# except:
# 	logger.error("Unable to add sensor compass: %s"%sys.exc_info()[0])


p = PubSub()
def dispatch(sensor):
	p.publish(sensor.getName(), sensor.getSensorVal())

for sensor in sensors:
    sensor.setPublishFunc(lambda sensor=sensor: dispatch(sensor))

if __name__=="__main__":
    from PhoenixMaster import PhoenixMaster
    PhoenixMaster([sensor.run for sensor in sensors])
