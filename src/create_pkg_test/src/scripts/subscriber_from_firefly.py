#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PointStamped

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
    

def listener():
    rospy.init_node('listener1',anonymous=True)
    rospy.Subscriber('/firefly/ground_truth/position',PointStamped,callback)
    rospy.spin()



if __name__ == '__main__':
    listener()