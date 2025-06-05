import asyncio
from services import *
async def main():
    #table create 
    # await create_table()
    # create user 
    await create_user("swet","swet@gmail.com")
asyncio.run(main())