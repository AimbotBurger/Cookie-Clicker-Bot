########## __main__ CHECK ##########
import sys

if __name__ == '__main__':
    sys.exit('This is not __main__, CookieClickerBot.py should be your __main__, please execute it with admin privileges to prevent errors')

########## LIBRARIES ##########
import tkinter as tk
from tkinter import ttk

m = tk.Tk() #We called our window m for simplicity
m.title("Cookie Cliker Bot by Handy") #Tittle
m.geometry('1280x720') #Canvas resolution

########## CANVAS SET UP ##########

canvas = tk.Canvas(m,width=1280, height=720) # We match the canvas resolution to the windows resolution
canvas.pack(fill='both', expand = True) #This tells how to arrange the elements

########## BUTTONS ##########

closeApp = tk.Button(m,text='Close App',width=50,height=2,command=m.destroy)
closeApp.pack(pady=20)

closeapp_canvas = canvas.create_window(50,20,anchor='nw', window = closeApp)
