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

PyPDF2 can be installed with the command:  'python -m pip install PyPDF2'.  Subsequently the installation
can be verified with the command: 'python -m pip show PyPDF2'.

## File List
**animal_classes.py** - a routine illustrating 'class' definition and usage.  
**capitals_dictionary.py** - a routine to quiz the user on state capitals, using a dictionary.  
**dictionaries.py** - a routine to illustrate the 'dictionary' data structure and its usage, as well as 'enumerate'.  
**dir_list.py**  - a routine to list the files and directories in a specified directory, and utilize the 'pathlib' module.   
**Factorization.py** - a routine to display all the factors of an integer value, implemented 'try', 'except' and 'sys.exit()' on error  
**fibonacci.py** - a routine to generate a fibonacci series up to 100    
**floating_ops.py** - a routine illustrating floating point operations and rounding  
**hello_world.py** - the infamous 'hello world' program  
**list_range.py** - a set of examples illustrating lists and ranges  
**multiplication_table.py** - a routine to generate the multiplication tables up to 15  
**number_ops.py** - a routine illustrating various number operations, conversions, and formatting   
**package_main.py** - a routine illustrating package usage, uses \package_sample subdirectory   
**poem_generator.py** - a routine to construct a poem from a list of words  
**quadratic.py** - a routine to solve the quadratic equation (for real or complex roots), based on user input of the a, b, c coefficients  
**sticks.py** - a routine generating the "pick up sticks" game  
**string_concatenation.py** - a routine illustrating various string manipulations  
**string_ops.py** - a routine illustrating built-in string methods  
**student_grades.py** - a program evaluating pass/fail student courses, illustrating lists, dictionaries, and loops  
**Temperature_Conversions.py** - a  routine to convert temperatures between Farenheight and Celsius  
**tuples_sets.py** - a routine illustrating the usage of tuples and sets  
**university_stats.py** - a program to determine the totals, means, and medians from a list of university lists
**User_Input_loops.py** - a routine illustrating the various looping methods  

**CSV-Work\csv-write-read.py** - a routine to write, then read a CSV file of numbers, and compute the average of each row. Also illustrates 'enumerate' and math operations for the average.  
**CSV-Work\high-scores.py** - a routine to read a CSV file of 'names & scores' and summarize the data to a new CSV file such that only a person's highest score is reported.

