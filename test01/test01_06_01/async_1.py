# coding:utf-8
# @Create time: 2021/3/25 11:31 上午
# @Author: KongJingchun
# @remark: 异步
import random
import time
import asyncio


# async 创建异步方法
async def a():
    for i in range(10):
        print(i, 'a')
        # time.sleep()休眠的是CPU，所以使用异步应该使用 asyncio.sleep() 并加await
        await asyncio.sleep(random.random() * 2)
    return 'a function'


async def b():
    for i in range(10):
        print(i, 'b')
        await asyncio.sleep(random.random() * 2)
    return 'b function'


async def main():
    # 启用异步方法的方式
    result = await asyncio.gather(
        a(),
        b()
    )
    print(result)


if __name__ == '__main__':
    start = time.time()
    # 调用启用异步的方法
    asyncio.run(main())
    print(time.time() - start)
