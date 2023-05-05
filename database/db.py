import sqlite3 as sq
from datetime import date, timedelta, timezone



class Database:
    def __init__(self, db_file):
        self.connection = sq.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))

    def add_messages_to_delete(self, current_post_id, message_id, chat_id):
        with self.connection:
            number = self.cursor.execute("SELECT COUNT(*) FROM `messages_to_delete` WHERE `chat_id` = ?", (chat_id,)).fetchone()
            if number[0] == 0:
                return self.cursor.execute("INSERT INTO messages_to_delete (current_post_id, messages_id, chat_id) VALUES (?, ?, ?)", (current_post_id, str(message_id), chat_id,))
            else:
                return self.cursor.execute("UPDATE messages_to_delete SET current_post_id = ?, messages_id = ? WHERE chat_id = ?", (current_post_id, str(message_id), chat_id,))

    def get_messages_to_delete(self, chat_id):
        with self.connection:
            data = self.cursor.execute("SELECT * FROM `messages_to_delete` WHERE `chat_id` = ?", (chat_id,)).fetchone()
            return data[0], data[1], data[2]

    def get_example_post(self, id):
        with self.connection:
            data = self.cursor.execute("SELECT * FROM `examples` WHERE `id` = ?", (id,)).fetchone()
            return data


db = Database('database.db')
if db.connection:
    print('The data base has been successfully connected')
else:
    print('Failed to connect to data base')
