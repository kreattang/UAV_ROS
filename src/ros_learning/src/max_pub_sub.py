#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('doubler')

def callback(msg):
    print(msg.data)


sub = rospy.Subscriber('number', Int32, callback)

rospy.spin()