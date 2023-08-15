# Ask for several numbers and perform mathmatical operations.
number1_str = input( "Enter the first numerical value as an integer: " )
number2_str = input( "Enter the second numerical value as a float: " )

number1 = int( number1_str )
number2 = float( number2_str )

sum_values = number1 + number2

print( "The sum of the input values is: " + str(sum_values) )
print( "The product of the input values is: " + str(number1 * number2) )

# Display the results using f-string and .format
output1 = f"The earlier sum was: {sum_values}"
output2 = "Once again the earlier sum was: {}".format(sum_values)

print( " " )
print( "Using f-string:" )
print( output1 )

print( " " )
print( "Using .format:" )
print( output2 )

# Find the starting position (index) of the word "sum" in the fist output.
index1 = output1.find("sum")
print( "The index of the word 'sum' in the f-string above is: " + str( index1 ) )
       
# An example 'while' loop
print( " " )
amount = float( input( "Enter the initial investment amount ($): " ) )
rate   = float( input( "Enter the yearly interest rate: " ) )
years  = float( input( "Enter the number of years for the investment: " ) )

final_value = 0.   # initialize
count       = 1

while count <= years:  # Note the ending colon
    final_value = amount + ( rate * amount )
    # Note the use of the numeric formatting in the following 'print' statement.
    print( "The final value after year %d is %.2f" % (count, final_value) )
    amount = final_value
    count  = count + 1

    
