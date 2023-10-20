""" A routine illustrating reading a web page using 'beautifulSoup."""


# Import the needed functions
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Define the (sample) URL to read (scrape).
url = "http://olympus.realpython.org/profiles/dionysus"

# Open and red the page, then assign the page content to a 'beautifilsoup opbject".
page = urlopen( url )
html = page.read().decode( 'utf-8' )
soup = BeautifulSoup( html, 'html.parser' )   # html.parser is the built-in python parser

# Display the raw page data
print( '\nThe raw page content:' )
print( soup )

# Display the page content without the HTML tabs
print( '\nThe page content without HTML tags:' )
print( soup.get_text() )

# Remove the newline characters and redisplay the page content without HTML tags
text = soup.get_text()
text_clean = text.replace( "\n\n", "\n" )

print( '\nThe page content without newlines and HTML tags:' )
print( text_clean )

# The page has images, get the image tags and data
images = []
images = soup.find_all( 'img' )

# Loop over all of the images and display their source name
src = []              # Create an empty list
for i in range( len(images) ):
    src.append( images[i]['src'] )

print( '\nThe image tag sources are:' )
for i in range( len(src) ):
    print( f"Image {i} is {src[i]}" )





