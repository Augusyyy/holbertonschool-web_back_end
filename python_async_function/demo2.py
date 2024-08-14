import time
import asyncio


async def fun():
    time.sleep(3)  # 第一台洗衣机,
    print('washer1 finished')  # 洗完了


coroutine_1 = fun()  # 协程是一个对象，不能直接运行
asyncio.run(coroutine_1)
asyncio.run(fun())