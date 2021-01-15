# asyncio.Future, аналог concurrent.futures.Future
# Future - объект, который выполняется но его выполнение не завершено.
# из объектов типа asyncio.Future можно создавать цепочки и дожидаться их выполнения в asyncio event loop.

import asyncio


async def slow_operation(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')


loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))

loop.run_until_complete(future)
print(future.result())
loop.close()