""" A script illustrating event (button click) processing."""

import tkinter as tk

##############################################################################
# Worker Functions to act on button-clicks.  These functions are tied to the 
# buttons thru the "command" option when the button is created (below).

def increase():                         # Function to increment the count
    count = int( lbl_count["text"] )    # Get the current count (value)
    lbl_count["text"] = f"{count+1}"



def decrease():                         # Function to decrement the count
    count = int( lbl_count["text"] )    # Get the current count (value)
    lbl_count["text"] = f"{count-1}"

#############################################################################

window = tk.Tk()

# Configure the dialog as 1 row of 3 columns.
window.rowconfigure( 0, weight=1, minsize=50 )   # Row 0, resize, minimum size is 50 pixels
window.columnconfigure( [0, 1, 2], weight=1, minsize=50 ) # All three columns, resize, minimum is 50

# Assign the "decrement" button to the main window, but position it in the first row, first column,
# with 'sticky' used to fill the grid cell in both directions.
btn_decrease = tk.Button( master=window, text="-", command=decrease )
btn_decrease.grid( row=0, column=0, sticky="nsew" )

# Assign the "increment" button to the main window, but position it in the first row, third column,
# with 'sticky' used to fill the grid cell in both directions.
btn_increase = tk.Button( master=window, text="+", command=increase )
btn_increase.grid( row=0, column=2, sticky="nsew" )

# Setup the 'label', which will report the cumulative value of the button clicks. Position the label
# in the first row, column 2.
lbl_count = tk.Label( master=window, text="0" )
lbl_count.grid( row=0, column=1 )


window.mainloop()           #Start the 'event' loop
