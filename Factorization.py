# This routine factors an integer value

import sys

try:
    int_value = int( input( "Enter an integer value to be factored: " ) )
except ValueError:
    #print( "Invalid entry made, need an integer." )
    sys.exit( "Invalid entry made, need an integer." )

# Make sure the value is an integer
range_value = abs( int_value ) 

# Check each integer less than 'int_value' for even divisibility.
for i in range( 1, range_value+1 ):
    if not( range_value % i ):
        print( f"{i} is a factor of {int_value}" )

