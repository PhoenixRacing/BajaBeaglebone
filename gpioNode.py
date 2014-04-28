from pydispatch import dispatcher
from Sensors.EdgeDetector import EdgeDetector
from Sensors.Pot import Pot
from Sensors.Accelerometer import Accelerometer
from Sensors.Gyro import Gyro
from Sensors.Barometer import Barometer
from Sensors.Compass import Compass

logger = logging.getLogger("PhoenixMaster.gpio")

sensors = []
try:
	sensors.append(EdgeDetector(["P8_10"], 1, "frontLeftHall: %s"%sys.exc_info()[0]))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:          
	sensor.append(EdgeDetector(["P9_12"], 1, "frontRightHall: %s"%sys.exc_info()[0]))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(EdgeDetector(["P8_8"], 1, "backLeftHall: %s"%sys.exc_info()[0]))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(EdgeDetector(["P9_15"], 1, "backRightHall: %s"%sys.exc_info()[0]))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(EdgeDetector(["P8_11"], 1, "tach: %s"%sys.exc_info()[0]))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(EdgeDetector(["P8_9"], 1, "outputShaft: %s"%sys.exc_info()[0]))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(Pot(["P9_40"],"brakePot: %s"%sys.exc_info()[0]))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(Pot(["P9_39"],"throttlePot: %s"%sys.exc_info()[0]))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(Accelerometer("Accelerometer: %s"%sys.exc_info()[0]))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(Gyro("Gyro: %s"%sys.exc_info()[0]))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(Barometer("Barometer: %s"%sys.exc_info()[0]))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])
try:
	sensors.append(Compass("Compass: %s"%sys.exc_info()[0]))
except:
	logger.error("Unable to add sensor: %s"%sys.exc_info()[0])

def dispatch(sensor):
	dispatcher.send(signal=sensor.getSensorVal(), sender=sensor.getName())

for sensor in sensors:
    sensor.setPublishFunc(lambda sensor=sensor: dispatch(sensor))

if __name__=="__main__":
    from PhoenixMaster import PhoenixMaster
    PhoenixMaster([sensor.run for sensor in sensors])
