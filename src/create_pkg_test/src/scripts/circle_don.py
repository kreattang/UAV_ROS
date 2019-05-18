#!/usr/bin/env python
# license removed for brevity
import rospy
import message_filters
import math
from nav_msgs.msg import Odometry, Path
from trajectory_msgs.msg import MultiDOFJointTrajectory, MultiDOFJointTrajectoryPoint
from geometry_msgs.msg import Twist, Transform, PointStamped, Pose, PoseStamped, Quaternion
from tf.msg import tfMessage
from tf.transformations import *

pub1 = rospy.Publisher('/firefly/command/trajectory', MultiDOFJointTrajectory, queue_size=10)
# pub2 = rospy.Publisher('/pelican_1/path', Path, queue_size = 10)
sub_odometry = message_filters.Subscriber('/firefly/ground_truth/odometry', Odometry)
# sub_odometry_1 = message_filters.Subscriber('/pelican/ground_truth/odometry', Odometry)
theta = math.pi/360.0
th0 = 0.0
path = Path()

def callback(odometry):
    global path
    global th0
    current_time = rospy.get_rostime()

    pelican_poses = PoseStamped()
    # pelican_poses.pose = odometry.pose.pose
    # pelican_poses.header.stamp = current_time
    # pelican_poses.header.frame_id = 'world'
    # path.poses.append(pelican_poses)

    th0 = th0 + theta
    rospy.loginfo("Current angle %s", th0)
    x_current = odometry.pose.pose.position.x
    y_current = odometry.pose.pose.position.y
    x_new = 7.0*math.cos(th0)
    y_new = 7.0*math.sin(th0)
    #x_new = x_current*math.cos(theta) - y_current*math.sin(theta)
    #y_new = x_current*math.sin(theta) + y_current*math.cos(theta)
    z_new = 4.0
    rospy.loginfo('the next position is (%s,%s,%s)', x_new, y_new, z_new)
    trajectory_point = MultiDOFJointTrajectoryPoint()
    trajectory = MultiDOFJointTrajectory()

    transform = Transform()
    transform.translation.x = x_new
    transform.translation.y = y_new
    transform.translation.z = z_new
    q_rot = quaternion_from_euler(0.0, 0.0, th0 + math.pi/2.0)
    #q_rot = quaternion_multiply(q_rot1, q_orig)
    transform.rotation.x = q_rot[0]
    transform.rotation.y = q_rot[1]
    transform.rotation.z = q_rot[2]
    transform.rotation.w = q_rot[3]

    trajectory_point.transforms.append(transform)
    trajectory.points.append(trajectory_point)

    pelican_poses.pose.position.x = x_new
    pelican_poses.pose.position.y = y_new
    pelican_poses.pose.position.z = z_new
    #pelican_poses.pose.orientation = q_new
    '''pelican_poses.pose.orientation.x = q_rot[0]
    pelican_poses.pose.orientation.y = q_rot[1]
    pelican_poses.pose.orientation.z = q_rot[2]
    pelican_poses.pose.orientation.w = q_rot[3]'''
    pelican_poses.header.stamp = current_time
    pelican_poses.header.frame_id = 'world'
    path.poses.append(pelican_poses)

    pub1.publish(trajectory)
    # pub2.publish(path)

if __name__ == '__main__':
    rospy.init_node('circle2', anonymous=True)
    now = rospy.get_rostime()
    path.header.stamp = now
    path.header.frame_id = 'world'
    # rospy.loginfo("Current time %i %i", now.secs, now.nsecs)
    ts = message_filters.TimeSynchronizer([sub_odometry], 10)
    ts.registerCallback(callback)
    rospy.spin()