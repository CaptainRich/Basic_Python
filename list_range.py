# Define a list 
a = [ 1, 3, "Houston", "Texas" ]
print( "The 3rd item in the list is: ", a[2] )

# Define an empty list
b = []

if a:
    print( "The list 'a' is not empty." )
else:
    print( "The list 'a' is empty." )

if b:
    print( "The list 'b' is not empty." )
else:
    print( "The list 'b' is empty." )    

    b.append( "Denver" )
    b.append( "Colorado" )
    print( "Now 'b' contains: ", b )

    # Exploring "range"

    c = list( range( 1, 5 ) )
    print( "The list 'c' built with 'range' contains: ", c )
    
    d = list( range( 1, 15, 3 ) )   # step over the values by 3
    print( "The list 'd' built with 'range' contains: ", d )

    d.extend( [16, 19, 22] )
    print( "The list 'd' contains: ", d )