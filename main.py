import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32api
import ctypes
import math
from grabscreen import grab_screen
from getmouse import mouse_check
import os

WIDTH = [400]
HEIGHT = [320]
def mouse_to_output(x, y):
    #[UpRight, UpLeft, DownLeft, DownRight]
    output = [0,0,0,0]
    if y < HEIGHT and x > WIDTH:
        output[0] = 1
    elif y < HEIGHT and x < WIDTH:
        output[1] = 1
    elif y > HEIGHT and x < WIDTH:
        output[2] = 1
    else:
        output[3] = 1

    return output


file_name = 'training_data.npy'
if os.path.isfile(file_name):
    print('File exists, loading previous data.')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh.')
    training_data = []

last_time = time.time()

while(True):
    screen = grab_screen(region=(0, 100, 800, 640))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    screen = cv2.resize(screen, (80,60))
    x, y = mouse_check()
    output = mouse_to_output(x, y)
    training_data.append([screen,output])
    #print('Loop took {} seconds.'.format(time.time()-last_time))
    last_time = time.time()
    if len(training_data) % 500 == 0:
        print(len(training_data))
        np.save(file_name, training_data)

    # cv2.imshow('window', new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break