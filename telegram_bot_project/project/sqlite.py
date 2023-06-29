import sqlite3
import asyncio
import aiosqlite

# conn = sqlite3.connect('instructions.db')
# cursor = conn.cursor()


def add_user(u_id, name, username):
    with sqlite3.connect('instructions.db') as db:
        cursor = db.cursor()
        # cursor.execute(f''''INSERT INTO users(user_id, user_name, username) VALUES ({u_id}, {name}, {username})
        # IF '{u_id}' NOT IN (SELECT user_id FROM users)''')
        if str(u_id) not in [i[0] for i in cursor.execute('''SELECT user_id FROM users''').fetchall()]:
            cursor.execute(f"INSERT INTO users(user_id, user_name, username) VALUES (?, ?, ?)", (u_id, name, username))
            db.commit()


def add_instruction(np):
    with sqlite3.connect('instructions.db') as db:
        cursor = db.cursor()
        cursor.execute('''INSERT INTO problems(name_problem) VALUES (?)''', (np,))
        db.commit()


# def show_problems():
#     with aiosqlite.connect('instructions.db') as db:
#         cursor = await db.execute("SELECT name_problem FROM problems")
#         return [i[0] for i in await cursor.fetchall()]
# async def main():
#     problems_list = await show_problems()
#     print(problems_list)
# asyncio.run(main())



# async def show_problems():
#     async with sqlite3.connect('instructions.db') as db:
#         cursor = db.cursor()
#         cursor.execute(f"SELECT name_problem FROM problems")
#         t = [i[0] for i in cursor.fetchall()]
#         return t



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