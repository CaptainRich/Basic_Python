""" A script illustrating Conway's Game of Life. """

import random, time, copy       # Necessary standard imports

WIDTH  = 60       # Define the size of the game grid
HEIGHT = 20

# Create a 'list' of 'lists' to represent the game grid cells.
nextCells = []

for x in range(WIDTH):
    column = []     # Create a new column for the grid

    # Loop over the cells in a column and randomly set the cells.
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append( '#' )  # Add a 'living' cell
        else:
            column.append( ' ')   # Add a 'dead' cell

    nextCells.append( column )    # Add the new column to the grid


    # Start the main game loop
    while True:                  # An infinite loop
        print( '\n\n\n\n\n' )    # Separate each new step (iteration) of the game
        currentCells = copy.deepcopy( nextCells )  # Copy the list of lists

        # Print the current grid to the screen
        for y in range(HEIGHT):
            for x in range(WIDTH):
                print( currentCells[x][y], end='' ) # Print the cell contents
            print()                                 # Print a newline at the end of each row

        # Calculate (determine) the next step's cells based on the current cell content.
        