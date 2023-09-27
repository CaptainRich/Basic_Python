# Routine to list all of the files in a directory.
import os
import pathlib

###############################################################################################
# Function to list all of the files in a directory (the argument to the function).
def view_dir( path='.', sorted=False):
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
# Function to scan for a list of directories, with subdirectories indented by level.
def scan_directory( path, num_blanks ):
    blanks = num_blanks
    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir():
                # Print the directory name, then scan it.
                print( ' '*blanks, entry.name )
                sub_path = path + '/' + entry.name    # Build the path to the subdirectory
                blanks = blanks + 4                   # Indent each level an additional 4 spaces
                scan_directory( sub_path, blanks )


#################################################################################################
# Main

path   = input( "Enter the desired directory to list:"  )
answer = input( "Do you want a sorted list (Y or N)?" )

sorted = False
if( answer.upper() == 'Y' ):
    sorted = True
    

view_dir( path, sorted )

# Now try the os.scandir function
print( '=================================================================\n' )
num_blanks = 2
scan_directory( path, num_blanks )

# Now use the 'pathlib' module to report on the 'readme.md' file.  Note that
# 'pathlib' must be imported above.

md_file_path = pathlib.Path( '/python_work/basic_python' )
md_file_path = md_file_path / 'readme.md'                       # append the filename
print( " " )
print( 'The file path to the "readme.md" file is: ', md_file_path )

# Check if this is an 'absolute' path
print( 'Is this path "absolute"? ', md_file_path.is_absolute() )

# Try to resolve the relative path into an absolute path
abs_file_path = md_file_path.resolve()
print( 'The resolved absolute path is: ', abs_file_path )

# Does the 'md' file exist
print( 'Existence of the "md" file is: ', md_file_path.exists() )

# Does the path point to a file or a directory?
if( md_file_path.is_file() ):
    print( 'The path points to a file.' )
elif( md_file_path.is_dir() ):
    print( 'The path points to a directory.' )
else:
    print( 'The path points to neither a file or a directory???' )

# Print the last component of the pathname.
print( 'The last component of the path is: ', md_file_path.name )

print( 'The "parent" of the last path component is: ', md_file_path.parent )







