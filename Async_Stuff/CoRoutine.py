""" Example of a CoRoutine (suspending execution). """

import asyncio


async def count():
    print( "one" )
    await asyncio.sleep( 3 )
    print( "two" )

async def main():
    await count()


asyncio.run( main() )
