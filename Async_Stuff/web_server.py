""" An example of an asynchronous web server. 
    NOTE: The virtual environment is required to run this script. """

import asyncio
from aiohttp import web 

async def handle( request ):
    # The output from this function can be seen in a web browser at
    # http://localhost:8080
    return web.Response( text = "Hello World!" )

app = web.Application()
app.add_routes( [web.get( '/', handle ) ] )

if __name__ == '__main__':
    web.run_app( app )

