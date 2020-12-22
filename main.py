# importing pyautogui and time
import pyautogui as pg
import time 

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

    # waits for 0.5 seconds
    time.sleep(0.5)

    # to make full screen:
    
    # holds command
    pg.keyDown('command')
    # holds control
    pg.keyDown('control')
    # presses f
    pg.hotkey('f')
    # releases control
    pg.keyUp('control')
    # releases command
    pg.keyUp('command')

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

    # waits for 0.5 seconds
    time.sleep(0.5)

    # to make full screen:

    # holds command
    pg.keyDown('command')
    # holds control
    pg.keyDown('control')
    # presses f
    pg.hotkey('f')
    # releases control
    pg.keyUp('control')
    # releases command
    pg.keyUp('command')

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

    # waits for 0.5 seconds
    time.sleep(0.5)


    # to make full screen:
    
    # holds command
    pg.keyDown('command')
    # holds control
    pg.keyDown('control')
    # presses f
    pg.hotkey('f')
    # releases control
    pg.keyUp('control')
    # releases command
    pg.keyUp('command')
