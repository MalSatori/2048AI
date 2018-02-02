import numpy as np
import cv2
import time
import os
from directkeys import UseKey, W, A, S, D
from time import sleep

WIDTH = [400]
HEIGHT = [320]


action = [UseKey(W), UseKey(A), UseKey(S), UseKey(D)]

class game:
    def frame_step(self, key, score=0):
        # last_time = time.time()

        # print('Loop took {} seconds.'.format(time.time()-last_time))
        # last_time = time.time()

        if key[0] == 1:
            action[0]
        elif key[1] == 1:
            action[1]
        elif key[2] == 1:
            action[2]
        elif key[3] == 1:
            action[3]

        reward = 0


        return reward, score
