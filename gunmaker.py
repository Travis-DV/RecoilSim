# -----------------------------------------------------------
#
#    Project:      Full Wepon Modding stuff
#    Author:       Travis Findley
#    Created:      1/3/2022
#    Description:  Wepon modding stuffs
#
# -----------------------------------------------------------

#Libs
from locale import currency
from random import randint
from time import sleep
import baseboard as bb
import recoil

#Fuctions
def settingset():
    guns = bb.guns
    ammotype = bb.ammotype
    magsize = bb.magsize
    workablemods = bb.workablemods
    cmods = bb.cmods
    mods = bb.mods
    parts = bb.parts
    return guns, ammotype, magsize, workablemods, cmods, mods, parts
def gunchooser():
    global error; global guns; global ammotype; global index2
    word = "What gun would you like to choose?\n"
    for g in guns:
        word += f" \033[1;32m{g}\033[1;0m chambered in: \033[1;35m{ammotype[index2]}\033[1;0m (\033[1;33m{index2+1}\033[1;0m)\n"
        index2 += 1
    while True:
        user_input = str.lower(input(word + " "))
        if user_input.isnumeric():
            gunpic = int(user_input)-1
            print(f"You choose the \033[1;32m{guns[gunpic]}\033[1;0m chambered in: \033[1;35m{ammotype[gunpic]}\033[1;0m!")
            break
        else:
            print(" " + error)
    return gunpic
def findpart():
    global cmods; global gunpic; global find; global word; global part; global index2
    index3 = 0
    action = 0
    for m in cmods[gunpic]:
        if find in m:
            cmods[gunpic][index3] = m.split("-")
            action = 1
            break
        index3 += 1
    if index2 > 0 and index2 < 6:
        word += ", "
    elif index2 >= 6:
        word += "!"
    if index2 < 6:
        if action == 1:
            word += f"{mods[part[0]][int(cmods[gunpic][index3][1])]} \033[1;0m(\033[1;33m{index2}\033[1;0m)"
        else:
            word += f"You do not have a {part[1]}\033[1;0m (\033[1;33m{index2}\033[1;0m)"
    save = cmods[gunpic]
    return word, save

#Other vars
error = "\033[1;31mError, try inputing again\033[1;0m"
word = "You have a: "
index2 = 0
yha = 0

#Actual user code
guns, ammotype, magsize, workablemods, cmods, mods, parts = settingset()
gunpic = gunchooser()
recoil.fr = bb.fr[gunpic]

while True:
    index2 = 0
    user_input = str.lower(input("Would you like to mod it? (\033[1;33my\033[1;0m, \033[1;31mn\033[1;0m)\n"))
    if user_input == "y":
        #on you have nothing at the end of your muzzle you have nothing on your muzzle
        while index2 < 7:
            if index2 < 6:
                find = f"{str(index2)}-"
                part = [index2, parts[index2]]
            word, save = findpart()
            index2 += 1
        break
    elif user_input == "n":
        print("Ok bye :)")
        break
    else:
        print(error)
while True:
    user_input = str.lower(input(f"{word}\nWhat do you want to change?\n"))
    if user_input.isnumeric():
        user_input = int(user_input)
        break
    else:
        print(error)
word = "You can change it to a, "; index2 = 0
for m in mods[user_input]:
    word += f"{m}\033[1;0m (\033[1;33m{index2}\033[1;0m)"
    if index2 < len(mods[user_input]) - 2:
        word += ", "
    elif index2 == len(mods[user_input]) - 2:
        word += ", or a "
    index2 += 1
while True:
    input2 = str.lower(input(f"{word}\n"))
    if input2.isnumeric():
        input2 = int(input2)
        break
    else:
        print(error)
if user_input == 0:
    magsize[input2] = int(((input2+14)*45)/29)
    bb.magsize[input2] = magsize[input2]
    print(magsize)
print(f"You want to change it to a {mods[user_input][input2]}\033[1;0m.")
user_input = str(user_input); input2 = str(input2)
while type(cmods[gunpic][0]) == list:
    t = cmods[gunpic][0]
    cmods[gunpic].remove(t)
    if t[0] == user_input:
            t = t[0] + "-" + input2
    else:
        t = t[0] + "-" + t[1]
    cmods[gunpic].append(t)
    bb.cmods = cmods