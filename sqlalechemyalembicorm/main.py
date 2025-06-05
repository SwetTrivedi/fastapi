from models import create_tables
import asyncio
from services import *
async def main():
    # await create_tables()
    # await create_user("swet","swettrivedi@gmail.com")
    # await create_user("ashish","ashish@gmail.com")
    # print(await get_user(1))
    # print(await get_all_user())
    # await update_user_email(1,"khushi@gmail.com")
    await(delete_user(2))
asyncio.run(main())