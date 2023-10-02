# A routine to read a CSV file of players and scores from multiple games, then output
# a new file with the player's name and hightest score.  The CSV file is defined as
# a 'dictionary', where the field names are: 'name' and 'score'.


import pathlib             # Needed for directory operations
import csv                 # Needed for CSV operations


####################################################################################
def get_scores( current_path ):
    """This function reads the CSV file of players and their scores."""

    high_scores = {}

    # Setup the input file name
    input_path = current_path / 'scores.csv'
    print( 'The input file path is: ', input_path )

    if( not input_path.exists() ):
        print( 'The input file "scores.csv" does not exist.' )
        exit()

    # Open and read all of the players and multiple scores.
    with input_path.open( mode='r', encoding='utf-8', newline='' ) as file:
        reader = csv.DictReader( file )

        field_names = reader.fieldnames
        print( "\nThe file's field names are: ", field_names )

        for row in reader:
            # Each row is a dictionary, where the keys are the field names.
            # Build a new dictionary, where the player names are the keys and
            # the value is the hightest score.  Player names (keys) only exist
            # once in the new dictionary (high_scores).

            print( 'Next row from CSV file is: ', row )

            key   = row["name"]
            value = int( row["score"] )

            # See if this key already exists in 'high_scores'
            if( key in high_scores ):
                # The key (player name) already exists, compare the scores and
                # keep (store) the highest one.
                stored_value = high_scores[key]
                if( value > stored_value ):
                    high_scores[key] = value   # Store the new (higher) value.

            else:
                # The key (player name) doesn't exist, add it and the value.
                high_scores[key] = value

    return high_scores, field_names   # Return a 'tuple'


####################################################################################
def store_data( current_path, high_scores, field_names ):
    """This function saves the summarized data to a new CSV file."""

     # Setup the output file name
    output_path = current_path / 'high_scores.csv'
    print( 'The output file path is: ', output_path )

    # Open the output file and write "numbers" in CSV format.
    # The null newline is because the CSV write includes a newline character.
    # This will delete the output file if it already exists.
    with output_path.open( mode='w', encoding='utf-8', newline='' ) as file:
        writer = csv.DictWriter( file, field_names )

        writer.writeheader()                 # This writes the field names.

        # Loop over the 'high_scores' dictionary and build the list of
        # output dictionaries, with the field names
        for name in high_scores:
            new_row_dict = {field_names[0]: name, field_names[1]: high_scores[name] }
            writer.writerow( new_row_dict )


####################################################################################
# Main
"""Main driver routine to read the raw CSV file, process the data, then write a new
 CSV with data summarization."""

# Setup the path to the current working directory, where the input and output files
# will be accessed.

# Obtain the current working directory, and setup the output file.
current_path = pathlib.Path.cwd()
print( '\nThe current working directory is: ', current_path )

# Read all of the data from the input CSV file into a 'dictionary'.  Vales are returned
# as a 'tuple'.
high_scores, field_names = get_scores( current_path )

# Optionally dump out the data just read.
answer = input( '\nDisplay the summarized score data? (Y or N): ' )
if( answer == 'Y'  or  answer == 'y' ):
    print( '\nThe field names from the CSV file are: ', field_names )
    for name in high_scores:
        print( f"For player {name}, the high score is {high_scores[name]}" )   


# Now write this summary data to a new CSV file.
store_data( current_path, high_scores, field_names )
print( "\n" )

