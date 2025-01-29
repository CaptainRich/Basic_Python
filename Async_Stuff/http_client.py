""" An example of an asynchronous HTTP client. 
    NOTE: The virtual environment is required to run this script. """

import asyncio
import aiohttp

async def fetch_data():
    # Start the HTTP client session
    async with aiohttp.ClientSession() as session:
        # Get the response from the 'mocked' web site.
        async with session.get( 'https://example.com' ) as response:
            data = await response.text()
            print( data )  # display the web page source


asyncio.run( fetch_data() )