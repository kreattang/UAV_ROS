#!/usr/bin/env python
'''learning_topic ROS Node'''
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PointStamped

def callback(data):
    '''learning_topic Callback Function'''
    rospy.loginfo("Header:%s",data.header)
    rospy.loginfo("Current position:%s,%s,%s", data.point.x,data.point.y,data
    .point.z)

def listener():
    '''learning_topic Subscriber'''
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('position', anonymous=True)

    rospy.Subscriber("/firefly/ground_truth/position", PointStamped, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
