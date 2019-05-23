#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from turtlesim.msg import Pose
from math import atan2, fabs, pi
from geometry_msgs.msg import Twist


velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)

def steering_angle(location, goal_pose):
        return atan2(goal_pose[1] - location[1], goal_pose[0] - location[0])

def angle_normal(angle):
    if angle < 0:
        return 360 + angle
    else:
        return angle

def callback(data):
    print(data.x, data.y, data.theta)
    steer_angle = angle_normal(steering_angle([data.x, data.y], [1,1])/pi*180.0)
    print("Should Steer Angle: ", steer_angle)
    current_angle = angle_normal(data.theta/pi*180.0)
    print("Current Heading Angle: ", current_angle)
    abs_angle = s
    



def listener():
    '''learning_topic Subscriber'''
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('position', anonymous=True)

    rospy.Subscriber("/turtle1/pose", Pose, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
