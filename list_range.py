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

# Insert text between the two elements of 'b'
b.insert( 1, "(snowy)" )
print( "After insertion, 'b' now contains: ", b )

# Reverse the list elements in 'b'
b.reverse()
print( "After reversing, 'b' now contains: ", b )

# Exploring "range"

c = list( range( 1, 5 ) )
print( "The list 'c' built with 'range' contains: ", c )
    
d = list( range( 1, 15, 3 ) )   # step over the values by 3
print( "The list 'd' built with 'range' contains: ", d )

d.extend( [16, 19, 22] )
print( "The list 'd' contains: ", d )


# Example of list-compression, uses a "for clause"
e = list( range( 1, 6 ) )
f = [x ** 2 for x in e ]
print( " The original list 'e':", e )
print( " 'e' squared using list-compression, to 'f':", f )

# A random numeric list with various inquiries
g = [ 2, 16, 20, 36, 43 ]
sumG = sum( g )
minG = min( g )
maxG = max( g )
print( "The list 'g' contains: ", g )
print( f" The sum of these values is ", sumG, " the min value is ", minG, " the max value is ", maxG )
      