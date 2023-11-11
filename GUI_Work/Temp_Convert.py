"""A temperature conversion script using Tkinter GUI features. """

import tkinter as tk

##########################################################################
# Worker functions to perform the actual temperature conversion.

def FtoC( in_value ):
    pass

def CtoF( in_value ):
    pass

def selection():
    # Determine which radio button was selected.
    option = str( selected.get() )
    print( "The selection was: ", option )


##########################################################################
# Main routine

window = tk.Tk()
window.title( "Temperature Converter" )
window.geometry("400x200+300+450")  # Width, Height, X position, Y position

# Configure the dialog as 3 rows.
# Row 0 will contain the radio buttons to select the direction of the conversion.
# Row 1 will contain the input and output labels.
# Row 2 will contain the input and output values (enter boxes)
# Row 3 will contain the 'go' button.
window.rowconfigure( [0, 1, 2, 3], weight=1, minsize=20 )   # Row 0, resize, minimum size is 100 pixels
window.columnconfigure( [0, 1], weight=1, minsize=200 )    # All three columns, resize, minimum is 50

# Setup the radio buttons and their location in the dialog
selected = tk.IntVar()
radio1   = tk.Radiobutton( window, text="Fahrenheit to Celsius", variable=selected, value=1 )
radio2   = tk.Radiobutton( window, text="Celsius to Fahrenheit", variable=selected, value=2 )

radio1.grid( row=0, column=0, sticky="ns" )
radio2.grid( row=0, column=1, sticky="ns" )

# Configure the (entry box) labels and their location in the dialog
label1  = tk.Label( window, text="Enter value to convert", fg='blue' )
label2  = tk.Label( window, text="Converted value is:", fg='blue' )

label1.grid( row=1, column=0, sticky="s" )
label2.grid( row=1, column=1, sticky="s" )


# Setup the entry boxes and their location in the dialog
entry1  = tk.Entry( window )
entry2  = tk.Entry( window )

entry1.grid( row=2, column=0, sticky="n" )
entry2.grid( row=2, column=1, sticky="n" )

# Setup the 'submit' button and its location in the dialog
submit_btn = tk.Button(  window, text='Submit', relief=tk.RAISED, command=selection )
submit_btn.grid( row=3, column=1, sticky='n' )



 # Invoke the 'event' loop
window.mainloop()                 
