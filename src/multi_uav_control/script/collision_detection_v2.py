#! /usr/bin/env python

import rospy
from math import atan2, cos, sin, sqrt, asin, degrees, fabs, radians
R_vo = 1.5
import time
import numpy as np
from fuzzy_control_new import Action
# from insert_record_mongo import insert_to_databse
import csv
# now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
# fname="/home/wenbing/Learning_ROS_ws/src/multi_uav_control/src/trajectory/"+now+r"trajectory.csv"
# csvFile = open(fname,'wb')
# csvFile.close()
# csv_trajectory = open(fname, 'a')
# writer = csv.writer(csv_trajectory)


def get_distance(position1, position2):
    return sqrt(pow((position1[0] - position2[0]), 2) +
                    pow((position1[1] - position2[1]), 2))

def relative_angle(owner, i):
    # retutn the direction agle
    return atan2(i[1] - owner[1], i[0]- owner[0])

def relative_velocity_angle(owner, i):
    point1 = [owner[0]+owner[3]*cos(owner[4])-i[3]*cos(i[4]), owner[1]+owner[3]*sin(owner[4])-i[3]*sin(i[4])]
    point2 = [owner[0], owner[1]]
    # print(point1, point2)
    return atan2(point1[1]-point2[1], point1[0]-point2[0])

def normalize_angle(angle):
    if angle > 0:
        return angle
    else:
        return 360 + angle

def get_relative_relationship(start, end, other):
   return (start[0] - other[0])*(end[1] - other[1]) - (start[1]-other[1])*(end[0]-other[0])



def Angle_Bet_TVect(Vec1,Vec2,Std):
    # print(Vec1,Vec2,Std)
    x = np.array([Vec1[0], Vec1[1]])
    y = np.array([Vec2[0], Vec2[1]])
    std = np.array([Std[0], Std[1]])
    x = x - std
    y = y - std
    Lx = np.sqrt(x.dot(x))
    Ly = np.sqrt(y.dot(y))
    cos_angle = x.dot(y) / (Lx * Ly+0.001)
    angle = np.arccos(cos_angle)
    angle2 = angle * 360 / 2 / np.pi
    return round(angle2,2)


def Relative_location(owner, i):
    Rel_loaction = ''
    Angle_Bet = Angle_Bet_TVect([owner[0]+ owner[3]*cos(owner[4]), owner[1]+ owner[3]*sin(owner[4])],[i[0], i[1]], [owner[0], owner[1]])
    # print([owner[0]+ owner[3]*cos(owner[4]), owner[1]+ owner[3]*sin(owner[4])],[i[0], i[1]], [owner[0], owner[1]])
    # print(Angle_Bet)
    if Angle_Bet <= 30:
        Rel_loaction = 'F'
    elif Angle_Bet > 30 and Angle_Bet <= 90:
        Relationship = get_relative_relationship([owner[0], owner[1]], [owner[0]+ owner[3]*cos(owner[4]), owner[1]+ owner[3]*sin(owner[4])],[i[0], i[1]])
        if Relationship > 0:
            Rel_loaction = 'L'
        if Relationship < 0:
            Rel_loaction = 'R'
    return Rel_loaction

def CRAF(owner, i):
    print(owner, i)
    v1 = np.array([owner[3]*cos(owner[4]), owner[3]*sin(owner[4])])
    v2 = np.array([i[3]*cos(i[4]), i[3]*sin(i[4])])
    relative_velocity = v1 - v2
    P_o = np.array([owner[0], owner[1]])
    P_i = np.array([i[0], i[1]])
    Loaction_Vec = P_i - P_o
    a = relative_velocity.dot(Loaction_Vec)
    b = np.linalg.norm(relative_velocity)**2
    t_CPA = a/float(b)
    # print(t_CPA)
    P_ot = np.array([owner[0]+owner[3]*cos(owner[4])*t_CPA, owner[1]+owner[3]*sin(owner[4])*t_CPA])
    P_it = np.array([i[0]+i[3]*cos(i[4])*t_CPA, i[1]+i[3]*sin(i[4])*t_CPA])
    d_CPA = round(np.linalg.norm(P_ot - P_it),10)
    # print(d_CPA)
    d = get_distance([owner[0], owner[1]], [i[0], i[1]])
    Collision_angle = degrees(asin(R_vo/float(d)+0.001))
    Relative_angle = normalize_angle(degrees(relative_angle(owner, i)))
    Velocity_angle = normalize_angle(degrees(owner[4]))
    alpha = fabs(Relative_angle - Velocity_angle)
    alpha_max = Collision_angle
    alpha_min = asin(0.3/(float(d)+0.001))
    # print(alpha)
    
    # calculate membership function
    if d_CPA >= 8:
        mu_d = 0
    elif d_CPA <= 0.5:
        mu_d = 1
    else:
        mu_d = (3 - d_CPA)/(3 - 0.5)
    if t_CPA >= 2:
        mu_t = 0
    elif t_CPA <= 0.5:
        mu_t = 1
    else:
        mu_t = (2 - t_CPA)/(2 - 0.5)
    if alpha > alpha_max:
        mu_alpha = 0
    elif alpha < alpha_min:
        mu_alpha = 1
    else:
        mu_alpha = (alpha_max - alpha) / float(alpha_max - alpha_min)
    
    craf = 1.0/3*mu_t + 1.0/3*mu_d + 1.0/3*mu_alpha
    return craf




def deal_conflicts(confllicts):
    # print(confllicts)
    temp = []
    if len(confllicts) == 0:
        pass
    elif len(confllicts) == 1:
        return confllicts[0]
    else:
        max_ROC = confllicts[0][1]
        for i in confllicts:
            if i[1] >= max_ROC:
                temp = i
                max_ROC = i[1]
    # del temp[1]
    return temp



def simplify_by_CRAF(confllicts):
    confllict_L = []
    confllict_F = []
    confllict_R = []
    final_conflict = []
    for c in confllicts:
        if c[0] == 'L':
            confllict_L.append(c)
        if c[0] == 'F':
            confllict_F.append(c)
        if c[0] == 'R':
            confllict_R.append(c)
    # print( confllict_L,confllict_F,confllict_R)
    for co in confllict_L,confllict_F,confllict_R:
        # print(co)
        if deal_conflicts(co):
            temp = deal_conflicts(co)
            del temp[1]
            final_conflict.append(temp)
    return final_conflict






def time2nearest_point(owner, i):
    p1 = [owner[0], owner[1]]
    p2 = [i[0], i[1]]
    d = get_distance(p1, p2)
    time = 0
    while d >5 and time < 10:
        time = time + 0.1
        # print(time)
        p1 = [owner[0] + owner[3]*cos(owner[4])*time, owner[1] + owner[3]*sin(owner[4])*time]
        p2 = [i[0]+i[3]*cos(i[4])*time, i[1]+i[3]*sin(i[4])*time]
        # print(p1, p2)
        d = get_distance(p1, p2)
        # print(d)
    # print(time)
    return time
        
def simplify_by_time(confllicts):
    confllict_L = []
    confllict_F = []
    confllict_R = []
    final_conflict = []
    for c in confllicts:
        if c[0] == 'L':
            confllict_L.append(c)
        if c[0] == 'F':
            confllict_F.append(c)
        if c[0] == 'R':
            confllict_R.append(c)
    for co in confllict_L, confllict_F, confllict_R:
        if co:
            final_conflict.append(sorted(co, key=(lambda x:x[1]))[0])
    if final_conflict:
        return final_conflict




def collision_detecter(owner, intruders):
    # record = {}
    # record['data_type'] = 'trajectory'
    # record['name'] = robot_name
    # record['own_loac'] = owner
    # record['intruders'] = intruders
    # record['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # insert_to_databse(record)
    collision = []
    for i in intruders:
        temp_collision = []
        d = get_distance([owner[0], owner[1]], [i[0], i[1]])
        print("Distance:", d)
        # if d < 0.5*R_vo:
        #     return [1, 5]
        # if d > 1.5*R_vo and d < 2*R_vo:
        #     return None
        if d < 8.0 and d > 2*R_vo:
            # print("In detection range!")
            Collision_angle = degrees(asin(2*R_vo/float(d)+0.001))
            # print("Collision angle", Collision_angle)
            Relative_angle = normalize_angle(degrees(relative_angle(owner, i)))
            # print("Relative position angle", Relative_angle)
            Velocity_angle = normalize_angle(degrees(relative_velocity_angle(owner, i)))
            # print("Relative velocity angle", Velocity_angle)
            if fabs(Relative_angle - Velocity_angle) <= Collision_angle:
                # print("In VO!")
                # print("info:", i)
                relative_location = Relative_location(owner, i)
                if relative_location:
                    # print("Relative Location:", relative_location)
                    # print("Time to nearest point:", time2nearest_point(owner,i))
                    temp_collision.append(relative_location)
                    temp_collision.append(time2nearest_point(owner,i))
                    temp_collision.append(d)
                    temp_collision.append(i)
                if temp_collision:
                    # print("One collision:", temp_collision)
                    collision.append(temp_collision)      
    if collision:
        # record_collision = {}
        # record_collision['data_type'] = 'all_collision'
        # record_collision['name'] = robot_name
        # record_collision['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # record_collision['all_collision'] = collision
        # print("All colliaion:", collision)
        # insert_to_databse(record_collision)
        sim_collision = simplify_by_time(collision)
        # print("Final collision:", sim_collision)
        # record_sim_collision = {}
        # record_sim_collision['data_type'] = 'sim_collision'
        # record_sim_collision['name'] = robot_name
        # # record_sim_collision['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # record_sim_collision['sim_collision'] = sim_collision
        # insert_to_databse(record_sim_collision)
    #     # return None    
        action = Action(sim_collision)
        # print("Should action:", action)
        if action:
            # record_action= {}
            # record_action['data_type'] = 'action'
            # record_action['name'] = robot_name
            # record_action['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # record_action['action'] = action
            # insert_to_databse(record_action)
            # print("ACTION INFO:",robot_name, action)
            return action
            


                     
