from pydispatch import dispatcher
from Sensors import EdgeDetector, Pot

def publishSensorVal(hall):
	print hall
	dispatcher.send(signal=hall.getSensorVal(), sender=hall.getName())

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

if __name__=="__main__":
	from PhoenixMaster import PhoenixMaster
	PhoenixMaster([
		backRightHall.run,
		frontRightHall.run,
		backLeftHall.run,
		frontLeftHall.run
		]
		)
