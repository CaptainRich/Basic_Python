# This routine illustrates a number of th built-in string operations.

# The 'title' method capitalizes the first character of each word in the string
s1 = "This is a very boring string, but it does have 1one complication."
s2 = "alphaonly"
s3 = "123456"

print( " " )
print( "The string 's1' is: ", s1 )
print( "The string 's2' is: ", s2 )
print( "The string 's3' is: ", s3 )

print( " " )
print( "The 'title()' method: ", s1.title() )
print( "The 'upper()' method: ", s1.upper() )
print( "The 'lower()' method: ", s1.lower() )
print( "The 'swapcase()' method: ", s1.swapcase() )

# See if the string 's1' is alpha-numeric.  I isn't because of the spaces.
print( " " )
print( "The 'isalnum()' method for 's1': ", s1.isalnum() )
print( "The 'isalpha()' method for 's2': ", s2.isalpha() )
print( "The 'isdigit()' method for 's3': ", s3.isdigit() )

# Split the 's1' string (into a list), using the "space" as the delimiter
s1List = s1.split( " " )
print( " " )
print( "After splitting 's1' into 's1List': ", s1List )
s1Join = "_".join( s1List )
print( "After rejoining the 's1List' into 's1Join': ", s1Join )

# Implement 'find' and 'replace'
print( " " )
print( "The index for the word 'boring' in 's1' should be 15: ", s1.find( 'boring' ) )
print( "Replacing 'boring' with 'exciting' in 's1': ", s1.replace( 'boring', 'exciting' ) )

# A few 'slice' examples
print( " ")
print( "A few 'slice' examples." )
print( "The 'slice[6:9] of 's1list: ", s1List[6:9] )
print( "The reverse of 's1list': ", s1List[::-1] )
