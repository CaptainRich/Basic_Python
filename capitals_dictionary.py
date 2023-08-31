# This routine prompts the user with a US State name and asks
# the user what the associated capital is.

import random     # Needed to randomly select a state.

# Define the dictionary (of States and their Capitals).
capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'madison',
    'Wyoming': 'Cheyenne',
}

####################################################################################
# This function randomly selects a State and its Capital.
def select_state():
    # Here the dictionary is converted to a 'list' for 'choice'.  We use '.items()' to
    # return both the key and its value as a tuple.
    state_and_capital = random.choice( list(capitals_dict.items() ) )
    return( state_and_capital )


######################################################################################
# Main program

# To start, randomly pick a State -break out the tuple into two separate variables.
state, capital = select_state()


print( " " )

# Start a loop to request user input until the correct response (or 'exit' is entered).
match = False
while not match:

    # Prompt the user to enter the Capital of the selected State.
    user_capital = input( f"Enter the capital city of {state}: " )

    # Make sure both the user's entry and the dictionary value are upper case for comparison
    dictionary_capital = capital.upper()
    user_input_capital = user_capital.upper()

    # Check if the user wants to quit. If so, report the state and its capital.
    if user_input_capital == "EXIT":
        print( f"The capital of {state} is {capital}.\n" )
        break

    elif dictionary_capital == user_input_capital:
        print( "Correct answer!\n" )
        match = True
        break

    else:
        print( "\nSorry that is incorrect, try again or 'exit' to end." )
