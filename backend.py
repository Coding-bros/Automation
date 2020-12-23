# importing pyautogui and time
import pyautogui as pg
import time 

def chrome():
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
