import asyncio


# Старая версия!
# @asyncio.coroutines
# def hello_world():
#     while True:
#         print('Hello World!')
#         yield from asyncio.sleep(1.0)
# После Python 3.5
async def hello_world():
    while True:
        print('Hello World!')
        await asyncio.sleep(1)


loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
loop.close()
