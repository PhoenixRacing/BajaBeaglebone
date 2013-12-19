#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from DashApp import dashApp

if __name__ == '__main__':
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber('chatter', String, dashApp.timeCallback)
	dashApp.run(debug=True)
