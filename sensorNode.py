from pydispatch import dispatcher
from Sensors import EdgeDetector, Pot

frontLeftHall = EdgeDetector(["P8_10"], 1)
def publishFrontLeftHall():
	print frontLeftHall
	dispatcher.send(signal=frontLeftHall.getSensorVal(), sender="frontLeftHall")
frontLeftHall.setPublishFunc(publishFrontLeftHall)

frontRightHall = EdgeDetector(["P8_10"], 1)
def publishFrontLeftHall():
	print frontRightHall
	dispatcher.send(signal=frontRightHall.getSensorVal(), sender="frontRightHall")
frontRightHall.setPublishFunc(publishFrontLeftHall)

backLeftHall = EdgeDetector(["P8_10"], 1)
def publishFrontLeftHall():
	print backLeftHall
	dispatcher.send(signal=backLeftHall.getSensorVal(), sender="backLeftHall")
backLeftHall.setPublishFunc(publishFrontLeftHall)

backRightHall = EdgeDetector(["P8_10"], 1)
def publishFrontLeftHall():
	print backRightHall
	dispatcher.send(signal=backRightHall.getSensorVal(), sender="backRightHall")
backRightHall.setPublishFunc(publishFrontLeftHall)



if __name__=="__main__":
	from PhoenixMaster import PhoenixMaster
	PhoenixMaster(
		backRightHall.run,
		frontRightHall.run,
		backLeftHall.run,
		backRightHall.run
		)
