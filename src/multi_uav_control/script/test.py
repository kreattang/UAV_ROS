#! /usr/bin/env python

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

