"""A routine illustrating basic plotting concepts."""

# Import the necessary library functions
import pathlib                          # Needed for directory operations
from matplotlib import pyplot as plt    # Plotting functions
import numpy as np                      # For matrix "np.arange"

# Define (acquire) the data to be plotted.  Here we have years versus expenses.

years  = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]    # the list of years corresponding to the expenses
hshold = [64444,69966,73198,104200,94467,99921,77413,89582]  # Sample household expenses
electy = [5973,3209,3194,3969,3130,3278,5354,4762]           # Sample electricity costs
entrn  = [23139,27895,21495,16907,20195,19902,20402,23976]   # Sample entertainment expenses
trips  = [43641,59737,55703,44743,11666,15528,30696,30896]   # Sample travel expenses

# Plot the household expenses by year. For documentation on 'matplotlib', see:
#  https://matplotlib.org/2.0.2/contents.html

# Obtain the current working directory, and setup the output file(s).
current_path = pathlib.Path.cwd()
outfile = current_path / 'exp-line.png'

# Setup and plot the expenses in a "line plot".
# Generate the array of "Y axis" values
yvalues = np.arange( 0, 110000, 5000 )

plt.title( "Yearly Expenses" )
plt.xlabel( "Years" )
plt.ylabel( "Dollars" )
plt.yticks( yvalues )
plt.plot( years, hshold, "g-o" )        # Green, solid line, with circles
plt.plot( years, electy, "b:^" )        # Blue, dotted line, with triangles
plt.plot( years, entrn, "m-.8" )        # Magenta, dash-dot line, with octagons
plt.plot( years, trips, "r--D")         # Red, dash-dash line, with diamonds  

# All three of these 'plot.grid' variations work.
#plt.grid( visible="true", which="both", axis="both" )
#plt.grid( True, linestyle=':' )
plt.grid( visible='true', which='both', color='#9e9b91', linestyle=':', linewidth=0.5, axis='both' )

plt.legend( ["Household", "Electricity", "Entertainment", "Travel"] )

# Save the plot to a file (before displaying it on the screen).
plt.savefig( outfile )
plt.show()

############################################################################################3
# Generate a bar chart of the 4 expenses, using the total of the 8 years.

sum_hshold = sum( hshold )
sum_electy = sum( electy )
sum_entrn  = sum( entrn )
sum_trips  = sum( trips )

centers    = ["Household", "Electricity", "Entertainment", "Travel"]
tops       = ( sum_hshold, sum_electy, sum_entrn, sum_trips )

plt.title( "Cummulative Yearly Expenses: 2016-2023" )
plt.ylabel( "Dollars" )
plt.bar( centers, tops )

# Save the plot to a file (before displaying it on the screen).
outfile = current_path / 'exp-bar.png'
plt.savefig( outfile )
plt.show()

