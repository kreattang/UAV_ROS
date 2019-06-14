#! /usr/bin/env python

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# membership function of the distance in region left
# membership function of the distance in region left
d_L = ctrl.Antecedent(np.arange(0, 8, 0.1), 'd_L')
d_L['N'] = fuzz.zmf(d_L.universe, 1.2, 8)
d_L['F'] = fuzz.smf(d_L.universe, 1.2, 8)

d_R = ctrl.Antecedent(np.arange(0,4, 0.1), 'd_R')
d_R['N'] = fuzz.zmf(d_R.universe, 1.2, 8)
d_R['F'] = fuzz.smf(d_R.universe, 1.2, 8)

d_F = ctrl.Antecedent(np.arange(0,4, 0.1), 'd_F')
d_F['N'] = fuzz.zmf(d_F.universe, 1.2, 8)
d_F['F'] = fuzz.smf(d_F.universe, 1.2, 8)
# d_R.view()


v = ctrl.Consequent(np.arange(0,1.1, 0.1), 'v')
v['VL'] = fuzz.trimf(v.universe, [0, 0, 0.8])
v['L'] = fuzz.trimf(v.universe, [0, 0.8, 1])
v['H'] = fuzz.trimf(v.universe, [0.8, 1, 1])
# v.view()

theta = ctrl.Consequent(np.arange(0,90.001, 0.1), 'theta')
theta['VS'] = fuzz.trimf(theta.universe, [0, 0, 22.5])
theta['S'] = fuzz.trimf(theta.universe, [0, 22.5, 45])
theta['M'] = fuzz.trimf(theta.universe, [22.5, 45, 67.5])
theta['B'] = fuzz.trimf(theta.universe, [45, 67.5, 90])
theta['VB'] = fuzz.trimf(theta.universe, [67.5, 90, 90])

# d_F.view()
# One Direction
# L
rule1 = ctrl.Rule(d_L['F'], v['VL'])
rule1_1 = ctrl.Rule(d_L['F'], theta['B'])
rule2 = ctrl.Rule(d_L['N'], v['L'])
rule2_1 = ctrl.Rule(d_L['N'], theta['M'])
FR_L = ctrl.ControlSystem([rule1, rule2, rule1_1, rule2_1])
FC_L = ctrl.ControlSystemSimulation(FR_L)

# F
rule3 = ctrl.Rule(d_F['F'], v['VL'])
rule3_1 = ctrl.Rule(d_F['F'], theta['M'])
rule4 = ctrl.Rule(d_F['N'], v['VL'])
rule5 = ctrl.Rule(d_F['N'], theta['B'])
FR_F = ctrl.ControlSystem([rule3, rule3_1, rule4, rule5])
FC_F = ctrl.ControlSystemSimulation(FR_F)

# R
rule6 = ctrl.Rule(d_R['F'], v['VL'])
rule7 = ctrl.Rule(d_R['F'], theta['B'])
rule8 = ctrl.Rule(d_R['N'], v['VL'])
rule9 = ctrl.Rule(d_R['N'], theta['VB'])
FR_R = ctrl.ControlSystem([rule6, rule7, rule8])
FC_R = ctrl.ControlSystemSimulation(FR_R)

#Two directions
# LF
rule10 = ctrl.Rule(d_L['F'] & d_F['F'], v['VL'])
rule11 = ctrl.Rule(d_L['F'] & d_F['N'], v['L'])
rule11_1 = ctrl.Rule(d_L['F'] & d_F['N'], theta['M'])
rule12 = ctrl.Rule(d_L['N'] & d_F['F'], v['H'])
rule12_1 = ctrl.Rule(d_L['N'] & d_F['F'], theta['S'])
rule13 = ctrl.Rule(d_L['N'] & d_F['N'], v['L'])
rule14 = ctrl.Rule(d_L['N'] & d_F['N'], theta['S'])
FR_LF = ctrl.ControlSystem([rule10, rule11, rule11_1, rule12, rule12_1, rule13, rule14])
FC_LF = ctrl.ControlSystemSimulation(FR_LF)

# RF
rule15 = ctrl.Rule(d_R['F'] & d_F['F'], v['VL'])
rule15_1 = ctrl.Rule(d_R['F'] & d_F['F'], theta['B'])
rule16 = ctrl.Rule(d_R['F'] & d_F['N'], v['L'])
rule17 = ctrl.Rule(d_R['F'] & d_F['N'], theta['M'])
rule18 = ctrl.Rule(d_R['N'] & d_F['F'], v['L'])
rule19 = ctrl.Rule(d_R['N'] & d_F['F'], theta['S'])
rule20 = ctrl.Rule(d_R['N'] & d_F['N'], v['L'])
rule21 = ctrl.Rule(d_R['N'] & d_F['N'], theta['S'])
FR_RF = ctrl.ControlSystem([rule15, rule15_1, rule16, rule17, rule18, rule19, rule20, rule21])
FC_RF = ctrl.ControlSystemSimulation(FR_RF)

# LR
rule22 = ctrl.Rule(d_L['F'] & d_R['F'], v['VL'])
rule23 = ctrl.Rule(d_L['F'] & d_R['F'], theta['B'])
rule24 = ctrl.Rule(d_L['F'] & d_R['N'], v['H'])
rule25 = ctrl.Rule(d_L['F'] & d_R['N'], theta['M'])
rule26 = ctrl.Rule(d_L['N'] & d_R['F'], v['H'])
rule27 = ctrl.Rule(d_L['N'] & d_R['F'], theta['M'])
rule28 = ctrl.Rule(d_L['N'] & d_R['N'], v['L'])
rule29 = ctrl.Rule(d_L['N'] & d_R['N'], theta['S'])
FR_LR = ctrl.ControlSystem([rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29])
FC_LR = ctrl.ControlSystemSimulation(FR_LR)


#Three directions
rule30 = ctrl.Rule(d_L['F'] & d_R['F'] & d_F['F'], v['VL'])
rule31 = ctrl.Rule(d_L['N'] & d_R['F'] & d_F['F'], v['H'])
rule32 = ctrl.Rule(d_L['N'] & d_R['F'] & d_F['F'], theta['VB'])
rule33 = ctrl.Rule(d_L['F'] & d_R['N'] & d_F['F'], v['H'])
rule34 = ctrl.Rule(d_L['F'] & d_R['N'] & d_F['F'], theta['B'])
rule35 = ctrl.Rule(d_L['F'] & d_R['F'] & d_F['N'], v['H'])
rule36 = ctrl.Rule(d_L['F'] & d_R['F'] & d_F['N'], theta['S'])
rule37 = ctrl.Rule(d_L['N'] & d_R['N'] & d_F['F'], v['L'])
rule38 = ctrl.Rule(d_L['N'] & d_R['N'] & d_F['F'], theta['M'])
rule39 = ctrl.Rule(d_L['N'] & d_R['F'] & d_F['N'], v['L'])
rule40 = ctrl.Rule(d_L['N'] & d_R['F'] & d_F['N'], theta['VS'])
rule41 = ctrl.Rule(d_L['F'] & d_R['N'] & d_F['N'], v['L'])
rule42 = ctrl.Rule(d_L['F'] & d_R['N'] & d_F['N'], theta['S'])
rule43 = ctrl.Rule(d_L['N'] & d_R['N'] & d_F['N'], v['VL'])
rule44 = ctrl.Rule(d_L['N'] & d_R['N'] & d_F['N'], theta['VS'])

FR_LRF = ctrl.ControlSystem([rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44])
FC_LRF = ctrl.ControlSystemSimulation(FR_LRF)


def Action(collision):
    print("collision:",collision)
    action_temp = [0 for i in range(2)]
    # One direction
    if len(collision) == 1:
        if collision[0][0] == 'L':
            Controller = FC_L
        if collision[0][0] == 'F':
            Controller = FC_F
        if collision[0][0] == 'R':
            Controller = FC_R
        arg1 = 'd_' + str(collision[0][0])
        Controller.input[arg1] = collision[0][2]
    if len(collision) == 2:
        if collision[0][0] != 'R' and collision[1][0] != 'R':
            Controller = FC_LF
        if collision[0][0] != 'L' and collision[1][0] != 'L':
            Controller = FC_RF
        if collision[0][0] != 'F' and collision[1][0] != 'F':
            Controller = FC_LR
        arg1 = 'd_' + str(collision[0][0])
        arg2 = 'd_' + str(collision[1][0])
        Controller.input[arg1] = collision[0][2]
        Controller.input[arg2] = collision[1][2]
    if len(collision) == 3:
        Controller = FC_LRF
        arg1 = 'd_' + str(collision[0][0])
        arg2 = 'd_' + str(collision[1][0])
        arg3 = 'd_' + str(collision[2][0])
        Controller.input[arg1] = collision[0][2]
        Controller.input[arg2] = collision[1][2]
        Controller.input[arg3] = collision[2][2]
    Controller.compute()
    output = Controller.output
    if 'v' in output:
        action_temp[0] = output['v']
    if 'theta' in output:
        action_temp[1] = output['theta']
    print("Should take action:", action_temp)
    # print action_temp
    return action_temp



# Action([['F', 0.7287429382528532, [4.851530218866315, 5.85082395189338, 1.8547781249919693, 0.6, 2.4339076781352182]], ['L', 0.7287429382528532, [4.851530218866315, 5.85082395189338, 1.8547781249919693, 0.6, 2.4339076781352182]],  ['R', 2.7287429382528532, [4.851530218866315, 5.85082395189338, 1.8547781249919693, 0.6, 2.4339076781352182]]])
# Action([['L', 1.161813702351307, [3.8587756875076282, 5.881825990704291, 2.041309093827154, 0.1, -1.549379799309445]], ['F', 3.5853657224869844, [5.572485755503922, 4.698448529359653, 1.8690891896749622, 0.13443831615930973, 2.1241076721387584]]])
# Action([['F', 0.9999999999999999, 3.104675472571028, [6.439674352369354, 13.609568270989906, 2.5397875793049542, 0, 0]]])