from pydispatch import dispatcher
from Sensors.EdgeDetector import EdgeDetector
from Sensors.Pot import Pot
from Sensors.Accelerometer import Accelerometer
from Sensors.Gyro import Gyro
from Sensors.Barometer import Barometer
from Sensors.Compass import Compass

logger = logging.getLogger("PhoenixMaster.gpio")

sensors = []

edgeDetectors = [
	(["P8_10"], 1, "frontLeftHall"),
	(["P9_12"], 1, "frontRightHall"),
	(["P8_8"], 1, "backLeftHall"),
	(["P9_15"], 1, "backRightHall"),
	(["P8_11"], 1, "tach"),
	(["P8_9"], 1, "outputShaft")]

for ed in edgeDetectors:
	try:
		sensors.append(EdgeDetector(ed[0], ed[1], ed[2]))
	except:
 		logger.error("Sensor %s failed", str(ed))

pots = [(["P9_40"], "brakePot"), (["P9_39"], "throttlePot")]

for pot in pots:
	try:
		sensors.append(Pot(pot[0], pot[1]))
	except:
		logger.error("Sensor %s failed", str(pot))
try:
	sensors.append(Accelerometer("Accelerometer"))
except:
	logger.error("Accelerometer failed")

try:
	sensors.append(Gyro("Gyro"))
except:
	logger.error("Gyro failed")

try:
	sensors.append(Barometer("Barometer"))
except:
	logger.error("Barometer failed")

try:
	sensors.append(Compass("Compass"))
except:
	logger.error("Compass failed")

def dispatch(sensor):
	dispatcher.send(signal=sensor.getSensorVal(), sender=sensor.getName())

for sensor in sensors:
    sensor.setPublishFunc(lambda sensor=sensor: dispatch(sensor))

if __name__=="__main__":
    from PhoenixMaster import PhoenixMaster
    PhoenixMaster([sensor.run for sensor in sensors])
