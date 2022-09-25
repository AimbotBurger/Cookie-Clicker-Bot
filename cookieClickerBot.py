"""
This was done using python 3.7.9. I couldn't get new versions of python to work, If you manage to make it work, please contact
me cause I would like to know what you did.
GO WINDOW FULLSCREEN MODE BEFORE STARTING THE GAME!

If you get an error in line 46 with win32, that means your script is not being runed as an admin, if you are using cmd, please make sure
it is runned as admin as well
"""
########## __name__ CHECK ##########
import sys

if __name__ != '__main__':
    sys.exit('Do not import! CookieClickerBot.py should be your __main__, please execute it with admin privileges to prevent errors')
    
########## BOT CREATION LIBRARIES ##########
from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
import threading

#NEW STUFF
import os
from core import *
from cookieGUI import *




########## MAIN LOOP ##########

#Upon starting it, you'll have 5 seconds to alt+tab into the game
time.sleep(5) 

#Will keep running until you stop the execution of the script
while True: 
    #Click the cookie on the middle
    click((daCookie.left+int(daCookie.width/2)),(daCookie.top+int(daCookie.height/2)),1)
    t1.start #goldenCookie
    t2.start #closeAchievement

    """
    Tap 'e' once and the clicking will stop, tap it again clicking will resume. Hold it for a little bit when resuming.
    Tap 'u' once to buy each upgrade once
    Tap 'i' once to buy the cheapest upgrade on the top right corner
    """
    if keyboard.is_pressed('e'):
        resume = False
        while resume == False:
            time.sleep(1)
            if keyboard.is_pressed('e'):
                resume=True
                time.sleep(1)

    elif keyboard.is_pressed('u'):
        buyUpgrades()

    elif keyboard.is_pressed('i'):
        buyOtherUpgrades(1)



