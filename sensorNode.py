from pydispatch import dispatcher
from Sensors import EdgeDetector, Pot

frontLeftHall = EdgeDetector(["P8_10"], 1)
def publishFrontLeftHall():
	print frontLeftHall
	dispatcher.send(signal=frontLeftHall.getSensorVal(), sender="frontLeftHall")
frontLeftHall.setPublishFunc(publishFrontLeftHall)

frontRightHall = EdgeDetector(["P8_11"], 1)
def publishFrontRightHall():
	print frontRightHall
	dispatcher.send(signal=frontRightHall.getSensorVal(), sender="frontRightHall")
frontRightHall.setPublishFunc(publishFrontRightHall)

backLeftHall = EdgeDetector(["P8_12"], 1)
def publishBackLeftHall():
	print backLeftHall
	dispatcher.send(signal=backLeftHall.getSensorVal(), sender="backLeftHall")
backLeftHall.setPublishFunc(publishBackLeftHall)

backRightHall = EdgeDetector(["P8_13"], 1)
def publishBackRightHall():
	print backRightHall
	dispatcher.send(signal=backRightHall.getSensorVal(), sender="backRightHall")
backRightHall.setPublishFunc(publishBackRightHall)

if __name__=="__main__":
	from PhoenixMaster import PhoenixMaster
	PhoenixMaster(
		backRightHall.run,
		frontRightHall.run,
		backLeftHall.run,
		frontLeftHall.run
		)
