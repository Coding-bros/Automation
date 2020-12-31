
# importing pyautogui and time
import pyautogui as pg
import time 
from tkinter import *
import sys

def chrome():
    """ 
    This Function opens spotlight,
    waits for 1 second, then opens chrome.
    after chrome opens, it makes the chrome full screen
    """
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

    # waits for 3 seconds
    time.sleep(3)

# ---------------------------

def terminal():
    """ 
    This Function opens spotlight,
    waits for 1 second, then opens terminal.
    after terminal opens, it makes the terminal full screen
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

    # waits for 3 seconds
    time.sleep(3)

# ---------------------------

def discord():
    """ 
    This Function opens spotlight,
    waits for 1 second, then opens discord.
    after discord opens, it makes the discord full screen
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

    # waits for 3 seconds
    time.sleep(3)
    # ---------------------------

def vsCode():
    """ 
    This Function opens spotlight,
    waits for 1 second, then opens vsCode.
    after vsCode opens, it makes the vsCode full screen
    """
    # holds command
    pg.keyDown('command')
    # presses space
    pg.hotkey('space')
    # releases command
    pg.keyUp('command')
    
    # waits for 1 second
    time.sleep(1)

    # types vsCode with pauses of 0.3 seconds
    pg.typewrite('visual studio code\n', 0.3)

    # waits for 3 seconds
    time.sleep(3)

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

window = Tk()
window.geometry("1024x900")

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
