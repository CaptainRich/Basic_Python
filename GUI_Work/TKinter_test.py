""" A short script to illustrate the use of the Tkinter GUI."""

import tkinter as tk

##########################################################
def get_response():
    name = entry.get()
    print( 'You entered: ', name )

############################################################

window = tk.Tk()            # Create the dialog window
frame1 = tk.Frame( master=window, width=200, height=150 )         # Create a frame to hold the widgets
frame1.pack(  )

label  = tk.Label( master=frame1, text='Enter your name:', bg='black', fg='yellow' )
label.place( x=35, y=20 )               # Put the label on the dialog, location is in pixels
entry  = tk.Entry( master=frame1 )
entry.place( x=20, y=50 )                 # Put the text entry box on the dialog


submit_btn = tk.Button(  master=frame1, text='Submit', relief=tk.RAISED, command=get_response )
submit_btn.place( x=55, y=80 )



window.mainloop()

