import sqlite3
class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def set_13(self, cur):
        with self.connection:
            return self.cursor.execute(f"UPDATE iphone SET i = ? WHERE user_id = 1", (cur,))

    def set_14(self, cur):
        with self.connection:
            return self.cursor.execute(f"UPDATE iphone SET ii = ? WHERE user_id = 1", (cur,))

    def get_13(self):
        with self.connection:
            result = self.cursor.execute(f"SELECT i FROM iphone WHERE user_id = 1").fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def get_14(self):
        with self.connection:
            result = self.cursor.execute(f"SELECT ii FROM iphone WHERE user_id = 1").fetchall()
            for row in result:
                signup = str(row[0])
            return signup



