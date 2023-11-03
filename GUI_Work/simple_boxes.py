"""A routine illustrating simple dialog boxes with 'easygui'.  There are additional types
   of boxes in the'easygui' library.  For complete details refer to the 'easygui' documnetation
   at: https://easygui.readthedocs.io/en/latest/api.html
"""

import easygui as gui

rtn = gui.msgbox( msg="This is the message box content.", title="This is the message box title.", ok_button="Click Here" )
print( "The returned value from the msgbox is: ", rtn )

rtn = gui.buttonbox(
    msg     = "This s the button box content.", 
    title   = "This is the button box title.",
    choices = ( "red", "yellow", "blue" )
)
print( "The returned value from the button box is: ", rtn )

possible_colors = ( "red", "yellow", "blue" )
rtn = gui.indexbox(
    msg     = "This s the index box content.", 
    title   = "This is the index box title.",
    choices = ( possible_colors )
)
print( "The returned value from the index box is: ", rtn )

rtn = gui.enterbox(
    msg     = "Enter your favorite color:", 
    title   = "This is the enter box title."
)
print( "The returned value from the enter box is: ", rtn )


rtn = gui.fileopenbox(
    title   = "Select the target file:"
)
print( "The returned value (file path) from the fileopen box is: ", rtn )


rtn = gui.diropenbox(
    title   = "Select the target directory:"
)
print( "The returned value (directory path) from the diropen box is: ", rtn )


rtn = gui.filesavebox(
    msg       = "Select the target directory to save to:",
    title     = "File Save Dialog",
    default   = "default_file_name.txt",
    filetypes = "*.txt"
)
print( "The returned value (file path) from the filesave box is: ", rtn )