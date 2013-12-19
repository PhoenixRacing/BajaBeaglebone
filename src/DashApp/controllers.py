from DashApp import dashApp
from flask import render_template

@dashApp.route('/')
@dashApp.route('/index')
def index():
	return "Hello, World!"

@dashApp.route('/time')
def time():
	return render_template('time.html', time=dashApp.time)

