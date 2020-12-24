# What Is This Automation Project

**This is A Code Made by the CodingBros So We Just Wanted To Make Our Lives Easier.** 

**So We Made this Automation Project Which Makes It So Much Simplier To Open The Apps We Use In Our Daily Life.**


**Feel Free To Add your Own Functions That You Use In. Your Daily Life.**

<br>
We Provided 6 Free Buttons Fou You To Add so To do it You Need basic Python Experience.

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
#
**PyAutoGui**

		pip install pyautogui

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

### Keep In Mind that For Now The Code is only Made for Mac We will Try To Do It For ***Windows*** and ***Linux*** soon.
#

## code
```py
from tkinter import *
import sys
import pyautogui as pg
import time 
# importing pyautogui and time
import pyautogui as pg
import time 


window = Tk()
# Settings/Preferences Of the Main Window
window.geometry('1000x600')
window.title('Automate')
window.config(bg="#444444")

def exit():
    """
    This Function Is Used to Quit the Windows Using the Quit Button 
    """
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
```
#
***Any Doubts??***

Contact Coding Bros at

- jaideep1163@gmail.com
- bkp.karthi@gmail.com

## ----------Thanks For Using Our Project------------
