from pydispatch import dispatcher
from Sensors.EdgeDetector import EdgeDetector
from Sensors.Pot import Pot
from Sensors.Accelerometer import Accelerometer
from Sensors.Gyro import Gyro
from Sensors.Barometer import Barometer
from Sensors.Compass import Compass


sensors = []
try:
	sensors.append(EdgeDetector(["P8_10"], 1, "frontLeftHall"))
except:
	pass
try:          
	sensor.append(EdgeDetector(["P9_12"], 1, "frontRightHall"))
except:
	pass
try:
	sensors.append(EdgeDetector(["P8_8"], 1, "backLeftHall"))
except:
	pass
try:
	sensors.append(EdgeDetector(["P9_15"], 1, "backRightHall"))
except:
	pass
try:
	sensors.append(EdgeDetector(["P8_11"], 1, "tach"))
except:
	pass
try:
	sensors.append(EdgeDetector(["P8_9"], 1, "outputShaft"))
except:
	pass
try:
	sensors.append(Pot(["P9_40"],"brakePot"))
except:
	pass
try:
	sensors.append(Pot(["P9_39"],"throttlePot"))
except:
	pass
try:
	sensors.append(Accelerometer("Accelerometer"))
except:
	pass
try:
	sensors.append(Gyro("Gyro"))
except:
	pass
try:
	sensors.append(Barometer("Barometer"))
except:
	pass
try:
	sensors.append(Compass("Compass"))
except:
	pass

def dispatch(sensor):
	dispatcher.send(signal=sensor.getSensorVal(), sender=sensor.getName())

for sensor in sensors:
    sensor.setPublishFunc(lambda sensor=sensor: dispatch(sensor))

if __name__=="__main__":
    from PhoenixMaster import PhoenixMaster
    PhoenixMaster([sensor.run for sensor in sensors])
