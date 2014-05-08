from PubSub import PubSub

halls = ["frontLeftHall","frontRightHall", "backLeftHall", "backRightHall"]

p = PubSub()
def lock(sender, allData):
	for hall in halls:
		if allData.get(hall, -1) == 0:
			p.publish("lock", True)
			return
	p.publish("lock", False)

def run():
	p.subscribe("allNode", lock)

#if __name__=="__main__":
#	run()
