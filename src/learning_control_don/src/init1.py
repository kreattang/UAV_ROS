#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String
from trajectory_msgs.msg import MultiDOFJointTrajectory, MultiDOFJointTrajectoryPoint
from geometry_msgs.msg import Transform, PoseStamped, Twist
from Vector3 import Vector3
import math
from tf.msg import tfMessage
from tf.transformations import *
import sys

def main(x, y, z, a, b, c):
    rospy.init_node('init1', anonymous=True)

    now = rospy.get_rostime()
    rospy.loginfo("Current time %i %i", now.secs, now.nsecs)

    pub1 = rospy.Publisher('/firefly/command/trajectory', MultiDOFJointTrajectory, queue_size=100)

# initial position of the first pelican
    trajectory1 = MultiDOFJointTrajectory()
    trajectory1_point = MultiDOFJointTrajectoryPoint()
    trajectory1.header.frame_id = 'firefly/base_link'

    transform1 = Transform()
    #transform1.translation.x = 0
    #transform1.translation.y = 0
    #transform1.translation.z = 4
    transform1.translation = Vector3(x, y, z)
    q_rot = quaternion_from_euler(a,b,c)
    transform1.rotation.x = q_rot[0]
    transform1.rotation.y = q_rot[1]
    transform1.rotation.z = q_rot[2]
    transform1.rotation.w = q_rot[3]
    
    velocity1 = Twist()
    accelerate1 = Twist()
    t = rospy.Time.now()
    trajectory1.header.stamp.secs = t.secs
    trajectory1.header.stamp.nsecs = t.nsecs
    trajectory1_point.transforms.append(transform1)
    trajectory1_point.velocities.append(velocity1)
    trajectory1_point.accelerations.append(accelerate1)
    trajectory1.points.append(trajectory1_point)

# publish the related messages
    rate = rospy.Rate(100)

    while not rospy.is_shutdown():
        pub1.publish(trajectory1)
        rate.sleep()


if __name__ == '__main__':
    myargv = rospy.myargv(argv=sys.argv)
    if len(myargv) == 4:
        main(float(myargv[1]), float(myargv[2]), float(myargv[3]), 0.0, 0.0, 0.0)
    elif len(myargv) == 7:
        main(float(myargv[1]), float(myargv[2]), float(myargv[3]), float(myargv[4]), float(myargv[5]), float(myargv[6]))
    else:
        rospy.loginfo('Set the default values: initial position [%s,%s,%s]', 0.0, 0.0, 4.0)
        main(0,0,5,0,0,0)