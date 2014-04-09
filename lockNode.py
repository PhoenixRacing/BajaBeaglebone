from pydispatch import dispatcher
import json

halls = ["frontLeftHall","frontRightHall", "backLeftHall", "backRightHall"]

def lock(sender, signal):
	allData = json.loads(signal)
	for hall in halls:
		if allData.get(hall, -1) == 0:
			dispatcher.send(sender="lock", signal=True)
			return
	dispatcher.send(sender="lock", signal=False)

def run():
	dispatcher.connect(lock, sender="allNode")

if __name__=="__main__":
	run()
