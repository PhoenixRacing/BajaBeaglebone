from DashApp import app, run
from pydispatch import dispatcher

def handleSpeed(sender, signal):
    print signal
    app.update_speed(signal)

dispatcher.connect(handleSpeed, sender="speed")

if __name__=="__main__":
    run()
