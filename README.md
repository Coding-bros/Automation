# What Is This Automation Project

**This is A Code Made by the CodingBros So We Just Wanted To Make Our Lives Easier.** 

**So We Made this Automation Project Which Makes It So Much Simplier To Open The Apps We Use In Our Daily Life.**


**Feel Free To Add your Own Functions That You Use In. Your Daily Life.**

<br>
We Provided 6 Free Buttons For You To Add Your Own Functions. To do it You Need basic Python Experience.

 We gave a small example of how to make functions for the free buttons

** **
## what all you need for this code to run "in MacOS":
**Terminal**

Press Command + Space and then type **terminal**

	cd Desktop

#

**git**

	brew install git
<br>

	git clone https://github.com/Coding-bros/Automation.git
<br>

	cd Automation
#

**Python**

	brew install python3

**Tkinter**

this is default in **MacOS** , no need to install if you have Python installed
for **linux**:

    sudo apt-get install python3-tk
#
**PyAutoGui**

    pip3 install pyautogui

#

### If the code doesn't work :
python3 -m venv (any name for the virtual env)

	python3 -m venv test
<br>

	source test/bin/activate
<br>

** **
## How To Add Own Functions

```py
def Your_Function():
	print('Hello World')
```

**Then :** 

```py
Button(text="Test")
```

**Add a comma, and then type command and add your function, like shown below :**

```py
Button(text="Test", command=Your_Function)
```

**Thats How You define Your Own Functions**
#

### The Code is Supported in All OSes

#

## code
```py
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

    Button(text="Extra", height=3, width=30).place(relx = 0.023, rely=0.8)

    Button(text="Extra", height=3, width=30).place(relx = 0.023, rely=1)

    Button(text="Extra", height=3, width=30).place(relx = 0.7, rely=0.010)

    Button(text="Extra", height=3, width=30).place(relx = 0.7, rely=0.2)

    Button(text="Extra", height=3, width=30).place(relx = 0.7, rely=0.4)

    Button(text="Extra", height=3, width=30).place(relx = 0.7, rely=0.6)

    Button(text="Extra", height=3, width=30).place(relx = 0.7, rely=0.8)

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
```
#
***Any Doubts??***

Contact Coding Bros at

- jaideep1163@gmail.com
- bkp.karthi@gmail.com

## ----------Thanks For Using Our Project------------
