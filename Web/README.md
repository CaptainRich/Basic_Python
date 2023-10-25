# $`\textcolor{blue}{\text{Python Basics - WEB Work}}`$
A collection of Python (.py) files illustrating  Python concepts in dealing 
with the WEB (Internet).  
Richard Ay (October 2023)

## $`\textcolor{blue}{\text{Table of Contents}}`$  
* [Setup](#setup)
* [Envirionment](#environment)
* [File List](#file-list)



## Setup
Refer to the main 'readme.md' in the directory above.  This 'readme.md' contains additional
information in setting up the 'virtual environment' and running the scripts in this
subdirectory.   

## Environment
To utilize these scripts, a virtual environment is created so that the installation of BeautifulSoup 
and MechanicalSoup remain local to this subdirectory, and does not affect the rest of the machine.

The virtual environment can be setup using the command: 
**'python -m venv "WEBenv" --upgrade-deps --prompt="WEBenv"'**

To start/stop the virtual environment, use the commands: **'WEBenv\scripts\activate'** or **'deactivate'**. Once
activated, the virtual environment will change the (terminal) prompt from (PS) to (WEBenv).

After starting the virtual environment, Beautifulsoup4 can be installed with the command:  
**'python -m pip install beautifulsoup4'**.  Subsequently the installation can be verified with the command: 
**'python -m pip show beautifulsoup4'**.  

For interacting with web pages, Mechanicalsoup should be installed, using the command:
**python -m pip install mechanicalsoup**.

## File List
**page_read.py** - an example of reading a webpage using 'beautifulsoup'.   
**form_submit.py** - an example of interacting with a web form using 'mechanicalsoup'.  
**scrape_updating.py** - an example of accessing a web page element that is constantly updated.
 
 

