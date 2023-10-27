"""A routine illustrating matrix manipulation."""

import numpy as np

#############################################################################################
# Main

# Define a 3*3 (2D) matrix, literally
m2d = np.array( [ [1,2,3], [4,5,6], [7,8,9] ] )  # Three rows of 3 columns
n2d = np.arange( 11, 20 )
n2d = n2d.reshape( 3, 3 )
print( "\nThe m2d array is:\n", m2d )
print( "\nThe matrix n2d is:\n", n2d )

print( "\nThe middle value of the middle row is: ", m2d[1,1] )

# Define a 3x3x2 (3D) matrix, literally.
m3d = np.array ([                  
    [ [1,2,3], [4,5,6] ],         # Row 1 has 2 columns, and 3 depths. So 1 is in the 1st plane,
    [ [7,8,9], [10,11,12] ],      # 2 is in the 2nd plane, and 3 is in the 3rd plane.  4 is in 
    [ [13,14,15], [16,17,18] ]    # row 1, column 2, 1st plane, 5 is row 1, column 2, 2nd plane, 
])
print( "\nThe m3d array is:\n", m3d )
print( "\nThe shape of m3d is: ", m3d.shape )
print( "\nThe middle value of the middle row of the 2nd plane is: ", m3d[1,1, 1] )

m3d = m3d * 2
print( "\nm3d times 2 is:\n", m3d )

# Multiply m2d by n2d
mn2d = np.matmul( m2d, n2d )
print( "\nThe result of multiplying m2d*n2d is:\n" )
print( mn2d )
