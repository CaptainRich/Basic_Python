# Define a "tuple", note just commas, no brackets or braces
tupleA = ( "hickory", "dicker", "dock", "goes", "the", "clock" )
len_tupleA = len( tupleA )
print( f"The length of 'tupleA' is {len_tupleA}" )
print( "tupleA contains: ", tupleA )
print( "Index 2 of tupleA is: ", tupleA[2] )

print( " " )
print( "Looping over tupleA yields: " )
for x in tupleA:
    print( f"tupleA element is: ", x )

# Unpack the tuple into individual variables 
v1, v2, v3, v4, v5, v6 = tupleA
print( "Unpacking tupleA into variables (v1 to v6) yields: ", v1, v2, v3, v4, v5, v6 )

# Display the "data type" of tupleA and v6
print( " " )
print( "The data type of tupleA is: ", type(tupleA) )
print( "The data type of variable v6 is ", type(v6) )


# Define a couple of "sets" and illustrate usage.
print( " " )
setA = set( 'abracadabra' )
setB = set( 'alacazam' )
print( "Unique letters in setA are: ", setA )
print( "Unique letters in setB are: ", setB )

print( " " )
print( "Letters in setA but not in setB are: ", setA-setB )
print( "Letters in either setA or setB are: ", setA | setB )
print( "Letters in both setA and setB are: ", setA & setB )
print( "Letters in setA or setB but not both are: ", setA ^ setB )

# Pushing and Popping a set
print( " " )
setA.add( 'q') 
print( "Added 'q' to setA yields: ", setA )
setA.pop()
print( "Just popped first element from setA yields: ", setA )

