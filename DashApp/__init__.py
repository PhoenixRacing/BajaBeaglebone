import random
import time
import datetime

from flask import Flask, render_template, session
from flask.ext.socketio import SocketIO, emit
from flask import Flask
from flask import render_template

class DashApp(Flask):
	def __init__(self):
		super(self.__class__, self).__init__(__name__)
		self.speed = 0

	def update_speed(self, speed):
		self.speed = speed


app = DashApp()
app.debug=True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


#Loads the dashboard for competition
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

#Loads the dashboard for test/practice driving
@app.route('/test_dash')
def competition():
	return render_template('test_dash.html', speed = 0)

@socketio.on('update', namespace='/test')
def test_message(message):
	emit('updateSpeed', {'speed': app.speed })

format = '%M:%S';

@socketio.on('update ptime', namespace='/test')
def test_ptime(message):
	prev_t = datetime.datetime.now();
	emit('updatePtime', {'prev': str(prev_t.strftime(format))})

@socketio.on('current time', namespace='/test')
def test_ctime(message):
	curr_t = datetime.datetime.now();
	emit('updateCtime', {'curr': str(curr_t.strftime(format))})

@socketio.on('update brake', namespace='/test')
#Assuming potentiometer value between 0 and 1
def test_brake(message):
	pot_value = float(random.randint(0,100))/(100);
	emit('updateBrake', {'brake': pot_value})

@socketio.on('update throttle', namespace='/test')
#Assuming potentiometer value between 0 and 1
def test_throttle(message):
	pot_value = float(random.randint(0,100))/(100);
	emit('updateThrottle', {'throttle': pot_value})

@socketio.on('update spin', namespace='/test')
def test_spin(message):
	s = 1;
	emit('updateSpin', {'spin': s})

@socketio.on('update lock', namespace='/test')
def test_lock(message):
	l = 1;
	emit('updateLock', {'lock': l})

def run():
        socketio.run(app)

def run_update_speed():
	while(True):
		app.update_speed(random.randint(1,25))
		time.sleep(1)

if __name__ == '__main__':
        import sys
        sys.path.append('../')
        from PhoenixMaster import *
        PhoenixMaster(run, run_update_speed)
