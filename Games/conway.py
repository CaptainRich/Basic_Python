""" A script illustrating Conway's Game of Life. """

import random, time, copy, sys       # Necessary standard imports

WIDTH  = 60       # Define the size of the game grid
HEIGHT = 20

ALIVE  = '■'      # Symbol indicating a living cell
DEAD   = ' '      # Symbol indicating a dead cell

# Create a 'dictionary' to represent the game grid cells. The keys to the 
# cells are the (x,y) tuples, i.e. the coordinates of the cell in the grid.
# The values of the keys are the symbols representing either 'DEAD' or 'ALIVE'.
nextCells = {}

# Loop over the rows in the grid
for x in range(WIDTH):

    # Loop over the cells in a column and randomly set the cells.
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            nextCells[(x,y)]  = ALIVE   # Add a 'living' cell
        else:
            nextCells[(x,y)]  = DEAD    # Add a 'dead' cell


# Start the main game loop
stepNum = 0
while True:                  # An infinite loop
    print( '\n\n\n\n\n' )    # Separate each new step (iteration) of the game
    currentCells = copy.deepcopy( nextCells )  # Copy the list of lists

    # Print the current grid to the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print( currentCells[(x,y)], end='' ) # Print the cell contents
        print()                                  # Print a newline at the end of each row

    stepNum += 1
    print( f' *** Use Crtl-C to end the simulation: {stepNum}' )

    # Calculate (determine) the next step's cells based on the current cell content.
    for x in range( WIDTH ):           # Loop over the rows in the grid
        for y in range( HEIGHT ):      # Loop over the columns in the grid
            # Get the neighboring coordinates of the current cell.
            # The '% WIDTH' ensures leftCoord is always between 0 and WIDTH-1.
            leftCoord  = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT

            # Count the number of living neighbors (cells with '#') for this cell.
            numNeighbors = 0

            if currentCells[(leftCoord,aboveCoord)] == ALIVE:
                numNeighbors += 1   # Top left neighbor is alive
            if currentCells[(x,aboveCoord)] == ALIVE:
                numNeighbors += 1   # Top neighbor is alive
            if currentCells[(rightCoord,aboveCoord)] == ALIVE:
                numNeighbors += 1   # Top right neighbor is alive

            if currentCells[(leftCoord,y)] == ALIVE:
                numNeighbors += 1   # Left neighbor is alive
            if currentCells[(rightCoord,y)] == ALIVE:
                numNeighbors += 1   # Right neighbor is alive

            if currentCells[(leftCoord,belowCoord)] == ALIVE:
                numNeighbors += 1   # Bottom left neighbor is alive
            if currentCells[(x,belowCoord)] == hash:
                numNeighbors += 1   # Bottom neighbor is alive
            if currentCells[(rightCoord,belowCoord)] == ALIVE:
                    numNeighbors += 1   # Bottom right neighbor is alive

            # All 8 neighbors have been checked.  Set the current cell's status
            # based on Conway's rules (2 or 3 live neighbors means current cell
            # is alive), anything else means the current cell is dead).
            if currentCells[(x,y)] == ALIVE and (numNeighbors == 2 or \
                                                 numNeighbors == 3 ):
                # Living cells with 2 or 3 live neighbors stay alive.
                nextCells[(x,y)] = ALIVE
            elif currentCells[(x,y)] == DEAD and (numNeighbors == 3 ):
                # Dead cells with 3 neighbors become alive.
                nextCells[(x,y)] = ALIVE
            else:
                # Everything else dies or stays dead.
                nextCells[(x,y)] = DEAD

    try:
        time.sleep( 1 )   # Add a 1-second pause to view the grid change.

    except KeyboardInterrupt:
        # User pressed 'Crtl-C'
        print( "End of Conway's Game of Life" )
        sys.exit() 

