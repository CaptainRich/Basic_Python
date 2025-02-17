""" An example of a 'context manager', coupled with a 'generator'.
    NOTE: The virtual environment is required to run this script. """

import asyncio
import aiofiles 

async def main():
    # Note the need for 'data.txt' here!
    async with aiofiles.open( 'data.txt' ) as f:
        contents = await f.read()
        print( contents )

asyncio.run( main() )

