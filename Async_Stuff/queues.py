""" An example of asynchronous queues for coordinating producer/consumer
    patterns. """

import asyncio

async def producer( queue ):
    # The function that produces the data for the queue.
    for i in range( 5 ):
        await queue.put( i )  # store the value in the queue
        print( f"Produced {i}" )
        await asyncio.sleep( 2 )

async def consumer( queue ):
    # The function that consumes data from the queue.
    while True:
        item = await queue.get()  # get an item from the queue, wait if needed
        print( f"Consumed {item}" )
        queue.task_done()



async def main():
    queue         = asyncio.Queue()
    producer_task = asyncio.create_task( producer( queue ) )
    consumer_task = asyncio.create_task( consumer( queue ) )

    # 'gather' runs both coroutines concurrently.  Note that if 'consumer_task'
    # is added to the 'gather' method, this script hangs???
    await asyncio.gather( producer_task, return_exceptions=True )

    await queue.join() # ensure all items are processed before exiting


asyncio.run( main() )