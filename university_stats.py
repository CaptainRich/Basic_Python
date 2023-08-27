# A program to develop statistics from a list of lists.

# The data in the following lists consists of: name, enrolled students, tuition.
universities = [
    [ 'California Institute of Technology', 2175, 37704 ],
    [ 'Harvard', 19627, 39849 ],
    [ 'MIT', 10566, 40732 ],
    [ 'Princeton', 7802, 37000 ],
    [ 'Rice', 5879, 35551 ],
    [ 'Stanford', 19535, 40569 ],
    [ 'Yale', 11701, 40500 ]
]

####################################################################################################
# This function returns a list of enrollment values and a list of tuition values.
def enrollment_stats( universities ):
    enrollments = []
    tuitions    = []

    # Loop over the universities and build (store) the values for enrollment and tuition
    numUniversities = len(universities)

    #for i in range( numUniversities ):
    for university in universities:
        enrollments.append( university[1] )
        tuitions.append( university[2] )

    # Return the new lists in a tuple
    return( enrollments, tuitions )

####################################################################################################
# This function determines the mean (average) of a list of numeric values
def list_mean( values ):
    mean       = sum(values) / len(values)

    return( mean )

####################################################################################################
# This function determines the median (middle value) of a list of numeric values
def list_median( values ):
    num_values = len(values)

    values.sort()      # this sorts the list in ascending order, in-place
    median_index = int( num_values / 2 )     # This gives the index of the median if 'num_values' is odd

    # If there are an odd number of values, the median is the middle value.  If there are an even number
    # of values, average the middle two values.

    if( (len(values) % 2) == 1 ):
        # There is an odd number of values, return the middle value
        return( values[ int( num_values / 2 ) ] )
               
    else:
        # There is an even number of values. Get the high/low index values, then average the
        # numeric values at those two locations.
        high_index = int( num_values / 2 )
        low_index  = high_index - 1
        return( (values[low_index] + values[high_index] ) / 2 )




####################################################################################################
# This is the main program to determine the desired statistics.

# Obtain the lists of enrollments and tuitions
enrollments, tuitions = enrollment_stats( universities )
print( " " )
print( "The university enrollments are: ", enrollments )
print( "The university tuitions are: ", tuitions )

# Determine the total students and the total tuition.
total_students = sum(enrollments)
total_tuition  = sum(tuitions)

print( " " )
print( '***************************************************' )
print( f'Total Students is:      {total_students: ,}' )
print( f'Total Tuition is   ($): {total_tuition: ,.2f}' )

# Determine the student mean and median
student_mean   = list_mean( enrollments )
student_median = list_median( enrollments )
print( " " )
print( f"Student Mean is       : {student_mean: ,.2f}" )
print( f"Student Median is     : {student_median: ,}" )

# Determine the tuition mean and median
tuition_mean   = list_mean( tuitions )
tuition_median = list_median( tuitions )
print( " " )
print( f"Tuitions Mean is   ($): {tuition_mean: ,.2f}" )
print( f"Tuitions Median is ($): {tuition_median: ,.2f}" )

print( '***************************************************' )
print( " " )
