#!/usr/bin/env python

import rospy  
from std_msgs.msg import String  
  
def callback(data):  
    rospy.loginfo(rospy.get_caller_id() + "callback:I heard %s", data.data)  
    #resp_str = "resp_str: I heard: " + data.data  
    talker(data)  
  
def listener():  
  
    # In ROS, nodes are uniquely named. If two nodes with the same  
    # node are launched, the previous one is kicked off. The  
    # anonymous=True flag means that rospy will choose a unique  
    # name for our 'listener' node so that multiple listeners can  
    # run simultaneously. http://blog.csdn.net/sonictl  
    rospy.init_node('responsor', anonymous=True)  
  
    rospy.Subscriber("uc0Response", String, callback)  
  
    # spin() simply keeps python from exiting until this node is stopped  
    rospy.spin()  
      
def talker(data):  
    pub = rospy.Publisher('uc0Command', String, queue_size=10)  
    rospy.loginfo("talker:I heard %s", data.data)  
  
    #while not rospy.is_shutdown():  
    resp_str = "resp_str: I heard: " + data.data  
    rospy.loginfo(resp_str)  
    if data.data == "cigit-pc\n" :  
        pub.publish(resp_str)  
    else:  
        rospy.loginfo("invalid seri data:" + data.data)  
          
if __name__ == '__main__':  
    #listener()  
    try:  
        listener()  
        #talker()  
    except rospy.ROSInterruptException:  
        pass  