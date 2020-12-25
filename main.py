from tkinter import *
import sys
import pyautogui as pg
import time 
# importing pyautogui and time
import pyautogui as pg
import time
import json
import os

window = Tk()

if sys.platform.startswith('win32'):
    from windows_support import *

#load in settings from json file
with open("settings.json","r") as file:
    content = file.read()
    settings = json.loads(content)

window_settings = settings['window']

window.geometry(window_settings['resolution'])
window.title(window_settings["title"])
window.config(bg=window_settings['bg'])

del window_settings #garbage collection

def exit():
    #This Function Is Used to Quit the Windows Using the Quit Button 
    sys.exit()
# Opening Functions

def chrome():
    """ 
    This Function opens spotlight,
    waits for 1 second, then opens chrome.
    after chrome opens, it 
    """
    if sys.platform.startswith('win32'):
        chrome_windows()
        return
    # holds command
    pg.keyDown('command')
    # presses space
    pg.hotkey('space')
    # releases command
    pg.keyUp('command')
    
    # waits for 1 second
    time.sleep(1)

    # types chrome in 0.3 seconds
    pg.typewrite('chrome\n', 0.3)

    # waits for 0.5 seconds
    time.sleep(0.5)

# ---------------------------

def terminal():
    """ 
    This Function opens spotlight,
    waits for 1 second, then opens terminal.
    """
    # holds command
    pg.keyDown('command')
    # presses space
    pg.hotkey('space')
    # releases command
    pg.keyUp('command')
    
    # waits for 1 second
    time.sleep(1)

    # types terminal with pauses of 0.3 seconds
    pg.typewrite('terminal\n', 0.3)

    # waits for 0.5 seconds
    time.sleep(0.5)

# ---------------------------

def discord():
    """ 
    This Function opens spotlight,
    waits for 1 second, then opens discord
    """
    # holds command
    pg.keyDown('command')
    # presses space
    pg.hotkey('space')
    # releases command
    pg.keyUp('command')
    
    # waits for 1 second
    time.sleep(1)

    # types discord with pauses of 0.3 seconds
    pg.typewrite('discord\n', 0.3)

    # waits for 0.5 seconds
    time.sleep(0.5)

# ---------------------------

def vsCode():
    """ 
    This Function opens spotlight,
    waits for 1 second, then opens VS Code.
    """
    # holds command
    pg.keyDown('command')
    # presses space
    pg.hotkey('space')
    # releases command
    pg.keyUp('command')
    
    # waits for 1 second
    time.sleep(1)

    # types Visual Studio Code with pauses of 0.2 seconds
    pg.typewrite('visual studio code\n', 0.2)

    # waits for 0.5 seconds
    time.sleep(0.5)

# Setting Buttons

Button(text="Open Chrome", height=3, width=30, command=chrome).place(relx = 0.023, rely=0.010)

Button(text="Open Discord", height=3, width=30, command = discord).place(relx = 0.023, rely=0.2)

Button(text="Open terminal", height=3, width=30, command = terminal).place(relx = 0.023, rely=0.4)

Button(text="Visual Studio Code", height=3, width=30, command = vsCode).place(relx = 0.023, rely=0.6)

Button(text="Test", height=3, width=30).place(relx = 0.023, rely=0.8)

Button(text="Test", height=3, width=30).place(relx = 0.023, rely=1)

Button(text="Test", height=3, width=30).place(relx = 0.7, rely=0.010)

Button(text="Test", height=3, width=30).place(relx = 0.7, rely=0.2)

Button(text="Test", height=3, width=30).place(relx = 0.7, rely=0.4)

Button(text="Test", height=3, width=30).place(relx = 0.7, rely=0.6)

Button(text="Test", height=3, width=30).place(relx = 0.7, rely=0.8)

# Quit Button

quit_button = Button(text="Exit", bg="red", height=3, width=30, command=exit)
quit_button.place(relx = 0.355, rely=0.4)

# MainLoop

window.mainloop()
