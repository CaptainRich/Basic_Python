# $`\textcolor{blue}{\text{Python Basics - Math Work}}`$
A collection of Python (.py) files illustrating  Python concepts in dealing 
with the a matricies and plotting.  
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
**'python -m venv "MATHenv" --upgrade-deps --prompt="MATHenv"'**

To start/stop the virtual environment, use the commands: **'MATHenv\scripts\activate'** or **'deactivate'**. Once
activated, the virtual environment will change the (terminal) prompt from (PS) to (MATHenv).

After starting the virtual environment, NumPY can be installed with the command:  
**'python -m pip install numpy'**.  Subsequently the installation can be verified with the command: 
**'python -m pip show numpy'**.   

Additionally, the plotting library (matplotlib) should be installed:
**'python -m pip install matplotlib'**.  Subsequently the installation can be verified with the command: 
**'python -m pip show matplotlib'**. 


## File List
**expense_plots.py** - an example illustrating basic plotting (graphs, bars) concepts.  
**matrix_math.py** - an example illustrating basic matrix manipulations'.    

 
 

