#!/usr/bin/env python

import rospy
from trajectory_msgs.msg import MultiDOFJointTrajectory,MultiDOFJointTrajectoryPoint
from geometry_msgs.msg import Vector3,Twist,Transform,Quaternion,Point
import std_msgs.msg
import tf
import math
import time


#Here, two parameters are the given position and velocity of UAV, respectively.
def publish_command(position,velocity):
    rospy.init_node('goto_poition',anonymous=True)
    firefly_command_publisher = rospy.Publisher('/firefly/command/trajectory',MultiDOFJointTrajectory,queue_size=10)
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
    
if __name__ == '__main__':
    # for i in range(1,10):
    #     try:
    #         publish_command([2*i,2*i,2],[0,0,0])
    #     except rospy.ROSInterruptException:
    #         pass
    #     time.sleep(1)
    try:
        publish_command([0,0,2],[0,0,0])
    except rospy.ROSInterruptException:
        pass
        


        
    
    








