#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from DashApp import *

if __name__ == '__main__':
	dashApp = DashApp()
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber('chatter', String, dashApp.callback)
	dashApp.run()
