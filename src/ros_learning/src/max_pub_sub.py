#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('doubler')

def callback(msg):
    doubled = Int32()
    doubled.data = msg.data * 2
    print(doubled.data)
    pub.publish(doubled)



pub = rospy.Publisher('doubled', Int32, queue_size=10)
sub = rospy.Subscriber('number', Int32, callback)

rospy.spin()