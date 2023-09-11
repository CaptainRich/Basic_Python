# Routine to list all of the files in a directory.
import os

###############################################################################################
# Function to list all of the files in a directory (the argument to the function).
def view_dir( path='.', sorted=True):
    names = os.listdir(path)   # Get a list of all files/directories in 'path'

    # Review/update the list so everything is lower case
    for index, name in enumerate( names ):
        names[index] = name.lower()

    if sorted:
        names.sort()               # Sort the list, in place

    # Display the list of files/directories.
    for name in names:
        print( name, '\n', end = ' ' )

#################################################################################################
# Main

path   = input( "Enter the desired directory to list:"  )
answer = input( "Do you want a sorted list (Y or N)?" )

if( answer.upper() == 'Y' ):
    sorted = True
else:
    sorted = False

view_dir( path, sorted )
