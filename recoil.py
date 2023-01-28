# -----------------------------------------------------------
#
#    Project:      Ricoil Sim v2
#    Author:       Travis Findley
#    Created:      27/2/2022
#    Description:  Cool Ricoil Sim, second try first one big bad
#
# -----------------------------------------------------------

#Importing libs
from random import randint
from time import sleep
#Importing other py files
import baseboard as bb

#Setting board
baseboard = [bb.baseboardTR, bb.baseboardTL, bb.baseboardBR, bb.baseboardBL]

#Other vars
bolletYN = 0
error = "\033[1;31mError, try inputing again\033[1;0m"
col = [0, 0]
row = [0, 0]
quarter = [0, 0]
fr = 0.2 #gunmaker.fr
action = 1

#Code
def printboard():
    global baseboard
    index2 = 0
    word = "\n"
    #Repets for every line in the top sections
    for s in baseboard[0]:
        #For every value in a line
        for spot in baseboard[0][index2]:
            word = whattoword(word, spot)
        for spot in baseboard[1][index2]:
            word = whattoword(word, spot)
        index2 += 1
        word += "\n"
    index2 = 0
    #Look above coments
    for s in baseboard[2]:
        for spot in baseboard[2][index2]:
            word = whattoword(word, spot)
        for spot in baseboard[3][index2]:
            word = whattoword(word, spot)
        index2 += 1
        word += "\n"
    index2 = 0
    print("\033[1;0m"+word)

#Finds what the number = in letters
def whattoword(word, spot):
    if type(spot) == str:
        word += "\033[1;31m.\033[1;0m"
    elif spot == -4:
        word += "\033[1;37m]\033[1;0m"
    elif spot == -3:
        word += "\033[1;37m[\033[1;0m"
    elif spot == -2:
        word += "\033[1;37m|\033[1;0m"
    elif spot == -1:
        word += "\033[1;37m-\033[1;0m"
    #Finds what to set if you want bollet holes
    if type(spot) != str and bolletYN == 1:
        if spot == 1:
            word += "\033[1;30m#\033[1;0m"
        elif spot > 1:
            word += "\033[1;35m"+str(spot)+"\033[1;0m"
        elif spot == 0:
            word += " "
    elif bolletYN != 1 and spot >= 0:
        word += " "
    return word

def ran(col, row, quarter):
    if action != 0:
        col[1] = col[0]
        row[1] = row[0]
        quarter[1] = quarter[0]
    col[0] = randint(1,6)
    row[0] = randint(0,3)
    quarter[0] = randint(0,3)
    return col,row,quarter

def firing():
    global baseboard; global error; global bolletYN; global col; global row; global quarter; global ran; global fr; global action; global printboard
    while True:
        user_input = input("Do you want bollet holes? (\033[1;33my\033[1;0m/\033[1;31mn\033[1;0m)\n\033[1;32m")
        if user_input == "y":
            bolletYN = 1
            break
        elif user_input == "n":
            bolletYN = 0
            break
        else:
            print(error)

#actualy does all that
    printboard()
    while True:
        fireamount = input("\033[1;0mHow much do you want to;  \033[1;31mFIRE!!!!\n")
        print("\033[1;0m")
        if fireamount.isnumeric():
            fireamount = int(fireamount)
            break
        else:
            print(error)
    baseboard[1][3][0] = 0

    while fireamount > 0:
        col, row, quarter = ran(col, row, quarter)
        count = [0, 0, 0, 0]
    #clearing old pointer
        if action == 1:
            if quarter[1] == 0:
                baseboard[0][row[1]][col[1]] = int(baseboard[0][row[1]][col[1]]) + 1
            elif quarter[1] == 1:
                baseboard[1][row[1]][col[1]] = int(baseboard[1][row[1]][col[1]]) + 1
            elif quarter[1] == 2:
                baseboard[2][row[1]][col[1]] = int(baseboard[2][row[1]][col[1]]) + 1
            elif quarter[1] == 3:
                baseboard[3][row[1]][col[1]] = int(baseboard[3][row[1]][col[1]]) + 1
        action = 1
    #Setting new spot
    #Top Right
        if quarter[0] == 0 and count[0] < 5 and baseboard[0][row[0]][col[0]] >= 0:
            baseboard[0][row[0]][col[0]] = str(baseboard[0][row[0]][col[0]])
            count = [count[0]+1, 0, 0, count[3]]
    #Top Left
        elif quarter[0] == 1 and count[1] < 6 and baseboard[1][row[0]][col[0]] >= 0:
            baseboard[1][row[0]][col[0]] = str(baseboard[1][row[0]][col[0]])
            count = [count[0], count[1]+1, 0, count[3]]
    #Bottem Right
        elif quarter[0] == 2 and count[2] < 2 and baseboard[2][row[0]][col[0]] >= 0:
            baseboard[2][row[0]][col[0]] = str(baseboard[2][row[0]][col[0]])
            count = [0, 0, count[2]+1, 0]
    #Bottem Left
        elif quarter[0] == 3 and count[3] < 4 and baseboard[3][row[0]][col[0]] >= 0:
            baseboard[3][row[0]][col[0]] = str(baseboard[3][row[0]][col[0]])
            count = [count[1], 0, 0, count[3]+1]
        else:
            action = 0
        if action == 1:
            fireamount -= 1
            printboard()
            sleep(fr)
while True:
    #Make based on mag size in gunmaker
    user_input = input("Do you still have Ammo? (\033[1;33my\033[1;0m/\033[1;31mn\033[1;0m)\n")
    if user_input == "n":
        print("Ok, leaving now! Have a good day :)")
        break
    elif user_input == "y":
        firing()
    else:
        print(error)