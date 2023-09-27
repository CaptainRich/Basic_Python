# Routine to write a CSV file then read its contents back.

import pathlib             # Needed for directory operations
import csv                 # Needed for CSV operations

####################################################################################
# Main

# Define the list of lists (of numbers)
numbers = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# Obtain the current working directory, adn setup the output file.
current_path = pathlib.Path.cwd()
print( '\nThe current working directory is: ', current_path )

outfile = current_path / 'numbers.csv'
print( 'The output file is: ', outfile )

# If the output file exists in the directory, delete it.
if( outfile.exists() ):
    outfile.unlink()

    if( not outfile.exists() ):
        print( 'Just deleted the output file' )

# Open the output file and write "numbers" in CSV format.
# The null newline is because the CSV write includes a newline character.
with outfile.open( mode='w', encoding='utf-8', newline='' ) as file:
    writer = csv.writer( file )

    # This 'for loop' could be eliminated if 'writer.writerows' was used.
    for number_row in numbers:
        writer.writerow( number_row )

# Once the scope of the above 'with' ends, the output file is automatically closed.
# Now open the new CSV file, read its contents and report the average value of each row.

new_numbers = []                 # Define an empty list

with outfile.open( mode='r', encoding='utf-8', newline='' ) as file:
    reader = csv.reader( file )

    for row in reader:
        # Need to convert the 'text' items to integers
        int_row = [ int(value) for value in row ]

        # Now append the row to the list of rows (lists).
        new_numbers.append( int_row )


# As above, once the scope of 'with' ends, the input file is closed.
# Now loop over the rows in the list, compute their average and report.
for index, row in enumerate( new_numbers ):
    average = sum(row) / len(row)
    print( 'Row ', index, ' is ', row, ' whose average value is: ', average )



    

