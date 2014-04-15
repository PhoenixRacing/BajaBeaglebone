from pydispatch import dispatcher
from Sensors.EdgeDetector import EdgeDetector
from Sensors.Pot import Pot
from Sensors.Accelerometer import Accelerometer
from Sensors.Gyro import Gyro
from Sensors.Barometer import Barometer
from Sensors.Compass import Compass

sensors = [EdgeDetector(["P9_11"], 1, "frontLeftHall"),
           EdgeDetector(["P9_12"], 1, "frontRightHall"),
           EdgeDetector(["P9_13"], 1, "backLeftHall"),
           EdgeDetector(["P9_15"], 1, "backRightHall"),
           Pot(["P9_40"],"brakePot"),
           Pot(["P9_39"],"throttlePot"),
           Accelerometer("Accelerometer"),
           Gyro("Gyro"),
           Barometer("Barometer"),
           Compass("Compass")]

def dispatch(sensor):
	dispatcher.send(signal=sensor.getSensorVal(), sender=sensor.getName())

for sensor in sensors:
    sensor.setPublishFunc(lambda sensor=sensor: dispatch(sensor))

if __name__=="__main__":
    from PhoenixMaster import PhoenixMaster
    PhoenixMaster([sensor.run for sensor in sensors])
