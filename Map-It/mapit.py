""" Map-It, a script to take an address and invoke Google Maps to
    display the location.  The address can be provided on the 
    commandline or in the Windows Clipboard. 
    
    Note: The import of 'pyperclip' requires the installation of
    'pyperclip'! This is why the associated code is commented out."""

import webbrowser
import sys
#import pyperclip

if len( sys.argv ) > 1:
    # Get the target address from the command line.  The 'join' function
    # will combine the address components, separating them with ' '.
    address = ' '.join( sys.argv[1:] )  

else:
    print( '\n You must specify an address on the command line.')
    exit()
    # Get the target address from the clipboard.
    #address = pyperclip.paste()

# Now fire off the webbrowser with the address.
webbrowser.open( 'https://www.google.com/maps/place/' + address )