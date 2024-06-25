# $`\textcolor{blue}{\text{Python Basics}}`$
A collection of Python (.py) files illustrationg basic Python concepts and operations 
to interact with Excel 
Richard Ay (August 2023, *updated June 2024*)

## $`\textcolor{blue}{\text{Table of Contents}}`$
* [Setup](#setup)
* [Environment](#environment)
* [Technologies and Imports](#Technologies-and-Imports)
* [References](#references)
* [File List](#file-list)




## Setup
There are two ways to use these small programs: (1) the Python IDLE or (2) VS Code.

For the Python IDLE, just start the IDLE (which opens a Python Shell), then select File/New
(which opens an Editor).  From the Editor, F5 will run the file with the output or 
diagnostics (tracebacks) appearing in the Shell.

For VS Code it is important to change the Terminal from "Git Bash" to "Power Shell".
Once in Power Shell, the command "python [filename].py will run the file with the 
output going to the terminal.  Note the suffix ".py" is required.

## Environment
A virtual environment is created so that the installation of openpyxl 
remains local to this subdirectory, and does not affect the rest of the machine.
This virtual environment is needed for xxxx, but not csv-write-read.py or 
high-scores.py.

The virtual environment can be setup using the command: 
**'python -m venv "ExcelEnv" --upgrade-deps --prompt="ExcelEnv"'**

To start/stop the virtual environment, use the commands: **'ExcelEnv\scripts\activate'** 
or **'deactivate'**. Once activated, the virtual environment will change the (terminal) 
prompt from (PS) to (ExcelEnv).

After starting the virtual environment, openpyxl can be installed 
with the commands:  
**'python -m pip install openpyxl==2.6.2'**  

Subsequently the installations can be verified with the command:   
**'python -m pip show openpyxl'**  

## Technologies and Imports
The following modules are necessary imports (imported in the .py files):  
- openpyxl  


## References
1. Python for You and Me, Kushal Das, Feb 17, 2021  
2. Python Basics: A practical Introduction to Python 3, David Amos, Dan Bader, 2022  
3. Python Ultimate Guide (web download, source unknown)  
4. Automate the Boring Stuff with Python, Al Sweigart, 2020



## File List

**csv-write-read.py** - a routine to write, then read a CSV file of numbers, and compute the average of each row. Also illustrates 'enumerate' and math operations for the average.  
**high-scores.py** - a routine to read a CSV file of 'names & scores' and summarize the data to a new CSV file such that only a person's highest score is reported.  

 
