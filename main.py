# importing pyautogui and time
import pyautogui as pg
import time 

#-----------------------------

ask = input('Are You On Mac Or Windows Or Linux: ')

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
# ---------------------------------
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