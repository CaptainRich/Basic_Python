""" An example of an asynchronous subprocess. 
    NOTE: This script will not run in a 'PowerShell' terminal, 
    instead use a 'Git Bash' terminal. """

import asyncio

async def run_subprocess():
    process = await asyncio.create_subprocess_exec(
        'ls',  '-l', stdout=asyncio.subprocess.PIPE,
         stderr=asyncio.subprocess.PIPE, shell=False  )
    
    stdout, stderr = await process.communicate()
    if process.returncode == 0:     # was the command successful?
        print( stdout.decode() )
    else:
        print( f"Error: {stderr.decode()}" )


asyncio.run( run_subprocess() )