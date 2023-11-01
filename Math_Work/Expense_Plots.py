"""A routine illustrating basic plotting concepts."""

# Import the necessary library functions
from matplotlib import pyplot as plt

# Define (acquire) the data to be plotted.  Here we have years versus expenses.

years  = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]    # the list of years corresponding to the expenses
hshold = [64444,69966,73198,104200,94467,99921,77413,89582]  # Sample household expenses
electy = [5973,3209,3194,3969,3130,3278,5354,4762]           # Sample electricity costs
entrn  = [23139,27895,21495,16907,20195,19902,20402,23976]   # Sample entertainment expenses
trips  = [43641,59737,55703,44743,11666,15528,30696,30896]   # Sample travel expenses

# Plot the household expenses by year. For documentation on 'matplotlib', see:
#  https://matplotlib.org/2.0.2/contents.html

plt.title( "Yearly Expenses" )
plt.xlabel( "Years" )
plt.ylabel( "Dollars" )
plt.legend( "Household, Electricity" )
plt.plot( years, hshold, "g-o" )        # Green, solid line, with circles
plt.plot( years, electy, "b:^" )        # Blue, dotted line, with triangles
plt.plot( years, entrn, "m-.8" )        # Magenta, dash-dot line, with octagons
plt.plot( years, trips, "r--D")         # Red, dash-dash line, with diamonds    
plt.show()

