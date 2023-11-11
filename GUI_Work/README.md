# $`\textcolor{blue}{\text{Python Basics - GUI Work}}`$
A collection of Python (.py) files illustrating  Python concepts in dealing 
with the a GUI (graphical user interface).  
Richard Ay (November 2023)

## $`\textcolor{blue}{\text{Table of Contents}}`$  
* [Setup](#setup)
* [Envirionment](#environment)
* [File List](#file-list)



## Setup
Refer to the main 'readme.md' in the directory above.  This 'readme.md' contains additional
information in setting up the 'virtual environment' and running the scripts in this
subdirectory.   

## Environment
To utilize these scripts, a virtual environment is created so that the installation of NumPY remains
local to this subdirectory, and does not affect the rest of the machine.

The virtual environment can be setup using the command: 
**'python -m venv "GUIenv" --upgrade-deps --prompt="GUIenv"'**

To start/stop the virtual environment, use the commands: **'GUIenv\scripts\activate'** or **'deactivate'**. Once
activated, the virtual environment will change the (terminal) prompt from (PS) to (GUIenv).

After starting the virtual environment, EasyGUI can be installed with the command:  
**'python -m pip install easygui'**.  Subsequently the installation can be verified with the command: 
**'python -m pip show easygui'**.   




## File List
**plus_minus.py** - an example of responding to button clicks and updating dialog text.  
**simple_boxes.py** - an example illustrating basic 'easygui' usage.  
**TKinter_grid.py** - an example illustrating tkinter usage with '.grid' and '.pack'.  
**TKinter_test.py** - an example illustrating basic 'tkinter' with '.place' and '.pack'.  

 
 

