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
		self.ptime = datetime.datetime.now()
		self.ctime = datetime.datetime.now()
		self.brake = 0
		self.throttle = 0
		self.spin = 0
		self.lock = 0

	def update_speed(self, speed):
		self.speed = speed

	def update_time(self, ptime, ctime):
		self.ptime = ptime
		self.ctime = ctime

	def update_brake_throttle(self, brake, throttle):
		self.brake = brake
		self.throttle = throttle

	def update_spin_lock(self, spin, lock):
		self.spin = spin
		self.lock = lock


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

@socketio.on('update time', namespace='/test')
def get_time(message):
	format = '%M:%S';
	prev_t = datetime.datetime.now();
	curr_t = datetime.datetime.now();
	emit('updateTime', {'prev':str(app.ptime.strftime(format)), 'curr': str(app.ctime.strftime(format))})


@socketio.on('update brake_throttle', namespace='/test')
def brake_and_throttle(message):
	emit('updateBrakeThrottle', {'brake': app.brake, 'throttle': app.throttle})

@socketio.on('update spin_lock', namespace='/test')
def spin_or_lock(message):
	emit('updateSL', {'spin': app.spin, 'lock': app.lock})


def run():
        socketio.run(app)

def run_update_speed():
	while(True):
		app.update_speed(random.randint(1,25))
		time.sleep(.001)

def run_update_time():
	while(True):
		p_time = datetime.datetime.now();
		c_time = datetime.datetime.now();
		app.update_time(p_time, c_time)
		time.sleep(.001)

def run_brake_throttle():
	while(True):
		b = float(random.randint(0,100))/(100);
		t = float(random.randint(0,100))/(100);
		app.update_brake_throttle(b, t)
		time.sleep(.001)

def run_spin_lock():
	while (True):
		s = 1;
		l = 1;
		app.update_spin_lock(s, l)
		time.sleep(.001)


if __name__ == '__main__':
        import sys
        sys.path.append('../')
        from PhoenixMaster import *
        PhoenixMaster(run, run_update_speed, run_update_time, run_brake_throttle, run_spin_lock)
