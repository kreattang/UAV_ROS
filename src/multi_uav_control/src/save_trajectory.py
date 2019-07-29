#! usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from math import sqrt
from Write_list_to_csv import wirte_list_to_csv
import time
target = False
class robot_position():
    def __init__(self, name):
        self.name = name
        self.position_x = 10
        self.position_y = 10
        self.position_subscriber = rospy.Subscriber('/'+self.name+'/ground_truth/odometry', Odometry, self.update_pose)
    def update_pose(self, data):
        self.position_x = data.pose.pose.position.x
        self.position_y = data.pose.pose.position.y

def get_distance(position1, position2):
    return sqrt(pow((position1[0] - position2[0]), 2) +
                    pow((position1[0] - position2[0]), 2))

def address():
    global target
    Tr = [[[] for i in range(2)] for j in range(3)]
    while True:
        if get_distance([R1.position_x, R1.position_y],[20, 0]) < 1 and get_distance([R2.position_x, R2.position_y],[0, 20]) < 1 and get_distance([R3.position_x, R3.position_y],[0, 0]) < 1:
            target = True
            break
    while target is True:
        print "saving"
        Tr[0][0].append(R1.position_x)
        Tr[0][1].append(R1.position_y)
        Tr[1][0].append(R2.position_x)
        Tr[1][1].append(R2.position_y)
        Tr[2][0].append(R3.position_x)
        Tr[2][1].append(R3.position_y)
        if get_distance([R1.position_x, R1.position_y],[0, 20]) < 1 and get_distance([R2.position_x, R2.position_y],[20, 0]) < 1 and get_distance([R3.position_x, R3.position_y],[20, 20]) < 1:
            target = False
            print "END!"
            wirte_list_to_csv(Tr, 'three_UAVs.csv')
            print ('Saved!')
            break
        time.sleep(0.5)

def listener():
    rospy.init_node('trajectory', anonymous=True)
    address()
    rospy.spin()

if __name__ == '__main__':
    R1 = robot_position('firefly1')
    R2 = robot_position('firefly2')
    R3 = robot_position('firefly3')
    listener()
