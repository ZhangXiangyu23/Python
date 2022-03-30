# coding:utf-8

import time
import random
import asyncio


async def a():
    for i in range(10):
        print(i, "a")
        await asyncio.sleep(random.random() * 2)
    return "a_function"


async def b():
    for i in range(10):
        print(i, "b")
        await asyncio.sleep(random.random() * 2)
    return "b_function"

async def main():
    result = await asyncio.gather(
        a(),
        b()
    )
    print(result)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print("耗时:%s" % (time.time() - start_time))