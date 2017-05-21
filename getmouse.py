import win32gui
import time


def mouse_check():
    posX = []
    posY = []
    flags, hcursor, (x, y) = win32gui.GetCursorInfo()
    posX.append(x)
    posY.append(y)
    #print(str(x) + ' ' + str(y))
    return posX, posY