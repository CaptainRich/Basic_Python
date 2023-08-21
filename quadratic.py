# Quadratic equation solver.
# This routine solves for the roots (x) of the equation:
# ax^2 + bx + c = 0

import math      # import

####################################################################################################
# Define the function to solve for 'real' roots of the quadratic equation
def real_roots( a, b, c, temp ):
    """This function solves for the 'real' roots of a quadratic equation."""
    root1 = ( -b + math.sqrt(temp) ) / (2.0 * a )
    root2 = ( -b - math.sqrt(temp) ) / (2.0 * a )
    print( 'The real roots of %dx^2 + %dx + %d are:' % (a, b, c) )
    print( 'Root 1 is: ', root1 )
    print( 'Root 2 is: ', root2 )
    print( 'sqrt(b^2-4ac) is: ', temp )

####################################################################################################
# Define the function to solve for the 'complex' roots of the quadratic equation
def complex_roots( a, b, c, temp ):
    """This function solves for the 'complex' roots of a quadratic equation."""
    coefficient_of_i = math.sqrt( abs( temp ) )
    two_a            = 2.0 * a
    real_root1       = (-b/two_a)
    complex_root1    = coefficient_of_i / two_a
    root1            = complex( real_root1, complex_root1 )
    root2            = root1.conjugate()    

    print( 'The complex roots of %dx^2 + %dx + %d are:' % (a, b, c) )
    print( f"Root 1 is: {root1: .5f} " )
    print( f"Root 2 is: {root2: .5f} " )
    print( 'sqrt(b^2-4ac) is: ', temp )


####################################################################################################
# Main program starts here.
print( 'This program solves for the roots of a quadratic equation' )
print( 'of the form "ax^2 + bx + c = 0"' )

a = int( input( 'Enter the coefficient "a": ' ) )
b = int( input( 'Enter the coefficient "b": ' ) )
c = int( input( 'Enter the coefficient "c": ' ) )
print( " " )

temp = (b * b) - 4 * a * c

if( temp < 0 ):
    complex_roots( a, b, c, temp )
else:
    real_roots( a, b, c, temp )
  
