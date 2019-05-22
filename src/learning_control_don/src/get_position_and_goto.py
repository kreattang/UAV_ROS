#! /usr/bin/env python


# import msg type
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PointStamped
import time
from trajectory_msgs.msg import MultiDOFJointTrajectory,MultiDOFJointTrajectoryPoint
from geometry_msgs.msg import Vector3,Twist,Transform,Quaternion,Point
import tf
import math
import std_msgs.msg
import random
import time


def publish_command(data):
    # rospy.init_node('goto_poition',anonymous=True)
    firefly_command_publisher = rospy.Publisher('/firefly/command/trajectory',MultiDOFJointTrajectory,queue_size=10)
    position = [round(data.point.x) + 1, round(data.point.y) + 1, round(data.point.z)+1]
    velocity = [0,0,0]
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
    rospy.loginfo("Have published %s into %s!",position+velocity,'/firefly/command/trajectory')
    rate = rospy.Rate(10)
    rate.sleep()

def callback(data):
    rospy.loginfo("Current position:%s,%s,%s", data.point.x,data.point.y,data.point.z)
    # print(position, velocity)
    try:
        publish_command(data)
    except rospy.ROSInterruptException:
        pass

rospy.init_node('simple_control')
pub = rospy.Publisher('position_publish_test', PointStamped)
rospy.Subscriber("/firefly/ground_truth/position", PointStamped, callback)
rospy.spin()



