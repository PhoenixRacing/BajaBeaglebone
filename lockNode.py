from pydispatch import dispatcher

def lock(sender, signal):
	lock = signal == 0
	dispatcher.send(sender=sender+"Locked", signal=lock)

def run():
	halls = ["frontLeftHall","frontRightHall", "backLeftHall", "backRightHall"]
	for hall in halls:
		dispatcher.connect(lock, sender=hall)

if __name__=="__main__":
	run()
