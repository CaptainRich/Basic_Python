# A dictionary in Python is similar to an object in Javascript, basically key:value pairs.

# A basic dictionary
data1 = { 'first':'John', 'last':'Smith', 'gender':'male' }
print( 'The entire dictionary is: ', data1 )
print( 'The last name using the key "last" is: ', data1['last'] )

# Add another key/value pair
data1['age'] = '35'
print( " " )
print( "Just added the 'age' key and value:")
print( 'The entire dictionary is: ', data1 )

# Change the age value
data1['age'] = '40'
print( 'The entire dictionary is: ', data1 )

# Reveal all of the keys in 'data1'
print( " " )
print( "The 'keys' in the dictionary are:" )
for x in data1:
    print( f"Key = {x}" )

print( "The key/value pairs in the dictionary are:" )
for x in data1.items():
    print( f"Key/Value = {x}" )

# Dump the data again, but this time include the sequence (index) value
print( " " )
print( "The key/value pairs (with sequence number starting with '1') in the dictionary are:" )
for i, j in enumerate( data1.items() , start=1 ):
    print( "Index %d key/value pair %s" % (i, j) )

