import random
import time
import datetime
import unicodedata

from flask import Flask, render_template, session, request
from flask.ext.socketio import SocketIO, emit

class Dashboard(Flask):
	def __init__(self):
		super(self.__class__, self).__init__(__name__)
		self.speed = 0
		self.ptime = 0
		self.ctime = 0
		self.brake = 0
		self.throttle = 0
		self.spin = 0
		self.lock = 0
		self.pit = 0

	def update_speed(self, speed):
		self.speed = speed

	def update_time(self, ptime, ctime):
		self.ptime = ptime
		self.ctime = ctime

	def update_brake(self, brake):
		self.brake = brake

	def update_throttle(self, throttle):
		self.throttle = throttle

	def update_spin_lock(self, lock, spin):
		self.lock = lock
		self.spin = spin

	def update_pit(self, pit):
		self.pit = pit



app = Dashboard() 
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



###Sockets stuff...

@socketio.on('update', namespace='/test')
def test_message(message):
	str(app.speed)
	if app.speed[1] == '.':
		app.speed = app.speed[:3]
	if app.speed[2] == '.':
		app.speed = app.speed[:4]
	emit('updateSpeed', {'speed': app.speed })

@socketio.on('update time', namespace='/test')
def get_time(message):
	format = '%M:%S';
	prev_t = '00:00';
	curr_t = '00:00';
	emit('updateTime', {'prev':app.ptime, 'curr': app.ctime})

#@socketio.on('update brake_throttle', namespace='/test')
#def brake_and_throttle(message):
#	emit('updateBrakeThrottle', {'brake': app.brake, 'throttle': app.throttle})
@socketio.on('update brake', namespace='/test')
def brake(message):
	emit('updateBrake', {'brake': app.brake})

@socketio.on('update throttle', namespace='/test')
def throttle(message):
	emit('updateThrottle', {'throttle': app.throttle})

@socketio.on('update spin_lock', namespace='/test')
def spin_or_lock(message):
	emit('updateSL', {'spin': app.spin, 'lock': app.lock})

@socketio.on('update pit', namespace='/test')
def pit(message):
	emit('updatePit', {'pit': app.pit})



###Post requests stuff...

#debug using: curl --data "speed=5" localhost:5000/updatespeed
@app.route('/updatespeed', methods = ['POST'])
def post_speed():
	speed = request.form['speed']
	app.update_speed(speed)
	return 'success\n'

@app.route('/updatetime', methods = ['POST'])
#TODO: make this work with datetime objects
def post_ptime():
	prev_time = request.form['prev_time']
	curr_time = request.form['curr_time']
	app.update_time(prev_time, curr_time)
	return 'success\n'

@app.route('/updatebrake', methods = ['POST'])
def post_brake():
#	brake = request.form['brake']
#	app.update_brake(brake)
#	return 'success\n'
	pass

@app.route('/updatethrottle', methods = ['POST'])
def post_throttle():
#	throttle = request.form['throttle']
#	app.update_throttle(throttle)
#	return 'success\n'
	pass

@app.route('/updatespinlock', methods = ['POST'])
def post_spin_lock():
	lock = request.form['lock']
	spin = request.form['spin']
	app.update_spin_lock(lock, spin)
	return 'success\n'

@app.route('/updatepit', methods = ['POST'])
def post_pit():
	pit = request.form['pit']
	print 'flask app says pit val is ', pit
	app.update_pit(pit)
	return 'success\n'


def run():
        socketio.run(app, host='0.0.0.0')

if __name__=="__main__":
	run()
