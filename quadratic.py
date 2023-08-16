# Quadratic equation solver.
# This routine solves for the roots (x) of the equation:
# ax^2 + bx + c = 0

import math      # import the 'math' module

print( 'This program solves for the roots of a quadratic equation' )
print( 'of the form "ax^2 + bx + c = 0"' )

a = int( input( 'Enter the coefficient "a": ' ) )
b = int( input( 'Enter the coefficient "b": ' ) )
c = int( input( 'Enter the coefficient "c": ' ) )

temp = (b * b) - 4 * a * c

if( temp < 0 ):
    print( 'Sorry, the roots of this quadratic are "imaginary".' )
else:
    root1 = ( -b + math.sqrt(temp) ) / (2.0 * a )
    root2 = ( -b - math.sqrt(temp) ) / (2.0 * a )
    print( 'The roots of %dx^2 + %dx + %d are:' % (a, b, c) )
    print( 'Root 1 is: ', root1 )
    print( 'Root 2 is: ', root2 )
    print( 'sqrt(b^2-4ac) is: ', temp )
