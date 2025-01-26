""" An example of an asynchronous generator. """

import asyncio

async def generate_numbers( n ):
    # Generate the numbers up to 'n'.
    for i in range( n ):
        await asyncio.sleep( 2 )
        yield i

async def main():
    async for num in generate_numbers( 5 ):
        print( num )

asyncio.run( main() )