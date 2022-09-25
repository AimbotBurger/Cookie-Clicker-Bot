########## __main__ CHECK ##########
import sys

if __name__ == '__main__':
    sys.exit('This is not __main__, CookieClickerBot.py should be your __main__, please execute it with admin privileges to prevent errors')

########## BOT CREATION LIBRARIES ##########
from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
import threading

import tkinter #Creating a GUI for the bot? Perhaps

#NEW STUFF
import os

########## DEF ##########

"""
CLick on coordinates x,y a certain amount of times
To find out the coordinates, use IDLE and type the following in case you want to implement something:
    >>>import pyautogui
    >>>pyautogui.displayMousePosition()
This will not only give you the coordinates your cursor it's at but also the RGB value of the position
"""
def click(x,y,repeat):
    i=0
    for i in range (repeat):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        #time.sleep(0.0005) #Not useful since there is no click limit set by the game lulw
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

"""
It will find the "cursorUpgrade.png" image on screen (setted it to grayscale so it doesn't have a hard time finding it). Setted the x on the
middle and the y as well, then went down 768 (eventhough we are going down we need to add it, not substract it) and then with each iteration
we go up a bit, to be more precise, 64, which is the actual distance between each upgrade. It will only click each of them once
"""
def buyUpgrades():
    for i in range (0,13):
        click(cursorUpgrade.left+int(cursorUpgrade.width/2),((cursorUpgrade.top+int(cursorUpgrade.height/2)+768-i*64)),1)
    
"""
This is honestly for fancies, cause achievements would pile up and end up obstructing part of the game screen.
It doesn't really ifluence the bot, It just annoyed me :)
"""
def closeAchievement():
    if closeAch != None:
        click(closeAch.left+int(closeAch.width/2),(closeAch.top+int(closeAch.height/2)),1)

"""
Turns out there was more upgrades, so this should find "upgradeFrame.png" and buy always the first one, since it's the cheapest one
"""
def buyOtherUpgrades(a):
    click(upgradeFrame.left+30,(upgradeFrame.top+int(upgradeFrame.height/2)),a)

"""
I haven't had that many golden cookies so I had to find the image on internet and crop it with paint, I don't even know if it works since
it's a random event lol
"""
def goldenCookie():
    if gold != None:
        click(gold.left+int(gold.width/2),(gold.top+int(gold.height/2)),1)




########## CREATING THREADS ##########
"""
I friend suggested I might want to thread some processed so clicks don't get delayed, therefore I delayed two processed that should always
be running, searching for a golden cookie and closing the achievement pop up.
"""
t1 = threading.Thread(target=goldenCookie)
t2 = threading.Thread(target=closeAchievement)




########## IMAGE SEARCH ##########
#We set up the Current Working Directory aka CWD
CWD = os.path.dirname(os.path.realpath(__file__))

""""
We alter the route by using join and adding the images folder into the route and our file name, just to avoid mistakes when typing and cause
#this is taking longer than I would admit
"""
#Search for the cookie by looking at "mainCookie.png"
daCookie = pyautogui.locateOnScreen(os.path.join(CWD, "images", "mainCookie.png"),grayscale =True,confidence=0.8)
#Search for "cursorUpgrade.png"
cursorUpgrade = pyautogui.locateOnScreen(os.path.join(CWD, "images", "cursorUpgrade.png"),grayscale =True,confidence=0.8)
#Search for "closeAchievement.png"path
closeAch = pyautogui.locateOnScreen(os.path.join(CWD, "images", "closeAchievement.png"),grayscale =True,confidence=0.8)
#Search for "upgradeFrame.png"
upgradeFrame = pyautogui.locateOnScreen(os.path.join(CWD, "images", "upgradeFrame.png"),grayscale =True,confidence=0.8)
#Search for "goldenCookie.png"
gold = pyautogui.locateOnScreen(os.path.join(CWD, "images", "goldenCookie.png"),grayscale =True,confidence=0.8)




########## CREATING GUI ##########
#Maybe someday




""" Could be really helpful:
https://medium.com/@martin.lees/image-recognition-for-automation-with-python-711ac617b4e5
"""