import numpy as np
import cv2
import time
from grabscreen import grab_screen
import os
from alexnet import alexnet
from check_keys import key_check
from win32api import SetCursorPos


SCREENWIDTH = 400
SCREENHEIGHT = 320

WIDTH = 80
HEIGHT = 60
LR = 1e-3
EPOCH = 8
MODEL_NAME = 'pyagar-{}-{}-{}-epoch.model'.format(LR, 'alexnetv2', EPOCH)

def upRight():
    #Mouse upper right quadrant
    SetCursorPos((SCREENWIDTH + 200, SCREENHEIGHT - 200))

def upLeft():
    #Mouse upper right quadrant
    SetCursorPos((SCREENWIDTH - 200, SCREENHEIGHT - 200))

def downRight():
    #Mouse lower right quadrant
    SetCursorPos((SCREENWIDTH + 200, SCREENHEIGHT + 200))

def downLeft():
    #Mouse lower left quadrant
    SetCursorPos((SCREENWIDTH - 200, SCREENHEIGHT + 200))

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

last_time = time.time()

paused = True
while(True):
    if not paused:
        screen = grab_screen(region=(0, 100, 800, 640))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (80,60))

        print('Frame took {} seconds.'.format(time.time()-last_time))
        last_time = time.time()

        prediction = model.predict([screen.reshape(WIDTH, HEIGHT,1)])[0]
        moves = list(np.around(prediction))
        print(moves, prediction)

        # move_thresh = .7
        # if prediction[0] > move_thresh:
        #     upRight()
        # elif prediction[1] > move_thresh:
        #     upLeft()
        # elif prediction[2] > move_thresh:
        #     downLeft()
        # elif prediction[3] > move_thresh:
        #     downRight()



        # [UpRight, UpLeft, DownLeft, DownRight]
        if moves == [0.,1.,0.,0.]:
            upLeft()
        elif moves == [1.,0.,0.,0.]:
            upRight()
        elif moves == [0.,0.,1.,0.]:
            downLeft()
        elif moves == [0.,0.,0.,1.]:
            downRight()

    keys = key_check()
    if 'T' in keys:
        if paused:
            paused = False
            time.sleep(1)
        else:
            paused = True
            time.sleep(1)