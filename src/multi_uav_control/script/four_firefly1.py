#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry, Path
from trajectory_msgs.msg import MultiDOFJointTrajectory,MultiDOFJointTrajectoryPoint
from geometry_msgs.msg import Vector3,Twist,Transform,Quaternion,Point, PointStamped, PoseStamped
import time, tf, math
import std_msgs.msg
from math import atan2, cos, sin, sqrt, degrees, radians
from collision_detection_v2 import collision_detecter
path = Path()
time_UAV1 = []
sep = ','


class Robot():
    def __init__(self, location, target, velocity):
        self.name = 'firefly1'
        self.location_x = 100
        self.location_y = 100
        self.location_z = 100
        self.initial_x = location[0]
        self.initial_y = location[1]
        self.initial_z = location[2]
        self.target_x = target[0]
        self.target_y = target[1]
        self.target_z = target[2]
        self.velocity = velocity
        self.velocity_angle = 0
        self.pose_subscriber =  rospy.Subscriber("/firefly1/ground_truth/odometry", Odometry, self.update_pose)
    def update_pose(self, data):
        self.location_x = data.pose.pose.position.x
        self.location_y = data.pose.pose.position.y
        self.location_z = data.pose.pose.position.z
        # publish velocity
        owner_velocity = Twist()
        owner_velocity.linear.x = self.velocity
        owner_velocity.linear.y = self.velocity_angle
        self.velocity_publisher = rospy.Publisher('/firefly1/velocity', Twist, queue_size = 10)
        self.velocity_publisher.publish(owner_velocity)

class Intruder():
    def __init__(self, intruder_name):
        self.name = intruder_name
        self.location_x = 100
        self.location_y = 100
        self.location_z = 100
        self.velocity = 0
        self.velocity_angle = 0
        self.pose_subscriber =  rospy.Subscriber('/'+self.name+'/ground_truth/odometry', Odometry, self.update_pose)
        self.vel_subscriber = rospy.Subscriber('/'+self.name+'/velocity', Twist, self.update_vel)
    def update_pose(self, data):
        self.location_x = data.pose.pose.position.x
        self.location_y = data.pose.pose.position.y
        self.location_z = data.pose.pose.position.z
    def update_vel(self, data):
        self.velocity = data.linear.x
        self.velocity_angle = data.linear.y


def publish_command(position,velocity):
    desired_yaw = -10
    desired_x = position[0]
    desired_y = position[1]
    desired_z = position[2]
    quaternion = tf.transformations.quaternion_from_euler(0,0,math.radians(desired_yaw))
    traj = MultiDOFJointTrajectory()
    header = std_msgs.msg.Header()
    header.stamp = rospy.Time()
    # header.frame_id =
    # traj.joint_names.append('base_link')
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
    rospy.loginfo("Have published %s into %s!",position + velocity,'/firefly1/command/trajectory')
    # rate = rospy.Rate(50)
    # rate.sleep()

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
    owner = [R1.location_x, R1.location_y, R1.location_z, R1.velocity, R1.velocity_angle]
    firefly2 = [I1.location_x, I1.location_y, I1.location_z, I1.velocity, I1.velocity_angle]
    firefly3 = [I2.location_x, I2.location_y, I2.location_z, I2.velocity, I2.velocity_angle]
    firefly4 = [I3.location_x, I3.location_y, I2.location_z, I3.velocity, I3.velocity_angle]
    # start = time.clock()
    action = collision_detecter(owner, [firefly2, firefly3, firefly4])
    # print("All infos:", owner, [firefly2, firefly3])
    if action is None:
        steer_angle = steering_angle()
        R1.velocity_angle = steer_angle
        R1.velocity = 2
        if distance2target() > 1:
            new_x = R1.location_x + R1.velocity*cos(R1.velocity_angle)
            new_y = R1.location_y + R1.velocity*sin(R1.velocity_angle)
            print("curent target:", new_x, new_y)
            print("curent location:",R1.location_x, R1.location_y)
            # new_xx = new_x - 1.40
            # new_yy = new_y + 1.40
            publish_command([new_x, new_y, R1.target_z],[0, 0, 0])
            # print("publish info:", [new_x, new_y, R1.target_z],[0, 0, 0])
            # print(R1.location_x, R1.location_y)
            # used_time = time.clock()-start
            # time_UAV1.append(used_time)
        else:
            # publish_command([R1.location_x, R1.location_x, R1.target_z],[0, 0, 0])
            rospy.loginfo("Firefly1 arrived target location!")
            # for ii in range(len(time_UAV1)):
            #     time_UAV1[ii] = str(time_UAV1[ii])
            # with open('/home/wenbing/Learning_ROS_ws/src/multi_uav_control/script/time_uav1.csv', 'a') as f:
            #     f.write(sep.join(time_UAV1))
            # rospy.loginfo("Writing")
    elif action is not None:
        print("Firefly1 Should action:", action)
        if action[0] + action[1] > 0:
            R1.velocity = R1.velocity - (R1.velocity - 0.3)*float(action[0])
            steer_angle = R1.velocity_angle - radians(float(action[1]))
            R1.velocity_angle = steer_angle
            if distance2target() > 1:
                new_x = R1.location_x + R1.velocity*cos(R1.velocity_angle)
                new_y = R1.location_y + R1.velocity*sin(R1.velocity_angle)
                publish_command([new_x, new_y, R1.target_z],[0, 0, 0])
                print("Should:", [new_x, new_y, R1.target_z],[0, 0, 0])
                # used_time = time.clock()-start
                # time_UAV1.append(used_time)
            else:
                # publish_command([R1.location_x, R1.location_x, R1.target_z],[0, 0, 0])
                rospy.loginfo("Firefly1 arrived target location!")
                # for ii in range(len(time_UAV1)):
                #     time_UAV1[ii] = str(time_UAV1[ii])
                # with open('./time_uav1.csv', 'a') as f:
                #     f.write(sep.join(time_UAV1))
                # rospy.loginfo("Writing")

def publish_trajectory(data):
    global path
    path.header = data.header
    pose = PoseStamped()
    pose.header = data.header
    pose.pose = data.pose.pose
    path.poses.append(pose)
    firefly1_path_pub.publish(path)

def listener():
    rospy.Subscriber("/firefly1/ground_truth/odometry", Odometry, callback)
    rospy.Subscriber('/firefly1/ground_truth/odometry', Odometry, publish_trajectory)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('firefly1_go2goal', anonymous=True)
    firefly1_path_pub = rospy.Publisher('/firefly1/path', Path, queue_size=10)
    firefly_command_publisher = rospy.Publisher('/firefly1/command/trajectory',MultiDOFJointTrajectory,queue_size=1)
    velocity_publisher = rospy.Publisher('/firefly1/velocity', Twist, queue_size = 10)
    R1 = Robot([20.5, -0.5, 2],[0, 20, 2], 2)
    while distance2initial() > 1:
        engine_angle = atan2(R1.initial_y - R1.location_y, R1.initial_x- R1.location_x)
        publish_command([R1.location_x + 2*cos(engine_angle), R1.location_y+2*sin(engine_angle), R1.initial_z],[0, 0, 0])
        R1.velocity = 2
        R1.velocity_angle = engine_angle
    if distance2initial() <= 1:
        rospy.loginfo("Firefly1 arrived initial location!")
        I1 = Intruder('firefly2')
        I2 = Intruder('firefly3')
        I3 = Intruder('firefly4')
        try:
            listener()
        except rospy.ROSInterruptException:
            pass