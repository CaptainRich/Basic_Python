# Test 'user interactive" input
prompt = "What day of the week is it? "
user_input = input( prompt )
print( "you answered: " + user_input )

# Capitalize the user input
user_input_caps = user_input.upper()
print( "capitalized response: " + user_input_caps )

# Get the first letter of the response
first_letter = user_input[0:1]  # this is a "slice".
print( "the first letter of the response is: " + first_letter )


# Setup an infinite loop, until the user exits.
while True:
    n = int( input( "Input a positive integer, or zero to exit:" ) )  

    if n < 0:
        continue     # ignore negative values, go back to the beginning of the loop

    elif n == 0:
        break        # this is the "I want to exit input"

    print( "The square of your input is: ", n * n )

print( "Exiting loop on zero." ) 

# Loop using the 'for' statement
for i in range( 0, 5 ):
    print( "A value in the range from 0 to 5 is: ", i )
else:
    print( "The range is exhausted, bye." )
       
