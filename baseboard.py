# "." = [3][7]
# -15
from random import randint
#--------------------------------------------------------------------
#RECOIL
baseboardTR = \
    [[-3, -1, -1, -1, -1, -1, -1, -1],\
    [-2, 0, 0, 0, 0, 0, 0, 0],\
    [-2, 0, 0, 0, 0, 0, 0, 0],\
    [-2, 0, 0, 0, 0, 0, 0, 0]]

# -17
baseboardTL = \
    [[-1, -1, -1, -1, -1, -1, -1, -4],\
    [0, 0, 0, 0, 0, 0, 0, -2],\
    [0, 0, 0, 0, 0, 0, 0, -2],\
    ["0", 0, 0, 0, 0, 0, 0, -2]]

# -14
baseboardBR = \
    [[-2, 0, 0, 0, 0, 0, 0, 0],\
    [-2, 0, 0, 0, 0, 0, 0, 0],\
    [-2, 0, 0, 0, 0, 0, 0, 0],\
    [-3, -1, -1, -1, -1, -1, -1, -1]]

# -11
baseboardBL = \
    [[0, 0, 0, 0, 0, 0, 0, -2],\
    [0, 0, 0, 0, 0, 0, 0, -2],\
    [0, 0, 0, 0, 0, 0, 0, -2],\
    [-1, -1, -1, -1, -1, -1, -1, -4]]

#-------------------------------------------------------------------------

#GUN MAKER
guns = ["Scar", "m4a1", "AK-47", "AK-74"] #, "name" to add new gun
ammotype = [".308", "5.56 NATO", "7.62", "7.62"] # the index is in order with the guns, IF NEW GUN ADDED ADD AMMO TYPE
magsize = [30, 30, 24, 34] #IF GUN ADDED ADD MAG SIZE
# in order top to bottom with guns
# IF ADD NEW GUN ADD MODS IT CAN USE
#[gun[row][collem]]
workablemods = [[[0,1],[0,1,2,3],[0,1],[0,1,2,3,4],[0,1],[0,1,2]],\
    [[0,1],[0,1,2,3],[0,1,2],[0,1,2,3,4],[0,1],[0,1,2]],\
    [[0,1],[0,1,2,3],[0,1,2],[0,1,2,3,4],[0,1],[0,1,2]],\
    [[0,1],[0,1,2,3],[0,1,2],[0,1,2,3,4],[0,1],[0,1,2]]]
#the current mods #ADD NEW LIST IF GUN ADDED
#Gun[row-col]
cmods = [["0-1","2-0","3-0"],["1-0","0-1","2-2","3-1","4-0","5-0"],["0-1","2-1","3-0"],["0-1","2-1","3-0"]]
mods = [["\033[1;36mSmall Mag", "\033[1;36mMediam Mag", "\033[1;36mDrum Mag", "\033[1;36mMeme Mag"],\
    ["\033[1;34mVertical Forgrip", "\033[1;34mAngled Forgrip"],\
    ["\033[1;35mSturdy Stock", "\033[1;35mLight Stock", "\033[1;35mFoldable Stock"],\
    ["\033[1;32mIron Sight", "\033[1;32mRed dot Sight", "\033[1;32mReflex Sight", "\033[1;32m4x Sight", "\033[1;32m8x Sight"],\
    ["\033[1;30mMuzzle Break", "\033[1;30mSupreser"],\
    ["\033[1;37mLazer Pointer", "\033[1;37mFlashLight", "\033[1;37mFinder"]]
parts = ["\033[1;36mmag", "\033[1;34mforgrip", "\033[1;35mstock", "\033[1;32msight", "\033[1;30mend of muzzle attachment", "\033[1;37mon muzzle attachemt"]
fr = [0.1 + randint(-10, 10)/10, randint(6315789473, 8571428571)/100000000000, 0.1 + randint(-100, 700)/100, 0.0923076923 + randint(-20, 10)/10]