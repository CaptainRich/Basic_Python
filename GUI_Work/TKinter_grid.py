"""A script illustrating the use of tkinter.grid. """

import tkinter as tk


############################################################

window = tk.Tk()  

# Define a 3x3 grid
for i in range(3):
    # Weight=1 means the column/row will grow as the window is resized.
    # Size is in pixels
    window.columnconfigure( i, weight=1, minsize=75 )
    window.rowconfigure( i, weight=1, minsize=50 )

    for j in range( 3 ):
        frame = tk.Frame( master=window, relief=tk.RAISED, borderwidth=1 )
        frame.grid( row=i, column=j, padx=5, pady=5 )

        label = tk.Label( master=frame, text=f"Row {i}\nColumn {j}" )
        label.pack( padx=5, pady=5 )

window.mainloop()