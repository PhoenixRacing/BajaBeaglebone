#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flask import Flask

# initialize the Flask app and define routes
app = Flask(__name__)
testString = 'hello fuckers'

@app.route('/')
def index():
	return testString

# define the callback
def callback(data):
	print 'hi'
	testString = data.data


if __name__ == '__main__':
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber('chatter', String, callback)
	app.run()
