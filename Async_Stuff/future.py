""" An example of a 'future'.  A 'future' represents an eventual result
    of an asynchronous operation, that may or may not complete. The 
    'future' acts as a placeholder for the result. """

import asyncio

async def fetch_data():
    await asyncio.sleep( 2 )
    return 42


async def main():
    future = asyncio.ensure_future( fetch_data() )
    result = await future
    print( result )


asyncio.run( main() )