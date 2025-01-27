# $`\textcolor{blue}{\text{Python Basics - Asynchronous Work}}`$
A collection of Python (.py) files illustrating Python concepts in dealing 
with asynchronous operations.  
Richard Ay (January 2024)

## $`\textcolor{blue}{\text{Table of Contents}}`$  
* [Setup](#setup)
* [Envirionment](#environment)
* [File List](#file-list)



## Setup
  

## Environment
To utilize these scripts, a virtual environment is created so that the installation of aiofiles remains
local to this subdirectory, and does not affect the rest of the machine.

The virtual environment can be setup using the command: 
**'python -m venv "ASYNCenv" --upgrade-deps --prompt="ASYNCenv"'**

To start/stop the virtual environment, use the commands: **'ASYNCenv\scripts\activate'** or **'deactivate'**. Once
activated, the virtual environment will change the (terminal) prompt from (PS) to (GUIenv).

After starting the virtual environment, EasyGUI can be installed with the command:  
**'python -m pip install aiofiles'**.  Subsequently the installation can be verified with the command: 
**'python -m pip show aiofiles'**.   




## File List
**context_managers.py** - an example of a context manager, using aiofiles (this is why the VENV is used).  
**CoRoutine.py** - an example of 'coroutines'.  
**data.txt** - the data file used by the 'context_manager.py' script.  
**Event_Loop.py** - an example of the asynchronous event loop'.  
**future.py** - an example illustrating the 'future' concept'.  
**generator.py** - an example of an asynchronous generator'.  
**tasks.py** - an example illustrating asynchronous coroutine tasks'.  

 
 

