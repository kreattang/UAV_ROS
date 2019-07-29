#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from turtlesim.msg import Pose
from math import atan2, fabs, pi, sqrt
from geometry_msgs.msg import Twist


velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)

def steering_angle(location, goal_pose):
        return atan2(goal_pose[1] - location[1], goal_pose[0] - location[0])

def angle_normal(angle):
    if angle < 0:
        return 360 + angle
    else:
        return angle
def euclidean_distance(location, goal_pose):
        return sqrt(pow((goal_pose[0]- location[0]), 2) +
                    pow((goal_pose[1] - location[1]), 2))
def callback(data):
    print(data.x, data.y, data.theta)
    steer_angle = steering_angle([data.x, data.y], [10,10])
    print("Should Steer Angle: ", steer_angle)
    current_angle = data.theta
    print("Current Heading Angle: ", current_angle)
    abs_angle = steer_angle - current_angle
    print("Relative Angle:", abs_angle)
    vel_msg = Twist()
    vel_msg.linear.x = 0.6
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    if fabs(abs_angle) > 0.01:
        vel_msg.angular.z = 10*abs_angle
    if euclidean_distance([data.x, data.y], [10, 10]) < 1:
        vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)
    print('Have Published :', vel_msg.angular.z)


    

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
