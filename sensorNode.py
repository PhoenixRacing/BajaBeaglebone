from pydispatch import dispatcher
from Sensors import EdgeDetector, Pot

frontLeftHall = EdgeDetector(["P8_10"], 1)
def publishFrontLeftHall():
	print frontLeftHall
	dispatcher.send(signal=frontLeftHall.getSensorVal(), sender="frontLeftHall")
frontLeftHall.setPublishFunc(publishFrontLeftHall)

if __name__=="__main__":
	frontLeftHall.run()