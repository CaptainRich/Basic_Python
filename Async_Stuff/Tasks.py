""" An illustration of asynchronous tasks,  Tasks are used to
    schedule and run coroutines concurrently. """

import asyncio

async def count( n, taskId ):
    for i in range( n ):
        print( "TaskID: ", taskId, "  i: ", i )
        await asyncio.sleep( 1 )


async def main():
    # Because of the "async", tasks 1 and 2 run simultaneously, each
    # printing an iteration in turn.
    task1 = asyncio.create_task( count( 5, 'TASK1' ) )
    task2 = asyncio.create_task( count( 3, '   task2' ) )

    await task1   #pause 'main' until 'task1' completes.
    await task2   #pause 'main' until 'task2' completes.


asyncio.run( main() )
