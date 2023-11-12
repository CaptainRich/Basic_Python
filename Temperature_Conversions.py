"""A simple temperature converter."""

# Setup a temperature conversion program.
flag_str = input( "Enter 'F' for 'Farenheight' to 'Celsius', or 'C' for the reverse: " )
flag_str = flag_str.upper()


# Branch based on the input, note the ending colon here.
if( flag_str == 'F' ):
    print( "Farenheight to Celsius Conversion:" )
    tempF = float( input( "Enter the temperature in degrees F: " ) )
    tempC = ( tempF - 32.0 ) * 5.0 / 9.0
    print( "%.2f degF is %.2f degC" % (tempF, tempC) )

elif( flag_str == 'C' ):
    print( "Celsius to Farenheight Conversion:" )
    tempC = float( input( "Enter the temperature in degrees C: " ) )
    tempF = ( tempC * 9.0 / 5.0 ) + 32.0
    print( "%.2f degC is %.2f degF" % (tempC, tempF) )

else:
    print( "Sorry, the option you entered is not valid!" )
