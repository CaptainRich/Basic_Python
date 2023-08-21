# This routine exercises a number of floating point operations.
import math

# Basic floating point rounding
floating1 = float( input( "Enter the first floating point number with 4 decimals: " ) )
floating2 = float( input( "Enter the second floating point number with 4 decimals: " ) )

print( "The first value rounded to three decimal places is: ", round( floating1, 3 ) )
print( "The second value rounded to three decimal places is: ", round( floating2, 3 ) )
print( "The absolute value of the second number is: ", abs( floating2 ) )

# Ask for two more values and determine if their difference is integral (an integer)
print( " " )
print( "Test for an integral difference: " )
floating3 = float( input( "Enter a 3rd floating point value: " ) )
floating4 = float( input( "Enter a 4th floating point value: " ) )
diff = floating3 - floating4
status = diff.is_integer()
print( f"The difference is:  {diff: .4f}" )
print( "This difference is an integer: ", status )

# Compute 'pi' and display the value to 10 places
pi = 4.0 * math.atan( 1.0 )
print( f"The computed value of 'PI' is: {pi: .10f}" )
