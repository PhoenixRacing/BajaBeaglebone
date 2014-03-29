from flask import Flask, render_template, session

#TODO: get this working with the init file

#Loads the dashboard for competition
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

#Loads the dashboard for test/practice driving
@app.route('/test_dash')
def competition():
	return render_template('test_dash.html', speed = 0)
