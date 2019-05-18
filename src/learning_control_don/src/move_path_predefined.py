#!/usr/bin/env python

import rospy
from trajectory_msgs.msg import MultiDOFJointTrajectory,MultiDOFJointTrajectoryPoint
from geometry_msgs.msg import Vector3,Twist,Transform,Quaternion,Point
from geometry_msgs.msg import PointStamped
from std_msgs.msg import String
import std_msgs.msg
import tf
import math
import time

firefly_command_publisher = rospy.Publisher('/firefly/command/trajectory',MultiDOFJointTrajectory,queue_size=10)

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
    time.sleep(3)
    firefly_command_publisher.publish(traj)
    rospy.loginfo("Have published %s into %s!",position+velocity,'/firefly/command/trajectory')


def callback(data):
    '''learning_topic Callback Function'''
    # rospy.loginfo("Header:%s",data.header)
    # rospy.loginfo("Current position:%s,%s,%s", data.point.x,data.point.y,data
    # .point.z)
    print(data.point.x,data.point.y,data.point.z)
    a = data.point.z
    publish_command([0,5,int(a)+2],[0,0,0])


def listener():
    '''learning_topic Subscriber'''
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    
    rospy.Subscriber("/firefly/ground_truth/position", PointStamped, callback)


if __name__ == '__main__':
    rospy.init_node('goto_poition',anonymous=True)
    # rospy.init_node('position', anonymous=True)
    rospy.Subscriber("/firefly/ground_truth/position", PointStamped, callback)
    