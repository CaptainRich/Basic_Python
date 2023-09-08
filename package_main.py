# Main function illustrating 'package' usage.

import package_sample.math as ps_math           # Rename to make usage typing shorter
import package_sample.string as ps_string

# Get the length and width from the user
length = int( input( "Enter the length of the rectangle: " ) )
width  = int( input( "Enter the width of the rectangle: " ) )

area = ps_math.area( length, width )

# Build the output string
print( ps_string.shout( length, width, area ) ) 
