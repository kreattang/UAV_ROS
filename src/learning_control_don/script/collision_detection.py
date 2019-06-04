#! /usr/bin/env python

import rospy
from math import atan2, cos, sin, sqrt, asin, degrees, fabs
R_vo = 0.9
import time
import numpy as np

def get_distance(position1, position2):
    return sqrt(pow((position1[0] - position2[0]), 2) +
                    pow((position1[0] - position2[0]), 2))

def relative_angle(owner, i):
    # retutn the direction agle
    return atan2(i[1] - owner[1], i[0]- owner[0])

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

def collision_detecter(owner, intruders):
    print(owner, intruders)
    for i in intruders:
        d = get_distance([owner[0], owner[1]], [i[0], i[1]])
        # print("Distance:", d)
        if d < 3 and d > R_vo:
            print("In detection range!")
            Collision_angle = degrees(asin(R_vo/float(d)+0.001))
            print("Collision angle", Collision_angle)
            Relative_angle = normalize_angle(degrees(relative_angle(owner, i)))
            print("Relative angle", Relative_angle)
            Velocity_angle = normalize_angle(degrees(owner[4]))
            print("Velocity angle", Velocity_angle)
            if fabs(Relative_angle - Velocity_angle) <= Collision_angle:
                print("In VO!\n")
                relative_location = Relative_location(owner, i)
                if relative_location:
                    print(relative_location)