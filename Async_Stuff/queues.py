""" An example of asynchronous queues for coordinating producer/consumer
    patterns. """

import asyncio

async def producer( queue ):
    # The function that produces the data for the queue.
    for i in range( 5 ):
        await queue.put( i )  # store the value in the queue
        print( f"Produced {i}" )
        await asyncio.sleep( 2 )

    await queue.put( None ) # A sentinel value to signal 'consumer' to stop

async def consumer( queue ):
    # The function that consumes data from the queue.
    while True:
        item = await queue.get()  # get an item from the queue, wait if needed

        if item is None :         # check for the sentinel value
            queue.task_done()
            break                 # exit the 'while' loop

        print( f"Consumed {item}" )
        queue.task_done()



async def main():
    queue         = asyncio.Queue()
    # The 'create_task' function schedules these tasks for execution
    producer_task = asyncio.create_task( producer( queue ) )
    consumer_task = asyncio.create_task( consumer( queue ) )

    # 'gather' runs both coroutines concurrently.  
    await asyncio.gather( producer_task, consumer_task, return_exceptions=True )

    await queue.join() # ensure all items are processed by 'consumer_task' before exiting


asyncio.run( main() )