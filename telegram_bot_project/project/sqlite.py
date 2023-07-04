import sqlite3
import asyncio
import string

import aiosqlite
import random


async def show_for_db(name, name_table):
    async with aiosqlite.connect('instructions.db') as db:
        cursor = await db.cursor()
        await cursor.execute(f"SELECT {name} FROM {name_table}")
        return [i[0] for i in await cursor.fetchall()]
# print(asyncio.get_event_loop().run_until_complete(show_for_db()))


# добавляет юзера при нажатии на команду старт
async def add_user(u_id, name, username) -> None:
    async with aiosqlite.connect('instructions.db') as db:
        cursor = await db.cursor()
        existing_users = await show_for_db(name='user_id', name_table='users')
        if str(u_id) not in existing_users:
            await cursor.execute(f"INSERT INTO users(user_id, user_name, username) VALUES (?, ?, ?)",
                                 (u_id, name, username))
            await db.commit()


# генерирует callback идентификатор
async def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


async def callback_func():
    async with aiosqlite.connect('instructions.db') as db:
        while True:
            a = await generate_random_string(10)
            existing_users = await show_for_db(name='callback', name_table='problems')
            if a not in existing_users:
                return a


# добавляет заголовок инструкции
async def add_instruction(np):
    async with aiosqlite.connect('instructions.db') as db:
        cursor = await db.cursor()
        await cursor.execute('''INSERT INTO problems(name_problem, callback) VALUES (?, ?)''',
                             (np, await callback_func()))
        await db.commit()


async def show_problems():
    async with aiosqlite.connect('instructions.db') as db:
        cursor = await db.cursor()
        await cursor.execute("SELECT name_problem FROM problems")
        return [i[0] for i in await cursor.fetchall()]


async def for_ikb_instructions():
    async with aiosqlite.connect('instructions.db') as db:
        cursor = await db.cursor()
        await cursor.execute("SELECT name_problem, callback FROM problems")
        return await cursor.fetchall()

# print(asyncio.get_event_loop().run_until_complete(for_ikb_instructions()))

# loop = asyncio.get_event_loop()
# print(loop.run_until_complete(for_ikb_instructions()))

# async def show_problems():
#     async with aiosqlite.connect('instructions.db') as db:
#         cursor = await db.execute("SELECT name_problem FROM problems")
#         return [i[0] for i in await cursor.fetchall()]


# print(asyncio.run(show_problems()))
# problems_list = await show_problems()

# with sqlite3.connect('instructions.db') as db:
#     cursor = db.cursor()
#     cursor.execute(f"SELECT name_problem FROM problems")
#     print([i[0] for i in cursor.fetchall()])


# with sqlite3.connect('instructions.db') as db:
#     cursor = db.cursor()
#     print([i[0] for i in cursor.execute('''SELECT user_id FROM users''').fetchall()])
#     if '428392590' not in cursor.execute('''SELECT user_id FROM users''').fetchall()[0]:
    #     print('tes')