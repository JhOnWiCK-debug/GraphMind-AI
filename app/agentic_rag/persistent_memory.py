import sqlite3


class PersistentMemory:

    def __init__(self):

        self.conn = sqlite3.connect(
            "memory.db",
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS conversations(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                question TEXT,

                answer TEXT
            )
            """
        )

        self.conn.commit()

    def add(
        self,
        question,
        answer
    ):

        self.cursor.execute(

            """
            INSERT INTO conversations
            (
                question,
                answer
            )
            VALUES
            (?,?)
            """,

            (
                question,
                answer
            )
        )

        self.conn.commit()

    def history(self):

        self.cursor.execute(

            """
            SELECT
                question,
                answer
            FROM conversations
            """
        )

        return self.cursor.fetchall()

    def clear(self):

        self.cursor.execute(

            """
            DELETE FROM conversations
            """
        )

        self.conn.commit()