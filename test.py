import orm

import asyncio

# import random

from models import User, Blog, Comment

async def test_save(loop):

    await orm.create_pool(loop=loop, user='root', password='ws2008!@#', database='awesome')

    u = User(name='Test4', email='tes4@example.com',passwd='888888', image='about:blank')

    await u.save()



if __name__ == "__main__":

    loop = asyncio.get_event_loop()

    tasks = [test_save(loop)]

    loop.run_until_complete(asyncio.wait(tasks))
    print('Test finished')