"""
This was done using python 3.7.9. I couldn't get new versions of python to work, If you manage to make it work, please contact
me cause I would like to know what you did.

GO WINDOW FULLSCREEN MODE BEFORE STARTING THE GAME!
"""

#Bot Creation Libraries
from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
import threading

#Creating a GUI for the bot? Perhaps
import tkinter

########## TIME FOR ALT+TAB ##########

#Upon starting it, you'll have 5 seconds to alt+tab into the game
time.sleep(5) 

########## CREATING GUI ##########
#Maybe someday

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
        #time.sleep(0.0005)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

"""
It will find the "cursorUpgrade.png" image on screen (setted it to grayscale so it doesn't have a hard time finding it). Setted the x on the
middle and the y as well, then went down 768 (eventhough we are going down we need to add it, not substract it) and then with each iteration
we go up a bit, to be more precise, 64, which is the actual distance between each upgrade. It will only click each of them once
"""
def buyUpgrades():
    cursorUpgrade = pyautogui.locateOnScreen('./images/cursorUpgrade.png',grayscale =True,confidence=0.6)
    for i in range (0,13):
        click(cursorUpgrade.left+int(cursorUpgrade.width/2),((cursorUpgrade.top+int(cursorUpgrade.height/2)+768-i*64)),1)
    
"""
This is honestly for fancies, cause achievements would pile up and end up obstructing part of the game screen.
It doesn't really ifluence the bot, It just annoyed me :)
"""
def closeAchievement():
    closeAch = pyautogui.locateOnScreen('./images/closeAchievement.png',grayscale =True,confidence=0.6)
    if closeAch != None:
        click(closeAch.left+int(closeAch.width/2),(closeAch.top+int(closeAch.height/2)),1)

"""
Turns out there was more upgrades, so this should find "upgradeFrame.png" and buy always the first one, since it's the cheapest one
"""
def buyOtherUpgrades(a):
    upgradeFrame = pyautogui.locateOnScreen('./images/upgradeFrame.png',grayscale =True,confidence=0.6)
    click(upgradeFrame.left+30,(upgradeFrame.top+int(upgradeFrame.height/2)),a)

"""
I haven't had that many golden cookies so I had to find the image on internet and crop it with paint, I don't even know if it works since
it's a random event lol
"""
def goldenCookie():
    gold = pyautogui.locateOnScreen('./images/goldenCookie.png',grayscale =True,confidence=0.6)
    if gold != None:
        click(gold.left+int(gold.width/2),(gold.top+int(gold.height/2)),1)

########## CREATING THREADS ##########
"""
I friend suggested I might want to thread some processed so clicks don't get delayed, therefore I delayed two processed that should always
be running, searching for a golden cookie and closing the achievement pop up.
"""
t1 = threading.Thread(target=goldenCookie)
t2 = threading.Thread(target=closeAchievement)

########## MAIN LOOP ##########

#Search for the cookie by looking at "mainCookie.png"
daCookie = pyautogui.locateOnScreen('./images/mainCookie.png',grayscale =True,confidence=0.8)

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

"""
WHAT ELSE?

- Would like to implement a GUI with tkinter, I know how to do it, I'm just lazy

- Also would be nice if I could use cheat engine and get the memory addresses for certain values, like the number of cookies or the number
  of farms for example and then do a tab in tkinter where you could change the values of the stuff. This should be easy but time consuming,
  since finding the static variable that writes the dynamic ones could be a pain in the ass.
"""