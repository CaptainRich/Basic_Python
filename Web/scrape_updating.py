"""A routine to scrap a web page, looking for a particular value that is constantly
   updated. The updated value is the roll of a die."""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import mechanicalsoup
import time                         # Needed for the "sleep" function

#########################################################################################
def count_html_string( url, search_string ):
    """A routine to count the occurrences of an HTML string."""
    # Open and red the page, then assign the page content to a 'beautifilsoup opbject".
    page = urlopen( url )
    html = page.read().decode( 'utf-8' )
    soup = BeautifulSoup( html, 'html.parser' )   # html.parser is the built-in python parser

    ids  = soup.find_all( id=search_string ) 
    count = len( ids )
    return count


#########################################################################################
# Main

url     = "http://olympus.realpython.org/dice"    # The web page to scrape.  
browser = mechanicalsoup.Browser()

# We are counting there being only one HTML tag with ID="result".  Check this before 
# committing to the logic below.
search_string = "result"
count = count_html_string( url, search_string )

if count == 1:
    print( f"\nThere is only  {count} tag with 'ids={search_string}': " )
else:
    print( f"\nThere are {count} tags with 'ids={search_string}', aborting: " )
    exit()

# Get 5 rolls of the dice.
limit = 5                                       # Number of dice rolls to get
for i in range( limit ):
    page   = browser.get( url )                 # Get the web page
    tag    = page.soup.select( "#result" )[0]   # Get the tag we want (it has the ID+result string).
    result = tag.text
    print( f"The result of the dice roll is: {result}." )

    # Now wait 5 seconds before repeating the acquisition of the next roll of the dice.
    if i < (limit-1):                           # Don't wait after the last acquisition
        time.sleep( 5 )                         # Wait 5 seconds

    