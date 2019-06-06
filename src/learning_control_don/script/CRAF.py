#! /usr/bin/env python

import rospy
import numpy as np
from math import sin, cos, sqrt, degrees, asin, atan2, fabs

R_vo = 0.9
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

def CRAF(owner, i):
    v1 = np.array([owner[3]*cos(owner[4]), owner[3]*sin(owner[4])])
    v2 = np.array([i[3]*cos(i[4]), i[3]*sin(i[4])])
    relative_velocity = v1 - v2
    P_o = np.array([owner[0], owner[1]])
    P_i = np.array([i[0], i[1]])
    Loaction_Vec = P_i - P_o
    a = relative_velocity.dot(Loaction_Vec)
    b = np.linalg.norm(relative_velocity)**2
    t_CPA = a/float(b)
    print(t_CPA)
    P_ot = np.array([owner[0]+owner[3]*cos(owner[4])*t_CPA, owner[1]+owner[3]*sin(owner[4])*t_CPA])
    P_it = np.array([i[0]+i[3]*cos(i[4])*t_CPA, i[1]+i[3]*sin(i[4])*t_CPA])
    d_CPA = round(np.linalg.norm(P_ot - P_it),10)
    print(d_CPA)
    d = get_distance([owner[0], owner[1]], [i[0], i[1]])
    Collision_angle = degrees(asin(R_vo/float(d)+0.001))
    Relative_angle = normalize_angle(degrees(relative_angle(owner, i)))
    Velocity_angle = normalize_angle(degrees(owner[4]))
    alpha = fabs(Relative_angle - Velocity_angle)
    alpha_max = Collision_angle
    alpha_min = asin(0.3/(float(d)+0.001))
    print(alpha)
    
    # calculate membership function
    if d_CPA >= 3:
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
    print(mu_t, mu_d, mu_alpha)
    return craf


    

    




# CRAF([2.567733183876978, 7.38920108657914, 2.0403270698619766, 0.6, -0.7824900956322092], [2.224021527868973, 2.3434219508877887, 1.9657633470038383, 0.6, 0.7776613998542459])
print(CRAF([-3, 0, 1, 1, 0], [0, -2, 3, 2, 1.5708]))
