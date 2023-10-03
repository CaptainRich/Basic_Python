# $`\textcolor{blue}{\text{Python Basics - PDF Work}}`$
A collection of Python (.py) files illustrationg  Python concepts in dealing 
with PDF files.
Richard Ay (September 2023, *updated October 2023*)

## $`\textcolor{blue}{\text{Table of Contents}}`$  
* [Setup](#setup)
* [Envirionment](#environment)
* [File List](#file-list)



## Setup
Refer to the main 'readme.md' in the directory above.  This 'readme.md' contains additional
information in setting up the 'virtual environment' and running the scripts in this
subdirectory. 

## Environment
To utilize these scripts, a virtual environment is created so that the installation of PyPDF2 remains
local to this subdirectory, and does not affect the rest of the machine.

The virtual environment can be setup using the command: 
**'python -m venv "PDFenv" --upgrade-deps --prompt="PDFenv"'**

To start/stop the virtual environment, use the commands: **'PDFenv\scripts\activate'** or **'deactivate'**. Once
activated, the virtual environment will change the (terminal) prompt from (PS) to (PDFenv).

After starting the virtual environment, PyPDF2 can be installed with the command:  
**'python -m pip install PyPDF2'**.  Subsequently the installation can be verified with the command: 
**'python -m pip show PyPDF2'**.

## File List
**PDF_Reader.py** - a routine illustrating accessing information from a PDF file.  This routine accesses
'Pride_and_Prejudice.pdf' and creates 'Pride_and_Prejudice.txt' as an output file.

