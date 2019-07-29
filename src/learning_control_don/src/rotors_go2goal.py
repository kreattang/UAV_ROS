#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from trajectory_msgs.msg import MultiDOFJointTrajectory,MultiDOFJointTrajectoryPoint
from geometry_msgs.msg import Vector3,Twist,Transform,Quaternion,Point
import time, tf, math
import std_msgs.msg
from math import atan2, cos, sin, sqrt

class Robot():
    def __init__(self, location, target):
        self.location_x = 100
        self.location_y = 100
        self.location_z = 100
        self.initial_x = location[0]
        self.initial_y = location[1]
        self.initial_z = location[2]
        self.target_x = target[0]
        self.target_y = target[1]
        self.target_z = target[2]
        self.pose_subscriber =  rospy.Subscriber("/firefly/ground_truth/odometry", Odometry, self.update_pose)
    def update_pose(self, data):
        self.location_x = data.pose.pose.position.x
        self.location_y = data.pose.pose.position.y
        self.location_z = data.pose.pose.position.z

def publish_command(position,velocity):
    desired_yaw = -10
    desired_x = position[0]
    desired_y = position[1]
    desired_z = position[2]
    quaternion = tf.transformations.quaternion_from_euler(0,0,math.radians(desired_yaw))
    traj = MultiDOFJointTrajectory()
    header = std_msgs.msg.Header()
    header.stamp = rospy.Time()
    header.frame_id = 'frame'
    traj.joint_names.append('base_link')
    traj.header = header
    transform = Transform(translation=Point(desired_x,desired_y,desired_z),rotation=Quaternion(quaternion[0],quaternion[1],quaternion[2],quaternion[3]))
    velocities = Twist()
    velocities.linear.x = velocity[0]
    velocities.linear.y = velocity[1]
    velocities.linear.z = velocity[2]
    accelerations = Twist()
    point = MultiDOFJointTrajectoryPoint([transform],[velocities],[accelerations],rospy.Time(2))
    traj.points.append(point)
    firefly_command_publisher.publish(traj)
    rospy.loginfo("Have published %s into %s!",position + velocity,'/firefly/command/trajectory')
    

def collision_detection():
    return False

def steering_angle():
    # retutn the direction agle
    return atan2(R1.target_y - R1.location_y, R1.target_x- R1.location_x)

def distance2target():
    return sqrt(pow((R1.target_x - R1.location_x), 2) +
                    pow((R1.target_y - R1.location_y), 2))

def distance2initial():
    return sqrt(pow((R1.initial_x - R1.location_x), 2) +
                    pow((R1.initial_y - R1.location_y), 2))



def callback(data):
    # update_pose(data)
    if collision_detection() is  not True:
        steer_angle = steering_angle()
        if distance2target() > 1:
            new_x = R1.location_x + velocity*cos(steer_angle)
            new_y = R1.location_y + velocity*sin(steer_angle)
            publish_command([new_x, new_y, R1.target_z],[0, 0, 0])
            print("Should:", [new_x, new_y, R1.target_z],[0, 0, 0])
        else:
            # publish_command([R1.location_x, R1.location_x, R1.target_z],[0, 0, 0])
            rospy.loginfo("Arrived target location!")
def listener():
    rospy.Subscriber("/firefly/ground_truth/odometry", Odometry, callback)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('rotors_go2goal', anonymous=True)
    velocity = 0.6
    firefly_command_publisher = rospy.Publisher('/firefly/command/trajectory',MultiDOFJointTrajectory,queue_size=10)
    R1 = Robot([1, 1, 2],[10, 10, 2])
    while distance2initial() > 1:
        publish_command([R1.initial_x, R1.initial_y, R1.initial_z],[0.05, 0.05, 0.05])
    if distance2initial() <= 1:
        rospy.loginfo("Arrived initial location!")
        try:
            listener()
        except rospy.ROSInterruptException:
            pass