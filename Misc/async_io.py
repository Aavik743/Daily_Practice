import asyncio


async def main():
    task = asyncio.create_task(not_main())
    print('A')
    await asyncio.sleep(3)
    print('B')
    await asyncio.sleep(5)
    return_value = await task
    print(f'This is a demo program for {return_value}')


async def not_main():
    await asyncio.sleep(2)
    print('1')
    await asyncio.sleep(4)
    print('2')
    return "asyncIO"


asyncio.run(main())
