import sqlite3


# conn = sqlite3.connect('instructions.db')
# cursor = conn.cursor()


async def add_user(u_id, name, username):
    with sqlite3.connect('instructions.db') as db:
        cursor = db.cursor()
        if str(u_id) not in [i[0] for i in cursor.execute('''SELECT user_id FROM users''').fetchall()]:
            cursor.execute('''INSERT INTO users(user_id, user_name, username) VALUES (?, ?, ?)''',
                           (u_id, name, username))
            db.commit()


async def add_instruction(name_problem):
    with sqlite3.connect('instructions.db') as db:
        cursor = db.cursor()
        cursor.execute('''INSERT INTO problems(name_problem) VALUES (?)''', name_problem)
        db.commit()


# with sqlite3.connect('instructions.db') as db:
#     cursor = db.cursor()
#     print([i[0] for i in cursor.execute('''SELECT user_id FROM users''').fetchall()])
#     if '428392590' not in cursor.execute('''SELECT user_id FROM users''').fetchall()[0]:
    #     print('tes')