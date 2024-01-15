# $`\textcolor{blue}{\text{Python Basics - 'Rich' Work}}`$
The files and scripts in this directory illustrate the usage of
the 'rich' package.  
Richard Ay (January 2024)

## $`\textcolor{blue}{\text{Table of Contents}}`$  
* [Setup](#setup)
* [Envirionment](#environment)
* [Technologies and References](#technologies-and-references)
* [File List](#file-list)



## Setup
Refer to the main 'readme.md' in the directory above.  This 'readme.md' contains additional
information in setting up the 'virtual environment' and running the scripts in this
subdirectory.   

## Environment
To utilize these scripts, a virtual environment is created so that the installation of NumPY remains
local to this subdirectory, and does not affect the rest of the machine.

The virtual environment can be setup using the command: 
**'python -m venv "RichTest" --upgrade-deps --prompt="RichTest"'**

To start/stop the virtual environment, use the commands: **'RichTest\scripts\activate'** or **'deactivate'**. Once
activated, the virtual environment will change the (terminal) prompt from (PS) to (RichTest).

After starting the virtual environment, the 'Rich' package can be installed with the command:  
**'python -m pip install rich'**.  Subsequently the installation can be verified with the command: 
**'python -m pip show rich'**.   

## Technologies and References
- The scripts in this directory utilize the 'rich package' and a virtual environment.  
- The reference for these scripts is:  https://realpython.com/python-rich-package.


## File List
**animation_status.py** - an example illustrating animated wait icons and status bars.    
**crypto_data.json** - a sample data set to illustrate dynamic table updating.   
**live_table.py** - an example of a dynamic table (live updating).  
**tables.py** - an example of setting up a static table to display data.  

 
 

