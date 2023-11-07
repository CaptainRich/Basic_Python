""" A short script to illustrate the use of the Tkinter GUI."""

import tkinter as tk

##########################################################
def get_response():
    name = entry.get()
    print( 'You entered: ', name )

############################################################

window = tk.Tk()            # Create the dialog window
label  = tk.Label( text='Enter your name:', bg='black', fg='yellow' )
label.pack()                # Put the label on the dialog
entry  = tk.Entry()
entry.pack()                # Put the text entry box on the dialog


submit_btn = tk.Button( text='Submit', command=get_response )
submit_btn.pack()


window.mainloop()

