#! /usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    print data.data


if __name__ == '__main__':
    rospy.init_node('learning_subscriber')
    sub = rospy.Subscriber('phrases',String,callback)
    rospy.spin()