import asyncio


async def send_hello() -> None:
    await asyncio.sleep(4)
    print('Hello')


async def send_bye() -> None:
    await asyncio.sleep(1)
    print('Bye')


async def gen1():
    for i in range(1000000):
        if i == 999999:
            # await asyncio.sleep(1)
            print('Yes1')


async def gen2():
    for i in range(5):
        if i == 4:
            print('Yes2')


async def main():
    # t1 = asyncio.create_task(send_hello())  # чтобы код выполнялся асинхронно нужно зарегистрировать задачу в переменную
    # t2 = asyncio.create_task(send_bye())

    t1 = asyncio.create_task(gen1())
    t2 = asyncio.create_task(gen2())

    await t1
    await t2


asyncio.run(main())