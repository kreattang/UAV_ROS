#! usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

class robot_position():
    def __init__(self, name):
        self.name = name
        self.position_x = 100
        self.position_y = 100
        self.position_subscriber = rospy.Subscriber('/'+self.name+'/ground_truth/odometry', Odometry, self.update_pose)
    def update_pose(self, data):
        self.position_x = data.pose.pose.position.x
        self.position_y = data.pose.pose.position.y
    




