# A routine to submit data to a 'login' form on the web.

import mechanicalsoup

# Create a 'browser' instance and use it to request the 'login' page.
browser    = mechanicalsoup.Browser()
url        = "http://olympus.realpython.org/login"
login_page = browser.get( url )
login_html = login_page.soup       # Assign the HTML content 

print( '\nThe page HTML:' )
print( login_html )          # This displays the HTML for the page just requested.

# Access the 'form' elements of the page
form = login_html.select( "form" )[0]        # The first 'form' element on the page
form.select( "input" )[0]["value"] = 'zeus'  # Set the first 'input' field value
form.select( "input" )[1]["value"] = 'ThunderDude'  # Set the second 'input' field value

# Submit the form, which should log us in
site_page = browser.submit( form, login_page.url )

# After a successful login, displaying the 'site_page.url' should show the URL of the page.
# This should differ from the 'url' variable defined above.
print( '\nThe URL and TITLE of the page following a successful login:' )
print( site_page.url )
page_title = site_page.soup.find( 'title' )
print( page_title )
print( page_title.text )

# In this particular example, the page (following the login) has three links to other (profile) pages
# defined in the HTML using the 'anchor' tag <a>.
links = site_page.soup.select( 'a' )

# Build the start of the full URL to the links on the 'site_page'.  Assume the starting URL
# is the URL above minus '/login'.
start_url = url[:-6]

# Iterate over the returned links on the page
print( '\nThe links on this new page are:' )
for link in links:
    address = start_url + link['href']     # This is the URL of the link
    text    = link.text                    # This the 'displayed' link text on the 'site_page'.
    print( f"{text}: {address}" )
