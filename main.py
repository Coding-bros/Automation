# importing pyautogui and time
import pyautogui as pg
import time 
from tkinter import *
import sys

"""
Pyautogui : Automation
Time : To make the automation a bit slower
tkinter : GUI
sys : To close the window
"""

#-----------------------------

ask = input('Are You On Mac Or Windows Or Linux: ')

# mac

if ask.strip().lower() == 'mac':
    def chromeM():
        """ 
        This Function opens spotlight,
        waits for 1 second, then opens chrome.
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

    def terminalM():
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

        # waits for 3 seconds
        time.sleep(3)

    # ---------------------------

    def discordM():
        """ 
        This Function opens spotlight,
        waits for 1 second, then opens discord.
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

    def vsCodeM():
        """ 
        This Function opens spotlight,
        waits for 1 second, then opens vsCode.
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
    
    # GUI (Mac)

    window = Tk()
    window.geometry("1024x900")

    Button(text="Open Chrome", height=3, width=30, command=chromeM).place(relx = 0.023, rely=0.010)

    Button(text="Open Discord", height=3, width=30, command = discordM).place(relx = 0.023, rely=0.2)

    Button(text="Open terminal", height=3, width=30, command = terminalM).place(relx = 0.023, rely=0.4)

    Button(text="Visual Studio Code", height=3, width=30, command = vsCodeM).place(relx = 0.023, rely=0.6)

    # Extra Buttons For the User (Mac)

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
# ---------------------------------

# windows or linux

if ask.strip().lower() == 'windows' or ask.strip().lower() == 'linux':
    def chrome():
        """ 
        This Function opens start menu,
        waits for 1 second, then opens chrome.
        """
        # presses the start menu button
        pg.hotkey('winleft')
        
        # waits for 1 second
        time.sleep(1)

        # types chrome in 0.3 seconds
        pg.typewrite('chrome\n', 0.3)

        # waits for 3 seconds
        time.sleep(3)

    # ---------------------------

    def terminal():
        """ 
        This Function opens start menu,
        waits for 1 second, then opens terminal.
        """
        # presses the start menu button
        pg.hotkey('winleft')
        
        # waits for 1 second
        time.sleep(1)

        # types terminal with pauses of 0.3 seconds
        pg.typewrite('terminal\n', 0.3)

        # waits for 3 seconds
        time.sleep(3)

    # ---------------------------

    def discord():
        """ 
        This Function opens start menu,
        waits for 1 second, then opens discord.
        """
        # presses the start menu button
        pg.hotkey('winleft')
        
        # waits for 1 second
        time.sleep(1)

        # types discord with pauses of 0.3 seconds
        pg.typewrite('discord\n', 0.3)

        # waits for 3 seconds
        time.sleep(3)
        # ---------------------------

    def vsCode():
        """ 
        This Function opens start menu,
        waits for 1 second, then opens vsCode.
        """
        # presses the start menu button
        pg.hotkey('winleft')
        
        # waits for 1 second
        time.sleep(1)

        # types vsCode with pauses of 0.3 seconds
        pg.typewrite('visual studio code\n', 0.3)

        # waits for 3 seconds
        time.sleep(3) 

    # GUI (windows & linux)
    window = Tk()
    window.geometry("1024x900")

    Button(text="Open Chrome", height=3, width=30, command=chrome).place(relx = 0.023, rely=0.010)

    Button(text="Open Discord", height=3, width=30, command = discord).place(relx = 0.023, rely=0.2)

    Button(text="Open terminal", height=3, width=30, command = terminal).place(relx = 0.023, rely=0.4)

    Button(text="Visual Studio Code", height=3, width=30, command = vsCode).place(relx = 0.023, rely=0.6)

    # Extra buttons for the user (windows or linux)

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