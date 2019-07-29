#! /usr/bin/env python

import rospy
from turtlesim.msg import Pose


def callback(Pose):
    print("location",Pose.x, Pose.y)

if __name__ == '__main__':
   rospy.init_node('turtle_control', anonymous=True)
   sub = rospy.Subscriber('/turtle1/pose', Pose, callback)
   rospy.spin()