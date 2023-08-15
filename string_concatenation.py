# Define two strings
string1 = "abra"
string2 = "cadabra"

# Display the individual strings
print( "string 1 is: " + string1 )
print( "string 2 is: " + string2 )
magic_string = string1 + string2
print( "the combined string is: " + magic_string )

# Display the 5th character in 'magic_string'.  Note indexing starts at 0,
# so the 5th character is at index '4'.
print( "the 5th character of the string is: " + magic_string[4] )

# Report the length of the string, converting an 'int' to a 'string'.
magic_length = len(magic_string)
print( "combined string has a length of " + str(magic_length) )

# The last character in a string can be accessed using an index of '-1'
print( "the last character in the string is: " + magic_string[-1] )

# Characters 4, 5, 6 of the string. In the code below, the 'slice' starts
# at index 4, and runs up to, but not including index 7.
chars456 = magic_string[4:7]
print( "characters 4,5,6 are: " + chars456 )

# Capitalize the first character of the combined string.  Note, strings can't
# be changed so we must create a new string.
Capped_magic_string = "A" + magic_string[1:]
print( "capitalize the first character: " + Capped_magic_string )

# Display the string completely in capital letters.
print( "combined string in caps is: " + magic_string.upper() )

# See if the combined string starts with "AB". Note the conversion from 'bool'
# to 'string'.
print( "does the combined string start with 'AB'?: " +
       str(magic_string.startswith( "AB" )) )






