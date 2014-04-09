from pydispatch import dispatcher
from Sensors.EdgeDetector import EdgeDetector
from Sensors.Pot import Pot

def publishSensorVal(sensor):
	dispatcher.send(signal=sensor.getSensorVal(), sender=sensor.getName())

frontLeftHall = EdgeDetector(["P9_11"], 1, "frontLeftHall")
def publishFrontLeftHall(): publishSensorVal(frontLeftHall)
frontLeftHall.setPublishFunc(publishFrontLeftHall)

frontRightHall = EdgeDetector(["P9_12"], 1, "frontRightHall")
def publishFrontRightHall(): publishSensorVal(frontRightHall)
frontRightHall.setPublishFunc(publishFrontRightHall)

backLeftHall = EdgeDetector(["P9_13"], 1, "backLeftHall")
def publishBackLeftHall(): publishSensorVal(backLeftHall)
backLeftHall.setPublishFunc(publishBackLeftHall)

backRightHall = EdgeDetector(["P9_21"], 1, "backRightHall")
def publishBackRightHall(): publishSensorVal(backRightHall)
backRightHall.setPublishFunc(publishBackRightHall)

brakePot = Pot(["P9_40"], "brakePot")
def publishBrakePot(): publishSensorVal(brakePot)
brakePot.setPublishFunc(publishBrakePot)

throttlePot = Pot(["P9_39"], "throttlePot")
def publishThrottlePot(): publishSensorVal(throttlePot)
throttlePot.setPublishFunc(publishThrottlePot)

if __name__=="__main__":
	from PhoenixMaster import PhoenixMaster
	PhoenixMaster([
		backRightHall.run,
		frontRightHall.run,
		backLeftHall.run,
		frontLeftHall.run,
		brakePot.run,
		throttlePot.run,
	])
