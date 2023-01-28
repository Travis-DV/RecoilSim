# -----------------------------------------------------------
#
#     Project:     Ricoil Sim
#    Author:       Travis Findley
#    Created:      1s/9/2022
#    Description:  Cool Ricoil Sim
# -----------------------------------------------------------

# Library imports
from os import kill
from random import randint
from time import sleep
from baseboard import baseboard
# import loading
# loading
#List
zeroed = baseboard
#starting variables
count = 0
col = 0
row = 0
line = ""
pirCR = [7, 3]
fr = 1
yn = 0
cntqurt = [0, 0, 0, 0]
ranCR = [0, 0]
action = 0
#Project
def pri3dL(zeroed, col, row, line, bolletYN):
    while len(zeroed) > row:
        if 15 == col:
            print(line)
            row = row+1
            col = 0
            if zeroed[row][col] == -3:
                line = "["
            elif zeroed[row][col] == -2:
                line = "|"
            elif bolletYN == 1:
                if zeroed[row][col] == 1:
                    line += "#"
                elif zeroed[row][col] > 1:
                    line += str(zeroed[row][col])
                elif zeroed[row][col] == 0:
                    line += " "
        elif 14 >= col:
            if zeroed[row][col] > 1:
                line += str(zeroed[row][col])
            elif zeroed[row][col] == -5:
                line += "."
            elif zeroed[row][col] == -4:
                line += "]"
            elif zeroed[row][col] == -3:
                line += "["
            elif zeroed[row][col] == -2:
                line += "|"
            elif zeroed[row][col] == -1:
                line += "-"
            if bolletYN == 1:
                if zeroed[row][col] == 1:
                    line += "#"
                elif zeroed[row][col] > 1:
                    line += str(zeroed[row][col])
                elif zeroed[row][col] == 0:
                    line += " "
            else:
                if zeroed[row][col] >= 0:
                    line += " "
        col = col+1
bolletYN = input("Do you want bollet holes? \n").lower()
if bolletYN == "y":
    yn = 1
pri3dL(zeroed, col, row, line, bolletYN)
input2 = int(input("FIRE!!!! \n"))-1
zeroed[3][7] = 0
inpvar = input2
def randomMove():
    ranCR[0] = randint(-2, 3)
    ranCR[1] = randint(-2, 3)
    return ranCR[0], ranCR[1]

def printlist(zeroed, col, row, line, pirCR, fr, pri3dL):
    zeroed[pirCR[1]][pirCR[0]] = -4
    pri3dL(zeroed, col, row, line)
    sleep(fr)
iteration = 0
while 0 <= inpvar:
    action = 0
    if yn == 0:
        zeroed[pirCR[1]][pirCR[0]] = 0
    else:
        zeroed[pirCR[1]][pirCR[0]] += 1
        ranCR[0], ranCR[1] = randomMove()
    if ranCR[0] == 0 or ranCR[1] == 0:
        ranCR[0], ranCR[1] = randomMove()
    pirCR[0] = pirCR[0]+ranCR[0]
    pirCR[1] = pirCR[1]+ranCR[1]
    if pirCR[0] > 0 and pirCR[0] < 14 and pirCR[1] > 0 and pirCR[1] < 6:
        if 3 <= pirCR[1] and 7 > pirCR[0] and 1 != action:
            if cntqurt[0] < 3:
                cntqurt[0] = cntqurt[0]+1
                cntqurt[1] = 0
                cntqurt[2] = 0
                cntqurt[3] = 0
                printlist(zeroed, col, row, line, pirCR[0], pirCR[1], fr, pri3dL)
                print(inpvar)
                action = 1
        elif 3 <= pirCR[1] and 7 <= pirCR[0] and 1 != action:
            if cntqurt[1] < 6:
                cntqurt[0] = 0
                cntqurt[1] = cntqurt[1]+1
                cntqurt[2] = 0
                cntqurt[3] = 0
                printlist(zeroed, col, row, line, pirCR, fr, pri3dL)
                print(inpvar)
                action = 1
        elif 3 > pirCR[1] and 7 >= pirCR[0] and 1 != action:
            if cntqurt[2] < 1:
                cntqurt[0] = 0
                cntqurt[1] = 0
                cntqurt[2] = cntqurt[2]+1
                cntqurt[3] = 0
                printlist(zeroed, col, row, line, pirCR[0], pirCR[1], fr, pri3dL)
                print(inpvar)
                action = 1
        elif 3 > pirCR[1] and 7 < pirCR[0] and 1 != action:
            if cntqurt[3] < 2:
                cntqurt[0] = 0
                cntqurt[1] = 0
                cntqurt[2] = 0
                cntqurt[3] = cntqurt[3]+1
                printlist(zeroed, col, row, line, pirCR[0], pirCR[1], fr, pri3dL)
                print(inpvar)
                action = 1
        else:
            action = 0
    else:
        pirCR[0] = pirCR[0]-ranCR[0]
        pirCR[1] = pirCR[1]-ranCR[1]
    if 0 == action:
        iteration += 1
        print(f"Iteration {iteration}")
    elif 1 == action:
        inpvar -= 1
printlist(zeroed, col, row, line, pirCR[0], pirCR[1], fr, pri3dL)